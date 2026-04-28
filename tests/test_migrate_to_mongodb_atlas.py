from typing import Any

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.migrate_to_mongodb_atlas_resource import MigrateToMongodbAtlasResource


def test_migrate_to_mongodb_atlas_return_connection_status(
    client: OpsManagerClient, org: dict[str, Any]
) -> None:
    resource = client.migrate_to_mongodb_atlas_resource
    path_params = MigrateToMongodbAtlasResource.ReturnConnectionStatusPathParams(org_id=org["id"])
    result = resource.return_connection_status(path_params, None)
    assert result is not None
    assert result["error"] == 404


def test_migrate_to_mongodb_atlas_connect_with_atlas_organization(
    client: OpsManagerClient, org
) -> None:
    """Test connect_with_atlas_organization."""
    resource = client.migrate_to_mongodb_atlas_resource
    path_params = MigrateToMongodbAtlasResource.ConnectWithAtlasOrganizationPathParams(
        org_id=org["id"]
    )
    body_params = MigrateToMongodbAtlasResource.ConnectWithAtlasOrganizationBodyParams(
        link_token="mock-link-token"
    )
    result = resource.connect_with_atlas_organization(path_params, None, body_params)
    assert result is not None
    assert "error" in result
    assert result["error"] == 404


def test_migrate_to_mongodb_atlas_remove_connection(client: OpsManagerClient, org) -> None:
    """Test remove_connection."""
    resource = client.migrate_to_mongodb_atlas_resource
    path_params = MigrateToMongodbAtlasResource.RemoveConnectionPathParams(org_id=org["id"])
    result = resource.remove_connection(path_params, None)
    assert result is not None
    assert "error" in result
    assert result["error"] == 404
