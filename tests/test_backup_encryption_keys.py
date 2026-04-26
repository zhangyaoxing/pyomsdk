from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.backup_encryption_keys_resource import BackupEncryptionKeysResource
from pyomsdk.resources.clusters_resource import ClustersResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _first_cluster_id(client: OpsManagerClient, project_id: str) -> str | None:
    result = client.clusters_resource.get_all_from_one_project(
        ClustersResource.GetAllFromOneProjectPathParams(project_id=project_id), None
    )
    items = result if isinstance(result, list) else result.get("results", [])
    if not items:
        return None
    return items[0].get("id") or items[0].get("_id")


def test_backup_encryption_keys_retrieve_kmip_master_key_id(
    client: OpsManagerClient, project: dict[str, Any]
) -> None:
    cluster_id = _first_cluster_id(client, project["id"])
    if not cluster_id:
        pytest.skip("No clusters found in project")

    resource = client.backup_encryption_keys_resource
    path_params = BackupEncryptionKeysResource.RetrieveKmipMasterKeyIdPathParams(
        group_id=project["id"], cluster_id=cluster_id
    )
    result = resource.retrieve_kmip_master_key_id(path_params, None)
    assert result is not None
    assert "error" not in result

def test_backup_encryption_keys_rotate_kmip_master_key_id(client: OpsManagerClient, project) -> None:
    """Test rotate_kmip_master_key_id."""
    resource = client.backup_encryption_keys_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        BackupEncryptionKeysResource.RotateKmipMasterKeyIdPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        BackupEncryptionKeysResource.RotateKmipMasterKeyIdQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.rotate_kmip_master_key_id(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

