from pyomsdk.ops_manager_client import OpsManagerClient


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_sync_store_get_all(client: OpsManagerClient) -> None:
    resource = client.sync_store_resource

    result = resource.get_all(None)
    assert result is not None
    assert "error" not in result
    assert "results" in result
    assert isinstance(result["results"], list)
    assert len(result["results"]) > 0
