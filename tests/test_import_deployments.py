from typing import Any

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.import_deployments_resource import ImportDeploymentsResource


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
    client: OpsManagerClient, project_with_cluster: dict[str, Any]
) -> None:
    resource = client.import_deployments_resource

    path_params = ImportDeploymentsResource.GetImportDeploymentRequestStatusPathParams(
        project_id=project_with_cluster["id"], import_process_id=project_with_cluster["id"]
    )
    result = resource.get_import_deployment_request_status(path_params, None)
    assert result is not None
    assert result["status"] == 404


def test_import_deployments_cancel_import_deployment_request(
    client: OpsManagerClient, project
) -> None:
    """Test cancel_import_deployment_request."""
    resource = client.import_deployments_resource
    path_params = ImportDeploymentsResource.CancelImportDeploymentRequestPathParams(
        project_id=project["id"],
        request_id=project["id"],
    )
    result = resource.cancel_import_deployment_request(path_params, None)
    assert result is not None
    assert "error" in result


def test_import_deployments_create_import_deployment_request(
    client: OpsManagerClient, project
) -> None:
    """Test create_import_deployment_request."""
    resource = client.import_deployments_resource
    path_params = ImportDeploymentsResource.CreateImportDeploymentRequestPathParams(
        project_id=project["id"],
    )
    body_params = ImportDeploymentsResource.CreateImportDeploymentRequestBodyParams(
        seed_hostport="example.com:27017",
        required_processes=["example.com:27017"],
    )
    result = resource.create_import_deployment_request(path_params, None, body_params)
    assert result is not None
    assert "error" in result
    assert result["error"] == 400


def test_import_deployments_delete_import_deployment_request(
    client: OpsManagerClient, project
) -> None:
    """Test delete_import_deployment_request."""
    resource = client.import_deployments_resource
    path_params = ImportDeploymentsResource.DeleteImportDeploymentRequestPathParams(
        project_id=project["id"],
        request_id=project["id"],
    )
    result = resource.delete_import_deployment_request(path_params, None)
    assert result is not None
    assert "error" in result
