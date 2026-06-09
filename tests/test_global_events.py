from pyomsdk.ops_manager_client import OpsManagerClient


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_global_events_get_all(client: OpsManagerClient) -> None:
    resource = client.global_events_resource

    result = resource.get_all(None)
    assert result is not None


def test_global_events_get_one(client: OpsManagerClient, org) -> None:
    """Test get_one."""
    resource = client.global_events_resource
    path_params = resource.GetOnePathParams(event_id=org["id"])
    result = resource.get_one(path_params, None)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "GLOBAL_EVENT_NOT_FOUND"
