from typing import Any
from uuid import uuid4

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.agents_resource import AgentsResource


def generate_api_key_desc() -> str:
    """Generate a unique description for API key."""
    return f"test-api-key-{uuid4().hex[:8]}"


def create_agent_api_key(
    client: OpsManagerClient, project_id: str, desc: str = ""
) -> dict[str, Any]:
    """Create an agent API key for testing."""
    agents_resource = client.agents_resource
    path_params = AgentsResource.CreateApiKeyPathParams(project_id=project_id)
    body_params = AgentsResource.CreateApiKeyBodyParams(desc=desc or generate_api_key_desc())
    return agents_resource.create_api_key(path_params, None, body_params)


def delete_agent_api_key(client: OpsManagerClient, api_agent_key_id: str) -> dict[str, Any]:
    """Delete an agent API key."""
    agents_resource = client.agents_resource
    path_params = AgentsResource.RemoveApiKeyPathParams(
        api_agent_key_id=api_agent_key_id,
        project_id=client.projects_resource.get_all(None).get("results", [{}])[0].get("id", ""),
    )
    return agents_resource.remove_api_key(path_params, None)
