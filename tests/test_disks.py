from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.disks_resource import DisksResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_disks_get_all(client: OpsManagerClient, project) -> None:
    resource = client.disks_resource
    path_params = DisksResource.GetAllPathParams(
        project_id=project["id"],
        host_id="non-existent-host-id",
    )

    result = resource.get_all(path_params, None)
    assert result is not None
    assert result["errorCode"] == "HOST_NOT_FOUND"


def test_disks_get_one(client: OpsManagerClient, project_with_cluster) -> None:
    """Test get_one."""
    resource = client.disks_resource
    path_params = DisksResource.GetOnePathParams(
        host_id="non-existent-host-id",
        partition_name="non-existent-partition-name",
        project_id=project_with_cluster["id"],
    )
    query_params = None
    result = resource.get_one(path_params, query_params)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "HOST_NOT_FOUND"
