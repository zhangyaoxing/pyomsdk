from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.databases_resource import DatabasesResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_databases_get_all(client: OpsManagerClient, project) -> None:
    resource = client.databases_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        DatabasesResource.GetAllPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        DatabasesResource.GetAllQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all(path_params, query_params)
    assert result is not None


def test_databases_get_by_name(client: OpsManagerClient, project) -> None:
    """Test get_by_name."""
    resource = client.databases_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        DatabasesResource.GetByNamePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        DatabasesResource.GetByNameQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_by_name(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)
