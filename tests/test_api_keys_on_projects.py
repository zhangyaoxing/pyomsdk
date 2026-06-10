from typing import Any

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.enums import GroupRole
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
        roles=[GroupRole.GROUP_READ_ONLY],
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


def test_api_keys_on_projects_modify_roles(
    client: OpsManagerClient, project: dict[str, Any]
) -> None:
    desc = "Test API Key for role modification"
    resource = client.api_keys_on_projects_resource
    create_path = ApiKeysOnProjectsResource.CreateAssignPathParams(project_id=project["id"])
    create_body = ApiKeysOnProjectsResource.CreateAssignBodyParams(
        desc=desc, roles=[GroupRole.GROUP_READ_ONLY]
    )
    created = resource.create_assign(create_path, None, create_body)
    assert created is not None
    assert "error" not in created

    api_key_id = created.get("id") or created.get("_id")
    assert api_key_id is not None

    try:
        path_params = ApiKeysOnProjectsResource.ModifyRolesPathParams(
            project_id=project["id"], api_key_id=api_key_id
        )
        body_params = ApiKeysOnProjectsResource.ModifyRolesBodyParams(
            roles=[GroupRole.GROUP_READ_ONLY]
        )

        result = resource.modify_roles(path_params, None, body_params)
        assert result is not None
        assert "error" not in result
    finally:
        unassign_path = ApiKeysOnProjectsResource.UnassignPathParams(
            project_id=project["id"], api_key_id=api_key_id
        )
        resource.unassign(unassign_path, None)
