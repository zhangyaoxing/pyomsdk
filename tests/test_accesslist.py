from collections.abc import Generator
from typing import Any
from uuid import uuid4

import pytest

# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name

from conftest import get_client
from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.access_list_resource import AccessListResource


def _random_ip_address() -> str:
    host = 1 + (int(uuid4().hex[:2], 16) % 254)
    return f"203.0.113.{host}"


def _add_access_list_entry(client: Any, user_id: str, ip_address: str) -> None:
    access_list_resource = client.access_list_resource
    path_params = AccessListResource.AddEntriesPathParams(user_id=user_id)
    body_params = [AccessListResource.AddEntriesBodyParams(ip_address=ip_address)]
    access_list_resource.add_entries(path_params, None, body_params)


def _delete_access_list_entry(client: Any, user_id: str, ip_address: str) -> None:
    access_list_resource = client.access_list_resource
    path_params = AccessListResource.DeleteEntryPathParams(
        user_id=user_id,
        access_list_entry=ip_address,
    )
    access_list_resource.delete_entry(path_params, None)


@pytest.fixture(name="user_with_access_list_entry")
def _user_with_access_list_entry_fixture(
    client: OpsManagerClient,
    user: dict[str, Any],
) -> Generator[tuple[dict[str, Any], str], None, None]:
    ip_address = _random_ip_address()
    _add_access_list_entry(client, user["id"], ip_address)
    yield user, ip_address
    _delete_access_list_entry(client, user["id"], ip_address)


def test_access_list_add_entries(client: OpsManagerClient, user: dict[str, Any]) -> None:
    resource = client.access_list_resource
    ip_address = _random_ip_address()

    path_params = AccessListResource.AddEntriesPathParams(user_id=user["id"])
    body_params = [AccessListResource.AddEntriesBodyParams(ip_address=ip_address)]

    result = resource.add_entries(path_params, None, body_params)
    assert result is not None

    _delete_access_list_entry(client, user["id"], ip_address)


def test_access_list_delete_entry(client: OpsManagerClient, user: dict[str, Any]) -> None:
    resource = client.access_list_resource
    ip_address = _random_ip_address()

    _add_access_list_entry(client, user["id"], ip_address)

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
