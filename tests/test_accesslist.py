from shared import get_client
from pyomsdk.resources.access_list_resource import AccessListResource


def test_access_list_add_entries() -> None:
    client = get_client()
    resource = client.access_list_resource

    path_params = AccessListResource.AddEntriesPathParams(user_id="user-1")
    query_params = AccessListResource.AddEntriesQueryParams(envelope=True, page_num=2)
    body_params = [AccessListResource.AddEntriesBodyParams(ip_address="192.168.1.1")]

    resource.add_entries(path_params, query_params, body_params)


def test_access_list_delete_entry() -> None:
    client = get_client()
    resource = client.access_list_resource

    path_params = AccessListResource.DeleteEntryPathParams(
        user_id="user-1", access_list_entry="10.0.0.1"
    )
    query_params = AccessListResource.DeleteEntryQueryParams(pretty=True)

    resource.delete_entry(path_params, query_params)


def test_access_list_get_for_current_user() -> None:
    client = get_client()
    resource = client.access_list_resource

    path_params = AccessListResource.GetForCurrentUserPathParams(user_id="user-1")
    query_params = AccessListResource.GetForCurrentUserQueryParams(items_per_page=50, page_num=3)

    resource.get_for_current_user(path_params, query_params)


def test_access_list_get_for_ip_address() -> None:
    client = get_client()
    resource = client.access_list_resource

    path_params = AccessListResource.GetForIpAddressPathParams(
        user_id="user-1", access_list_entry="203.0.113.5"
    )
    query_params = AccessListResource.GetForIpAddressQueryParams(envelope=True)

    resource.get_for_ip_address(path_params, query_params)
