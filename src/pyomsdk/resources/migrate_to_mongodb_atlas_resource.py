"""Auto-generated client for MigrateToMongodbAtlasResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class MigrateToMongodbAtlasResource(BaseResource):
    """Client for MigrateToMongodbAtlasResource resource."""

    class ConnectWithAtlasOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="orgId")
        """Unique 24-hexadecimal digit string that identifies the source organization that contains your projects.
        """

    class ConnectWithAtlasOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query.

For endpoints that return one result, the response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

    class ConnectWithAtlasOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        link_token: str = Field(serialization_alias="linkToken")
        """String that contains the information necessary to connect from MongoDB Cloud Manager or Ops Manager to MongoDB Atlas during a Live Migration from a MongoDB Cloud Manager or Ops Manager deployment to a cluster in MongoDB Atlas.

When you migrate data from a MongoDB Cloud Manager or Ops Manager deployment, you need to do the following:

Generate a link-token in MongoDB Atlas

Enter it in your MongoDB Cloud Manager or Ops Manager organization’s settings.

You use the same link-token to migrate each deployment in your MongoDB Cloud Manager or Ops Manager organization sequentially, one at a time. You can generate multiple link-tokens in MongoDB Atlas. Use one unique link-token for each MongoDB Cloud Manager or Ops Manager organization.
        """

    def connect_with_atlas_organization(
        self,
        path_params: ConnectWithAtlasOrganizationPathParams,
        query_params: Optional[ConnectWithAtlasOrganizationQueryParams],
        body_params: ConnectWithAtlasOrganizationBodyParams,
    ) -> dict[str, Any]:
        """
        ## Connect One Organization with One Atlas Organization
        ### Document:
        [Connect with Atlas Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/cloud-migration/link-the-organization-with-atlas/)
        ### Endpoint:
        `POST /orgs/{orgId}/liveExport/migrationLink`
        ### Description
        Connect the source Ops Manager organization with a target MongoDB Atlas organization.
        """
        return self._request(
            "POST",
            "/orgs/{orgId}/liveExport/migrationLink",
            path_params,
            query_params,
            body_params,
        )

    class RemoveConnectionPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="orgId")
        """Unique 24-hexadecimal digit string that identifies the source organization that contains your projects.
        """

    class RemoveConnectionQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query.

For endpoints that return one result, the response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

    def remove_connection(
        self,
        path_params: RemoveConnectionPathParams,
        query_params: Optional[RemoveConnectionQueryParams],
    ) -> dict[str, Any]:
        """
        ## Remove the Connection between Organizations
        ### Document:
        [Remove Connection](https://www.mongodb.com/docs/ops-manager/current/reference/api/cloud-migration/remove-the-link-between-organizations/)
        ### Endpoint:
        `DELETE /orgs/{orgId}/liveExport/migrationLink`
        ### Description
        Remove the connection between the source Ops Manager organization and the target MongoDB Atlas organization. This stops the source organization from synchronizing data with the target organization.
        """
        return self._request(
            "DELETE",
            "/orgs/{orgId}/liveExport/migrationLink",
            path_params,
            query_params,
            None,
        )

    class ReturnConnectionStatusPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="orgId")
        """Unique 24-hexadecimal digit string that identifies the source organization that contains the projects to be migrated to MongoDB Atlas.
        """

    class ReturnConnectionStatusQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query.

For endpoints that return one result, the response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

    def return_connection_status(
        self,
        path_params: ReturnConnectionStatusPathParams,
        query_params: Optional[ReturnConnectionStatusQueryParams],
    ) -> dict[str, Any]:
        """
        ## Return the Status of the Connection between Organizations
        ### Document:
        [Return Connection Status](https://www.mongodb.com/docs/ops-manager/current/reference/api/cloud-migration/return-the-status-of-the-organization-link/)
        ### Endpoint:
        `GET /orgs/{orgId}/liveExport/migrationLink/status`
        ### Description
        Return the status of the connection between the specified source Ops Manager organization and the target MongoDB Atlas organization.
        """
        return self._request(
            "GET",
            "/orgs/{orgId}/liveExport/migrationLink/status",
            path_params,
            query_params,
            None,
        )
