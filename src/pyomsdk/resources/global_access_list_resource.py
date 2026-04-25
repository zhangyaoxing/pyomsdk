"""Auto-generated client for GlobalAccessListResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class GlobalAccessListResource(BaseResource):
    """Client for GlobalAccessListResource resource."""

    class CreateEntryQueryParams(BaseModel):
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

    class CreateEntryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cidr_block: str = Field(serialization_alias="cidrBlock")
        """Access list entry in IPv4 or IPv6 CIDR notation to be added.
        """

        description: str = Field(serialization_alias="description")
        """Description of the Global Access List Entry. Must be between 1 and 250 characters in length.
        """

    def create_entry(
        self,
        query_params: Optional[CreateEntryQueryParams],
        body_params: CreateEntryBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Global Access List Entry
        ### Document:
        [Create Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/create-one-global-access-list/)
        ### Endpoint:
        `POST /admin/accessList`
        ### Description
        Create one Global Access List Entry for Ops Manager.
        """
        return self._request(
            "POST",
            "/admin/accessList",
            None,
            query_params,
            body_params,
        )

    class DeleteEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        access_list_id: str = Field(serialization_alias="ACCESS-LIST-ID")
        """Unique identifier for the access list entry you want to delete.
        """

    class DeleteEntryQueryParams(BaseModel):
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

    def delete_entry(
        self,
        path_params: DeleteEntryPathParams,
        query_params: Optional[DeleteEntryQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Access List Entry for a Global API Key
        ### Document:
        [Delete Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/delete-one-global-access-list/)
        ### Endpoint:
        `DELETE /admin/accessList/{ACCESS-LIST-ID}`
        ### Description
        Delete one Global Access List Entry from Ops Manager using the unique identifier for the desired IP address.
        """
        return self._request(
            "DELETE",
            "/admin/accessList/{ACCESS-LIST-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllEntriesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag that indicates whether the response body should be in a prettyprint format.
        """

    def get_all_entries(
        self,
        query_params: Optional[GetAllEntriesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Access List Entries for a Global API Key
        ### Document:
        [Get All Entries](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-all-global-access-list/)
        ### Endpoint:
        `GET /admin/accessList`
        ### Description
        Return all Global Access List Entries for Ops Manager.
        """
        return self._request(
            "GET",
            "/admin/accessList",
            None,
            query_params,
            None,
        )

    class GetOneEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        access_list_id: str = Field(serialization_alias="ACCESS-LIST-ID")
        """Unique identifier for the Global Access List Entry.
        """

    class GetOneEntryQueryParams(BaseModel):
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

    def get_one_entry(
        self,
        path_params: GetOneEntryPathParams,
        query_params: Optional[GetOneEntryQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Global Access List Entry
        ### Document:
        [Get One Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-one-global-access-list/)
        ### Endpoint:
        `GET /admin/accessList/{ACCESS-LIST-ID}`
        ### Description
        Return one Global Access List Entry using the unique identifier for the desired IP address.
        """
        return self._request(
            "GET",
            "/admin/accessList/{ACCESS-LIST-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdateEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        access_list_id: str = Field(serialization_alias="ACCESS-LIST-ID")
        """Unique identifier for the Global Access List Entry.
        """

    class UpdateEntryQueryParams(BaseModel):
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

    def update_entry(
        self,
        path_params: UpdateEntryPathParams,
        query_params: Optional[UpdateEntryQueryParams],
    ) -> dict[str, Any]:
        """
        ## Update One Global Access List Entry
        ### Document:
        [Update Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/update-one-global-access-list/)
        ### Endpoint:
        `PATCH /admin/accessList/{ACCESS-LIST-ID}`
        ### Description
        Update the values of one Global Access List Entry using the unique identifier for the desired IP address.
        """
        return self._request(
            "PATCH",
            "/admin/accessList/{ACCESS-LIST-ID}",
            path_params,
            query_params,
            None,
        )
