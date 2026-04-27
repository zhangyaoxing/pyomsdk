from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.backup_encryption_keys_resource import BackupEncryptionKeysResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_backup_encryption_keys_retrieve_kmip_master_key_id(
    client: OpsManagerClient, project_with_cluster: dict[str, Any], cluster: dict[str, Any]
) -> None:
    cluster_id = cluster["id"]
    if not cluster_id:
        pytest.skip("No clusters found in project")

    resource = client.backup_encryption_keys_resource
    path_params = BackupEncryptionKeysResource.RetrieveKmipMasterKeyIdPathParams(
        project_id=project_with_cluster["id"], cluster_id=cluster_id
    )
    result = resource.retrieve_kmip_master_key_id(path_params, None)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "GET_ENCRYPTION_KEY_DISABLED_FOR_WT_CHECKPOINTS"


def test_backup_encryption_keys_rotate_kmip_master_key_id(
    client: OpsManagerClient, project_with_cluster: dict[str, Any], cluster: dict[str, Any]
) -> None:
    """Test rotate_kmip_master_key_id."""
    resource = client.backup_encryption_keys_resource
    path_params = BackupEncryptionKeysResource.RotateKmipMasterKeyIdPathParams(
        project_id=project_with_cluster["id"], cluster_id=cluster["id"]
    )
    result = resource.rotate_kmip_master_key_id(
        path_params, BackupEncryptionKeysResource.RotateKmipMasterKeyIdQueryParams(pretty=True)
    )
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "CANNOT_ROTATE_KEY_ENCRYPTION_DISABLED"
