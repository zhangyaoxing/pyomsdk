from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.telemetry_resource import TelemetryResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_telemetry_retrieve_telemetry_data(client: OpsManagerClient) -> None:
    resource = client.telemetry_resource
    org = None
    project = None
    user = None
    api_key = None

    result = resource.retrieve_telemetry_data()
    assert result is not None

def test_telemetry_toggle_telemetry_status(client: OpsManagerClient) -> None:
    """Test toggle_telemetry_status."""
    resource = client.telemetry_resource
    org = None
    project = None
    user = None
    api_key = None
    body_params = build_model_or_skip(
        TelemetryResource.ToggleTelemetryStatusBodyParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.toggle_telemetry_status(body_params)
    assert result is not None
    assert_success_or_skip(result)

