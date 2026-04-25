from typing import Any
import pytest
from shared import get_client
from pyomsdk.resources.enums import AllRole
from pyomsdk.resources.users_resource import UsersResource


def get_user_info() -> dict[str, Any]:
    user_info = {
        "email_address": "new.user@example.com",
        "first_name": "New",
        "last_name": "User",
        "password": "Passw0rd!",
        "username": "new.user",
    }
    return user_info


def asserts_user_info(user: dict[str, Any]) -> None:
    user_info = get_user_info()
    assert user["emailAddress"] == user_info["email_address"]
    assert user["firstName"] == user_info["first_name"]
    assert user["lastName"] == user_info["last_name"]
    assert user["username"] == user_info["username"]


@pytest.fixture(name="user")
def new_user():
    client = get_client()
    result = add_user(client)

    yield result

    delete_user(client, result["id"])


def add_user(client: Any) -> dict[str, Any]:
    resource = client.users_resource
    body_params = UsersResource.CreateBodyParams(
        **get_user_info(),
        roles=[
            UsersResource.CreateBodyParams.RolesParams(
                role_name=AllRole.GLOBAL_READ_ONLY,
            )
        ],
    )

    result = resource.create(None, body_params)
    return result


def delete_user(client: Any, user_id: str) -> None:
    resource = client.users_resource
    delete_path_params = UsersResource.DeletePathParams(user_id=user_id)
    delete_query_params = UsersResource.DeleteQueryParams(envelope=True)
    resource.delete(delete_path_params, delete_query_params)


def test_users_create_first_user() -> None:
    client = get_client()
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


def test_users_get_by_id(user) -> None:
    client = get_client()
    resource = client.users_resource
    created_user = user

    path_params = UsersResource.GetByIdPathParams(user_id=created_user["id"])
    query_params = UsersResource.GetByIdQueryParams(pretty=True)

    user = resource.get_by_id(path_params, query_params)
    assert user is not None
    asserts_user_info(user)


def test_users_get_by_name(user) -> None:
    client = get_client()
    resource = client.users_resource
    created_user = user
    path_params = UsersResource.GetByNamePathParams(user_name=created_user["username"])

    user = resource.get_by_name(path_params, None)
    asserts_user_info(user)


def test_users_update_roles(user) -> None:
    client = get_client()
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
    assert result["roles"][0]["roleName"] == AllRole.GLOBAL_BACKUP_ADMIN


def test_users_delete() -> None:
    client = get_client()
    resource = client.users_resource
    created_user = add_user(client)

    path_params = UsersResource.DeletePathParams(user_id=created_user["id"])

    result = resource.delete(path_params, None)

    assert result is None
