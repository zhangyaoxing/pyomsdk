from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.configuration_resource import ConfigurationResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_configuration_get_the_automation_configuration(
    client: OpsManagerClient, project_with_cluster
) -> None:
    resource = client.configuration_resource
    path_params = ConfigurationResource.GetTheAutomationConfigurationPathParams(
        project_id=project_with_cluster["id"]
    )

    result = resource.get_the_automation_configuration(path_params, None)
    assert result is not None
    assert "processes" in result
