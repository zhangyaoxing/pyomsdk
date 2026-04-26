import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.backup_daemon_resource import BackupDaemonResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_backup_daemon_get_all(client: OpsManagerClient) -> None:
    resource = client.backup_daemon_resource
    query_params = BackupDaemonResource.GetAllQueryParams(pretty=True)
    result = resource.get_all(query_params)
    assert result is not None
    assert_success_or_skip(result)


def test_backup_daemon_get_by_id(client: OpsManagerClient) -> None:
    resource = client.backup_daemon_resource
    all_result = resource.get_all(BackupDaemonResource.GetAllQueryParams())
    items = all_result if isinstance(all_result, list) else all_result.get("results", [])
    if not items:
        pytest.skip("No backup daemons configured")

    machine = items[0].get("machine") or items[0].get("hostname")
    head_root_dir = items[0].get("headRootDirectory") or ""
    if not machine:
        pytest.skip("Backup daemon entry has no machine/hostname field")

    path_params = BackupDaemonResource.GetByIdPathParams(
        machine=machine, head_root_directory=head_root_dir
    )
    result = resource.get_by_id(path_params, None)
    assert result is not None
    assert_success_or_skip(result)


def test_backup_daemon_create(client: OpsManagerClient, project) -> None:
    """Test create."""
    resource = client.backup_daemon_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        BackupDaemonResource.CreatePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        BackupDaemonResource.CreateQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    body_params = build_model_or_skip(
        BackupDaemonResource.CreateBodyParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.create(path_params, query_params, body_params)
    assert result is not None
    assert_success_or_skip(result)


def test_backup_daemon_delete(client: OpsManagerClient, project) -> None:
    """Test delete."""
    resource = client.backup_daemon_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        BackupDaemonResource.DeletePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        BackupDaemonResource.DeleteQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.delete(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)


def test_backup_daemon_update(client: OpsManagerClient, project) -> None:
    """Test update."""
    resource = client.backup_daemon_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        BackupDaemonResource.UpdatePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        BackupDaemonResource.UpdateQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    body_params = build_model_or_skip(
        BackupDaemonResource.UpdateBodyParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.update(path_params, query_params, body_params)
    assert result is not None
    assert_success_or_skip(result)
