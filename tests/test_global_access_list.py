from pyomsdk.ops_manager_client import OpsManagerClient


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_global_access_list_get_all_entries(client: OpsManagerClient) -> None:
    resource = client.global_access_list_resource

    result = resource.get_all_entries(None)
    assert result is not None
    assert result["results"] is not None
    assert isinstance(result["results"], list)
    assert len(result["results"]) >= 0
