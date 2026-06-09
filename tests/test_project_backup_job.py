from typing import Optional
import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.project_backup_job_resource import ProjectBackupJobResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_project_backup_job_get_all(client: OpsManagerClient) -> None:
    resource = client.project_backup_job_resource
    query_params = ProjectBackupJobResource.GetAllQueryParams(pretty=True)
    result = resource.get_all(query_params)
    assert result is not None
    assert "error" not in result


def test_project_backup_job_get_by_id(client: OpsManagerClient) -> None:
    resource = client.project_backup_job_resource
    all_result = resource.get_all(ProjectBackupJobResource.GetAllQueryParams())
    items: Optional[list] = all_result.get("results", []) if all_result else None
    if not items:
        pytest.skip("No backup jobs configured")

    job_id = items[0].get("id") or items[0].get("_id") or items[0].get("projectId")
    if not job_id:
        pytest.skip("Backup job entry has no id field")

    path_params = ProjectBackupJobResource.GetByIdPathParams(project_id=job_id)
    result = resource.get_by_id(path_params, None)
    assert result is not None
    assert "error" not in result


def test_project_backup_job_update(client: OpsManagerClient, project) -> None:
    """Test update."""
    resource = client.project_backup_job_resource
    all_result = resource.get_all(ProjectBackupJobResource.GetAllQueryParams())
    items: Optional[list] = all_result.get("results", []) if all_result else None
    if not items:
        pytest.skip("No backup jobs configured")
    resource = client.project_backup_job_resource
    path_params = resource.UpdatePathParams(project_id=project["id"])
    result = resource.update(path_params, None, None)
    # Endpoint can return 204 No Content on success.
    if result is None:
        return
    assert "error" not in result
