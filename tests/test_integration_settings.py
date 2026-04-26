from typing import Any

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
