from typing import Any

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.migrate_to_mongodb_atlas_resource import MigrateToMongodbAtlasResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_migrate_to_mongodb_atlas_return_connection_status(
    client: OpsManagerClient, org: dict[str, Any]
) -> None:
    resource = client.migrate_to_mongodb_atlas_resource
    path_params = MigrateToMongodbAtlasResource.ReturnConnectionStatusPathParams(org_id=org["id"])
    result = resource.return_connection_status(path_params, None)
    assert result is not None
    assert_success_or_skip(result)


def test_migrate_to_mongodb_atlas_connect_with_atlas_organization(
    client: OpsManagerClient, org
) -> None:
    """Test connect_with_atlas_organization."""
    resource = client.migrate_to_mongodb_atlas_resource
    project = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        MigrateToMongodbAtlasResource.ConnectWithAtlasOrganizationPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        MigrateToMongodbAtlasResource.ConnectWithAtlasOrganizationQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    body_params = build_model_or_skip(
        MigrateToMongodbAtlasResource.ConnectWithAtlasOrganizationBodyParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.connect_with_atlas_organization(path_params, query_params, body_params)
    assert result is not None
    assert_success_or_skip(result)


def test_migrate_to_mongodb_atlas_remove_connection(client: OpsManagerClient, org) -> None:
    """Test remove_connection."""
    resource = client.migrate_to_mongodb_atlas_resource
    project = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        MigrateToMongodbAtlasResource.RemoveConnectionPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        MigrateToMongodbAtlasResource.RemoveConnectionQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.remove_connection(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)
