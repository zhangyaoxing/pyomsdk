import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.project_backup_job_resource import ProjectBackupJobResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


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
    items = all_result if isinstance(all_result, list) else all_result.get("results", [])
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
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        ProjectBackupJobResource.UpdatePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        ProjectBackupJobResource.UpdateQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    body_params = build_model_or_skip(
        ProjectBackupJobResource.UpdateBodyParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.update(path_params, query_params, body_params)
    # Endpoint can return 204 No Content on success.
    if result is None:
        return
    assert_success_or_skip(result)
