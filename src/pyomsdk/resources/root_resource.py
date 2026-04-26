"""Auto-generated client for RootResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class RootResource(BaseResource):
    """Client for RootResource resource."""

    class RootQueryParams(BaseModel):
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

    def root(
        self,
        query_params: Optional[RootQueryParams],
    ) -> dict[str, Any]:
        """
        ## Root
        ### Document:
        [Root](https://www.mongodb.com/docs/ops-manager/current/reference/api/root/)
        ### Endpoint:
        `GET /`
        ### Description
        The root resource is the starting point for the Ops Manager API. From here, you can traverse the links to reach all other API resources.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/",
            None,
            query_params,
            None,
        )
