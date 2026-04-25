from typing import Any
from conftest import get_user_info, get_client, add_user, delete_user
from pyomsdk.resources.enums import AllRole
from pyomsdk.resources.users_resource import UsersResource


def asserts_user_info(user: dict[str, Any]) -> None:
    user_info = get_user_info()
    assert user["emailAddress"] == user_info["email_address"]
    assert user["firstName"] == user_info["first_name"]
    assert user["lastName"] == user_info["last_name"]
    assert user["username"] == user_info["username"]


def test_users_create_first_user(client) -> None:
    resource = client.users_resource

    query_params = UsersResource.CreateFirstUserQueryParams(whitelist="203.0.113.10")
    body_params = UsersResource.CreateFirstUserBodyParams(**get_user_info())

    result = resource.create_first_user(query_params, body_params)
    assert result is not None
    user = result.get("user")
    assert user is not None
    asserts_user_info(user)

    # Cleanup: delete the created user
    user_id = user["id"]
    delete_user(client, user_id)


def test_users_create(user) -> None:
    result = user
    assert result is not None
    asserts_user_info(result)


def test_users_get_by_id(client, user) -> None:
    resource = client.users_resource
    created_user = user

    path_params = UsersResource.GetByIdPathParams(user_id=created_user["id"])
    query_params = UsersResource.GetByIdQueryParams(pretty=True)

    user = resource.get_by_id(path_params, query_params)
    assert user is not None
    asserts_user_info(user)


def test_users_get_by_name(client, user) -> None:
    resource = client.users_resource
    created_user = user
    path_params = UsersResource.GetByNamePathParams(user_name=created_user["username"])

    user = resource.get_by_name(path_params, None)
    asserts_user_info(user)


def test_users_update_roles(client, user) -> None:
    resource = client.users_resource
    created_user = user

    path_params = UsersResource.UpdateRolesPathParams(user_id=created_user["id"])
    body_params = UsersResource.UpdateRolesBodyParams(
        roles=[
            UsersResource.UpdateRolesBodyParams.RolesParams(
                role_name=AllRole.GLOBAL_BACKUP_ADMIN,
            )
        ]
    )

    result = resource.update_roles(path_params, None, body_params)
    assert result is not None
    asserts_user_info(result)
    assert len(result["roles"]) == 1
    # assert result["roles"][0]["roleName"] == AllRole.GLOBAL_BACKUP_ADMIN


def test_users_delete(client) -> None:
    resource = client.users_resource
    created_user = add_user(client, get_user_info())

    path_params = UsersResource.DeletePathParams(user_id=created_user["id"])

    result = resource.delete(path_params, None)

    assert result is None
