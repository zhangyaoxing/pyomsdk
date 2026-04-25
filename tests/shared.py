import os

from pyomsdk import OpsManagerClient


def get_client() -> OpsManagerClient:
    public_key = os.getenv("PUBLIC_KEY", "")
    private_key = os.getenv("PRIVATE_KEY", "")
    base_url = os.getenv("BASE_URL", "")
    client = OpsManagerClient(base_url=base_url, public_key=public_key, private_key=private_key)
    return client
