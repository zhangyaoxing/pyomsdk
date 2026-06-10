from json import JSONDecodeError
from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.integration_settings_resource import IntegrationSettingsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_integration_settings_get_all_configurations(
    client: OpsManagerClient, project: dict[str, Any]
) -> None:
    resource = client.integration_settings_resource
    path_params = IntegrationSettingsResource.GetAllConfigurationsPathParams(
        project_id=project["id"]
    )
    result = resource.get_all_configurations(path_params, None)
    assert result is not None
    assert "error" not in result
    assert len(result["results"]) == 0


def test_integration_settings_return_latest_prometheus_targets(
    client: OpsManagerClient, project: dict[str, Any]
) -> None:
    resource = client.integration_settings_resource
    path_params = IntegrationSettingsResource.ReturnLatestPrometheusTargetsPathParams(
        project_id=project["id"]
    )

    try:
        result = resource.return_latest_prometheus_targets(path_params, None)
    except JSONDecodeError:
        pytest.skip("Prometheus target discovery endpoint returned a non-JSON response")
    assert result is not None
    if "error" in result:
        pytest.skip("Prometheus target discovery is not available for this project")
    assert result is not None
