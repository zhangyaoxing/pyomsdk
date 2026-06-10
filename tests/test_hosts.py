from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.hosts_resource import HostsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_hosts_get_all(client: OpsManagerClient, project_with_cluster, cluster) -> None:
    resource = client.hosts_resource
    path_params = HostsResource.GetAllPathParams(project_id=project_with_cluster["id"])
    query_params = HostsResource.GetAllQueryParams(
        cluster_id=cluster["id"],
    )

    result = resource.get_all(path_params, query_params)
    assert result is not None
    assert "results" in result
    assert isinstance(result["results"], list)
    assert len(result["results"]) > 0


def test_hosts_get_by_id_and_hostname_port(
    client: OpsManagerClient, project_with_cluster, cluster
) -> None:
    resource = client.hosts_resource
    all_path = HostsResource.GetAllPathParams(project_id=project_with_cluster["id"])
    all_query = HostsResource.GetAllQueryParams(cluster_id=cluster["id"])
    all_hosts = resource.get_all(all_path, all_query)
    host = all_hosts["results"][0]

    host_id = host.get("id") or host.get("_id")
    assert host_id is not None

    by_id_path = HostsResource.GetByIdPathParams(
        project_id=project_with_cluster["id"], host_id=host_id
    )
    by_id = resource.get_by_id(by_id_path, None)
    assert by_id is not None
    assert "error" not in by_id

    hostname = host.get("hostname") or host.get("hostName")
    port = host.get("port")
    assert hostname is not None
    assert port is not None

    by_name_path = HostsResource.GetByHostnamePortPathParams(
        project_id=project_with_cluster["id"], hostname=hostname, port=str(port)
    )
    by_name = resource.get_by_hostname_port(by_name_path, None)
    assert by_name is not None
    assert "error" not in by_name
