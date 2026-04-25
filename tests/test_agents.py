from typing import Any
from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.agents_resource import AgentsResource
from pyomsdk.resources.enums import AgentType
from tests.shared.agent import create_agent_api_key, delete_agent_api_key, generate_api_key_desc


def test_agents_create_api_key(client: OpsManagerClient, project: dict) -> None:
    """Test creating an agent API key."""
    desc = generate_api_key_desc()
    api_key = create_agent_api_key(client, project["id"], desc)
    assert api_key is not None
    assert api_key.get("_id") is not None
    assert api_key.get("desc") == desc
    delete_agent_api_key(client, api_key["_id"])


def test_agents_remove_api_key(
    client: OpsManagerClient, project: dict, api_key: dict[str, Any]
) -> None:
    """Test removing an agent API key."""
    desc = generate_api_key_desc()
    api_key = create_agent_api_key(client, project["id"], desc)
    assert api_key is not None
    assert api_key.get("_id") is not None
    assert api_key.get("desc") == desc
    result = delete_agent_api_key(client, api_key["_id"])
    assert result == {}


def test_agents_get_all_api_keys(
    client: OpsManagerClient, project: dict, api_key: dict[str, Any]
) -> None:
    """Test getting all agent API keys for a project."""
    resource = client.agents_resource

    path_params = AgentsResource.GetAllApiKeysPathParams(project_id=project["id"])
    query_params = AgentsResource.GetAllApiKeysQueryParams(pretty=True)

    result = resource.get_all_api_keys(path_params, query_params)
    assert result is not None
    assert len(result) > 0
    assert any(key.get("_id") == api_key["_id"] for key in result)


def test_agents_get_all(client: OpsManagerClient, project: dict) -> None:
    """Test getting links to agent resources for a project."""
    resource = client.agents_resource

    path_params = AgentsResource.GetAllPathParams(project_id=project["id"])
    query_params = AgentsResource.GetAllQueryParams(pretty=True)

    result = resource.get_all(path_params, query_params)
    assert result is not None
    assert "links" in result
    assert isinstance(result["links"], list)


def test_agents_get_by_type(client: OpsManagerClient, project: dict) -> None:
    """Test getting agents by type for a project."""
    resource = client.agents_resource

    path_params = AgentsResource.GetByTypePathParams(
        project_id=project["id"], type=AgentType.AUTOMATION
    )
    result = resource.get_by_type(path_params, None)
    assert result is not None
    assert result["results"] is not None
    assert isinstance(result["results"], list)
    assert len(result["results"]) == 0


def test_agents_retrieve_all_versions(client: OpsManagerClient) -> None:
    """Test retrieving all agent versions globally."""
    resource = client.agents_resource

    query_params = AgentsResource.RetrieveAllVersionsQueryParams(pretty=True)

    result = resource.retrieve_all_versions(query_params)
    assert result is not None
    assert "automationMinimumVersion" in result
    assert "automationVersion" in result
    assert "biConnectorMinimumVersion" in result
    assert "biConnectorVersion" in result
    assert "mongoDbToolsVersion" in result


def test_agents_retrieve_for_one_project(client: OpsManagerClient, project: dict) -> None:
    """Test retrieving all agent versions for one project."""
    resource = client.agents_resource

    path_params = AgentsResource.RetrieveForOneProjectPathParams(project_id=project["id"])
    query_params = AgentsResource.RetrieveForOneProjectQueryParams(pretty=True)

    result = resource.retrieve_for_one_project(path_params, query_params)
    assert result is not None
    assert result["count"] == 0
