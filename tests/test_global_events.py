from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.global_events_resource import GlobalEventsResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_global_events_get_all(client: OpsManagerClient) -> None:
    resource = client.global_events_resource
    org = None
    project = None
    user = None
    api_key = None
    query_params = build_model_or_skip(
        GlobalEventsResource.GetAllQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all(query_params)
    assert result is not None

def test_global_events_get_one(client: OpsManagerClient, org) -> None:
    """Test get_one."""
    resource = client.global_events_resource
    project = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        GlobalEventsResource.GetOnePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        GlobalEventsResource.GetOneQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_one(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

