import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.s3_compatible_blockstore_v20_resource import (
    S3CompatibleBlockstoreV20Resource,
)


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_s3_compatible_blockstore_v20_get_all(client: OpsManagerClient) -> None:
    resource = client.s3_compatible_blockstore_v20_resource
    result = resource.get_all(None)
    assert result is not None
    assert "error" not in result


def test_s3_compatible_blockstore_v20_get_by_id(client: OpsManagerClient) -> None:
    resource = client.s3_compatible_blockstore_v20_resource
    all_result = resource.get_all(None)
    assert all_result is not None
    assert "error" not in all_result

    items = all_result.get("results") or []
    if not items:
        pytest.skip("No S3-compatible blockstores found")
    store = items[0]
    store_id = store.get("id") or store.get("_id")
    assert store_id is not None

    path_params = S3CompatibleBlockstoreV20Resource.GetByIdPathParams(
        s3_blockstore_config_id=store_id
    )
    result = resource.get_by_id(path_params, None)
    assert result is not None
    assert "error" not in result
