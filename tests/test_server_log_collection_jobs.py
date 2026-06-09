from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.server_log_collection_jobs_resource import (
    ServerLogCollectionJobsResource,
)


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_server_log_collection_jobs_get_all_jobs(client: OpsManagerClient) -> None:
    resource = client.server_log_collection_jobs_resource
    result = resource.get_all_jobs(None)
    assert result is not None
    assert "error" not in result
    assert "results" in result


def test_server_log_collection_jobs_list_active_servers(client: OpsManagerClient) -> None:
    resource = client.server_log_collection_jobs_resource
    result = resource.list_active_servers(None)
    assert result is not None
    assert "error" not in result
    assert "results" in result


def test_server_log_collection_jobs_get_one_job(client: OpsManagerClient) -> None:
    resource = client.server_log_collection_jobs_resource
    path_params = ServerLogCollectionJobsResource.GetOneJobPathParams(
        job_id="000000000000000000000000"
    )
    result = resource.get_one_job(path_params, None)
    assert result is not None
    assert "error" in result


def test_server_log_collection_jobs_delete(client: OpsManagerClient) -> None:
    resource = client.server_log_collection_jobs_resource
    path_params = ServerLogCollectionJobsResource.DeletePathParams(
        job_id="000000000000000000000000"
    )
    result = resource.delete(path_params, None)
    assert result is not None
    assert "error" in result


def test_server_log_collection_jobs_retry(client: OpsManagerClient) -> None:
    resource = client.server_log_collection_jobs_resource
    path_params = ServerLogCollectionJobsResource.RetryPathParams(job_id="000000000000000000000000")
    result = resource.retry(path_params, None)
    assert result is not None
    assert "error" in result


def test_server_log_collection_jobs_download_logs(client: OpsManagerClient) -> None:
    resource = client.server_log_collection_jobs_resource
    path_params = ServerLogCollectionJobsResource.DownloadLogsPathParams(
        job_id="000000000000000000000000"
    )
    result = resource.download_logs(path_params, None)
    assert result is not None
    assert "error" in result


def test_server_log_collection_jobs_create(client: OpsManagerClient) -> None:
    resource = client.server_log_collection_jobs_resource
    body_params = ServerLogCollectionJobsResource.CreateBodyParams(
        log_collection_from_date="2026-01-01T00:00:00Z"
    )
    result = resource.create(None, body_params)
    assert result is not None
    assert "error" in result


def test_server_log_collection_jobs_extend_expiration(client: OpsManagerClient) -> None:
    resource = client.server_log_collection_jobs_resource
    path_params = ServerLogCollectionJobsResource.ExtendExpirationPathParams(
        job_id="000000000000000000000000"
    )
    body_params = ServerLogCollectionJobsResource.ExtendExpirationBodyParams(
        expiration_date="2099-01-01T00:00:00Z"
    )
    result = resource.extend_expiration(path_params, None, body_params)
    assert result is not None
    assert "error" in result
