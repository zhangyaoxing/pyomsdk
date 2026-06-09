from pyomsdk.ops_manager_client import OpsManagerClient


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_global_alert_configurations_get_all(client: OpsManagerClient) -> None:
    resource = client.global_alert_configurations_resource

    result = resource.get_all(None)
    assert result is not None
    assert "results" in result
    assert isinstance(result["results"], list)
    assert len(result["results"]) > 0
