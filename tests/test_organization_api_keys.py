from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.organization_api_keys_resource import OrganizationApiKeysResource
from tests.shared.resource_api import build_model_or_skip


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_organization_api_keys_get_all(client: OpsManagerClient, org) -> None:
    resource = client.organization_api_keys_resource
    project = None
    user = None
    api_key = None
    path_params = build_model_or_skip(
        OrganizationApiKeysResource.GetAllPathParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )
    query_params = build_model_or_skip(
        OrganizationApiKeysResource.GetAllQueryParams,
        client=client,
        org=org,
        project=project,
        user=user,
        api_key=api_key,
    )

    result = resource.get_all(path_params, query_params)
    assert result is not None
