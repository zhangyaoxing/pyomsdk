import os

from ops_manager_sdk import OpsManagerClient
from ops_manager_sdk import ClientConfig


def get_client() -> OpsManagerClient:
    public_key = os.getenv("PUBLIC_KEY", "")
    private_key = os.getenv("PRIVATE_KEY", "")
    base_url = os.getenv("BASE_URL", "")
    config = ClientConfig(base_url=base_url, public_key=public_key, private_key=private_key)
    client = OpsManagerClient(config)
    return client
