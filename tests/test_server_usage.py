from pyomsdk.ops_manager_client import OpsManagerClient


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_server_usage_get_default_server_type(client: OpsManagerClient, project) -> None:
    resource = client.server_usage_resource
    path_params = resource.GetDefaultServerTypePathParams(group_id=project["id"])

    result = resource.get_default_server_type(path_params, None)
    assert result is not None
    assert result["name"] == "PRODUCTION_SERVER"
