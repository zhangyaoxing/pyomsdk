"""Auto-generated client for DatabasesResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class DatabasesResource(BaseResource):
    """Client for DatabasesResource resource."""

    class GetByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        database_name: str = Field("None", serialization_alias="DATABASE-NAME")
        """(Required.) The name of the MongoDB database.
        """

        host_id: str = Field("None", serialization_alias="HOST-ID")
        """(Required.) Unique identifier of the host running the MongoDB process.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """(Required.) Unique identifier of the project that owns this MongoDB process.
        """

    class GetByNameQueryParams(BaseModel):
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

    def get_by_name(
        self,
        path_params: GetByNamePathParams,
        query_params: Optional[GetByNameQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get a Database by Name
        - Document: [Get by Name](https://www.mongodb.com/docs/ops-manager/current/reference/api/database-get-by-name/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}",
            path_params,
            query_params,
            None,
        )

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field("None", serialization_alias="HOST-ID")
        """(Required.) Unique identifier of the host running the MongoDB process.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """(Required.) Unique identifier of the project that owns this MongoDB process.
        """

    class GetAllQueryParams(BaseModel):
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

    def get_all(
        self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Databases on One Host
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/databases-get-all-on-host/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/databases`
        - Description: Retrieve all databases running on the specified host.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases",
            path_params,
            query_params,
            None,
        )
