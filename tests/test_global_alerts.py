import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.global_alerts_resource import GlobalAlertsResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _first_global_alert_id(client: OpsManagerClient) -> str:
    """Get the first global alert ID."""
    resource = client.global_alerts_resource
    query_params = GlobalAlertsResource.GetAllQueryParams(pretty=True, page_num=1)

    result = resource.get_all(query_params)

    if isinstance(result, dict):
        results = result.get("results", [])
    elif isinstance(result, list):
        results = result
    else:
        results = []

    if not results:
        pytest.skip("No global alerts found")

    alert_id = results[0].get("id") or results[0].get("_id")
    if not alert_id:
        pytest.skip("First global alert does not expose id/_id")

    return alert_id


def test_global_alerts_get_all(client: OpsManagerClient) -> None:
    """Test getting all global alerts."""
    resource = client.global_alerts_resource
    org = None
    project = None
    user = None
    api_key = None
    query_params = build_model_or_skip(
        GlobalAlertsResource.GetAllQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all(query_params)
    assert result is not None
    assert "error" not in result


def test_global_alerts_get_one(client: OpsManagerClient) -> None:
    """Test getting a specific global alert by ID."""
    resource = client.global_alerts_resource
    alert_id = _first_global_alert_id(client)

    query_params = GlobalAlertsResource.GetOneQueryParams(pretty=True)

    result = resource.get_one(alert_id, query_params)
    assert result is not None
    assert "error" not in result


def test_global_alerts_acknowledge_one(client: OpsManagerClient) -> None:
    """Test acknowledging a global alert."""
    resource = client.global_alerts_resource
    alert_id = _first_global_alert_id(client)

    query_params = GlobalAlertsResource.AcknowledgeOneQueryParams(pretty=True)
    body_params = GlobalAlertsResource.AcknowledgeOneBodyParams(
        acknowledged_until="2099-12-31T23:59:59Z",
        acknowledgement_comment="Test acknowledgement",
    )

    result = resource.acknowledge_one(alert_id, query_params, body_params)
    assert result is not None
    assert "error" not in result
