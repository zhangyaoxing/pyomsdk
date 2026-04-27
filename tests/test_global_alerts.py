from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.global_alerts_resource import GlobalAlertsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_global_alerts_get_all(client: OpsManagerClient) -> None:
    """Test getting all global alerts."""
    resource = client.global_alerts_resource
    result = resource.get_all(None)
    assert result is not None
    assert "error" not in result
    assert "results" in result
    assert isinstance(result["results"], list)


def test_global_alerts_get_one(client: OpsManagerClient, project) -> None:
    """Test getting a specific global alert by ID."""
    resource = client.global_alerts_resource

    path_params = GlobalAlertsResource.GetOnePathParams(alert_id=project["id"])

    result = resource.get_one(path_params, None)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "INVALID_ALERT_ID"


def test_global_alerts_acknowledge_one(client: OpsManagerClient, project) -> None:
    """Test acknowledging a global alert."""
    resource = client.global_alerts_resource

    path_params = GlobalAlertsResource.AcknowledgeOnePathParams(alert_id=project["id"])
    body_params = GlobalAlertsResource.AcknowledgeOneBodyParams(
        acknowledged_until="2099-12-31T23:59:59Z",
        acknowledgement_comment="Test acknowledgement",
    )

    result = resource.acknowledge_one(path_params, None, body_params)
    assert result is not None
    assert "error" in result
    assert result["errorCode"] == "INVALID_ALERT_ID"
