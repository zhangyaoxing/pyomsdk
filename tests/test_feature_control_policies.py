from typing import Any

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.feature_control_policies_resource import FeatureControlPoliciesResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_feature_control_policies_retrieve_all(client: OpsManagerClient) -> None:
    """Test retrieving all feature control policies globally."""
    resource = client.feature_control_policies_resource

    query_params = build_model_or_skip(
        FeatureControlPoliciesResource.RetrieveAllQueryParams,
        client=client,
        org=None,
        project=None,
        user=None,
        api_key=None,
    )

    result = resource.retrieve_all(query_params)
    assert result is not None
    assert "error" not in result


def test_feature_control_policies_retrieve_for_one_project(
    client: OpsManagerClient, project
) -> None:
    """Test retrieving feature control policies for one project."""
    resource = client.feature_control_policies_resource
    org = None
    project = project
    user = None
    api_key = None
    path_params = build_model_or_skip(
        FeatureControlPoliciesResource.RetrieveForOneProjectPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        FeatureControlPoliciesResource.RetrieveForOneProjectQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.retrieve_for_one_project(path_params, query_params)
    assert result is not None
    assert "error" not in result


def test_feature_control_policies_update(client: OpsManagerClient, project: dict[str, Any]) -> None:
    """Test updating feature control policies for a project."""
    resource = client.feature_control_policies_resource

    path_params = FeatureControlPoliciesResource.UpdatePathParams(project_id=project["id"])
    query_params = FeatureControlPoliciesResource.UpdateQueryParams(pretty=True)
    body_params = FeatureControlPoliciesResource.UpdateBodyParams()

    result = resource.update(path_params, query_params, body_params)
    assert result is not None
    assert "error" not in result
