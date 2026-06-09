from pyomsdk.ops_manager_client import OpsManagerClient


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_telemetry_retrieve_telemetry_data(client: OpsManagerClient) -> None:
    resource = client.telemetry_resource

    result = resource.retrieve_telemetry_data()
    assert result is not None
    assert result["enabled"] is True


def test_telemetry_toggle_telemetry_status(client: OpsManagerClient) -> None:
    """Test toggle_telemetry_status."""
    resource = client.telemetry_resource
    body_params = resource.ToggleTelemetryStatusBodyParams(enabled=True)
    result = resource.toggle_telemetry_status(body_params)
    assert result == {}
