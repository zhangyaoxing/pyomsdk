"""Auto-generated client for GlobalEventsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class GlobalEventsResource(BaseResource):
    """Client for GlobalEventsResource resource."""

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

        event_type: Optional[str] = Field("None", serialization_alias="eventType")
        """Return only events of the specified types. Accepted values include:

To review the types of events that generate alerts, see Alert Types.

For a complete list of events included in the Ops Manager audit log, see Audit Events.
        """

        items_per_page: Optional[float] = Field(
            100.0, serialization_alias="itemsPerPage"
        )
        """Number of items to return per page, up to a maximum of 500.
        """

        max_date: Optional[str] = Field("None", serialization_alias="maxDate")
        """Return only events for which the created date is less than or equal to the specified Timestamp in ISO 8601 date and time format in UTC.
        """

        min_date: Optional[str] = Field("None", serialization_alias="minDate")
        """Return only events for which the created date is greater than or equal to the specified Timestamp in ISO 8601 date and time format in UTC.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """Page number (1-index based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

    def get_all(
        self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Global Events
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-global/)
        - Resource: `GET /globalEvents`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/globalEvents",
            None,
            query_params,
            None,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        event_id: str = Field("None", serialization_alias="eventId")
        """Unique identifier of the desired event.
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
        ## Get One Global Event
        - Document: [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-global/)
        - Resource: `GET /globalEvents/{eventId}`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/globalEvents/{eventId}",
            path_params,
            query_params,
            None,
        )
