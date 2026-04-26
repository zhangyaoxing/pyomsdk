"""Auto-generated client for AutomationResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class AutomationResource(BaseResource):
    """Client for AutomationResource resource."""

    class GetStatusOfLast50PlansPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """(Required.) The unique identifier for the group.
        """

    class GetStatusOfLast50PlansQueryParams(BaseModel):
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

    def get_status_of_last_50_plans(
        self,
        path_params: GetStatusOfLast50PlansPathParams,
        query_params: Optional[GetStatusOfLast50PlansQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Automation Status of Last 50 Plans
        ### Document:
        [Get Status of Last 50 Plans](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-status-full/)
        ### Endpoint:
        `GET /groups/{GROUP-ID}/automationStatus/full`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{GROUP-ID}/automationStatus/full",
            path_params,
            query_params,
            None,
        )

    class GetStatusPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) The unique identifier for the project.
        """

    class GetStatusQueryParams(BaseModel):
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

    def get_status(
        self,
        path_params: GetStatusPathParams,
        query_params: Optional[GetStatusQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Automation Status of Latest Plan
        ### Document:
        [Get Status](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-status/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/automationStatus`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationStatus",
            path_params,
            query_params,
            None,
        )
