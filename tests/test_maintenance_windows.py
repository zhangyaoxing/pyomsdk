from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.maintenance_windows_resource import MaintenanceWindowsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_maintenance_windows_get_all(client: OpsManagerClient, project) -> None:
    resource = client.maintenance_windows_resource
    path_params = resource.GetAllPathParams(project_id=project["id"])

    result = resource.get_all(path_params, None)
    assert result is not None
    assert "error" not in result
    assert result["results"] is not None
    assert isinstance(result["results"], list)
    assert len(result["results"]) == 0


def test_maintenance_windows_create_get_update_delete(
    client: OpsManagerClient, project: dict
) -> None:
    resource = client.maintenance_windows_resource
    path_params = MaintenanceWindowsResource.CreatePathParams(project_id=project["id"])
    body_params = MaintenanceWindowsResource.CreateBodyParams(
        alert_type_names=["HOST"],
        description="Test maintenance window",
        start_date="2030-01-01T00:00:00Z",
        end_date="2030-01-01T01:00:00Z",
    )

    created = resource.create(path_params, None, body_params)
    assert created is not None
    assert "error" not in created

    mw_id = created.get("id") or created.get("_id")
    assert mw_id is not None

    try:
        get_path = MaintenanceWindowsResource.GetOnePathParams(
            project_id=project["id"], mw_id=mw_id
        )
        get_result = resource.get_one(get_path, None)
        assert get_result is not None
        assert "error" not in get_result

        update_path = MaintenanceWindowsResource.UpdatePathParams(
            project_id=project["id"], mw_id=mw_id
        )
        update_body = MaintenanceWindowsResource.UpdateBodyParams(
            alert_type_names=["HOST"],
            description="Updated test maintenance window",
            start_date="2030-01-01T00:00:00Z",
            end_date="2030-01-01T02:00:00Z",
        )
        updated = resource.update(update_path, None, update_body)
        assert updated is not None
        assert "error" not in updated
    finally:
        delete_path = MaintenanceWindowsResource.DeletePathParams(
            project_id=project["id"], mw_id=mw_id
        )
        resource.delete(delete_path, None)
