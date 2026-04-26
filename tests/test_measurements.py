from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.hosts_resource import HostsResource
from pyomsdk.resources.measurements_resource import MeasurementsResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _first_host_id(client: OpsManagerClient, project_id: str) -> str | None:
    result = client.hosts_resource.get_all(
        HostsResource.GetAllPathParams(project_id=project_id), None
    )
    items = result if isinstance(result, list) else result.get("results", [])
    if not items:
        return None
    return items[0].get("id") or items[0].get("_id")


def test_measurements_get_types(client: OpsManagerClient, project: dict[str, Any]) -> None:
    resource = client.measurements_resource
    path_params = MeasurementsResource.GetTypesPathParams(
        project_id=project["id"], host_id="placeholder"
    )
    # GetTypesPathParams requires host_id but the endpoint may not need it for listing types
    # Skip if no hosts
    host_id = _first_host_id(client, project["id"])
    if not host_id:
        pytest.skip("No hosts found in project")
    path_params = MeasurementsResource.GetTypesPathParams(project_id=project["id"], host_id=host_id)
    result = resource.get_types(path_params, None)
    assert result is not None
    assert "error" not in result


def test_measurements_host(client: OpsManagerClient, project: dict[str, Any]) -> None:
    host_id = _first_host_id(client, project["id"])
    if not host_id:
        pytest.skip("No hosts found in project")

    resource = client.measurements_resource
    path_params = MeasurementsResource.HostPathParams(project_id=project["id"], host_id=host_id)
    query_params = MeasurementsResource.HostQueryParams(
        granularity="PT1M",
        period="P1D",
    )
    result = resource.host(path_params, query_params)
    assert result is not None
    assert "error" not in result

def test_measurements_database(client: OpsManagerClient, project) -> None:
    """Test database."""
    resource = client.measurements_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        MeasurementsResource.DatabasePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        MeasurementsResource.DatabaseQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.database(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

def test_measurements_disk_partition(client: OpsManagerClient, project) -> None:
    """Test disk_partition."""
    resource = client.measurements_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        MeasurementsResource.DiskPartitionPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        MeasurementsResource.DiskPartitionQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.disk_partition(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

