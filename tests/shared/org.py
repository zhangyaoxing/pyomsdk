from pyomsdk import OpsManagerClient
from pyomsdk.resources.enums import OrgRole


def create_org(client: OpsManagerClient, org_name: str) -> str:
    """Create a new organization and return its ID."""
    orgs_resource = client.organizations_resource
    org = orgs_resource.create_organization(
        None, body_params=orgs_resource.CreateOrganizationBodyParams(name=org_name)
    )
    return org


def delete_org(client: OpsManagerClient, org_id: str) -> None:
    """Delete an organization by its ID."""
    orgs_resource = client.organizations_resource
    path_params = orgs_resource.DeleteOrganizationPathParams(org_id=org_id)
    orgs_resource.delete_organization(path_params, None)


def create_api_key(client: OpsManagerClient, org_id: str, desc: str) -> dict:
    """Create an API key for the organization."""
    api_keys_resource = client.organization_api_keys_resource
    path_params = api_keys_resource.CreatePathParams(org_id=org_id)
    body_params = api_keys_resource.CreateBodyParams(desc=desc, roles=[OrgRole.ORG_OWNER])
    return api_keys_resource.create(path_params, None, body_params)
