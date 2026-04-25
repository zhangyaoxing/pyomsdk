from typing import Any
from uuid import uuid4

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.projects_resource import ProjectsResource
from tests.shared.project import create_project


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def _project_id(project: dict[str, Any]) -> str:
    return project.get("id") or project.get("_id")


def test_projects_create(client: OpsManagerClient, org: dict[str, Any]) -> None:
    resource = client.projects_resource
    project_name = f"Temp Project {uuid4().hex[:8]}"

    created_project = create_project(client, org["id"], project_name)
    created_project_id = _project_id(created_project)

    assert created_project is not None
    assert created_project_id is not None
    assert created_project.get("name") == project_name

    path_params = ProjectsResource.DeletePathParams(project_id=created_project_id)
    result = resource.delete(path_params, None)
    assert result == {}


def test_projects_get_by_id(client: OpsManagerClient, project: dict[str, Any]) -> None:
    resource = client.projects_resource

    path_params = ProjectsResource.GetByIdPathParams(project_id=_project_id(project))
    query_params = ProjectsResource.GetByIdQueryParams(pretty=True)

    result = resource.get_by_id(path_params, query_params)
    assert result is not None
    assert _project_id(result) == _project_id(project)


def test_projects_get_by_name(client: OpsManagerClient, org: dict[str, Any]) -> None:
    resource = client.projects_resource
    project_name = f"Temp Project {uuid4().hex[:8]}"

    created_project = create_project(client, org["id"], project_name)
    created_project_id = _project_id(created_project)

    path_params = ProjectsResource.GetByNamePathParams(group_name=project_name)
    query_params = ProjectsResource.GetByNameQueryParams(pretty=True)

    result = resource.get_by_name(path_params, query_params)
    assert result is not None
    assert _project_id(result) == created_project_id
    assert result.get("name") == project_name

    delete_path_params = ProjectsResource.DeletePathParams(project_id=created_project_id)
    delete_result = resource.delete(delete_path_params, None)
    assert delete_result == {}


def test_projects_get_all(client: OpsManagerClient, project: dict[str, Any]) -> None:
    resource = client.projects_resource

    query_params = ProjectsResource.GetAllQueryParams(pretty=True, page_num=1)

    result = resource.get_all(query_params)
    assert result is not None

    projects = result.get("results", [])
    assert isinstance(projects, list)
    assert any(_project_id(item) == _project_id(project) for item in projects)


def test_projects_update(client: OpsManagerClient, org: dict[str, Any]) -> None:
    resource = client.projects_resource
    original_name = f"Temp Project {uuid4().hex[:8]}"
    renamed_name = f"Renamed Project {uuid4().hex[:8]}"

    created_project = create_project(client, org["id"], original_name)
    created_project_id = _project_id(created_project)

    path_params = ProjectsResource.UpdatePathParams(project_id=created_project_id)
    query_params = ProjectsResource.UpdateQueryParams(pretty=True)
    body_params = ProjectsResource.UpdateBodyParams(name=renamed_name)

    result = resource.update(path_params, query_params, body_params)
    assert result is not None
    assert _project_id(result) == created_project_id
    assert result.get("name") == renamed_name

    delete_path_params = ProjectsResource.DeletePathParams(project_id=created_project_id)
    delete_result = resource.delete(delete_path_params, None)
    assert delete_result == {}


def test_projects_get_all_users(client: OpsManagerClient, project: dict[str, Any]) -> None:
    resource = client.projects_resource

    path_params = ProjectsResource.GetAllUsersPathParams(project_id=_project_id(project))
    query_params = ProjectsResource.GetAllUsersQueryParams(
        flatten_teams=True,
        include_org_users=True,
    )

    result = resource.get_all_users(path_params, query_params)
    assert result is not None

    users = result.get("results", [])
    assert isinstance(users, list)


def test_projects_delete(client: OpsManagerClient, org: dict[str, Any]) -> None:
    resource = client.projects_resource
    project_name = f"Temp Project {uuid4().hex[:8]}"

    created_project = create_project(client, org["id"], project_name)
    created_project_id = _project_id(created_project)

    path_params = ProjectsResource.DeletePathParams(project_id=created_project_id)

    result = resource.delete(path_params, None)
    assert result == {}
