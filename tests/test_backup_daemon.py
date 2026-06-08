from urllib.parse import quote
import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.backup_daemon_resource import BackupDaemonResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_backup_daemon_get_all(client: OpsManagerClient, backup_daemon) -> None:
    assert backup_daemon is not None
    assert backup_daemon["assignmentEnabled"]


def test_backup_daemon_get_by_id(client: OpsManagerClient, backup_daemon) -> None:
    resource = client.backup_daemon_resource

    first_item = backup_daemon
    assert "machine" in first_item and "headRootDirectory" in first_item["machine"]
    machine = first_item["machine"].get("machine")
    head_root_dir = first_item["machine"].get("headRootDirectory")
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


def test_backup_daemon_update(client: OpsManagerClient, backup_daemon) -> None:
    """Test update."""
    resource = client.backup_daemon_resource
    machine = backup_daemon["machine"]
    path_params = BackupDaemonResource.UpdatePathParams(
        machine=machine.get("machine"),
        head_root_directory=quote(machine.get("headRootDirectory", ""), safe=""),
    )
    query_params = None
    body_params = BackupDaemonResource.UpdateBodyParams(
        assignment_enabled=True,
        machine=BackupDaemonResource.UpdateBodyParams.MachineParams(
            machine=machine.get("machine"), head_root_directory=machine.get("headRootDirectory", "")
        ),
    )
    result = resource.update(path_params, query_params, body_params)
    assert result is not None
    assert "error" not in result
    assert result["assignmentEnabled"] is True
