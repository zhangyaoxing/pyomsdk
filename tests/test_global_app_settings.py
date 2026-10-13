import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.global_app_settings_resource import GlobalAppSettingsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_global_app_settings_get_settings(client: OpsManagerClient) -> None:
    resource = client.global_app_settings_resource
    result = resource.get_settings(None)
    assert result is not None
    assert "error" not in result


def test_global_app_settings_update_settings(client: OpsManagerClient) -> None:
    """Send the current settings back, so the installation is left unchanged."""
    resource = client.global_app_settings_resource
    current = resource.get_settings(GlobalAppSettingsResource.GetSettingsQueryParams())
    assert current is not None
    assert "error" not in current

    db_properties = current.get("dbProperties") or current.get("db_properties")
    if not db_properties:
        pytest.skip("The global app settings expose no dbProperties to update")

    body_params = GlobalAppSettingsResource.UpdateSettingsBodyParams(db_properties=db_properties)
    result = resource.update_settings(None, body_params)
    assert result is not None
    assert "error" not in result
