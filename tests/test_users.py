from pytest import mark
from shared import get_client
from pyomsdk.resources.enums import AllRole
from pyomsdk.resources.users_resource import UsersResource


@mark.run(order=1)
def test_users_create_first_user() -> None:
    client = get_client()
    resource = client.users_resource

    query_params = UsersResource.CreateFirstUserQueryParams(whitelist="203.0.113.10")
    body_params = UsersResource.CreateFirstUserBodyParams(
        email_address="first.user@example.com",
        first_name="First",
        last_name="User",
        password="Passw0rd!",
        username="first.user@example.com",
    )

    resource.create_first_user(query_params, body_params)


@mark.run(order=2)
def test_users_create() -> None:
    client = get_client()
    resource = client.users_resource

    query_params = UsersResource.CreateQueryParams(envelope=True)
    body_params = UsersResource.CreateBodyParams(
        email_address="new.user@example.com",
        first_name="New",
        last_name="User",
        mobile_number="+1-202-555-0101",
        password="Passw0rd!",
        roles=[
            UsersResource.CreateBodyParams.RolesParams(
                role_name=AllRole.GLOBAL_READ_ONLY,
            )
        ],
        username="new.user@example.com",
    )

    resource.create(query_params, body_params)


@mark.run(order=3)
def test_users_get_by_id() -> None:
    client = get_client()
    resource = client.users_resource

    path_params = UsersResource.GetByIdPathParams(user_id="698117018b47f47002806d04")
    query_params = UsersResource.GetByIdQueryParams(pretty=True)

    resource.get_by_id(path_params, query_params)


@mark.run(order=4)
def test_users_get_by_name() -> None:
    client = get_client()
    resource = client.users_resource

    path_params = UsersResource.GetByNamePathParams(user_name="new.user@example.com")
    query_params = UsersResource.GetByNameQueryParams(envelope=True)

    resource.get_by_name(path_params, query_params)


@mark.run(order=5)
def test_users_update_roles() -> None:
    client = get_client()
    resource = client.users_resource

    path_params = UsersResource.UpdateRolesPathParams(user_id="698117018b47f47002806d04")
    query_params = UsersResource.UpdateRolesQueryParams(pretty=True)
    body_params = UsersResource.UpdateRolesBodyParams(
        roles=[
            UsersResource.UpdateRolesBodyParams.RolesParams(
                role_name=AllRole.GLOBAL_READ_ONLY,
            )
        ]
    )

    resource.update_roles(path_params, query_params, body_params)


@mark.run(order=6)
def test_users_delete() -> None:
    client = get_client()
    resource = client.users_resource

    path_params = UsersResource.DeletePathParams(user_id="698117018b47f47002806d04")
    query_params = UsersResource.DeleteQueryParams(envelope=True)

    resource.delete(path_params, query_params)
