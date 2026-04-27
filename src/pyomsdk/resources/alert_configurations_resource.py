"""Auto-generated client for AlertConfigurationsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class AlertConfigurationsResource(BaseResource):
    """Client for AlertConfigurationsResource resource."""

    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for this Project.
        """

    class CreateQueryParams(BaseModel):
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

    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        enabled: Optional[bool] = Field(None, serialization_alias="enabled")
        """If omitted, the configuration is disabled.
        """

        event_type_name: EventTypeName = Field(serialization_alias="eventTypeName")
        """The type of event that triggers an alert.

Values include:

Agent

AUTOMATION_AGENT_DOWN

AUTOMATION_AGENT_UP

BACKUP_AGENT_CONF_CALL_FAILURE

BACKUP_AGENT_DOWN

BACKUP_AGENT_UP

BACKUP_AGENT_VERSION_BEHIND

BACKUP_AGENT_VERSION_CURRENT

MONITORING_AGENT_DOWN

MONITORING_AGENT_UP

MONITORING_AGENT_VERSION_BEHIND

MONITORING_AGENT_VERSION_CURRENT

NEW_AGENT

Automation Configuration

AUTOMATION_CONFIG_PUBLISHED_AUDIT

Backup

BAD_CLUSTERSHOTS

CLUSTER_BLACKLIST_UPDATED_AUDIT

CLUSTER_CHECKKPOINT_UPDATED_AUDIT

CLUSTER_CREDENTIAL_UPDATED_AUDIT

CLUSTER_SNAPSHOT_SCHEDULE_UPDATED_AUDIT

CLUSTER_STATE_CHANGED_AUDIT

CLUSTER_STORAGE_ENGINE_UPDATED_AUDIT

CLUSTERSHOT_DELETED_AUDIT

CLUSTERSHOT_EXPIRY_UPDATED_AUDIT

CONSISTENT_BACKUP_CONFIGURATION

GOOD_CLUSTERSHOT

INCONSISTENT_BACKUP_CONFIGURATION

INITIAL_SYNC_FINISHED_AUDIT

INITIAL_SYNC_STARTED_AUDIT

OPLOG_BEHIND

OPLOG_CURRENT

RESTORE_REQUESTED_AUDIT

RESYNC_PERFORMED

RESYNC_REQUIRED

RS_BLACKLIST_UPDATED_AUDIT

RS_CREDENTIAL_UPDATED_AUDIT

RS_ROTATE_MASTER_KEY_AUDIT

RS_SNAPSHOT_SCHEDULE_UPDATED_AUDIT

RS_STATE_CHANGED_AUDIT

RS_STORAGE_ENGINE_UPDATED_AUDIT

SNAPSHOT_DELETED_AUDIT

SNAPSHOT_EXPIRY_UPDATED_AUDIT

SYNC_PENDING_AUDIT

SYNC_REQUIRED_AUDIT

BI Connector

BI_CONNECTOR_DOWN

BI_CONNECTOR_UP

Cluster

CLUSTER_MONGOS_IS_MISSING

CLUSTER_MONGOS_IS_PRESENT

SHARD_ADDED

SHARD_REMOVED

Data Explorer Accessed

DATA_EXPLORER

DATA_EXPLORER_CRUD

Host

ADD_HOST_AUDIT

ADD_HOST_TO_REPLICA_SET_AUDIT

DELETE_HOST_AUDIT

HOST_DOWN

HOST_RECOVERING

HOST_RESTARTED

HOST_ROLLBACK

HOST_SSL_CERTIFICATE_STALE

OUTSIDE_METRIC_THRESHOLD

REMOVE_HOST_FROM_REPLICA_SET_AUDIT

UNDELETE_HOST_AUDIT

VERSION_BEHIND

Organization

ALL_ORG_USERS_HAVE_MFA

ORG_API_KEY_ADDED

ORG_API_KEY_DELETED

ORG_EMPLOYEE_ACCESS_RESTRICTED

ORG_EMPLOYEE_ACCESS_UNRESTRICTED

ORG_PUBLIC_API_ACCESS_LIST_NOT_REQUIRED

ORG_PUBLIC_API_ACCESS_LIST_REQUIRED

ORG_RENAMED

ORG_TWO_FACTOR_AUTH_OPTIONAL

ORG_TWO_FACTOR_AUTH_REQUIRED

ORG_USERS_WITHOUT_MFA

Project

ALL_USERS_HAVE_MULTI_FACTOR_AUTH

USERS_WITHOUT_MULTI_FACTOR_AUTH

Replica Set

CONFIGURATION_CHANGED

ENOUGH_HEALTHY_MEMBERS

MEMBER_ADDED

MEMBER_REMOVED

MULTIPLE_PRIMARIES

NO_PRIMARY

ONE_PRIMARY

PRIMARY_ELECTED

TOO_FEW_HEALTHY_MEMBERS

TOO_MANY_ELECTIONS

TOO_MANY_UNHEALTHY_MEMBERS

Team

TEAM_ADDED_TO_GROUP

TEAM_CREATED

TEAM_DELETED

TEAM_NAME_CHANGED

TEAM_REMOVED_FROM_GROUP

TEAM_ROLES_MODIFIED

TEAM_UPDATED

USER_ADDED_TO_TEAM

User

INVITED_TO_GROUP

INVITED_TO_ORG

JOIN_GROUP_REQUEST_APPROVED_AUDIT

JOIN_GROUP_REQUEST_DENIED_AUDIT

JOINED_GROUP

JOINED_ORG

JOINED_TEAM

REMOVED_FROM_GROUP

REMOVED_FROM_ORG

REMOVED_FROM_TEAM

REQUESTED_TO_JOIN_GROUP

USER_ROLES_CHANGED_AUDIT

To review the full list of events that generate alerts and their descriptions, see Alert Types. For a complete list of events included in the Ops Manager audit log, see Audit Events.
        """

        class MatchersParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            field_name: Optional[MatcherFieldName] = Field(None, serialization_alias="fieldName")
            """Name of the field in the target object to match on.

Host alerts support these fields:

HOSTNAME

PORT

HOSTNAME_AND_PORT

REPLICA_SET_NAME

TYPE_NAME

Replica set alerts support these fields:

REPLICA_SET_NAME

SHARD_NAME

CLUSTER_NAME

Sharded cluster alerts support these fields:

CLUSTER_NAME

SHARD_NAME

All other types of alerts do not support matchers.
            """

            operator: Optional[MatcherOperator] = Field(None, serialization_alias="operator")
            """Operator to test the field's value. Accepted values are:

EQUALS

NOT_EQUALS

CONTAINS

NOT_CONTAINS

STARTS_WITH

ENDS_WITH

REGEX
            """

            value: Optional[MatcherValue] = Field(None, serialization_alias="value")
            """Value to test with the specified operator.

If matchers.fieldName is set to TYPE_NAME, you can match on the following values:

PRIMARY

SECONDARY

STANDALONE

CONFIG

MONGOS
            """

        matchers: Optional[list[MatchersParams]] = Field(None, serialization_alias="matchers")
        """Rules to apply when matching an object against this alert configuration. Only entities that match all these rules are checked for an alert condition.

You can filter using the matchers array only when the eventTypeName specifies an event for a host, replica set, or sharded cluster.
        """

        class MetricThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            metric_name: Optional[str] = Field(None, serialization_alias="metricName")
            """Name of the metric to check. Supports the same values as the metricName field of the alerts resource.
            """

            mode: Optional[str] = Field(None, serialization_alias="mode")
            """Set to AVERAGE to compute the average of this metric.
            """

            operator: Optional[ThresholdOperator] = Field(None, serialization_alias="operator")
            """Operator to apply when checking the current metric value against the threshold value. Accepted values are:

GREATER_THAN

LESS_THAN
            """

            threshold: Optional[int] = Field(None, serialization_alias="threshold")
            """Threshold value outside of which an alert is triggered.
            """

            units: Optional[Unit] = Field(None, serialization_alias="units")
            """Units for the threshold value. Depends on the type of metric.

For example, a metric that measures memory consumption would have a byte measurement, while a metric that measures time would have a time unit.

Accepted values are:

RAW

BITS

BYTES

KILOBITS

KILOBYTES

MEGABITS

MEGABYTES

GIGABITS

GIGABYTES

TERABYTES

PETABYTES

MILLISECONDS

SECONDS

MINUTES

HOURS

DAYS
            """

        metric_threshold: MetricThresholdParams = Field(serialization_alias="metricThreshold")
        """Threshold that will cause an alert to be triggered. Required if "eventTypeName" : "OUTSIDE_METRIC_THRESHOLD".
        """

        class NotificationsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            api_token: str = Field(serialization_alias="apiToken")
            """Slack API token or Bot token. Required if "notifications.typeName" : "SLACK". If the token later becomes invalid, Ops Manager sends an email to the Project owner and eventually removes the token.

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

View or edit the alert through the UI.

Query the third-party integration settings through the API.
            """

            channel_name: str = Field(serialization_alias="channelName")
            """Slack channel name. Required if "notifications.typeName" : "SLACK".
            """

            datadog_api_key: str = Field(serialization_alias="datadogApiKey")
            """DataDog API Key. Found in the DataDog dashboard. Required if "notifications.typeName" : "DATADOG".

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

View or edit the alert through the UI.

Query the third-party integration settings through the API.
            """

            delay_min: Optional[int] = Field(None, serialization_alias="delayMin")
            """Number of minutes to wait after an alert condition is detected before sending out the first notification.
            """

            email_address: str = Field(serialization_alias="emailAddress")
            """Email address to which to send notification. Required if "notifications.typeName" : "EMAIL".
            """

            email_enabled: bool = Field(serialization_alias="emailEnabled")
            """Determines if email notifications should be sent. Required if:

"notifications.typeName" : "GROUP"

"notifications.typeName" : "USER"
            """

            interval_min: Optional[int] = Field(None, serialization_alias="intervalMin")
            """Number of minutes to wait between successive notifications for unacknowledged alerts that are not resolved.
            """

            microsoft_teams_webhook_url: str = Field(serialization_alias="microsoftTeamsWebhookUrl")
            """Microsoft Teams channel incoming webhook URL. Required if "notifications.typeName" : "MICROSOFT_TEAMS".

When you view or edit the alert for a webhook notification, the URL appears partially redacted, and the secret appears completely redacted.
            """

            mobile_number: str = Field(serialization_alias="mobileNumber")
            """Mobile number to send SMS messages to. Required if "notifications.typeName" : "SMS".
            """

            notification_token: str = Field(serialization_alias="notificationToken")
            """A HipChat API token. Required if "notifications.typeName" : "HIP_CHAT". If the token later becomes invalid, Ops Manager sends an email to the Project owner and eventually removes the token.

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

View or edit the alert through the UI.

Query the third-party integration settings through the API.
            """

            role: str = Field(serialization_alias="role")
            """Ops Manager role in current Project. Required if "notifications.typeName" : "GROUP".
            """

            room_name: str = Field(serialization_alias="roomName")
            """HipChat room name. Required if "notifications.typeName" : "HIP_CHAT".
            """

            service_key: str = Field(serialization_alias="serviceKey")
            """PagerDuty integration key. Required if "notifications.typeName" : "PAGER_DUTY".

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

View or edit the alert through the UI.

Query the third-party integration settings through the API.
            """

            sms_enabled: bool = Field(serialization_alias="smsEnabled")
            """Flag indicating SMS notifications must be sent. Required if:

"notifications.typeName" : "GROUP"

"notifications.typeName" : "USER"
            """

            team_id: Optional[str] = Field(None, serialization_alias="teamId")
            """Unique identifier of a team.
            """

            type_name: Optional[NotificationsTypeName] = Field(None, serialization_alias="typeName")
            """Type of alert notification. Accepted values are:

DATADOG

EMAIL

GROUP (Project)

HIPCHAT

ORG

PAGER_DUTY

SLACK

SMS (Twilio integration must be configured)

USER

WEBHOOK
            """

            username: str = Field(serialization_alias="username")
            """Name of an Ops Manager user to which to send notifications. Specify a user in the Project that owns the alert configuration. Required if "notifications.typeName" : "USER".
            """

            webhook_body_template: Optional[str] = Field(
                None, serialization_alias="webhookBodyTemplate"
            )
            """Template for the body content of webhook notifications. You can use variables in the template that are replaced with alert-specific values when the notification is sent.
            """

            webhook_headers_template: Optional[str] = Field(
                None, serialization_alias="webhookHeadersTemplate"
            )
            """Template for custom headers to include in webhook notifications. You can use variables in the template that are replaced with alert-specific values when the notification is sent.
            """

            webhook_secret: Optional[str] = Field(None, serialization_alias="webhookSecret")
            """A value used to authenticate with the Webhook that accepts and forwards the notification. You can explicitly declare a secret only in a request that has both:

A notifications.typeName of WEBHOOK

An explicitly declared notifications.webhookURL

You can configure a webhookSecret for a default webhookURL only either on the Integrations page, or with the Integrations API.

To explicitly declare a webhookURL without a webhookSecret, omit this field.

After creating a webhook notification, the URL is partially redacted when you view or edit the alert, and the secret is completely redacted.
            """

            webhook_url: Optional[str] = Field(None, serialization_alias="webhookUrl")
            """URL for the webhook that triggers this notification. If you do not explicitly declare a webhookUrl, your request will use the default webhookUrl set either on the Integrations page, or with the Integrations API.

After creating a webhook notification, the URL is partially redacted when you view or edit the alert, and the secret is completely redacted.
            """

        notifications: list[NotificationsParams] = Field(serialization_alias="notifications")
        """Notifications to send when an alert condition is detected.
        """

        class ThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            operator: Optional[ThresholdOperator] = Field(None, serialization_alias="operator")
            """Operator to apply when checking the current metric value against the threshold value.

GREATER_THAN

LESS_THAN
            """

            threshold: Optional[int] = Field(None, serialization_alias="threshold")
            """Threshold value outside of which an alert is triggered.
            """

        threshold: ThresholdParams = Field(serialization_alias="threshold")
        """Threshold that will cause an alert to be triggered. Required if:

"eventTypeName" : "TOO_FEW_HEALTHY_MEMBERS"

"eventTypeName" : TOO_MANY_UNHEALTHY_MEMBERS
        """

    def create(
        self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create an Alert Configuration
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-create-config/)
        ### Endpoint:
        `POST /groups/{PROJECT-ID}/alertConfigs`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{PROJECT-ID}/alertConfigs",
            path_params,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_config_id: str = Field(serialization_alias="ALERT-CONFIG-ID")
        """Unique identifier for this alert configuration.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for this Project.
        """

    class DeleteQueryParams(BaseModel):
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

    def delete(
        self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete an Alert Configuration
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-delete-config/)
        ### Endpoint:
        `DELETE /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )

    class EnableDisablePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_config_id: str = Field(serialization_alias="ALERT-CONFIG-ID")
        """Unique identifier for this alert configuration.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for this Project.
        """

    class EnableDisableQueryParams(BaseModel):
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

    class EnableDisableBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        enabled: Optional[bool] = Field(None, serialization_alias="enabled")
        """Specify true to enable; false to disable.
        """

    def enable_disable(
        self,
        path_params: EnableDisablePathParams,
        query_params: Optional[EnableDisableQueryParams],
        body_params: Optional[EnableDisableBodyParams],
    ) -> dict[str, Any]:
        """
        ## Enable/Disable Alert Configuration
        ### Document:
        [Enable/Disable](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-enable-disable-config/)
        ### Endpoint:
        `PATCH /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}`
        ### Description
        No description.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )

    class GetAllForAProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for this Project.
        """

    class GetAllForAProjectQueryParams(BaseModel):
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

    def get_all_for_a_project(
        self,
        path_params: GetAllForAProjectPathParams,
        query_params: Optional[GetAllForAProjectQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Alert Configurations for a Project
        ### Document:
        [Get All for a Project](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-all-configs/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/alertConfigs`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/alertConfigs",
            path_params,
            query_params,
            None,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_config_id: str = Field(serialization_alias="ALERT-CONFIG-ID")
        """Unique identifier for this alert configuration.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for this Project.
        """

    class GetOneQueryParams(BaseModel):
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

    def get_one(
        self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get an Alert Configuration
        ### Document:
        [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-config/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )

    class GetMatchersFieldNamesQueryParams(BaseModel):
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

    def get_matchers_field_names(
        self,
        query_params: Optional[GetMatchersFieldNamesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Alert Configuration Matchers Field Names
        ### Document:
        [Get Matchers Field Names](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-matchers-field-names/)
        ### Endpoint:
        `GET /alertConfigs/matchers/fieldNames`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/alertConfigs/matchers/fieldNames",
            None,
            query_params,
            None,
        )

    class GetOpenAlertsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_config_id: str = Field(serialization_alias="ALERT-CONFIG-ID")
        """Unique identifier for this alert configuration.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for this Project.
        """

    class GetOpenAlertsQueryParams(BaseModel):
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

    def get_open_alerts(
        self,
        path_params: GetOpenAlertsPathParams,
        query_params: Optional[GetOpenAlertsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Open Alerts for Alert Configuration
        ### Document:
        [Get Open Alerts](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-open-alerts/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}/alerts`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}/alerts",
            path_params,
            query_params,
            None,
        )

    class TestProjectAlertConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_config_id: str = Field(serialization_alias="ALERT-CONFIG-ID")
        """Unique 24-hexadecimal digit string that identifies the alert configuration.
        """

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the project.
        """

        notification_id: str = Field(serialization_alias="NOTIFICATION-ID")
        """Unique 24-hexadecimal digit string that identifies the notification method within the alert configuration.
        """

    def test_project_alert_configuration(
        self,
        path_params: TestProjectAlertConfigurationPathParams,
    ) -> dict[str, Any]:
        """
        ## Test Project Alert Configuration
        ### Document:
        [Test Project Alert Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-test-config/)
        ### Endpoint:
        `POST /api/public/v1.0/groups/{GROUP-ID}/alertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test`
        ### Description
        Triggers a test notification for a specific notification method in a project alert configuration. This endpoint sends a test payload with dummy data and rendered templates to validate your webhook configuration.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{GROUP-ID}/alertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test",
            path_params,
            None,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_config_id: str = Field(serialization_alias="ALERT-CONFIG-ID")
        """Unique identifier for this alert configuration.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for this Project.
        """

    class UpdateQueryParams(BaseModel):
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

    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        enabled: Optional[bool] = Field(None, serialization_alias="enabled")
        """If omitted, the configuration is disabled.
        """

        event_type_name: EventTypeName = Field(serialization_alias="eventTypeName")
        """The type of event that triggers an alert.

Values include:

Agent

AUTOMATION_AGENT_DOWN

AUTOMATION_AGENT_UP

BACKUP_AGENT_CONF_CALL_FAILURE

BACKUP_AGENT_DOWN

BACKUP_AGENT_UP

BACKUP_AGENT_VERSION_BEHIND

BACKUP_AGENT_VERSION_CURRENT

MONITORING_AGENT_DOWN

MONITORING_AGENT_UP

MONITORING_AGENT_VERSION_BEHIND

MONITORING_AGENT_VERSION_CURRENT

NEW_AGENT

Automation Configuration

AUTOMATION_CONFIG_PUBLISHED_AUDIT

Backup

BAD_CLUSTERSHOTS

CLUSTER_BLACKLIST_UPDATED_AUDIT

CLUSTER_CHECKKPOINT_UPDATED_AUDIT

CLUSTER_CREDENTIAL_UPDATED_AUDIT

CLUSTER_SNAPSHOT_SCHEDULE_UPDATED_AUDIT

CLUSTER_STATE_CHANGED_AUDIT

CLUSTER_STORAGE_ENGINE_UPDATED_AUDIT

CLUSTERSHOT_DELETED_AUDIT

CLUSTERSHOT_EXPIRY_UPDATED_AUDIT

CONSISTENT_BACKUP_CONFIGURATION

GOOD_CLUSTERSHOT

INCONSISTENT_BACKUP_CONFIGURATION

INITIAL_SYNC_FINISHED_AUDIT

INITIAL_SYNC_STARTED_AUDIT

OPLOG_BEHIND

OPLOG_CURRENT

RESTORE_REQUESTED_AUDIT

RESYNC_PERFORMED

RESYNC_REQUIRED

RS_BLACKLIST_UPDATED_AUDIT

RS_CREDENTIAL_UPDATED_AUDIT

RS_ROTATE_MASTER_KEY_AUDIT

RS_SNAPSHOT_SCHEDULE_UPDATED_AUDIT

RS_STATE_CHANGED_AUDIT

RS_STORAGE_ENGINE_UPDATED_AUDIT

SNAPSHOT_DELETED_AUDIT

SNAPSHOT_EXPIRY_UPDATED_AUDIT

SYNC_PENDING_AUDIT

SYNC_REQUIRED_AUDIT

BI Connector

BI_CONNECTOR_DOWN

BI_CONNECTOR_UP

Cluster

CLUSTER_MONGOS_IS_MISSING

CLUSTER_MONGOS_IS_PRESENT

SHARD_ADDED

SHARD_REMOVED

Data Explorer Accessed

DATA_EXPLORER

DATA_EXPLORER_CRUD

Host

ADD_HOST_AUDIT

ADD_HOST_TO_REPLICA_SET_AUDIT

DELETE_HOST_AUDIT

HOST_DOWN

HOST_RECOVERING

HOST_RESTARTED

HOST_ROLLBACK

HOST_SSL_CERTIFICATE_STALE

OUTSIDE_METRIC_THRESHOLD

REMOVE_HOST_FROM_REPLICA_SET_AUDIT

UNDELETE_HOST_AUDIT

VERSION_BEHIND

Organization

ALL_ORG_USERS_HAVE_MFA

ORG_API_KEY_ADDED

ORG_API_KEY_DELETED

ORG_EMPLOYEE_ACCESS_RESTRICTED

ORG_EMPLOYEE_ACCESS_UNRESTRICTED

ORG_PUBLIC_API_ACCESS_LIST_NOT_REQUIRED

ORG_PUBLIC_API_ACCESS_LIST_REQUIRED

ORG_RENAMED

ORG_TWO_FACTOR_AUTH_OPTIONAL

ORG_TWO_FACTOR_AUTH_REQUIRED

ORG_USERS_WITHOUT_MFA

Project

ALL_USERS_HAVE_MULTI_FACTOR_AUTH

USERS_WITHOUT_MULTI_FACTOR_AUTH

Replica Set

CONFIGURATION_CHANGED

ENOUGH_HEALTHY_MEMBERS

MEMBER_ADDED

MEMBER_REMOVED

MULTIPLE_PRIMARIES

NO_PRIMARY

ONE_PRIMARY

PRIMARY_ELECTED

TOO_FEW_HEALTHY_MEMBERS

TOO_MANY_ELECTIONS

TOO_MANY_UNHEALTHY_MEMBERS

Team

TEAM_ADDED_TO_GROUP

TEAM_CREATED

TEAM_DELETED

TEAM_NAME_CHANGED

TEAM_REMOVED_FROM_GROUP

TEAM_ROLES_MODIFIED

TEAM_UPDATED

USER_ADDED_TO_TEAM

User

INVITED_TO_GROUP

INVITED_TO_ORG

JOIN_GROUP_REQUEST_APPROVED_AUDIT

JOIN_GROUP_REQUEST_DENIED_AUDIT

JOINED_GROUP

JOINED_ORG

JOINED_TEAM

REMOVED_FROM_GROUP

REMOVED_FROM_ORG

REMOVED_FROM_TEAM

REQUESTED_TO_JOIN_GROUP

USER_ROLES_CHANGED_AUDIT

To review the full list of events that generate alerts and their descriptions, see Alert Types. For a complete list of events included in the Ops Manager audit log, see Audit Events.
        """

        class MatchersParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            field_name: Optional[MatcherFieldName] = Field(None, serialization_alias="fieldName")
            """Name of the field in the target object to match on.

Host alerts support these fields:

HOSTNAME

PORT

HOSTNAME_AND_PORT

REPLICA_SET_NAME

TYPE_NAME

Replica set alerts support these fields:

REPLICA_SET_NAME

SHARD_NAME

CLUSTER_NAME

Sharded cluster alerts support these fields:

CLUSTER_NAME

SHARD_NAME

All other types of alerts do not support matchers.
            """

            operator: Optional[MatcherOperator] = Field(None, serialization_alias="operator")
            """Operator to test the field's value. Accepted values are:

EQUALS

NOT_EQUALS

CONTAINS

NOT_CONTAINS

STARTS_WITH

ENDS_WITH

REGEX
            """

            value: Optional[MatcherValue] = Field(None, serialization_alias="value")
            """Value to test with the specified operator.

If matchers.fieldName is set to TYPE_NAME, you can match on the following values:

PRIMARY

SECONDARY

STANDALONE

CONFIG

MONGOS
            """

        matchers: Optional[list[MatchersParams]] = Field(None, serialization_alias="matchers")
        """Rules to apply when matching an object against this alert configuration. Only entities that match all these rules are checked for an alert condition.

You can filter using the matchers array only when the eventTypeName specifies an event for a host, replica set, or sharded cluster.
        """

        class MetricThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            metric_name: Optional[str] = Field(None, serialization_alias="metricName")
            """Name of the metric to check. Supports the same values as the metricName field of the alerts resource.
            """

            mode: Optional[str] = Field(None, serialization_alias="mode")
            """Set to AVERAGE to compute the average of this metric.
            """

            operator: Optional[ThresholdOperator] = Field(None, serialization_alias="operator")
            """Operator to apply when checking the current metric value against the threshold value. Accepted values are:

GREATER_THAN

LESS_THAN
            """

            threshold: Optional[int] = Field(None, serialization_alias="threshold")
            """Threshold value outside of which an alert is triggered.
            """

            units: Optional[Unit] = Field(None, serialization_alias="units")
            """Units for the threshold value. Depends on the type of metric.

For example, a metric that measures memory consumption would have a byte measurement, while a metric that measures time would have a time unit.

Accepted values are:

RAW

BITS

BYTES

KILOBITS

KILOBYTES

MEGABITS

MEGABYTES

GIGABITS

GIGABYTES

TERABYTES

PETABYTES

MILLISECONDS

SECONDS

MINUTES

HOURS

DAYS
            """

        metric_threshold: MetricThresholdParams = Field(serialization_alias="metricThreshold")
        """Threshold that will cause an alert to be triggered. Required if "eventTypeName" : "OUTSIDE_METRIC_THRESHOLD".
        """

        class NotificationsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            api_token: str = Field(serialization_alias="apiToken")
            """Slack API token or Bot token. Required if "notifications.typeName" : "SLACK". If the token later becomes invalid, Ops Manager sends an email to the Project owner and eventually removes the token.

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

View or edit the alert through the UI.

Query the third-party integration settings through the API.
            """

            channel_name: str = Field(serialization_alias="channelName")
            """Slack channel name. Required if "notifications.typeName" : "SLACK".
            """

            datadog_api_key: str = Field(serialization_alias="datadogApiKey")
            """DataDog API Key. Found in the DataDog dashboard. Required if "notifications.typeName" : "DATADOG".

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

View or edit the alert through the UI.

Query the third-party integration settings through the API.
            """

            delay_min: Optional[int] = Field(None, serialization_alias="delayMin")
            """Number of minutes to wait after an alert condition is detected before sending out the first notification.
            """

            email_address: str = Field(serialization_alias="emailAddress")
            """Email address to which to send notification. Required if "notifications.typeName" : "EMAIL".
            """

            email_enabled: bool = Field(serialization_alias="emailEnabled")
            """Determines if email notifications should be sent. Required if:

"notifications.typeName" : "GROUP"

"notifications.typeName" : "USER"
            """

            interval_min: Optional[int] = Field(None, serialization_alias="intervalMin")
            """Number of minutes to wait between successive notifications for unacknowledged alerts that are not resolved.
            """

            microsoft_teams_webhook_url: str = Field(serialization_alias="microsoftTeamsWebhookUrl")
            """Microsoft Teams channel incoming webhook URL. Required if "notifications.typeName" : "MICROSOFT_TEAMS".

When you view or edit the alert for a webhook notification, the URL appears partially redacted, and the secret appears completely redacted.
            """

            mobile_number: str = Field(serialization_alias="mobileNumber")
            """Mobile number to send SMS messages to. Required if "notifications.typeName" : "SMS".
            """

            notification_token: str = Field(serialization_alias="notificationToken")
            """A HipChat API token. Required if "notifications.typeName" : "HIP_CHAT". If the token later becomes invalid, Ops Manager sends an email to the Project owner and eventually removes the token.

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

View or edit the alert through the UI.

Query the third-party integration settings through the API.
            """

            role: str = Field(serialization_alias="role")
            """Ops Manager role in current Project. Required if "notifications.typeName" : "GROUP".
            """

            room_name: str = Field(serialization_alias="roomName")
            """HipChat room name. Required if "notifications.typeName" : "HIP_CHAT".
            """

            service_key: str = Field(serialization_alias="serviceKey")
            """PagerDuty integration key. Required if "notifications.typeName" : "PAGER_DUTY".

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

View or edit the alert through the UI.

Query the third-party integration settings through the API.
            """

            sms_enabled: bool = Field(serialization_alias="smsEnabled")
            """Flag indicating SMS notifications must be sent. Required if:

"notifications.typeName" : "GROUP"

"notifications.typeName" : "USER"
            """

            team_id: Optional[str] = Field(None, serialization_alias="teamId")
            """Unique identifier of a team.
            """

            type_name: Optional[NotificationsTypeName] = Field(None, serialization_alias="typeName")
            """Type of alert notification. Accepted values are:

DATADOG

EMAIL

GROUP (Project)

HIPCHAT

ORG

PAGER_DUTY

SLACK

SMS (Twilio integration must be configured)

USER

WEBHOOK
            """

            username: str = Field(serialization_alias="username")
            """Name of an Ops Manager user to which to send notifications. Specify a user in the Project that owns the alert configuration. Required if "notifications.typeName" : "USER".
            """

            webhook_body_template: Optional[str] = Field(
                None, serialization_alias="webhookBodyTemplate"
            )
            """Template for the body content of webhook notifications. You can use variables in the template that are replaced with alert-specific values when the notification is sent.
            """

            webhook_headers_template: Optional[str] = Field(
                None, serialization_alias="webhookHeadersTemplate"
            )
            """Template for custom headers to include in webhook notifications. You can use variables in the template that are replaced with alert-specific values when the notification is sent.
            """

            webhook_secret: Optional[str] = Field(None, serialization_alias="webhookSecret")
            """A value used to authenticate with the Webhook that accepts and forwards the notification. You can explicitly declare a secret only in a request that has both:

A notifications.typeName of WEBHOOK

An explicitly declared notifications.webhookURL

You can configure a webhookSecret for a default webhookURL only either on the Integrations page, or with the Integrations API.

To explicitly declare a webhookURL without a webhookSecret, omit this field.

After creating a webhook notification, the URL is partially redacted when you view or edit the alert, and the secret is completely redacted.
            """

            webhook_url: Optional[str] = Field(None, serialization_alias="webhookUrl")
            """URL for the webhook that triggers this notification. If you do not explicitly declare a webhookUrl, your request will use the default webhookUrl set either on the Integrations page, or with the Integrations API.

After creating a webhook notification, the URL is partially redacted when you view or edit the alert, and the secret is completely redacted.
            """

        notifications: list[NotificationsParams] = Field(serialization_alias="notifications")
        """Notifications to send when an alert condition is detected.
        """

        class ThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            operator: Optional[ThresholdOperator] = Field(None, serialization_alias="operator")
            """Operator to apply when checking the current metric value against the threshold value.

GREATER_THAN

LESS_THAN
            """

            threshold: Optional[int] = Field(None, serialization_alias="threshold")
            """Threshold value outside of which an alert is triggered.
            """

        threshold: ThresholdParams = Field(serialization_alias="threshold")
        """Threshold that will cause an alert to be triggered. Required if:

"eventTypeName" : "TOO_FEW_HEALTHY_MEMBERS"

"eventTypeName" : TOO_MANY_UNHEALTHY_MEMBERS
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update an Alert Configuration
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-update-config/)
        ### Endpoint:
        `PUT /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}`
        ### Description
        No description.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
