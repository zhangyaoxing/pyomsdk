from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.clusters_resource import ClustersResource
from pyomsdk.resources.snapshot_schedule_resource import SnapshotScheduleResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _first_cluster_id(client: OpsManagerClient, project_id: str) -> str | None:
    result = client.clusters_resource.get_all_from_one_project(
        ClustersResource.GetAllFromOneProjectPathParams(project_id=project_id), None
    )
    items = result.get("results", [])
    if not items:
        return None
    return items[0].get("id") or items[0].get("_id")


def test_snapshot_schedule_get_schedule(
    client: OpsManagerClient, project_with_cluster: dict[str, Any]
) -> None:
    cluster_id = _first_cluster_id(client, project_with_cluster["id"])
    if not cluster_id:
        pytest.skip("No clusters found in project")

    resource = client.snapshot_schedule_resource
    path_params = SnapshotScheduleResource.GetSchedulePathParams(
        project_id=project_with_cluster["id"], cluster_id=cluster_id
    )
    result = resource.get_schedule(path_params, None)
    assert result is not None
    assert "error" not in result


def test_snapshot_schedule_update(client: OpsManagerClient, project_with_cluster) -> None:
    """Test update."""
    cluster_id = _first_cluster_id(client, project_with_cluster["id"])
    if not cluster_id:
        pytest.skip("No clusters found in project")
    resource = client.snapshot_schedule_resource
    path_params = SnapshotScheduleResource.UpdatePathParams(
        project_id=project_with_cluster["id"], cluster_id=cluster_id
    )
    body_params = SnapshotScheduleResource.UpdateBodyParams(full_incremental_day_of_week="MONDAY")
    result = resource.update(path_params, None, body_params)
    assert result is not None
    assert "error" not in result
    assert result["fullIncrementalDayOfWeek"] == "MONDAY"
