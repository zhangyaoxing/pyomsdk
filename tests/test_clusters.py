from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.clusters_resource import ClustersResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_clusters_get_all_from_one_project(client: OpsManagerClient, project) -> None:
    resource = client.clusters_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        ClustersResource.GetAllFromOneProjectPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        ClustersResource.GetAllFromOneProjectQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all_from_one_project(path_params, query_params)
    assert result is not None


def test_clusters_get_all_from_all_projects(client: OpsManagerClient, project) -> None:
    """Test get_all_from_all_projects."""
    resource = client.clusters_resource
    org = None
    user = None
    api_key = None
    query_params = build_model_or_skip(
        ClustersResource.GetAllFromAllProjectsQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_all_from_all_projects(query_params)
    assert result is not None
    assert_success_or_skip(result)


def test_clusters_get_one(client: OpsManagerClient, project) -> None:
    """Test get_one."""
    resource = client.clusters_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        ClustersResource.GetOnePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        ClustersResource.GetOneQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_one(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)


def test_clusters_update(client: OpsManagerClient, project) -> None:
    """Test update."""
    resource = client.clusters_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        ClustersResource.UpdatePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        ClustersResource.UpdateQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    body_params = build_model_or_skip(
        ClustersResource.UpdateBodyParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.update(path_params, query_params, body_params)
    assert result is not None
    assert_success_or_skip(result)
