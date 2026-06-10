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


def test_sync_store_get_by_id(client: OpsManagerClient) -> None:
    resource = client.sync_store_resource
    all_result = resource.get_all(None)
    store = all_result["results"][0]
    store_id = store.get("id") or store.get("_id")
    assert store_id is not None

    path_params = resource.GetByIdPathParams(sync_store_config_id=store_id)
    result = resource.get_by_id(path_params, None)
    assert result is not None
    assert "error" not in result
