from uuid import uuid4

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.access_list_resource import AccessListResource


def random_ip() -> str:
    host = 1 + (int(uuid4().hex[:2], 16) % 254)
    return f"203.0.113.{host}"


def add_accesslist(client: OpsManagerClient, user_id: str, ip_address: str) -> None:
    access_list_resource = client.access_list_resource
    path_params = AccessListResource.AddEntriesPathParams(user_id=user_id)
    body_params = [AccessListResource.AddEntriesBodyParams(ip_address=ip_address)]
    access_list_resource.add_entries(path_params, None, body_params)


def delete_accesslist(client: OpsManagerClient, user_id: str, ip_address: str) -> None:
    access_list_resource = client.access_list_resource
    path_params = AccessListResource.DeleteEntryPathParams(
        user_id=user_id,
        access_list_entry=ip_address,
    )
    access_list_resource.delete_entry(path_params, None)
