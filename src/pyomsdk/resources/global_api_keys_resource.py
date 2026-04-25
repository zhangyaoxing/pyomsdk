"""Auto-generated client for GlobalApiKeysResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class GlobalApiKeysResource(BaseResource):
    """Client for GlobalApiKeysResource resource."""

    class CreateQueryParams(BaseModel):
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

    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        desc: str = Field(serialization_alias="desc")
        """Description of the Global API Key. Must be between 1 and 250 characters in length.
        """

        roles: GlobalRole = Field(serialization_alias="roles")
        """List of roles that the Global API Key needs to have. If the roles array is provided:

Provide at least one role

Make sure all roles are valid.

Global roles accepted by default include:

Role Value in API
	
Role



GLOBAL_AUTOMATION_ADMIN

	

Global Automation Admin




GLOBAL_BACKUP_ADMIN

	

Global Backup Admin




GLOBAL_MONITORING_ADMIN

	

Global Monitoring Admin




GLOBAL_OWNER

	

Global Owner




GLOBAL_READ_ONLY

	

Global Read Only




GLOBAL_USER_ADMIN

	

Global User Admin
        """

    def create(
        self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Global API Key
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/create-one-global-api-key/)
        ### Endpoint:
        `POST /admin/apiKeys`
        ### Description
        Create one Global API Key for Ops Manager.
        """
        return self._request(
            "POST",
            "/admin/apiKeys",
            None,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        api_key_id: str = Field(serialization_alias="API-KEY-ID")
        """Unique identifier for the API key you want to delete. Use the /admin/apiKeys endpoint to retrieve all API keys to which the authenticated user has access.
        """

    class DeleteQueryParams(BaseModel):
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

    def delete(
        self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Global API Key
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/delete-one-global-api-key/)
        ### Endpoint:
        `DELETE /admin/apiKeys/{API-KEY-ID}`
        ### Description
        Delete one Global API Key from Ops Manager using the unique identifier for that Key.
        """
        return self._request(
            "DELETE",
            "/admin/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllRolesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(None, serialization_alias="envelope")
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

        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """Page number (1-index based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

    def get_all_roles(
        self,
        query_params: Optional[GetAllRolesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Roles for Global API Keys
        ### Document:
        [Get All Roles](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-all-global-api-key-roles/)
        ### Endpoint:
        `GET /admin/apiKeys/roles`
        ### Description
        Return a list of acceptable Global Roles for Global API Keys.
        """
        return self._request(
            "GET",
            "/admin/apiKeys/roles",
            None,
            query_params,
            None,
        )

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag that indicates whether the response body should be in a prettyprint format.
        """

    def get_all(
        self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Global API Keys
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-all-global-api-keys/)
        ### Endpoint:
        `GET /admin/apiKeys`
        ### Description
        Return all Global API Keys for Ops Manager.
        """
        return self._request(
            "GET",
            "/admin/apiKeys",
            None,
            query_params,
            None,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        api_key_id: str = Field(serialization_alias="API-KEY-ID")
        """Unique identifier for the Global API Key you want to retrieve.
        """

    class GetOneQueryParams(BaseModel):
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

    def get_one(
        self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Global API Key
        ### Document:
        [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-one-global-api-key/)
        ### Endpoint:
        `GET /admin/apiKeys/{API-KEY-ID}`
        ### Description
        Return one Global API Key for Ops Manager using the unique identifier for that Key.
        """
        return self._request(
            "GET",
            "/admin/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        api_key_id: str = Field(serialization_alias="API-KEY-ID")
        """Unique identifier for the Global API key you want to update.
        """

    class UpdateQueryParams(BaseModel):
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

    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        desc: Optional[str] = Field(None, serialization_alias="desc")
        """Description of the key. This parameter is optional; however, the request must contain either a desc parameter or a roles parameter. If desc is provided, it must be between 1 and 250 characters long.
        """

        roles: Optional[GlobalRole] = Field(None, serialization_alias="roles")
        """List of roles that the Global API Key needs to have. If the roles array is provided:

Provide at least one role

Make sure all roles are valid.

Global roles accepted by default include:

Role Value in API
	
Role



GLOBAL_AUTOMATION_ADMIN

	

Global Automation Admin




GLOBAL_BACKUP_ADMIN

	

Global Backup Admin




GLOBAL_MONITORING_ADMIN

	

Global Monitoring Admin




GLOBAL_OWNER

	

Global Owner




GLOBAL_READ_ONLY

	

Global Read Only




GLOBAL_USER_ADMIN

	

Global User Admin
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update One Global API Key
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/update-one-global-api-key/)
        ### Endpoint:
        `PATCH /admin/apiKeys/{API-KEY-ID}`
        ### Description
        Update values of one Global API Key from Ops Manager using the unique identifier for that Key.
        """
        return self._request(
            "PATCH",
            "/admin/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )
