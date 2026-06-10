import pytest

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


def test_deployment_regions_get_one(client: OpsManagerClient) -> None:
    resource = client.deployment_regions_resource
    all_regions = resource.get_all(DeploymentRegionsResource.GetAllQueryParams(pretty=True))
    assert all_regions is not None
    assert "error" not in all_regions
    if not all_regions.get("results"):
        pytest.skip("No deployment regions found")

    region = all_regions["results"][0]
    region_id = region.get("id") or region.get("_id")
    assert region_id is not None

    path_params = DeploymentRegionsResource.GetOnePathParams(deployment_id=region_id)
    result = resource.get_one(path_params, None)
    assert result is not None
    assert "error" not in result
