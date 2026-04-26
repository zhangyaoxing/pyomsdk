from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.sync_store_resource import SyncStoreResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_sync_store_get_all(client: OpsManagerClient) -> None:
    resource = client.sync_store_resource
    org = None
    project = None
    user = None
    api_key = None
    query_params = build_model_or_skip(
        SyncStoreResource.GetAllQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all(query_params)
    assert result is not None
