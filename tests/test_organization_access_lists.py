from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.organization_access_lists_resource import OrganizationAccessListsResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_organization_access_lists_get_all_entries(client: OpsManagerClient, org) -> None:
    resource = client.organization_access_lists_resource
    project = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        OrganizationAccessListsResource.GetAllEntriesPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        OrganizationAccessListsResource.GetAllEntriesQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all_entries(path_params, query_params)
    assert result is not None

def test_organization_access_lists_create_entries(client: OpsManagerClient, org) -> None:
    """Test create_entries."""
    resource = client.organization_access_lists_resource
    project = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        OrganizationAccessListsResource.CreateEntriesPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        OrganizationAccessListsResource.CreateEntriesQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    entry = build_model_or_skip(
        OrganizationAccessListsResource.CreateEntriesBodyParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    body_params = [entry]
    result = resource.create_entries(path_params, query_params, body_params)
    assert result is not None
    assert_success_or_skip(result)

def test_organization_access_lists_delete_entry(client: OpsManagerClient, org) -> None:
    """Test delete_entry."""
    resource = client.organization_access_lists_resource
    project = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        OrganizationAccessListsResource.DeleteEntryPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        OrganizationAccessListsResource.DeleteEntryQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.delete_entry(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

def test_organization_access_lists_get_one_entry(client: OpsManagerClient, org) -> None:
    """Test get_one_entry."""
    resource = client.organization_access_lists_resource
    project = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        OrganizationAccessListsResource.GetOneEntryPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        OrganizationAccessListsResource.GetOneEntryQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_one_entry(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

