from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.hosts_resource import HostsResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_hosts_get_all(client: OpsManagerClient, project) -> None:
    resource = client.hosts_resource
    org = None
    project = project
    user = None
    api_key = None
    path_params = build_model_or_skip(
        HostsResource.GetAllPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        HostsResource.GetAllQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all(path_params, query_params)
    assert result is not None
