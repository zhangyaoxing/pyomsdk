from typing import Optional
import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.s3_oplog_resource import S3OplogResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_s3_oplog_get_all(client: OpsManagerClient) -> None:
    resource = client.s3_oplog_resource
    query_params = S3OplogResource.GetAllQueryParams(pretty=True)
    result = resource.get_all(query_params)
    assert result is not None
    assert_success_or_skip(result)


def test_s3_oplog_get_by_id(client: OpsManagerClient) -> None:
    resource = client.s3_oplog_resource
    all_result = resource.get_all(S3OplogResource.GetAllQueryParams())
    items: Optional[list] = all_result.get("results", []) if all_result else None
    if not items:
        pytest.skip("No S3 oplog configs found")

    config_id = items[0].get("id") or items[0].get("_id")
    path_params = S3OplogResource.GetByIdPathParams(s3_oplog_config_id=config_id)
    result = resource.get_by_id(path_params, None)
    assert result is not None
    assert_success_or_skip(result)


def test_s3_oplog_create(client: OpsManagerClient) -> None:
    """Test create."""
    resource = client.s3_oplog_resource
    body_params = resource.CreateBodyParams(
        accepted_tos=True,
        id="S3OplogStore",
        path_style_access_enabled=True,
        s3_bucket_endpoint="localhost",
        s3_bucket_name="my-oplog-bucket",
        s3_max_connections=10,
        sse_enabled=False,
        uri="/oplogs",
        disable_proxy_s3=True,
        aws_access_key="fake-access-key-id",
        aws_secret_key="fake-secret-access-key",
    )
    result = resource.create(None, body_params)
    assert "error" in result
    assert result["errorCode"] == "BACKUP_S3_CONNECTION_FAILED"


def test_s3_oplog_delete(client: OpsManagerClient) -> None:
    """Test delete."""
    resource = client.s3_oplog_resource
    path_params = resource.DeletePathParams(s3_oplog_config_id="S3OplogStore")
    result = resource.delete(path_params, None)
    assert result is None


def test_s3_oplog_update(client: OpsManagerClient) -> None:
    """Test update."""
    resource = client.s3_oplog_resource
    path_params = resource.UpdatePathParams(s3_oplog_config_id="S3OplogStore")
    body_params = resource.UpdateBodyParams(
        accepted_tos=True,
        path_style_access_enabled=True,
        s3_bucket_endpoint="localhost",
        s3_bucket_name="my-oplog-bucket",
        s3_max_connections=10,
        sse_enabled=False,
        uri="/oplogs",
        disable_proxy_s3=True,
        aws_access_key="fake-access-key-id",
        aws_secret_key="fake-secret-access-key",
    )
    result = resource.update(path_params, None, body_params)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "BACKUP_S3_CONNECTION_FAILED"
