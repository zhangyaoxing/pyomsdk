"""Auto-generated client for GlobalAlertsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class GlobalAlertsResource(BaseResource):
    """Client for GlobalAlertsResource resource."""

    class AcknowledgeOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_id: str = Field(serialization_alias="ALERT-ID")
        """Unique identifier of the alert you want to acknowledge.
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

        acknowledged_until: str = Field(serialization_alias="acknowledgedUntil")
        """Timestamp in ISO 8601 date and time format in UTC through which you acknowledge this alert. After this time passes, Ops Manager reverts the alert to un-acknowledged.

To prevent the alert from resuming any time soon, set the date and time to some point in the distant future.

To un-acknowledge an alert, specify a time and date in the past.
        """

        acknowledgement_comment: Optional[str] = Field(
            serialization_alias="acknowledgementComment"
        )
        """Comment describing the alert acknowledgement.
        """

    def acknowledge_one(
        self,
        path_params: AcknowledgeOnePathParams,
        query_params: Optional[AcknowledgeOneQueryParams],
        body_params: AcknowledgeOneBodyParams,
    ) -> dict[str, Any]:
        """
        ## Acknowledge One Global Alert
        - Document: [Acknowledge One](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alerts-ack-one/)
        - Resource: `PATCH /globalAlerts/{ALERT-ID}`
        - Description: You can acknowledge one alert until the time and date you specify. You can also un-acknowledge an alert by specifying a date and time in the past.
        """
        return self._request(
            "PATCH",
            "/globalAlerts/{ALERT-ID}",
            path_params,
            query_params,
            body_params,
        )

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        created_on_or_after: Optional[str] = Field(
            serialization_alias="createdOnOrAfter"
        )
        """Creation date of alerts you want to return. Ops Manager returns alerts created on or after the date you indicate.
        """

        created_on_or_before: Optional[str] = Field(
            serialization_alias="createdOnOrBefore"
        )
        """Creation date of alerts you want to return. Ops Manager returns alerts created on or before the date you indicate.
        """

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

        status: Optional[AlertStatus] = Field(serialization_alias="status")
        """Status of alerts you want to return. Ops Manager returns alerts that match the status you indicate. Accepted values include:

TRACKING

	

Alert conditions exist, but the condition hasn't persisted for long enough to trigger an alert.




OPEN

	

Alert is open.




CLOSED

	

Alert is closed.
        """

    def get_all(
        self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Global Alerts
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alerts-get-all/)
        - Resource: `GET /globalAlerts`
        - Description: Retrieve all global alerts.
        """
        return self._request(
            "GET",
            "/globalAlerts",
            None,
            query_params,
            None,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_id: str = Field(serialization_alias="ALERT-ID")
        """Unique identifier of the alert you want to retrieve.
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
        ## Get One Global Alert
        - Document: [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alerts-get-one/)
        - Resource: `GET /globalAlerts/{ALERT-ID}`
        - Description: Retrieve one alert by its ALERT-ID.
        """
        return self._request(
            "GET",
            "/globalAlerts/{ALERT-ID}",
            path_params,
            query_params,
            None,
        )
