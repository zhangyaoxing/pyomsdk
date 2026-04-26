from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.clusters_resource import ClustersResource
from pyomsdk.resources.restore_jobs_resource import RestoreJobsResource


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


def test_restore_jobs_get_all_cluster(client: OpsManagerClient, project: dict[str, Any]) -> None:
    cluster_id = _first_cluster_id(client, project["id"])
    if not cluster_id:
        pytest.skip("No clusters found in project")

    resource = client.restore_jobs_resource
    path_params = RestoreJobsResource.GetAllClusterPathParams(
        project_id=project["id"], cluster_id=cluster_id
    )
    result = resource.get_all_cluster(path_params, None)
    assert result is not None
    assert "error" not in result
