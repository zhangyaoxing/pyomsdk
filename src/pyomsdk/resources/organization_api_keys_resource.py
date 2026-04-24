"""Auto-generated client for OrganizationApiKeysResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class OrganizationApiKeysResource(BaseResource):
    """Client for OrganizationApiKeysResource resource."""

    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        """Unique identifier for the organization whose API keys you want to retrieve. Use the /orgs endpoint to retrieve all organizations to which the authenticated user has access.
        """

    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set "envelope" : true in the query.

For endpoints that return one result, response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body

For endpoints that return a list of results, the results object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(
            100.0, serialization_alias="itemsPerPage"
        )
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """Page number (1-index based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        desc: Optional[str] = Field(serialization_alias="desc")
        """Description of the API key. Must be between 1 and 250 characters in length.
        """

        roles: Optional[list[str]] = Field(serialization_alias="roles")
        """List of roles that the API key should have. There must be at least one role listed, and all roles must be valid for an Organization.

Organization roles include:

Role Value in API
	
Role



ORG_OWNER

	

Organization Owner




ORG_MEMBER

	

Organization Member




ORG_GROUP_CREATOR

	

Organization Project Creator




ORG_READ_ONLY

	

Organization Read Only
        """

    def create(
        self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Create an API Key
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/create-one-org-api-key/)
        ### Endpoint:
        `POST /orgs/{ORG-ID}/apiKeys`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/apiKeys",
            path_params,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        api_key_id: str = Field(serialization_alias="API-KEY-ID")
        """Unique identifier of the API Key.
        """

        org_id: str = Field(serialization_alias="ORG-ID")
        """Unique identifier of the organization that owns the API Key.
        """

    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set "envelope" : true in the query.

For endpoints that return one result, response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body

For endpoints that return a list of results, the results object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(
            100.0, serialization_alias="itemsPerPage"
        )
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """Page number (1-index based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

    def delete(
        self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One API Key
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/delete-one-api-key/)
        ### Endpoint:
        `DELETE /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        """The unique identifier for the organization whose API keys you want to retrieve. Use the /orgs endpoint to retrieve all organizations to which the authenticated user has access.
        """

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set "envelope" : true in the query.

For endpoints that return one result, response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body

For endpoints that return a list of results, the results object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(
            100.0, serialization_alias="itemsPerPage"
        )
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """Page number (1-index based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

    def get_all(
        self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All API Keys
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/get-all-org-api-keys/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}/apiKeys`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/apiKeys",
            path_params,
            query_params,
            None,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        api_key_id: str = Field(serialization_alias="API-KEY-ID")
        """The unique identifier for the API key you want to retrieve. Request the /orgs/{ORG-ID}/apiKeys endpoint to retrieve all API keys for the specified organization to which the authenticated user has access.
        """

        org_id: str = Field(serialization_alias="ORG-ID")
        """The unique identifier for the organization whose API keys you want to retrieve. Use the /orgs endpoint to retrieve all organizations to which the authenticated user has access.
        """

    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set "envelope" : true in the query.

For endpoints that return one result, response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body

For endpoints that return a list of results, the results object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(
            100.0, serialization_alias="itemsPerPage"
        )
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """Page number (1-index based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

    def get_one(
        self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One API Key
        ### Document:
        [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/get-one-org-api-key/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        api_key_id: str = Field(serialization_alias="API-KEY-ID")
        """Unique identifier for the API key you want to update. Request the /orgs/{ORG-ID}/apiKeys endpoint to retrieve all API keys to which the authenticated user has access for the specified organization.
        """

        org_id: str = Field(serialization_alias="ORG-ID")
        """Unique identifier for the organization whose API keys you want to retrieve. Use the /orgs endpoint to retrieve all organizations to which the authenticated user has access.
        """

    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set "envelope" : true in the query.

For endpoints that return one result, response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body

For endpoints that return a list of results, the results object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(
            100.0, serialization_alias="itemsPerPage"
        )
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """Page number (1-index based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        desc: Optional[str] = Field(serialization_alias="desc")
        """Description of the key. This parameter is optional; however, the request must contain either a desc parameter or a roles parameter. If desc is provided, it must be between 1 and 250 characters long.
        """

        roles: Optional[list[str]] = Field(serialization_alias="roles")
        """List of roles that the API key should have. This parameter is optional; however, the request must contain either a desc parameter or a roles parameter. If roles is provided, there must be at least one role listed, and all roles must be valid for an Organization.

Organization roles include:

Role Value in API
	
Role



ORG_OWNER

	

Organization Owner




ORG_MEMBER

	

Organization Member




ORG_GROUP_CREATOR

	

Organization Project Creator




ORG_READ_ONLY

	

Organization Read Only
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update an API Key
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/update-one-org-api-key/)
        ### Endpoint:
        `PATCH /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}`
        ### Description
        No description.
        """
        return self._request(
            "PATCH",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )
