import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.key_vault_resource import KeyVaultResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_key_vault_get_all(client: OpsManagerClient) -> None:
    resource = client.key_vault_resource
    result = resource.get_all(None)
    assert result is not None
    assert "error" not in result


def test_key_vault_get_by_id(client: OpsManagerClient) -> None:
    resource = client.key_vault_resource
    all_result = resource.get_all(None)
    assert all_result is not None
    assert "error" not in all_result

    items = all_result.get("results") or []
    if not items:
        pytest.skip("No key vault configurations found")
    key_vault_id = items[0].get("id") or items[0].get("_id")
    assert key_vault_id is not None

    path_params = KeyVaultResource.GetByIdPathParams(key_vault_id=key_vault_id)
    result = resource.get_by_id(path_params, None)
    assert result is not None
    assert "error" not in result
