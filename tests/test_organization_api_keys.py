from pyomsdk.ops_manager_client import OpsManagerClient
from tests.shared.org_api_key import create_org_api_key

# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_organization_api_keys_get_all(client: OpsManagerClient, org) -> None:
    resource = client.organization_api_keys_resource
    path_params = resource.GetAllPathParams(org_id=org["id"])
    result = resource.get_all(path_params, None)
    assert result is not None


def test_organization_api_keys_create(org_api_key) -> None:
    assert org_api_key is not None
    assert "id" in org_api_key


def test_organization_api_keys_delete(client: OpsManagerClient, org) -> None:
    resource = client.organization_api_keys_resource
    api_key = create_org_api_key(client, org["id"], "Test API Key")
    path_params = resource.DeletePathParams(org_id=org["id"], api_key_id=api_key["id"])
    result = resource.delete(path_params, None)
    assert result is None
