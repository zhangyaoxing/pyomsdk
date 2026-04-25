from typing import Any
from uuid import uuid4

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.organizations_resource import OrganizationsResource
from tests.shared.org import create_org, delete_org


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _org_id(org: dict[str, Any]) -> str:
    return org.get("id") or org.get("_id")


def test_organizations_create_organization(client: OpsManagerClient) -> None:
    org_name = f"Temp Org {uuid4().hex[:8]}"
    created_org = create_org(client, org_name)

    assert created_org is not None
    assert _org_id(created_org) is not None
    assert created_org.get("name") == org_name

    delete_org(client, _org_id(created_org))


def test_organizations_get_one_organization(client: OpsManagerClient, org: dict[str, Any]) -> None:
    resource = client.organizations_resource

    path_params = OrganizationsResource.GetOneOrganizationPathParams(org_id=_org_id(org))
    query_params = OrganizationsResource.GetOneOrganizationQueryParams(pretty=True)

    result = resource.get_one_organization(path_params, query_params)
    assert result is not None
    assert _org_id(result) == _org_id(org)


def test_organizations_get_all_organizations(client: OpsManagerClient, org: dict[str, Any]) -> None:
    resource = client.organizations_resource

    query_params = OrganizationsResource.GetAllOrganizationsQueryParams(pretty=True, page_num=1)

    result = resource.get_all_organizations(query_params)
    assert result is not None

    organizations = result.get("results", [])
    assert isinstance(organizations, list)
    assert any(_org_id(item) == _org_id(org) for item in organizations)


def test_organizations_rename_organization(client: OpsManagerClient) -> None:
    original_name = f"Temp Org {uuid4().hex[:8]}"
    renamed_name = f"Renamed Org {uuid4().hex[:8]}"
    created_org = create_org(client, original_name)
    created_org_id = _org_id(created_org)

    resource = client.organizations_resource
    path_params = OrganizationsResource.RenameOrganizationPathParams(org_id=created_org_id)
    query_params = OrganizationsResource.RenameOrganizationQueryParams(pretty=True)
    body_params = OrganizationsResource.RenameOrganizationBodyParams(name=renamed_name)

    result = resource.rename_organization(path_params, query_params, body_params)
    assert result is not None
    assert _org_id(result) == created_org_id
    assert result.get("name") == renamed_name

    delete_org(client, created_org_id)


def test_organizations_get_all_projects(
    client: OpsManagerClient,
    org: dict[str, Any],
    project: dict[str, Any],
) -> None:
    resource = client.organizations_resource

    path_params = OrganizationsResource.GetAllProjectsPathParams(org_id=_org_id(org))
    query_params = OrganizationsResource.GetAllProjectsQueryParams(pretty=True, page_num=1)

    result = resource.get_all_projects(path_params, query_params)
    assert result is not None

    projects = result.get("results", [])
    assert isinstance(projects, list)
    assert any(
        (item.get("id") or item.get("_id")) == (project.get("id") or project.get("_id"))
        for item in projects
    )


def test_organizations_delete_organization(client: OpsManagerClient) -> None:
    org_name = f"Temp Org {uuid4().hex[:8]}"
    created_org = create_org(client, org_name)
    created_org_id = _org_id(created_org)

    resource = client.organizations_resource
    path_params = OrganizationsResource.DeleteOrganizationPathParams(org_id=created_org_id)

    result = resource.delete_organization(path_params, None)
    assert result is None
