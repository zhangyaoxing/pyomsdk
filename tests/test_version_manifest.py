from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.version_manifest_resource import VersionManifestResource
from tests.shared.resource_api import build_model_or_skip, assert_success_or_skip


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
    org = None
    project = None
    user = None
    api_key = None
    query_params = build_model_or_skip(
        VersionManifestResource.UpdateQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    result = resource.update(query_params)
    assert result is not None
    assert_success_or_skip(result)

