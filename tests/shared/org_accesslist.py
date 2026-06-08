from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.organization_access_lists_resource import OrganizationAccessListsResource


def add_org_access_list_entry(client: OpsManagerClient, api_key_id, org_id, ip_addr) -> dict:
    resource = OrganizationAccessListsResource
    path_params = resource.CreateEntriesPathParams(
        api_key_id=api_key_id,
        org_id=org_id,
    )
    body_params = resource.CreateEntriesBodyParams(ip_address=ip_addr)
    return client.organization_access_lists_resource.create_entries(
        path_params, None, [body_params]
    )


def delete_org_access_list_entry(client: OpsManagerClient, api_key_id, org_id, ip_addr) -> None:
    resource = OrganizationAccessListsResource
    path_params = resource.DeleteEntryPathParams(
        api_key_id=api_key_id, org_id=org_id, access_list_entry=ip_addr
    )
    client.organization_access_lists_resource.delete_entry(path_params, None)
