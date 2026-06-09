from typing import Any

from pyomsdk.ops_manager_client import OpsManagerClient


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_feature_control_policies_retrieve_all(client: OpsManagerClient) -> None:
    """Test retrieving all feature control policies globally."""
    resource = client.feature_control_policies_resource
    query_params = resource.RetrieveAllQueryParams(pretty=True)

    result = resource.retrieve_all(query_params)
    assert result is not None
    assert "error" not in result
    assert len(result) > 0


def test_feature_control_policies_retrieve_for_one_project(
    client: OpsManagerClient, project
) -> None:
    """Test retrieving feature control policies for one project."""
    resource = client.feature_control_policies_resource
    path_params = resource.RetrieveForOneProjectPathParams(project_id=project["id"])
    query_params = resource.RetrieveForOneProjectQueryParams(pretty=True)

    result = resource.retrieve_for_one_project(path_params, query_params)
    assert result is not None
    assert "error" not in result
    assert len(result["policies"]) == 0


def test_feature_control_policies_update(client: OpsManagerClient, project: dict[str, Any]) -> None:
    """Test updating feature control policies for a project."""
    resource = client.feature_control_policies_resource

    path_params = resource.UpdatePathParams(project_id=project["id"])
    query_params = resource.UpdateQueryParams(pretty=True)
    body_params = resource.UpdateBodyParams(
        external_management_system=resource.UpdateBodyParams.ExternalManagementSystemParams(
            name="test-system",
            system_id="test-system-id",
            version="1.0",
        ),
        policies=[],
    )

    result = resource.update(path_params, query_params, body_params)
    assert result is not None
    assert "error" not in result
    assert result["externalManagementSystem"]["name"] == "test-system"
    assert result["externalManagementSystem"]["systemId"] == "test-system-id"
    assert result["externalManagementSystem"]["version"] == "1.0"
