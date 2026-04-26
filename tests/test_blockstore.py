from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.blockstore_resource import BlockstoreResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_blockstore_get_all(client: OpsManagerClient) -> None:
    resource = client.blockstore_resource
    org = None
    project = None
    user = None
    api_key = None
    query_params = build_model_or_skip(
        BlockstoreResource.GetAllQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all(query_params)
    assert result is not None
