from typing import Any, Optional

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.configuration_resource import ConfigurationResource
from pyomsdk.resources.re_election_jobs_resource import ReElectionJobsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _first_replica_set_id(client: OpsManagerClient, project_id: str) -> Optional[str]:
    """Return the id of the first replica set of the project's automation config."""
    resource = client.configuration_resource
    config = resource.get_the_automation_configuration(
        ConfigurationResource.GetTheAutomationConfigurationPathParams(project_id=project_id), None
    )
    replica_sets: list[dict[str, Any]] = (config or {}).get("replicaSets") or []
    if not replica_sets:
        return None
    return replica_sets[0].get("_id") or replica_sets[0].get("id")


def test_re_election_jobs_get_all(
    client: OpsManagerClient, project_with_cluster: dict[str, Any]
) -> None:
    project_id = project_with_cluster["id"]
    rs_id = _first_replica_set_id(client, project_id)
    if not rs_id:
        pytest.skip("No replica set found in the project automation config")

    resource = client.re_election_jobs_resource
    path_params = ReElectionJobsResource.GetAllPathParams(group_id=project_id, rs_id=rs_id)
    result = resource.get_all(path_params, None)
    assert result is not None
    assert "error" not in result


def test_re_election_jobs_get_one(
    client: OpsManagerClient, project_with_cluster: dict[str, Any]
) -> None:
    project_id = project_with_cluster["id"]
    rs_id = _first_replica_set_id(client, project_id)
    if not rs_id:
        pytest.skip("No replica set found in the project automation config")

    resource = client.re_election_jobs_resource
    all_path_params = ReElectionJobsResource.GetAllPathParams(group_id=project_id, rs_id=rs_id)
    all_result = resource.get_all(all_path_params, None)
    items: list[dict[str, Any]] = (all_result or {}).get("results") or []
    if not items:
        pytest.skip("No re-election jobs found for the replica set")

    job_id = items[0].get("id") or items[0].get("_id")
    assert job_id is not None

    path_params = ReElectionJobsResource.GetOnePathParams(
        group_id=project_id, rs_id=rs_id, reelection_job_id=job_id
    )
    result = resource.get_one(path_params, None)
    assert result is not None
    assert "error" not in result
