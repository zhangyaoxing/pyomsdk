import pytest
import os
from typing import Any
from pyomsdk import OpsManagerClient
from pyomsdk.resources.enums import AllRole
from pyomsdk.resources.users_resource import UsersResource


def get_client() -> OpsManagerClient:
    public_key = os.getenv("PUBLIC_KEY", "")
    private_key = os.getenv("PRIVATE_KEY", "")
    base_url = os.getenv("BASE_URL", "")
    client = OpsManagerClient(base_url=base_url, public_key=public_key, private_key=private_key)
    return client


def get_user_info(
    username: str = "new.user",
    email_address: str = "new.user@example.com",
    first_name: str = "New",
    last_name: str = "User",
    password: str = "Passw0rd!",
) -> dict[str, Any]:
    return {
        "email_address": email_address,
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
        "username": username,
    }


def add_user(client: OpsManagerClient, user_info: dict[str, Any]) -> dict[str, Any]:
    users_resource = client.users_resource
    body_params = UsersResource.CreateBodyParams(
        **user_info,
        roles=[
            UsersResource.CreateBodyParams.RolesParams(
                role_name=AllRole.GLOBAL_OWNER,
            )
        ],
    )
    return users_resource.create(None, body_params)


def delete_user(client: OpsManagerClient, user_id: str) -> None:
    users_resource = client.users_resource
    path_params = UsersResource.DeletePathParams(user_id=user_id)
    users_resource.delete(path_params, None)


@pytest.fixture(name="user")
def new_user():
    client = get_client()
    result = add_user(client, get_user_info())

    yield result

    delete_user(client, result["id"])
