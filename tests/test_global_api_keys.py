from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.global_api_keys_resource import GlobalApiKeysResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_global_api_keys_get_all(client: OpsManagerClient) -> None:
    resource = client.global_api_keys_resource
    result = resource.get_all(None)
    assert result is not None


def test_global_api_keys_get_one(client: OpsManagerClient) -> None:
    """Test get_one."""
    resource = client.global_api_keys_resource
    all_keys = resource.get_all(None)
    path_params = GlobalApiKeysResource.GetOnePathParams(api_key_id=all_keys["results"][0]["id"])
    result = resource.get_one(path_params, None)
    assert result is not None
    assert "error" not in result
    assert "id" in result
    assert result["id"] == all_keys["results"][0]["id"]
