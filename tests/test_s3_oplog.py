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
    items = all_result if isinstance(all_result, list) else all_result.get("results", [])
    if not items:
        pytest.skip("No S3 oplog configs found")

    config_id = items[0].get("id") or items[0].get("_id")
    path_params = S3OplogResource.GetByIdPathParams(s3_oplog_config_id=config_id)
    result = resource.get_by_id(path_params, None)
    assert result is not None
    assert_success_or_skip(result)


def test_s3_oplog_create(client: OpsManagerClient, project) -> None:
    """Test create."""
    resource = client.s3_oplog_resource
    org = None
    user = None
    api_key = None
    query_params = build_model_or_skip(
        S3OplogResource.CreateQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    body_params = build_model_or_skip(
        S3OplogResource.CreateBodyParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.create(query_params, body_params)
    assert result is not None
    assert_success_or_skip(result)


def test_s3_oplog_delete(client: OpsManagerClient, project) -> None:
    """Test delete."""
    resource = client.s3_oplog_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        S3OplogResource.DeletePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        S3OplogResource.DeleteQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.delete(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)


def test_s3_oplog_update(client: OpsManagerClient, project) -> None:
    """Test update."""
    resource = client.s3_oplog_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        S3OplogResource.UpdatePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        S3OplogResource.UpdateQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    body_params = build_model_or_skip(
        S3OplogResource.UpdateBodyParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.update(path_params, query_params, body_params)
    assert result is not None
    assert_success_or_skip(result)
