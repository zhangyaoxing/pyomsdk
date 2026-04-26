from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.alert_configurations_resource import AlertConfigurationsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _alert_config_id(alert_config: dict[str, Any]) -> str | None:
    return alert_config.get("id") or alert_config.get("_id")


def _results_list(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        results = payload.get("results")
        if isinstance(results, list):
            return results
        return []
    if isinstance(payload, list):
        return payload
    return []


def _first_alert_config_id(
    client: OpsManagerClient,
    project_id: str,
) -> str:
    resource = client.alert_configurations_resource
    path_params = AlertConfigurationsResource.GetAllForAProjectPathParams(project_id=project_id)
    query_params = AlertConfigurationsResource.GetAllForAProjectQueryParams(pretty=True, page_num=1)

    result = resource.get_all_for_a_project(path_params, query_params)
    configs = _results_list(result)

    if not configs:
        pytest.skip("No alert configurations found in the target project")

    config_id = _alert_config_id(configs[0])
    if not config_id:
        pytest.skip("First alert configuration does not expose id/_id")

    return config_id


def test_alert_configurations_get_all_for_a_project(
    client: OpsManagerClient,
    project: dict[str, Any],
) -> None:
    resource = client.alert_configurations_resource

    path_params = AlertConfigurationsResource.GetAllForAProjectPathParams(project_id=project["id"])
    query_params = AlertConfigurationsResource.GetAllForAProjectQueryParams(pretty=True, page_num=1)

    result = resource.get_all_for_a_project(path_params, query_params)
    assert result is not None
    assert "error" not in result

    configs = _results_list(result)
    assert isinstance(configs, list)


def test_alert_configurations_get_one(
    client: OpsManagerClient,
    project: dict[str, Any],
) -> None:
    resource = client.alert_configurations_resource
    alert_config_id = _first_alert_config_id(client, project["id"])

    path_params = AlertConfigurationsResource.GetOnePathParams(
        project_id=project["id"],
        alert_config_id=alert_config_id,
    )
    query_params = AlertConfigurationsResource.GetOneQueryParams(pretty=True)

    result = resource.get_one(path_params, query_params)
    assert result is not None
    assert "error" not in result
    assert _alert_config_id(result) == alert_config_id


def test_alert_configurations_get_open_alerts(
    client: OpsManagerClient,
    project: dict[str, Any],
) -> None:
    resource = client.alert_configurations_resource
    alert_config_id = _first_alert_config_id(client, project["id"])

    path_params = AlertConfigurationsResource.GetOpenAlertsPathParams(
        project_id=project["id"],
        alert_config_id=alert_config_id,
    )
    query_params = AlertConfigurationsResource.GetOpenAlertsQueryParams(pretty=True, page_num=1)

    result = resource.get_open_alerts(path_params, query_params)
    assert result is not None

    alerts = _results_list(result)
    assert isinstance(alerts, list)


def test_alert_configurations_get_matchers_field_names(client: OpsManagerClient) -> None:
    resource = client.alert_configurations_resource

    query_params = AlertConfigurationsResource.GetMatchersFieldNamesQueryParams(pretty=True)

    result = resource.get_matchers_field_names(query_params)
    assert result is not None
    assert "error" not in result

    if isinstance(result, dict):
        field_names = result.get("fieldNames") or result.get("results") or []
    else:
        field_names = result

    assert isinstance(field_names, list)
