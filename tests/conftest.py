import os
from pathlib import Path
import pytest
from pyomsdk import OpsManagerClient
from tests.shared.accesslist import add_accesslist, delete_accesslist, random_ip
from tests.shared.org import create_org, delete_org
from tests.shared.user import add_user, get_user_info, delete_user
from tests.shared.project import create_project, delete_project
from tests.shared.agent import create_agent_api_key, delete_agent_api_key


def _load_env_file() -> None:
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text().splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue

        key, value = stripped.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_env_file()


@pytest.fixture(name="client")
def get_client():
    public_key = os.getenv("PUBLIC_KEY", "")
    private_key = os.getenv("PRIVATE_KEY", "")
    base_url = os.getenv("BASE_URL", "")
    client = OpsManagerClient(base_url=base_url, public_key=public_key, private_key=private_key)
    yield client


@pytest.fixture(name="user")
def new_user(client: OpsManagerClient):
    user = add_user(client, get_user_info())
    yield user
    delete_user(client, user["id"])


@pytest.fixture(name="org")
def new_organization(client: OpsManagerClient):
    org = create_org(client, "Temp Org for Testing")
    yield org
    delete_org(client, org["id"])


@pytest.fixture(name="project")
def new_project(client: OpsManagerClient, org: dict):
    project = create_project(client, org["id"])
    yield project
    delete_project(client, project["id"])


@pytest.fixture(name="project_with_cluster")
def get_project_with_cluster(client: OpsManagerClient):
    project_resource = client.projects_resource
    project_name = "MongoDB"
    project = project_resource.get_by_name(
        project_resource.GetByNamePathParams(group_name=project_name), None
    )
    if project is None:
        pytest.skip(f"Project with name '{project_name}' not found, skipping test.")
    yield project


@pytest.fixture(name="cluster")
def cluster(client: OpsManagerClient, project_with_cluster: dict):
    cluster_resource = client.clusters_resource
    pid: str = project_with_cluster.get("id")
    clusters = cluster_resource.get_all_from_one_project(
        cluster_resource.GetAllFromOneProjectPathParams(project_id=pid), None
    )
    if not clusters or "results" not in clusters or not clusters["results"]:
        pytest.skip(
            f"No clusters found in project '{project_with_cluster['name']}', skipping test."
        )
    return clusters["results"][0]


@pytest.fixture(name="api_key")
def new_api_key(client: OpsManagerClient, project: dict):
    api_key = create_agent_api_key(client, project["id"])
    yield api_key
    api_key_id = api_key.get("id") or api_key.get("_id")
    if api_key_id:
        delete_agent_api_key(client, api_key_id, project["id"])


@pytest.fixture(name="user_with_access_list_entry")
def user_with_access_list_entry_fixture(
    client: OpsManagerClient,
    user: dict,
):
    ip_address = random_ip()
    add_accesslist(client, user["id"], ip_address)
    yield user, ip_address
    delete_accesslist(client, user["id"], ip_address)
