from pyomsdk.resources.enums import OrgRole
from pyomsdk.resources.organization_api_keys_resource import OrganizationApiKeysResource
from pyomsdk.ops_manager_client import OpsManagerClient


def create_org_api_key(client: OpsManagerClient, org_id, description) -> dict:
    resource = OrganizationApiKeysResource
    path_params = resource.CreatePathParams(org_id=org_id)
    role = OrgRole.ORG_OWNER
    body_params = resource.CreateBodyParams(desc=description, roles=[role])
    return client.organization_api_keys_resource.create(path_params, None, body_params)


def delete_org_api_key(client: OpsManagerClient, org_id, api_key_id) -> None:
    resource = OrganizationApiKeysResource
    path_params = resource.DeletePathParams(org_id=org_id, api_key_id=api_key_id)
    client.organization_api_keys_resource.delete(path_params, None)
