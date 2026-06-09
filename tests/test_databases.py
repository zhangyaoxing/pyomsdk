from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.databases_resource import DatabasesResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_databases_get_all(client: OpsManagerClient, project_with_cluster) -> None:
    resource = client.databases_resource
    path_params = DatabasesResource.GetAllPathParams(
        host_id="non-existent-host-id", project_id=project_with_cluster["id"]
    )

    result = resource.get_all(path_params, None)
    assert result is not None


def test_databases_get_by_name(client: OpsManagerClient, project_with_cluster) -> None:
    """Test get_by_name."""
    resource = client.databases_resource
    path_params = DatabasesResource.GetByNamePathParams(
        database_name="admin",
        host_id="non-existent-host-id",
        project_id=project_with_cluster["id"],
    )
    query_params = None
    result = resource.get_by_name(path_params, query_params)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "HOST_NOT_FOUND"
