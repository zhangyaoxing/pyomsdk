from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.disks_resource import DisksResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_disks_get_all(client: OpsManagerClient, project) -> None:
    resource = client.disks_resource
    org = None
    project = project
    user = None
    api_key = None
    path_params = build_model_or_skip(
        DisksResource.GetAllPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        DisksResource.GetAllQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all(path_params, query_params)
    assert result is not None

def test_disks_get_one(client: OpsManagerClient, project) -> None:
    """Test get_one."""
    resource = client.disks_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        DisksResource.GetOnePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        DisksResource.GetOneQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_one(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

