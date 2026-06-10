from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.enums import OrgRole
from pyomsdk.resources.organization_api_keys_resource import OrganizationApiKeysResource
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


def test_organization_api_keys_get_one(
    client: OpsManagerClient, org: dict, org_api_key: dict
) -> None:
    resource = client.organization_api_keys_resource
    path_params = OrganizationApiKeysResource.GetOnePathParams(
        org_id=org["id"], api_key_id=org_api_key["id"]
    )

    result = resource.get_one(path_params, None)
    assert result is not None
    assert "error" not in result
    assert result["id"] == org_api_key["id"]


def test_organization_api_keys_update(
    client: OpsManagerClient, org: dict, org_api_key: dict
) -> None:
    resource = client.organization_api_keys_resource
    path_params = OrganizationApiKeysResource.UpdatePathParams(
        org_id=org["id"], api_key_id=org_api_key["id"]
    )
    body_params = OrganizationApiKeysResource.UpdateBodyParams(
        desc="Updated Test API Key", roles=[OrgRole.ORG_OWNER]
    )

    result = resource.update(path_params, None, body_params)
    assert result is not None
    assert "error" not in result
    assert result["id"] == org_api_key["id"]
