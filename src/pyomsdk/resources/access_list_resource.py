"""Auto-generated client for AccessListResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class AccessListResource(BaseResource):
    """Client for AccessListResource resource."""

    class AddEntriesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        user_id: str = Field(serialization_alias="USER-ID")
        """(Required.) Unique identifier of the current user. To retrieve the ID of the current user, see Get All Users in One Project.
        """

    class AddEntriesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(
            100.0, serialization_alias="itemsPerPage"
        )
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag that indicates whether the response body should be in a prettyprint format.
        """

    class AddEntriesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        ip_address: str = Field(serialization_alias="ipAddress")
        """(Required.) The IP address or CIDR block that you want to add to the specified user's access list.
        """

    def add_entries(
        self,
        path_params: AddEntriesPathParams,
        query_params: Optional[AddEntriesQueryParams],
        body_params: list[AddEntriesBodyParams],
    ) -> dict[str, Any]:
        """
        ## Add Entries to an Access List
        ### Document:
        [Add Entries](https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-add-entries/)
        ### Endpoint:
        `POST /users/{USER-ID}/accessList`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/users/{USER-ID}/accessList",
            path_params,
            query_params,
            body_params,
        )

    class DeleteEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        access_list_entry: str = Field(serialization_alias="ACCESS-LIST-ENTRY")
        """The IP or CIDR address. If the entry includes a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /.
        """

        user_id: str = Field(serialization_alias="USER-ID")
        """(Required.) Unique identifier of the current user. To retrieve the ID of the current user, see Get All Users in One Project.
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
        ## Delete One Entry from One Access List
        ### Document:
        [Delete Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-delete-entry/)
        ### Endpoint:
        `DELETE /users/{USER-ID}/accessList/{ACCESS-LIST-ENTRY}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/users/{USER-ID}/accessList/{ACCESS-LIST-ENTRY}",
            path_params,
            query_params,
            None,
        )

    class GetForCurrentUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        user_id: str = Field(serialization_alias="USER-ID")
        """(Required.) User Unique identifier of the current user. To retrieve the ID of the current user, see Get All Users in One Project.
        """

    class GetForCurrentUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(
            100.0, serialization_alias="itemsPerPage"
        )
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag that indicates whether the response body should be in a prettyprint format.
        """

    def get_for_current_user(
        self,
        path_params: GetForCurrentUserPathParams,
        query_params: Optional[GetForCurrentUserQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Access List for the Current User
        ### Document:
        [Get for Current User](https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-get-for-current-user/)
        ### Endpoint:
        `GET /users/{USER-ID}/accessList`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/users/{USER-ID}/accessList",
            path_params,
            query_params,
            None,
        )

    class GetForIpAddressPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        access_list_entry: str = Field(serialization_alias="ACCESS-LIST-ENTRY")
        """The IP or CIDR address. If the entry includes a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /.
        """

        user_id: str = Field(serialization_alias="USER-ID")
        """(Required.) Unique identifier of the current user. To retrieve the ID of the current user, see Get All Users in One Project.
        """

    class GetForIpAddressQueryParams(BaseModel):
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

    def get_for_ip_address(
        self,
        path_params: GetForIpAddressPathParams,
        query_params: Optional[GetForIpAddressQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Access List for an IP Address
        ### Document:
        [Get for IP Address](https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-get-for-ip-address/)
        ### Endpoint:
        `GET /users/{USER-ID}/accessList/{ACCESS-LIST-ENTRY}`
        ### Description
        Retrieves an access list entity if the value of IP-ADDRESS equals the value of the entity's ipAddress field. This does not retrieve an object where the value of IP-ADDRESS is contained within the values allowed by the cidrBlock field.
        """
        return self._request(
            "GET",
            "/users/{USER-ID}/accessList/{ACCESS-LIST-ENTRY}",
            path_params,
            query_params,
            None,
        )
