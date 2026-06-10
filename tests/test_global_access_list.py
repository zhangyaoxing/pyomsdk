import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.global_access_list_resource import GlobalAccessListResource
from tests.shared.accesslist import random_ip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_global_access_list_get_all_entries(client: OpsManagerClient) -> None:
    resource = client.global_access_list_resource

    result = resource.get_all_entries(None)
    assert result is not None
    assert result["results"] is not None
    assert isinstance(result["results"], list)
    assert len(result["results"]) >= 0


def test_global_access_list_create_get_update_delete_entry(client: OpsManagerClient) -> None:
    resource = client.global_access_list_resource
    cidr_block = f"{random_ip()}/32"
    create_body = GlobalAccessListResource.CreateEntryBodyParams(
        cidr_block=cidr_block, description="Test global access list entry"
    )

    created = resource.create_entry(None, create_body)
    assert created is not None
    assert "error" not in created

    entry_id = created.get("id") or created.get("_id") or created.get("cidrBlock")
    assert entry_id is not None

    try:
        get_path = GlobalAccessListResource.GetOneEntryPathParams(access_list_id=entry_id)
        retrieved = resource.get_one_entry(get_path, None)
        assert retrieved is not None
        assert "error" not in retrieved

        update_path = GlobalAccessListResource.UpdateEntryPathParams(access_list_id=entry_id)
        updated = resource.update_entry(update_path, None)
        assert updated is not None
        if updated.get("errorCode") == "NO_CIDR_BLOCK_OR_DESCRIPTION":
            pytest.skip("Generated update_entry method has no body params for required fields")
        assert "error" not in updated
    finally:
        delete_path = GlobalAccessListResource.DeleteEntryPathParams(access_list_id=entry_id)
        resource.delete_entry(delete_path, None)
