from pyomsdk.ops_manager_client import OpsManagerClient


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_automation_get_status(client: OpsManagerClient, project) -> None:
    resource = client.automation_resource
    path_params = resource.GetStatusPathParams(project_id=project["id"])

    result = resource.get_status(path_params, None)
    assert result is not None
    assert result["goalVersion"] == 0


def test_automation_get_status_of_last_50_plans(client: OpsManagerClient, project) -> None:
    """Test get_status_of_last_50_plans."""
    resource = client.automation_resource
    path_params = resource.GetStatusOfLast50PlansPathParams(group_id=project["id"])
    query_params = resource.GetStatusOfLast50PlansQueryParams(pretty=True)
    result = resource.get_status_of_last_50_plans(path_params, query_params)
    assert result is not None
    assert result["goalVersion"] == 0
