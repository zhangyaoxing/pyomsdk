from pyomsdk.ops_manager_client import OpsManagerClient

# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_s3_compatible_blockstore_get_all(client: OpsManagerClient) -> None:
    resource = client.s3_compatible_blockstore_resource
    result = resource.get_all(None)
    assert result is not None
