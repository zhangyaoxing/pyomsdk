from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.root_resource import RootResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_root_root(client: OpsManagerClient) -> None:
    resource = client.root_resource
    query_params = RootResource.RootQueryParams(pretty=True)

    result = resource.root(query_params)
    assert result is not None
    assert "error" not in result
