from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.events_resource import EventsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_events_get_all_project(client: OpsManagerClient, project) -> None:
    resource = client.events_resource
    path_params = EventsResource.GetAllProjectPathParams(
        group_id=project["id"],
    )
    query_params = None
    result = resource.get_all_project(path_params, query_params)
    assert result is not None
    assert len(result["results"]) == 3


def test_events_get_all_organization(client: OpsManagerClient, org) -> None:
    """Test get_all_organization."""
    resource = client.events_resource
    path_params = EventsResource.GetAllOrganizationPathParams(
        org_id=org["id"],
    )
    query_params = None
    result = resource.get_all_organization(path_params, query_params)
    assert result is not None
    assert len(result["results"]) > 0


def test_events_get_one_organization(client: OpsManagerClient, org) -> None:
    """Test get_one_organization."""
    resource = client.events_resource
    path_params = EventsResource.GetOneOrganizationPathParams(
        org_id=org["id"],
        event_id=org["id"],
    )
    query_params = None
    result = resource.get_one_organization(path_params, query_params)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "ORG_EVENT_NOT_FOUND"


def test_events_get_one_project(client: OpsManagerClient, project) -> None:
    """Test get_one_project."""
    resource = client.events_resource
    path_params = EventsResource.GetOneProjectPathParams(
        group_id=project["id"],
        event_id=project["id"],
    )
    query_params = None
    result = resource.get_one_project(path_params, query_params)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "EVENT_NOT_FOUND"
