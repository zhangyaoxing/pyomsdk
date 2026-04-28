from typing import Any


from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.hosts_resource import HostsResource
from pyomsdk.resources.measurements_resource import MeasurementsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _first_host_id(client: OpsManagerClient, project_with_cluster: dict[str, Any]) -> str | None:
    result = client.hosts_resource.get_all(
        HostsResource.GetAllPathParams(project_id=project_with_cluster["id"]), None
    )
    items = result if isinstance(result, list) else result.get("results", [])
    if not items:
        return None
    return items[0].get("id") or items[0].get("_id")


def test_measurements_get_types(
    client: OpsManagerClient, project_with_cluster: dict[str, Any]
) -> None:
    resource = client.measurements_resource
    host_id = _first_host_id(client, project_with_cluster)
    path_params = MeasurementsResource.GetTypesPathParams(
        project_id=project_with_cluster["id"],
        host_id=host_id,
    )
    query_params = MeasurementsResource.GetTypesQueryParams(
        granularity="PT1M",
        period="P1D",
    )
    result = resource.get_types(path_params, query_params)
    assert result is not None
    assert "error" not in result
    assert result["hostId"] == host_id


def test_measurements_host(client: OpsManagerClient, project_with_cluster: dict[str, Any]) -> None:
    host_id = _first_host_id(client, project_with_cluster)

    resource = client.measurements_resource
    path_params = MeasurementsResource.HostPathParams(
        project_id=project_with_cluster["id"], host_id=host_id
    )
    query_params = MeasurementsResource.HostQueryParams(
        granularity="PT1M",
        period="P1D",
    )
    result = resource.host(path_params, query_params)
    assert result is not None
    assert "error" not in result
    assert result["hostId"] == host_id


def test_measurements_database(client: OpsManagerClient, project_with_cluster) -> None:
    """Test database."""
    resource = client.measurements_resource
    host_id = _first_host_id(client, project_with_cluster)
    path_params = MeasurementsResource.DatabasePathParams(
        project_id=project_with_cluster["id"],
        host_id=host_id,
        database_name="test",
    )
    query_params = MeasurementsResource.DatabaseQueryParams(
        granularity="PT1M",
        period="P1D",
    )
    result = resource.database(path_params, query_params)
    assert result is not None
    assert "error" not in result
    assert result["hostId"] == host_id


def test_measurements_disk_partition(client: OpsManagerClient, project_with_cluster) -> None:
    """Test disk_partition."""
    resource = client.measurements_resource
    host_id = _first_host_id(client, project_with_cluster)
    path_params = MeasurementsResource.DiskPartitionPathParams(
        project_id=project_with_cluster["id"],
        host_id=host_id,
        partition_name="non-existent-partition",
    )
    query_params = MeasurementsResource.DiskPartitionQueryParams(
        granularity="PT1M",
        period="P1D",
    )
    result = resource.disk_partition(path_params, query_params)
    assert result is not None
    assert "error" not in result
    assert result["hostId"] == host_id
