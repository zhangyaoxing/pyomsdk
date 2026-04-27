from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.global_access_list_resource import GlobalAccessListResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_global_access_list_get_all_entries(client: OpsManagerClient) -> None:
    resource = client.global_access_list_resource
    org = None
    project = None
    user = None
    api_key = None
    query_params = build_model_or_skip(
        GlobalAccessListResource.GetAllEntriesQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all_entries(query_params)
    assert result is not None
    assert result["results"] is not None
    assert isinstance(result["results"], list)
    assert len(result["results"]) > 0
