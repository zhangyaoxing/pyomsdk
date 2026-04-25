from typing import Any
from pyomsdk import OpsManagerClient
from pyomsdk.resources.enums import AllRole


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
    body_params = users_resource.CreateBodyParams(
        **user_info,
        roles=[
            users_resource.CreateBodyParams.RolesParams(
                role_name=AllRole.GLOBAL_OWNER,
            )
        ],
    )
    return users_resource.create(None, body_params)


def delete_user(client: OpsManagerClient, user_id: str) -> dict[str, Any]:
    users_resource = client.users_resource
    path_params = users_resource.DeletePathParams(user_id=user_id)
    return users_resource.delete(path_params, None)
