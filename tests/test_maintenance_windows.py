from pyomsdk.ops_manager_client import OpsManagerClient


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
