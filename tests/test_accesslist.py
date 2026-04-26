from typing import Any

# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.access_list_resource import AccessListResource
from tests.shared.accesslist import add_accesslist, delete_accesslist, random_ip


def test_access_list_add_entries(client: OpsManagerClient, user: dict[str, Any]) -> None:
    resource = client.access_list_resource
    ip_address = random_ip()

    path_params = AccessListResource.AddEntriesPathParams(user_id=user["id"])
    body_params = [AccessListResource.AddEntriesBodyParams(ip_address=ip_address)]

    result = resource.add_entries(path_params, None, body_params)
    assert result is not None
    assert "error" not in result

    delete_accesslist(client, user["id"], ip_address)


def test_access_list_delete_entry(client: OpsManagerClient, user: dict[str, Any]) -> None:
    resource = client.access_list_resource
    ip_address = random_ip()

    add_accesslist(client, user["id"], ip_address)

    path_params = AccessListResource.DeleteEntryPathParams(
        user_id=user["id"],
        access_list_entry=ip_address,
    )

    result = resource.delete_entry(path_params, None)
    assert result is None


def test_access_list_get_for_current_user(
    client: OpsManagerClient,
    user_with_access_list_entry: tuple[dict[str, Any], str],
) -> None:
    resource = client.access_list_resource
    created_user, _ = user_with_access_list_entry

    path_params = AccessListResource.GetForCurrentUserPathParams(user_id=created_user["id"])
    query_params = AccessListResource.GetForCurrentUserQueryParams(items_per_page=50, page_num=1)

    result = resource.get_for_current_user(path_params, query_params)
    assert result is not None
    assert "error" not in result


def test_access_list_get_for_ip_address(
    client: OpsManagerClient,
    user_with_access_list_entry: tuple[dict[str, Any], str],
) -> None:
    resource = client.access_list_resource
    created_user, ip_address = user_with_access_list_entry

    path_params = AccessListResource.GetForIpAddressPathParams(
        user_id=created_user["id"],
        access_list_entry=ip_address,
    )

    result = resource.get_for_ip_address(path_params, None)
    assert result is not None
    assert "error" not in result
