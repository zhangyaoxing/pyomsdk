from typing import Any

import pytest

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.import_deployments_resource import ImportDeploymentsResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_import_deployments_get_import_deployment_requests(
    client: OpsManagerClient, project: dict[str, Any]
) -> None:
    resource = client.import_deployments_resource
    path_params = ImportDeploymentsResource.GetImportDeploymentRequestsPathParams(
        project_id=project["id"]
    )
    result = resource.get_import_deployment_requests(path_params, None)
    assert result is not None
    assert "error" not in result


def test_import_deployments_get_import_deployment_request_status(
    client: OpsManagerClient, project: dict[str, Any]
) -> None:
    resource = client.import_deployments_resource
    all_result = resource.get_import_deployment_requests(
        ImportDeploymentsResource.GetImportDeploymentRequestsPathParams(project_id=project["id"]),
        None,
    )
    items = all_result if isinstance(all_result, list) else all_result.get("results", [])
    if not items:
        pytest.skip("No import deployment requests found")

    import_id = items[0].get("id") or items[0].get("_id")
    path_params = ImportDeploymentsResource.GetImportDeploymentRequestStatusPathParams(
        project_id=project["id"], import_process_id=import_id
    )
    result = resource.get_import_deployment_request_status(path_params, None)
    assert result is not None
    assert "error" not in result

def test_import_deployments_cancel_import_deployment_request(client: OpsManagerClient, project) -> None:
    """Test cancel_import_deployment_request."""
    resource = client.import_deployments_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        ImportDeploymentsResource.CancelImportDeploymentRequestPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        ImportDeploymentsResource.CancelImportDeploymentRequestQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.cancel_import_deployment_request(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

def test_import_deployments_create_import_deployment_request(client: OpsManagerClient, project) -> None:
    """Test create_import_deployment_request."""
    resource = client.import_deployments_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        ImportDeploymentsResource.CreateImportDeploymentRequestPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        ImportDeploymentsResource.CreateImportDeploymentRequestQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    body_params = build_model_or_skip(
        ImportDeploymentsResource.CreateImportDeploymentRequestBodyParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.create_import_deployment_request(path_params, query_params, body_params)
    assert result is not None
    assert_success_or_skip(result)

def test_import_deployments_delete_import_deployment_request(client: OpsManagerClient, project) -> None:
    """Test delete_import_deployment_request."""
    resource = client.import_deployments_resource
    org = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        ImportDeploymentsResource.DeleteImportDeploymentRequestPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        ImportDeploymentsResource.DeleteImportDeploymentRequestQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.delete_import_deployment_request(path_params, query_params)
    assert result is not None
    assert_success_or_skip(result)

