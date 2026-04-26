from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.alerts_resource import AlertsResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _first_alert_id(client: OpsManagerClient, project_id: str) -> str:
    """Get the first alert ID from the project's alerts list."""
    resource = client.alerts_resource
    path_params = AlertsResource.GetAllPathParams(project_id=project_id)
    query_params = AlertsResource.GetAllQueryParams(pretty=True, page_num=1)

    result = resource.get_all(path_params, query_params)

    if isinstance(result, dict):
        results = result.get("results", [])
    elif isinstance(result, list):
        results = result
    else:
        results = []

    if not results:
        pytest.skip("No alerts found in the target project")

    alert_id = results[0].get("id") or results[0].get("_id")
    if not alert_id:
        pytest.skip("First alert does not expose id/_id")

    return alert_id


def test_alerts_get_all(client: OpsManagerClient, project) -> None:
    """Test getting all alerts in a project."""
    resource = client.alerts_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        AlertsResource.GetAllPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        AlertsResource.GetAllQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all(path_params, query_params)
    assert result is not None
    assert "error" not in result


def test_alerts_get_one(client: OpsManagerClient, project: dict[str, Any]) -> None:
    """Test getting a specific alert by ID."""
    resource = client.alerts_resource
    alert_id = _first_alert_id(client, project["id"])

    path_params = AlertsResource.GetOnePathParams(
        project_id=project["id"],
        alert_id=alert_id,
    )
    query_params = AlertsResource.GetOneQueryParams(pretty=True)

    result = resource.get_one(path_params, query_params)
    assert result is not None
    assert "error" not in result


def test_alerts_acknowledge_one(client: OpsManagerClient, project: dict[str, Any]) -> None:
    """Test acknowledging an alert."""
    resource = client.alerts_resource
    alert_id = _first_alert_id(client, project["id"])

    path_params = AlertsResource.AcknowledgeOnePathParams(
        project_id=project["id"],
        alert_id=alert_id,
    )
    query_params = AlertsResource.AcknowledgeOneQueryParams(pretty=True)
    body_params = AlertsResource.AcknowledgeOneBodyParams(
        acknowledged_until="2099-12-31T23:59:59Z",
        acknowledgement_comment="Test acknowledgement",
    )

    result = resource.acknowledge_one(path_params, query_params, body_params)
    assert result is not None
    assert "error" not in result
