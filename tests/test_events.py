from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.events_resource import EventsResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_events_get_all_project(client: OpsManagerClient, project) -> None:
    resource = client.events_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        EventsResource.GetAllProjectPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        EventsResource.GetAllProjectQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all_project(path_params, query_params)
    assert result is not None


def test_events_get_all_organization(client: OpsManagerClient, project) -> None:
    """Test get_all_organization."""
    resource = client.events_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        EventsResource.GetAllOrganizationPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        EventsResource.GetAllOrganizationQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_all_organization(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)


def test_events_get_one_organization(client: OpsManagerClient, project) -> None:
    """Test get_one_organization."""
    resource = client.events_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        EventsResource.GetOneOrganizationPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        EventsResource.GetOneOrganizationQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_one_organization(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)


def test_events_get_one_project(client: OpsManagerClient, project) -> None:
    """Test get_one_project."""
    resource = client.events_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        EventsResource.GetOneProjectPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        EventsResource.GetOneProjectQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_one_project(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)
