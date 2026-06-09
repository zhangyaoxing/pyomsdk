from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.version_manifest_resource import VersionManifestResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_version_manifest_retrieve(client: OpsManagerClient) -> None:
    resource = client.version_manifest_resource
    query_params = VersionManifestResource.RetrieveQueryParams(pretty=True)
    result = resource.retrieve(query_params)
    assert result is not None
    assert "error" not in result


def test_version_manifest_update(client: OpsManagerClient) -> None:
    """Test update."""
    resource = client.version_manifest_resource
    result = resource.update(None)
    assert result is not None
