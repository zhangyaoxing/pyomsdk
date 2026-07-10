r"""Auto-generated client for EventsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class EventsResource(BaseResource):
    r"""Client for EventsResource resource."""

    class GetAllOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="orgId")
        r"""Unique identifier of the organization associated with the events.
        """

    class GetAllOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=None, serialization_alias="envelope")
        r"""Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `"envelope" : true` in the
query.

For endpoints that return one result, response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |

For endpoints that return a list of results, the `results`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        event_type: Optional[str] = Field(default=None, serialization_alias="eventType")
        r"""Return only events of the specified types.

To review the types of events that generate alerts, see
[Alert Types.](/docs/ops-manager/current/reference/alert-types/)

For a complete list of events included in the Ops Manager audit log, see
[Audit Events.](/docs/ops-manager/current/reference/audit-events/)
        """

        include_raw: Optional[bool] = Field(default=False, serialization_alias="includeRaw")
        r"""Specifies whether to include the `raw` document in the output.
The `raw` document contains additional meta information about
the event.

**IMPORTANT:** The values in the `raw` document differ depending
on the resource that the event applies to. Use this field with caution,
as its structure may vary across resource types.
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        max_date: Optional[str] = Field(default=None, serialization_alias="maxDate")
        r"""Return only events for which the created date is less than or
equal to the specified Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC.
        """

        min_date: Optional[str] = Field(default=None, serialization_alias="minDate")
        r"""Return only events for which the created date is greater than
or equal to the specified Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC.
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""Page number (1-index based).
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_all_organization(
        self,
        path_params: GetAllOrganizationPathParams,
        query_params: Optional[GetAllOrganizationQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get All Organization Events
        ### Document:
        [Get All (Organization)](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-for-org/)
        ### Endpoint:
        `GET /orgs/{orgId}/events`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{orgId}/events",
            path_params,
            query_params,
            None,
        )

    class GetAllProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="groupId")
        r"""Unique identifier of the project associated with the
desired event.
        """

    class GetAllProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=None, serialization_alias="envelope")
        r"""Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `"envelope" : true` in the
query.

For endpoints that return one result, response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |

For endpoints that return a list of results, the `results`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        event_type: Optional[str] = Field(default=None, serialization_alias="eventType")
        r"""Return only events of the specified types.

To review the types of events that generate alerts, see
[Alert Types.](/docs/ops-manager/current/reference/alert-types/)

For a complete list of events included in the Ops Manager audit log, see
[Audit Events.](/docs/ops-manager/current/reference/audit-events/)
        """

        include_raw: Optional[bool] = Field(default=False, serialization_alias="includeRaw")
        r"""Specifies whether to include the `raw` document in the output.
The `raw` document contains additional meta information about
the event.

**IMPORTANT:** The values in the `raw` document differ depending
on the resource that the event applies to. Use this field with caution,
as its structure may vary across resource types.
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        max_date: Optional[str] = Field(default=None, serialization_alias="maxDate")
        r"""Return only events for which the created date is less than or
equal to the specified Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC.
        """

        min_date: Optional[str] = Field(default=None, serialization_alias="minDate")
        r"""Return only events for which the created date is greater than
or equal to the specified Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC.
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""Page number (1-index based).
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_all_project(
        self,
        path_params: GetAllProjectPathParams,
        query_params: Optional[GetAllProjectQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get All Project Events
        ### Document:
        [Get All (Project)](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-for-project/)
        ### Endpoint:
        `GET /groups/{groupId}/events`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{groupId}/events",
            path_params,
            query_params,
            None,
        )

    class GetOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        event_id: str = Field(serialization_alias="eventId")
        r"""Unique identifier of the desired event.
        """

        org_id: str = Field(serialization_alias="orgId")
        r"""Unique identifier of the organization associated with the
desired event.
        """

    class GetOneOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Specifies whether or not to wrap the response in an [envelope.](/docs/ops-manager/current/core/api/#std-label-api-envelope)
        """

        include_raw: Optional[bool] = Field(default=False, serialization_alias="includeRaw")
        r"""Specifies whether to include the `raw` document in the output.
The `raw` document contains additional meta information about
the event.

**IMPORTANT:** The values in the `raw` document differ depending
on the resource that the event applies to. Use this field with caution,
as its structure may vary across resource types.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Displays response in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_one_organization(
        self,
        path_params: GetOneOrganizationPathParams,
        query_params: Optional[GetOneOrganizationQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get One Organization Event
        ### Document:
        [Get One (Organization)](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-for-org/)
        ### Endpoint:
        `GET /orgs/{orgId}/events/{eventId}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{orgId}/events/{eventId}",
            path_params,
            query_params,
            None,
        )

    class GetOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        event_id: str = Field(serialization_alias="eventId")
        r"""Unique identifier of the desired event.
        """

        group_id: str = Field(serialization_alias="groupId")
        r"""Unique identifier of the project associated with the
desired event.
        """

    class GetOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Specifies whether or not to wrap the response in an [envelope.](/docs/ops-manager/current/core/api/#std-label-api-envelope)
        """

        include_raw: Optional[bool] = Field(default=False, serialization_alias="includeRaw")
        r"""Specifies whether to include the `raw` document in the output.
The `raw` document contains additional meta information about
the event.

**IMPORTANT:** The values in the `raw` document differ depending
on the resource that the event applies to. Use this field with caution,
as its structure may vary across resource types.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Displays response in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_one_project(
        self,
        path_params: GetOneProjectPathParams,
        query_params: Optional[GetOneProjectQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get One Project Event
        ### Document:
        [Get One (Project)](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-for-project/)
        ### Endpoint:
        `GET /groups/{groupId}/events/{eventId}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{groupId}/events/{eventId}",
            path_params,
            query_params,
            None,
        )
