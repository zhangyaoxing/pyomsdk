from typing import Any

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.log_collection_jobs_resource import LogCollectionJobsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_log_collection_jobs_get_all_jobs(
    client: OpsManagerClient, project: dict[str, Any]
) -> None:
    resource = client.log_collection_jobs_resource
    path_params = LogCollectionJobsResource.GetAllJobsPathParams(group_id=project["id"])
    result = resource.get_all_jobs(path_params, None)
    assert result is not None
    assert "error" not in result
    assert len(result["results"]) == 0


def test_log_collection_jobs_get_job(client: OpsManagerClient, project: dict[str, Any]) -> None:
    resource = client.log_collection_jobs_resource
    path_params = LogCollectionJobsResource.GetJobPathParams(
        group_id=project["id"], job_id=project["id"]
    )
    result = resource.get_job(path_params, None)
    assert result is not None
    assert "error" in result
    assert result["error"] == 404
