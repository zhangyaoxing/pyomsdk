from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.backup_configurations_resource import BackupConfigurationsResource
from pyomsdk.resources.clusters_resource import ClustersResource
from pyomsdk.resources.enums import BackupStatusName


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _first_cluster_id(client: OpsManagerClient, project_id: str) -> str | None:
    result = client.clusters_resource.get_all_from_one_project(
        ClustersResource.GetAllFromOneProjectPathParams(project_id=project_id), None
    )
    items = result if isinstance(result, list) else result.get("results", [])
    if not items:
        return None
    return items[0].get("id") or items[0].get("_id")


def test_backup_configurations_get_all(
    client: OpsManagerClient, project_with_cluster: dict[str, Any]
) -> None:
    resource = client.backup_configurations_resource
    path_params = BackupConfigurationsResource.GetAllPathParams(
        project_id=project_with_cluster["id"]
    )
    result = resource.get_all(path_params, None)
    assert result is not None
    assert "error" not in result
    assert len(result.get("results", [])) > 0


def test_backup_configurations_get_one(
    client: OpsManagerClient, project_with_cluster: dict[str, Any]
) -> None:
    cluster_id = _first_cluster_id(client, project_with_cluster["id"])
    if not cluster_id:
        pytest.skip("No clusters found in project")

    resource = client.backup_configurations_resource
    path_params = BackupConfigurationsResource.GetOnePathParams(
        project_id=project_with_cluster["id"], cluster_id=cluster_id
    )
    result = resource.get_one(path_params, None)
    assert result is not None
    assert "error" not in result


def test_backup_configurations_update(
    client: OpsManagerClient,
    project_with_cluster: dict[str, Any],
    cluster: dict[str, Any],
) -> None:
    """Test update."""
    resource = client.backup_configurations_resource

    path_params = BackupConfigurationsResource.UpdatePathParams(
        cluster_id=cluster["id"],
        project_id=project_with_cluster["id"],
    )
    body_params = BackupConfigurationsResource.UpdateBodyParams(
        status_name=BackupStatusName.STARTED
    )
    result = resource.update(path_params, None, body_params)
    assert result is not None
    assert result["error"] == 409
