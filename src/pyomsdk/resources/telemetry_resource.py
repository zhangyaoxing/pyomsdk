"""Auto-generated client for TelemetryResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class TelemetryResource(BaseResource):
    """Client for TelemetryResource resource."""

    def retrieve_telemetry_data(
        self,
    ) -> dict[str, Any]:
        """
        ## Retrieve Telemetry Data
        ### Document:
        [Retrieve Telemetry Data](https://www.mongodb.com/docs/ops-manager/current/reference/api/telemetry/get-data/)
        ### Endpoint:
        `GET /collection/details`
        ### Description
        Retrieve telemetry collection status and configuration details for your Ops Manager installation.
        """
        return self._request(
            "GET",
            "/collection/details",
            None,
            None,
            None,
        )

    class ToggleTelemetryStatusBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        enabled: bool = Field(serialization_alias="enabled")
        """Set to true to enable telemetry, or false to disable telemetry.
        """

    def toggle_telemetry_status(
        self,
        body_params: ToggleTelemetryStatusBodyParams,
    ) -> dict[str, Any]:
        """
        ## Toggle Telemetry Status
        ### Document:
        [Toggle Telemetry Status](https://www.mongodb.com/docs/ops-manager/current/reference/api/telemetry/toggle-status/)
        ### Endpoint:
        `PATCH /collection/status`
        ### Description
        Enable or disable telemetry collection for your Ops Manager installation.
        """
        return self._request(
            "PATCH",
            "/collection/status",
            None,
            None,
            body_params,
        )
