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
