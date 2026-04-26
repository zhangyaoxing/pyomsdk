from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.server_usage_resource import ServerUsageResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_server_usage_get_default_server_type(client: OpsManagerClient, project) -> None:
    resource = client.server_usage_resource
    org = None
    project = project
    user = None
    api_key = None
    path_params = build_model_or_skip(
        ServerUsageResource.GetDefaultServerTypePathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        ServerUsageResource.GetDefaultServerTypeQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_default_server_type(path_params, query_params)
    assert result is not None
