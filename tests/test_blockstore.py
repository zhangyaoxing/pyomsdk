from pyomsdk.ops_manager_client import OpsManagerClient


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_blockstore_get_all(client: OpsManagerClient) -> None:
    resource = client.blockstore_resource

    result = resource.get_all(None)
    assert result is not None
    assert len(result["results"]) == 0
