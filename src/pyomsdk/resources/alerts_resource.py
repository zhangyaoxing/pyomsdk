"""Auto-generated client for AlertsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class AlertsResource(BaseResource):
    """Client for AlertsResource resource."""

    class AcknowledgeOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_id: str = Field(serialization_alias="ALERT-ID")
        """Unique identifier for the Alert.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for the Project in which this alert is set.
        """

    class AcknowledgeOneQueryParams(BaseModel):
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

    class AcknowledgeOneBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        acknowledged_until: Optional[str] = Field(None, serialization_alias="acknowledgedUntil")
        """Timestamp in ISO 8601 date and time format in UTC until which the alert should be acknowledged.

To acknowledge an alert "forever", set the field value to a large number of years in the future. Recommend setting to 100 years in the future.

To unacknowledge an acknowledged alert, remove this parameter from your request.
        """

        acknowledgement_comment: Optional[str] = Field(
            None, serialization_alias="acknowledgementComment"
        )
        """Text description of the reason for this acknowledgement.

Ops Manager displays the comment next to the message that the alert has been acknowledged.
        """

    def acknowledge_one(
        self,
        path_params: AcknowledgeOnePathParams,
        query_params: Optional[AcknowledgeOneQueryParams],
        body_params: Optional[AcknowledgeOneBodyParams],
    ) -> dict[str, Any]:
        """
        ## Acknowledge One Alert
        ### Document:
        [Acknowledge One](https://www.mongodb.com/docs/ops-manager/current/reference/api/alerts-acknowledge-alert/)
        ### Endpoint:
        `PATCH /groups/{PROJECT-ID}/alerts/{ALERT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/groups/{PROJECT-ID}/alerts/{ALERT-ID}",
            path_params,
            query_params,
            body_params,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_id: str = Field(serialization_alias="ALERT-ID")
        """(Required.) Alert identifier.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) Project identifier.
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
        ## Get One Alert
        ### Document:
        [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/alerts-get-alert/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/alerts/{ALERT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/alerts/{ALERT-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) Project identifier.
        """

    class GetAllQueryParams(BaseModel):
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

        status: Optional[AlertStatus] = Field(None, serialization_alias="status")
        """Specify a status to return only those alerts with the specified status. Omit to return all alerts.

Ops Manager accepts the following values:

TRACKING

To return alerts with TRACKING status. If an alert's configuration specifies a notification delay, Ops Manager assigns the alert the TRACKING status until the delay period ends. After the delay, Ops Manager sets the status to OPEN, if the condition persists.

If an alert's configuration has multiple notifications, each with its own notification delay, Ops Manager uses the smallest delay value to determine when to move the alert from TRACKING to OPEN.

OPEN
To return all open alerts.
CLOSED
To return all closed alerts.
        """

    def get_all(
        self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Alerts
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/alerts-get-all-alerts/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/alerts`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/alerts",
            path_params,
            query_params,
            None,
        )
