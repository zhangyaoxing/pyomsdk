from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.clusters_resource import ClustersResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_clusters_get_all_from_one_project(client: OpsManagerClient, project_with_cluster) -> None:
    resource = client.clusters_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        ClustersResource.GetAllFromOneProjectPathParams,
        client=client,
        org=org,
        project=project_with_cluster,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        ClustersResource.GetAllFromOneProjectQueryParams,
        client=client,
        org=org,
        project=project_with_cluster,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all_from_one_project(path_params, query_params)
    assert result is not None
    assert len(result["results"]) > 0


def test_clusters_get_all_from_all_projects(client: OpsManagerClient) -> None:
    """Test get_all_from_all_projects."""
    resource = client.clusters_resource
    query_params = None
    result = resource.get_all_from_all_projects(query_params)
    assert result is not None
    assert len(result["results"]) > 0


def test_clusters_get_one(client: OpsManagerClient, project_with_cluster, cluster) -> None:
    """Test get_one."""
    resource = client.clusters_resource
    path_params = ClustersResource.GetOnePathParams(
        project_id=project_with_cluster["id"], cluster_id=cluster["id"]
    )
    result = resource.get_one(path_params, None)
    assert result is not None
    assert "clusterName" in result


def test_clusters_update(client: OpsManagerClient, project_with_cluster, cluster) -> None:
    """Test update."""
    resource = client.clusters_resource
    path_params = ClustersResource.UpdatePathParams(
        project_id=project_with_cluster["id"], cluster_id=cluster["id"]
    )
    query_params = None
    body_params = ClustersResource.UpdateBodyParams(cluster_name=cluster["clusterName"])
    result = resource.update(path_params, query_params, body_params)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "NOT_SHARDED"
