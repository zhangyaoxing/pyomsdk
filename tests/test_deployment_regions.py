from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.deployment_regions_resource import DeploymentRegionsResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_deployment_regions_get_all(client: OpsManagerClient) -> None:
    resource = client.deployment_regions_resource
    query_params = DeploymentRegionsResource.GetAllQueryParams(pretty=True)
    result = resource.get_all(query_params)
    assert result is not None
    assert "error" not in result
