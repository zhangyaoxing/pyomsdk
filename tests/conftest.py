import os
import pytest
from pyomsdk import OpsManagerClient
from tests.shared.accesslist import add_accesslist, delete_accesslist, random_ip
from tests.shared.org import create_org, delete_org
from tests.shared.user import add_user, get_user_info, delete_user
from tests.shared.project import create_project, delete_project
from tests.shared.agent import create_agent_api_key, delete_agent_api_key


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


@pytest.fixture(name="api_key")
def new_api_key(client: OpsManagerClient, project: dict):
    api_key = create_agent_api_key(client, project["id"])
    yield api_key
    delete_agent_api_key(client, api_key["id"])


@pytest.fixture(name="user_with_access_list_entry")
def _user_with_access_list_entry_fixture(
    client: OpsManagerClient,
    user: dict,
):
    ip_address = random_ip()
    add_accesslist(client, user["id"], ip_address)
    yield user, ip_address
    delete_accesslist(client, user["id"], ip_address)
