from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.performance_advisor_resource import PerformanceAdvisorResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_performance_advisor_get_namespaces(client: OpsManagerClient, project) -> None:
    resource = client.performance_advisor_resource
    org = None
    project = project
    user = None
    api_key = None
    path_params = build_model_or_skip(
        PerformanceAdvisorResource.GetNamespacesPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        PerformanceAdvisorResource.GetNamespacesQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_namespaces(path_params, query_params)
    assert result is not None

def test_performance_advisor_get_slow_query_logs(client: OpsManagerClient, project) -> None:
    """Test get_slow_query_logs."""
    resource = client.performance_advisor_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        PerformanceAdvisorResource.GetSlowQueryLogsPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        PerformanceAdvisorResource.GetSlowQueryLogsQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_slow_query_logs(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

def test_performance_advisor_get_suggested_indexes(client: OpsManagerClient, project) -> None:
    """Test get_suggested_indexes."""
    resource = client.performance_advisor_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        PerformanceAdvisorResource.GetSuggestedIndexesPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        PerformanceAdvisorResource.GetSuggestedIndexesQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_suggested_indexes(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

