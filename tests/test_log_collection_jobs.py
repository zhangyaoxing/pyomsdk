from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.log_collection_jobs_resource import LogCollectionJobsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_log_collection_jobs_get_all_jobs(
    client: OpsManagerClient, project: dict[str, Any]
) -> None:
    resource = client.log_collection_jobs_resource
    path_params = LogCollectionJobsResource.GetAllJobsPathParams(project_id=project["id"])
    result = resource.get_all_jobs(path_params, None)
    assert result is not None
    assert "error" not in result


def test_log_collection_jobs_get_job(client: OpsManagerClient, project: dict[str, Any]) -> None:
    resource = client.log_collection_jobs_resource
    all_result = resource.get_all_jobs(
        LogCollectionJobsResource.GetAllJobsPathParams(project_id=project["id"]), None
    )
    items = all_result if isinstance(all_result, list) else all_result.get("results", [])
    if not items:
        pytest.skip("No log collection jobs found in project")

    job_id = items[0].get("id") or items[0].get("_id")
    path_params = LogCollectionJobsResource.GetJobPathParams(group_id=project["id"], job_id=job_id)
    result = resource.get_job(path_params, None)
    assert result is not None
    assert "error" not in result
