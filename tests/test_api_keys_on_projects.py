from typing import Any

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.api_keys_on_projects_resource import ApiKeysOnProjectsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_api_keys_on_projects_get_all(client: OpsManagerClient, project: dict[str, Any]) -> None:
    resource = client.api_keys_on_projects_resource
    path_params = ApiKeysOnProjectsResource.GetAllPathParams(project_id=project["id"])
    result = resource.get_all(path_params, None)
    assert result is not None
    assert "error" not in result


def test_api_keys_on_projects_create_and_unassign(
    client: OpsManagerClient, project: dict[str, Any]
) -> None:
    desc: str = "Test API Key for project"
    resource = client.api_keys_on_projects_resource
    path_params = ApiKeysOnProjectsResource.CreateAssignPathParams(project_id=project["id"])
    body_params = ApiKeysOnProjectsResource.CreateAssignBodyParams(
        desc=desc,
        roles=["GROUP_READ_ONLY"],
    )
    created = resource.create_assign(path_params, None, body_params)
    assert created is not None
    assert "error" not in created
    assert created.get("desc") == desc

    api_key_id = created.get("id") or created.get("_id")
    if api_key_id:
        unassign_path = ApiKeysOnProjectsResource.UnassignPathParams(
            project_id=project["id"], api_key_id=api_key_id
        )
        resource.unassign(unassign_path, None)
