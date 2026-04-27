from urllib.parse import quote
import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.backup_daemon_resource import BackupDaemonResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_backup_daemon_get_all(client: OpsManagerClient) -> None:
    resource = client.backup_daemon_resource
    result = resource.get_all(None)
    assert result is not None
    assert result["totalCount"] > 0


def test_backup_daemon_get_by_id(client: OpsManagerClient) -> None:
    resource = client.backup_daemon_resource
    all_result = resource.get_all(BackupDaemonResource.GetAllQueryParams())
    items = all_result if isinstance(all_result, list) else all_result.get("results", [])
    if not items:
        pytest.skip("No backup daemons configured")

    machine = items[0].get("machine").get("machine")
    head_root_dir = items[0].get("machine").get("headRootDirectory")
    head_root_dir = quote(head_root_dir, safe="")
    if not machine:
        pytest.skip("Backup daemon entry has no machine/hostname field")

    path_params = BackupDaemonResource.GetByIdPathParams(
        machine=machine, head_root_directory=head_root_dir
    )
    result = resource.get_by_id(path_params, None)
    assert result is not None
    assert result["assignmentEnabled"] is True


def test_backup_daemon_create(client: OpsManagerClient) -> None:
    """Test create."""
    resource = client.backup_daemon_resource
    path_params = BackupDaemonResource.CreatePathParams(machine="example.com")
    query_params = None
    body_params = BackupDaemonResource.CreateBodyParams(
        machine=BackupDaemonResource.CreateBodyParams.MachineParams(
            machine="example.com", head_root_directory="/data/backupd"
        )
    )
    result = resource.create(path_params, query_params, body_params)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "DAEMON_MACHINE_CONFIG_NOT_FOUND"


def test_backup_daemon_delete(client: OpsManagerClient) -> None:
    """Test delete."""
    resource = client.backup_daemon_resource
    path_params = BackupDaemonResource.DeletePathParams(
        machine="example.com", head_root_directory=quote("/data/backupd", safe="")
    )
    query_params = None
    result = resource.delete(path_params, query_params)
    assert result is None


def test_backup_daemon_update(client: OpsManagerClient) -> None:
    """Test update."""
    resource = client.backup_daemon_resource
    machine = {
        "machine": "backup-daemon",
        "head_root_directory": quote("/headDB/", safe=""),
    }
    path_params = BackupDaemonResource.UpdatePathParams(**machine)
    query_params = None
    body_params = BackupDaemonResource.UpdateBodyParams(
        assignment_enabled=True,
        machine=BackupDaemonResource.UpdateBodyParams.MachineParams(**machine),
    )
    result = resource.update(path_params, query_params, body_params)
    assert result is not None
    assert "error" not in result
    assert result["assignmentEnabled"] is True
