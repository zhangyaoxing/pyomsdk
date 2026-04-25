from typing import Any

from pyomsdk.ops_manager_client import OpsManagerClient


def create_project(
    client: OpsManagerClient,
    org_id: str,
    name: str = "Temp Project for Testing",
) -> dict[str, Any]:
    """Create a new project and return the created project document."""
    projects_resource = client.projects_resource
    project = projects_resource.create(
        None,
        body_params=projects_resource.CreateBodyParams(name=name, org_id=org_id),
    )
    return project


def delete_project(client: OpsManagerClient, project_id: str) -> None:
    """Delete a project by its ID."""
    projects_resource = client.projects_resource
    path_params = projects_resource.DeletePathParams(project_id=project_id)
    projects_resource.delete(path_params, None)
