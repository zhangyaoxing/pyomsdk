from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.organization_access_lists_resource import OrganizationAccessListsResource
from tests.shared.org import create_api_key


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_organization_access_lists_get_all_entries(client: OpsManagerClient, org) -> None:
    resource = client.organization_access_lists_resource
    org_key = create_api_key(client, org["id"], "Test API Key for Organization Access Lists")
    path_params = OrganizationAccessListsResource.GetAllEntriesPathParams(
        org_id=org["id"], api_key_id=org_key["id"]
    )

    result = resource.get_all_entries(path_params, None)
    assert result is not None
    assert result["results"] is not None
    assert isinstance(result["results"], list)
    assert len(result["results"]) >= 0


def test_organization_access_lists_create_entries(org_access_list_entry) -> None:
    """Test create_entries."""
    assert org_access_list_entry is not None


def test_organization_access_lists_delete_entry(
    client: OpsManagerClient, org, org_api_key, org_access_list_entry
) -> None:
    """Test delete_entry."""
    resource = client.organization_access_lists_resource
    entry = org_access_list_entry["results"][0]
    path_params = resource.DeleteEntryPathParams(
        api_key_id=org_api_key["id"], org_id=org["id"], access_list_entry=entry["ipAddress"]
    )
    result = resource.delete_entry(path_params, None)
    assert result is None


def test_organization_access_lists_get_one_entry(
    client: OpsManagerClient, org, org_api_key, org_access_list_entry
) -> None:
    """Test get_one_entry."""
    resource = client.organization_access_lists_resource
    entry = org_access_list_entry["results"][0]
    path_params = resource.GetOneEntryPathParams(
        api_key_id=org_api_key["id"], org_id=org["id"], access_list_entry=entry["ipAddress"]
    )
    result = resource.get_one_entry(path_params, None)
    assert result is not None
    assert result["ipAddress"] == entry["ipAddress"]
