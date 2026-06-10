from uuid import uuid4

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient

# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_teams_get_all(client: OpsManagerClient, org) -> None:
    resource = client.teams_resource
    path_params = resource.GetAllPathParams(org_id=org["id"])

    result = resource.get_all(path_params, None)
    assert result is not None
    assert "error" not in result


def test_teams_create_get_add_remove_user_rename_delete(
    client: OpsManagerClient, org: dict, user: dict
) -> None:
    resource = client.teams_resource
    name = f"Test Team {uuid4().hex[:8]}"
    create_path = resource.CreatePathParams(org_id=org["id"])
    create_body = resource.CreateBodyParams(name=name)

    created = resource.create(create_path, None, create_body)
    assert created is not None
    if created.get("errorCode") == "CANNOT_CREATE_EMPTY_TEAM":
        pytest.skip("Ops Manager requires team creation to include at least one user")
    assert "error" not in created

    team_id = created.get("id") or created.get("_id")
    assert team_id is not None

    try:
        get_by_id_path = resource.GetOneByIdPathParams(org_id=org["id"], team_id=team_id)
        by_id = resource.get_one_by_id(get_by_id_path, None)
        assert by_id is not None
        assert "error" not in by_id

        get_by_name_path = resource.GetOneByNamePathParams(org_id=org["id"], team_name=name)
        by_name = resource.get_one_by_name(get_by_name_path, None)
        assert by_name is not None
        assert "error" not in by_name

        add_users_path = resource.AddUsersPathParams(org_id=org["id"], team_id=team_id)
        add_users_body = [resource.AddUsersBodyParams(id=user["id"])]
        added = resource.add_users(add_users_path, None, add_users_body)
        assert added is not None
        assert "error" not in added

        users_path = resource.GetAllTeamUsersPathParams(org_id=org["id"], team_id=team_id)
        users = resource.get_all_team_users(users_path, None)
        assert users is not None
        assert "error" not in users

        remove_user_path = resource.RemoveUserPathParams(
            org_id=org["id"], team_id=team_id, user_id=user["id"]
        )
        resource.remove_user(remove_user_path, None)

        renamed_name = f"{name} Renamed"
        rename_path = resource.RenamePathParams(org_id=org["id"], team_id=team_id)
        rename_body = resource.RenameBodyParams(name=renamed_name)
        renamed = resource.rename(rename_path, None, rename_body)
        assert renamed is not None
        assert "error" not in renamed
    finally:
        delete_path = resource.DeletePathParams(org_id=org["id"], team_id=team_id)
        resource.delete(delete_path, None)
