from pyomsdk.ops_manager_client import OpsManagerClient

# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_teams_get_all(client: OpsManagerClient, org) -> None:
    resource = client.teams_resource
    path_params = resource.GetAllPathParams(org_id=org["id"])

    result = resource.get_all(path_params, None)
    assert result is not None
    assert "error" not in result
