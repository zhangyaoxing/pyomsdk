from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.configuration_resource import ConfigurationResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_configuration_get_the_automation_configuration(client: OpsManagerClient, project) -> None:
    resource = client.configuration_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        ConfigurationResource.GetTheAutomationConfigurationPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        ConfigurationResource.GetTheAutomationConfigurationQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_the_automation_configuration(path_params, query_params)
    assert result is not None
