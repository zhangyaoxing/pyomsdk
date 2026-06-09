from pyomsdk.ops_manager_client import OpsManagerClient


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_performance_advisor_get_namespaces(client: OpsManagerClient, project_with_cluster) -> None:
    resource = client.performance_advisor_resource
    path_params = resource.GetNamespacesPathParams(
        project_id=project_with_cluster["id"], host_id="mongo_1_1"
    )

    result = resource.get_namespaces(path_params, None)
    assert result is not None


def test_performance_advisor_get_slow_query_logs(
    client: OpsManagerClient, project_with_cluster
) -> None:
    """Test get_slow_query_logs."""
    resource = client.performance_advisor_resource
    path_params = resource.GetSlowQueryLogsPathParams(
        project_id=project_with_cluster["id"], host_id="mongo_1_1"
    )
    result = resource.get_slow_query_logs(path_params, None)
    assert result is not None
    assert "error" not in result


def test_performance_advisor_get_suggested_indexes(
    client: OpsManagerClient, project_with_cluster
) -> None:
    """Test get_suggested_indexes."""
    resource = client.performance_advisor_resource
    path_params = resource.GetSuggestedIndexesPathParams(
        project_id=project_with_cluster["id"], host_id="mongo_1_1"
    )
    result = resource.get_suggested_indexes(path_params, None)
    assert result is not None
    assert "error" not in result
