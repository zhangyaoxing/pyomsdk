"""Auto-generated client for IntegrationSettingsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class IntegrationSettingsResource(BaseResource):
    """Client for IntegrationSettingsResource resource."""

    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        integration_type: IntegrationType = Field(
            serialization_alias="INTEGRATION-TYPE"
        )
        """Third-party service identifier. Accepted values are:

DATADOG

HIP_CHAT

PAGER_DUTY

SLACK

NEW_RELIC

OPS_GENIE

VICTOR_OPS

WEBHOOK
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Project identifier.
        """

    class CreateQueryParams(BaseModel):
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

    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        type: IntegrationType = Field(serialization_alias="type")
        """The type of the third-party integration.
        """

    def create(
        self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
                ## Create a Configuration for a Third-Party Service Integration
                - Document: [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-create/)
                - Resource: `POST /groups/{PROJECT-ID}/integrations/{INTEGRATION-TYPE}`
                - Description: Use the following dataclasses to pass the integration settings:

        - PagerDutyIntegrationSettings
        - SlackIntegrationSettings
        - DatadogIntegrationSettings
        - HipChatIntegrationSettings
        - OpsgenieIntegrationSettings
        - VictorOpsIntegrationSettings
        - WebhookIntegrationSettings
        - MicrosoftTeamsIntegrationSettings
        - PrometheusIntegrationSettings

        """
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        integration_type: IntegrationType = Field(
            serialization_alias="INTEGRATION-TYPE"
        )
        """Third-party service identifier. Accepted values are:

DATADOG

HIP_CHAT

PAGER_DUTY

SLACK

NEW_RELIC

OPS_GENIE

VICTOR_OPS

WEBHOOK
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Project identifier.
        """

    class DeleteQueryParams(BaseModel):
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

    def delete(
        self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete a Configuration for a Third-Party Service Integration
        - Document: [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-delete/)
        - Resource: `DELETE /groups/{PROJECT-ID}/integrations/{INTEGRATION-TYPE}`
        - Description: No description.
        """
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            None,
        )

    class ReturnLatestPrometheusTargetsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique 24-hexadecimal digit string that identifies your project.
        """

    class ReturnLatestPrometheusTargetsQueryParams(BaseModel):
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

    def return_latest_prometheus_targets(
        self,
        path_params: ReturnLatestPrometheusTargetsPathParams,
        query_params: Optional[ReturnLatestPrometheusTargetsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Return the Latest Targets for Prometheus
        - Document: [Return Latest Prometheus Targets](https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-discovery/)
        - Resource: `GET /groups/{PROJECT-ID}/discovery`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/discovery",
            path_params,
            query_params,
            None,
        )

    class GetAllConfigurationsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Project identifier.
        """

    class GetAllConfigurationsQueryParams(BaseModel):
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

    def get_all_configurations(
        self,
        path_params: GetAllConfigurationsPathParams,
        query_params: Optional[GetAllConfigurationsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Configurations for Third-Party Service Integrations
        - Document: [Get All Configurations](https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-get-all/)
        - Resource: `GET /api/public/v1.0/groups/{PROJECT-ID}/integrations`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/integrations",
            path_params,
            query_params,
            None,
        )

    class GetOneConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        integration_type: IntegrationType = Field(
            serialization_alias="INTEGRATION-TYPE"
        )
        """Third-party service identifier. Accepted values are:

DATADOG

HIP_CHAT

PAGER_DUTY

SLACK

NEW_RELIC

OPS_GENIE

VICTOR_OPS

WEBHOOK
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Project identifier.
        """

    class GetOneConfigurationQueryParams(BaseModel):
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

    def get_one_configuration(
        self,
        path_params: GetOneConfigurationPathParams,
        query_params: Optional[GetOneConfigurationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get the Configuration of a Third-Party Service Integration
        - Document: [Get One Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-get-one/)
        - Resource: `GET /groups/{PROJECT-ID}/integrations/{INTEGRATION-TYPE}`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        integration_type: IntegrationType = Field(
            serialization_alias="INTEGRATION-TYPE"
        )
        """Third-party service identifier. Accepted values are:

DATADOG

HIP_CHAT

PAGER_DUTY

SLACK

NEW_RELIC

OPS_GENIE

VICTOR_OPS

WEBHOOK
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Project identifier.
        """

    class UpdateQueryParams(BaseModel):
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

    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        type: IntegrationType = Field(serialization_alias="type")
        """The type of the third-party integration.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """
                ## Update a Configuration for a Third-Party Service Integration
                - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-update/)
                - Resource: `PUT /groups/{PROJECT-ID}/integrations/{INTEGRATION-TYPE}`
                - Description: Use the following dataclasses to pass the integration settings:

        - PagerDutyIntegrationSettings
        - SlackIntegrationSettings
        - DatadogIntegrationSettings
        - HipChatIntegrationSettings
        - OpsgenieIntegrationSettings
        - VictorOpsIntegrationSettings
        - WebhookIntegrationSettings
        - MicrosoftTeamsIntegrationSettings
        - PrometheusIntegrationSettings

        """
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            body_params,
        )
