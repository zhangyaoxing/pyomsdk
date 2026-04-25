from pyomsdk import OpsManagerClient


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
