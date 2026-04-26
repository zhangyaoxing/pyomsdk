from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.automation_resource import AutomationResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_automation_get_status(client: OpsManagerClient, project) -> None:
    resource = client.automation_resource
    org = None
    project = project
    user = None
    api_key = None
    path_params = build_model_or_skip(
        AutomationResource.GetStatusPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        AutomationResource.GetStatusQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_status(path_params, query_params)
    assert result is not None

def test_automation_get_status_of_last_50_plans(client: OpsManagerClient, project) -> None:
    """Test get_status_of_last_50_plans."""
    resource = client.automation_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        AutomationResource.GetStatusOfLast50PlansPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        AutomationResource.GetStatusOfLast50PlansQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.get_status_of_last_50_plans(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

