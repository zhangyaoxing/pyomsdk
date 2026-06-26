r"""Auto-generated client for GlobalAlertConfigurationsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class GlobalAlertConfigurationsResource(BaseResource):
    r"""Client for GlobalAlertConfigurationsResource resource."""

    class GetAllOpenAlertsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        global_alert_config_id: str = Field(serialization_alias="GLOBAL-ALERT-CONFIG-ID")
        r"""Unique identifier of the global alert configuration for which you
want to retrieve open alerts.
        """

    class GetAllOpenAlertsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `envelope : true` in the
query.

For endpoints that return a list of results, the `content`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag that indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_all_open_alerts(
        self,
        path_params: GetAllOpenAlertsPathParams,
        query_params: Optional[GetAllOpenAlertsQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get All Open Alerts Triggered by One Global Alert Configuration
        ### Document:
        [Get All Open Alerts](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configuration-get-all-open-alerts-triggered/)
        ### Endpoint:
        `GET /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}/alerts`
        ### Description
        Retrieve all open alerts triggered by a global alert configuration
        identified by its `GLOBAL-ALERT-CONFIG-ID`.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}/alerts",
            path_params,
            query_params,
            None,
        )

    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        enabled: Optional[bool] = Field(default=None, serialization_alias="enabled")
        r"""Toggle that specifies whether the alert configuration is enabled.
        """

        event_type_name: EventTypeName = Field(serialization_alias="eventTypeName")
        r"""Type of event for which this alert configuration triggers
an alert.

To review the types of events that generate alerts, see
[Alert Types.](/docs/ops-manager/current/reference/alert-types/)

For a complete list of events included in the Ops Manager audit log, see
[Audit Events.](/docs/ops-manager/current/reference/audit-events/)
        """

        for_all_groups: bool = Field(serialization_alias="forAllGroups")
        r"""Toggle that specifies whether the global alert configuration
applies to all groups. Also affects whether you can use the
`tags` array to target the configuration to specific groups.

If `true`, the configuration applies to all groups. You can
target the alert configuration to specific groups through the
`tags` array.

If `false`, the configuration applies only to the groups
specified in the `groupIds` array. You must specify at
least one project in the `groupIds` array. You can't use the
`tags` array for this alert configuration.
        """

        group_ids: Optional[list[str]] = Field(default=None, serialization_alias="groupIds")
        r"""IDs of the groups to which this alert configuration applies.
This field applies only if `forAllGroups` is set to `false`.
        """

        class MatchersParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            field_name: Optional[MatcherFieldName] = Field(
                default=None, serialization_alias="fieldName"
            )
            r"""Name of the field in the target object on which to match.

- Host alerts support these fields:

  - `HOSTNAME`
  - `PORT`
  - `HOSTNAME_AND_PORT`
  - `REPLICA_SET_NAME`
  - `TYPE_NAME`
- Replica set alerts support these fields:

  - `REPLICA_SET_NAME`
  - `SHARD_NAME`
  - `CLUSTER_NAME`
- Sharded cluster alerts support these fields:

  - `CLUSTER_NAME`
  - `SHARD_NAME`

All other types of alerts do not support matchers.
            """

            operator: Optional[MatcherOperator] = Field(
                default=None, serialization_alias="operator"
            )
            r"""Operator to test the field's value. Accepted values are:

- `EQUALS`
- `NOT_EQUALS`
- `CONTAINS`
- `NOT_CONTAINS`
- `STARTS_WITH`
- `ENDS_WITH`
- `REGEX`
            """

            value: Optional[MatcherValue] = Field(default=None, serialization_alias="value")
            r"""Value to test with the specified operator.

If `matchers.fieldName` is set to `TYPE_NAME`, you can match on
the following values:

- `PRIMARY`
- `SECONDARY`
- `STANDALONE`
- `CONFIG`
- `MONGOS`
            """

        matchers: Optional[list[MatchersParams]] = Field(
            default=None, serialization_alias="matchers"
        )
        r"""Rules to apply when matching an object against this global alert
configuration. Ops Manager only checks entities that match *all* these
rules for an alert condition.

You can filter using the `matchers` array only when the
`eventTypeName` specifies an event for a host, replica set, or
sharded cluster.
        """

        class MetricThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            metric_name: Optional[str] = Field(default=None, serialization_alias="metricName")
            r"""Name of the metric to check. Supports the same values as the
`metricName` field of the `globalAlerts` resource. For a list
of possible values, see
[Measurement Types for Global Alerts.](/docs/ops-manager/current/reference/api/global-alerts/#std-label-measurement-types-for-global-alerts-api)
            """

            mode: Optional[str] = Field(default=None, serialization_alias="mode")
            r"""This is set to `AVERAGE` and computes the current metric value
as an average.
            """

            operator: Optional[ThresholdOperator] = Field(
                default=None, serialization_alias="operator"
            )
            r"""Operator to apply when checking the current metric value
against `metricThreshold.threshold`. Possible values are:

- `GREATER_THAN`
- `LESS_THAN`
            """

            threshold: Optional[int] = Field(default=None, serialization_alias="threshold")
            r"""Threshold value outside of which this alert configuration
triggers an alert.
            """

            units: Optional[Unit] = Field(default=None, serialization_alias="units")
            r"""Units for `metricThreshold.threshold`. The units depend on
the type of metric.

Accepted values are:

- `RAW`
- `BITS`
- `BYTES`
- `KILOBITS`
- `KILOBYTES`
- `MEGABITS`
- `MEGABYTES`
- `GIGABITS`
- `GIGABYTES`
- `TERABYTES`
- `PETABYTES`
- `MILLISECONDS`
- `SECONDS`
- `MINUTES`
- `HOURS`
- `DAYS`

For example, a metric that measures memory consumption can use `BYTES`,
while a metric that measures time can use `HOURS`.
            """

        metric_threshold: Optional[MetricThresholdParams] = Field(
            default=None, serialization_alias="metricThreshold"
        )
        r"""Threshold that causes this alert configuration to trigger
an alert. Only required if `eventTypeName` is set to
`OUTSIDE_METRIC_THRESHOLD`.
        """

        class NotificationsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            api_token: Optional[str] = Field(default=None, serialization_alias="apiToken")
            r"""Slack API token or Bot token. Only accepted for `SLACK`
notifications. If the token later becomes invalid, Ops Manager sends an
email to the project owner and removes the token.
            """

            channel_name: Optional[str] = Field(default=None, serialization_alias="channelName")
            r"""Slack channel name. Only accepted for `SLACK` notifications.
            """

            delay_min: Optional[int] = Field(default=None, serialization_alias="delayMin")
            r"""Number of minutes to wait after an alert condition is
detected before Ops Manager sends out the first notification.
            """

            email_address: Optional[Any] = Field(default=None, serialization_alias="emailAddress")
            r"""Email address to which to send notification. Only accepted for
`EMAIL` notifications.
            """

            email_enabled: Optional[bool] = Field(default=None, serialization_alias="emailEnabled")
            r"""Toggle specifying whether Ops Manager sends email notifications.
Only accepted for `GROUP` and `USER` notifications.
            """

            interval_min: Optional[int] = Field(default=None, serialization_alias="intervalMin")
            r"""Number of minutes to wait between successive notifications
for unacknowledged, unresolved alerts that this alert
configuration triggers.
            """

            microsoft_teams_webhook_url: Optional[str] = Field(
                default=None, serialization_alias="microsoftTeamsWebhookUrl"
            )
            r"""Microsoft Teams channel incoming webhook URL. Only accepted
for `MICROSOFT_TEAMS` notifications.
            """

            notification_token: Optional[str] = Field(
                default=None, serialization_alias="notificationToken"
            )
            r"""HipChat API token. Only accepted for `HIP_CHAT` notifications.
If the token later becomes invalid, Ops Manager sends an email to the
project owner and removes the token.
            """

            room_name: Optional[str] = Field(default=None, serialization_alias="roomName")
            r"""HipChat room name. Only accepted for `HIP_CHAT` notifications.
            """

            service_key: Optional[str] = Field(default=None, serialization_alias="serviceKey")
            r"""PagerDuty integration key. Only accepted for `PAGER_DUTY`
notifications. If the key later becomes invalid, Ops Manager sends an
email to the project owner and removes the key.

All new PagerDuty keys use their [Events API v2](https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgw-events-api-v2-overview).
If you have an Events API v1 key, you can continue to use that key
with Ops Manager.
            """

            sms_enabled: Optional[bool] = Field(default=None, serialization_alias="smsEnabled")
            r"""Toggle specifying whether Ops Manager sends SMS notifications. Only
accepted for `GROUP` and `USER` notifications.
            """

            type_name: NotificationsTypeName = Field(serialization_alias="typeName")
            r"""Type of alert notification this alert configuration triggers.
Accepted values are:

- `ADMIN`
- `GROUP`
- `USER`
- `EMAIL`
- `SMS` (Available only if Ops Manager is configured for [Twilio integration](/docs/ops-manager/current/reference/config/ui-settings/#std-label-twilio-sms-alert-settings).)
- `HIPCHAT`
- `SLACK`
- `PAGER_DUTY`
            """

            username: Optional[str] = Field(default=None, serialization_alias="username")
            r"""Name of the Ops Manager user to whom to send notifications. Only
present for `USER` notifications.
            """

            webhook_body_template: Optional[str] = Field(
                default=None, serialization_alias="webhookBodyTemplate"
            )
            r"""Template for the body content of webhook notifications.
You can use variables in the template that are replaced with
alert-specific values when the notification is sent.
            """

            webhook_headers_template: Optional[str] = Field(
                default=None, serialization_alias="webhookHeadersTemplate"
            )
            r"""Template for custom headers to include in webhook notifications.
You can use variables in the template that are replaced with
alert-specific values when the notification is sent.
            """

            webhook_secret: Optional[str] = Field(default=None, serialization_alias="webhookSecret")
            r"""A value used to authenticate with the Webhook that accepts and
forwards the notification. You can explicitly declare a secret
only in a request that has both:

- A `notifications.typeName` of `WEBHOOK`
- An explicitly declared `notifications.webhookURL`

You can configure a `webhookSecret` for a default
`webhookURL` only with the
[Admin Console.](/docs/ops-manager/current/tutorial/manage-global-alerts/#std-label-mms-manage-global-alerts)

To explicitly declare a `webhookURL` without a
`webhookSecret`, omit this field.
            """

            webhook_url: Optional[str] = Field(default=None, serialization_alias="webhookUrl")
            r"""URL for the webhook that triggers this notification. If you do
not explicitly declare a `webhookUrl`, your request will use
the default `webhookUrl` set in the
[Admin Console.](/docs/ops-manager/current/tutorial/manage-global-alerts/#std-label-mms-manage-global-alerts)
            """

        notifications: list[NotificationsParams] = Field(serialization_alias="notifications")
        r"""Notifications Ops Manager sends when it detects an alert that this
alert configuration describes.
        """

        tags: Optional[list[str]] = Field(default=None, serialization_alias="tags")
        r"""Tags associated with this alert configuration.
        """

        class ThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            operator: Optional[ThresholdOperator] = Field(
                default=None, serialization_alias="operator"
            )
            r"""Operator to apply when checking the current metric value against
`threshold.threshold`. Accepted values are:

- `GREATER_THAN`
- `LESS_THAN`
            """

            threshold: Optional[int] = Field(default=None, serialization_alias="threshold")
            r"""Threshold value outside of which this alert configuration
triggers an alert.
            """

        threshold: Optional[ThresholdParams] = Field(default=None, serialization_alias="threshold")
        r"""Threshold that causes this alert configuration to trigger
an alert. Only required if `eventTypeName` is set to one of the
following values:

- `TOO_FEW_HEALTHY_MEMBERS`
- `TOO_MANY_UNHEALTHY_MEMBERS`
        """

        type_name: Optional[str] = Field(default=None, serialization_alias="typeName")
        r"""*This field is deprecated and will be ignored.*
        """

    def create(
        self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        r"""
        ## Create One Global Alert Configuration
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-create-one/)
        ### Endpoint:
        `POST /globalAlertConfigs`
        ### Description
        Create one global alert configuration.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/globalAlertConfigs",
            None,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        global_alert_config_id: str = Field(serialization_alias="GLOBAL-ALERT-CONFIG-ID")
        r"""Unique identifier of the global alert configuration you want to
delete.
        """

    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def delete(
        self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Delete One Global Alert Configuration
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-delete-one/)
        ### Endpoint:
        `DELETE /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}`
        ### Description
        Delete one global alert configuration.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `envelope : true` in the
query.

For endpoints that return a list of results, the `content`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag that indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_all(
        self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get All Global Alert Configurations
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-get-all/)
        ### Endpoint:
        `GET /globalAlertConfigs`
        ### Description
        Retrieve all global alert configurations.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/globalAlertConfigs",
            None,
            query_params,
            None,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        global_alert_config_id: str = Field(serialization_alias="GLOBAL-ALERT-CONFIG-ID")
        r"""Unique identifier of the global alert configuration you want to
retrieve.
        """

    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_one(
        self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get One Global Alert Configuration
        ### Document:
        [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-get-one/)
        ### Endpoint:
        `GET /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}`
        ### Description
        Retrieve one global alert configuration by its
        `GLOBAL-ALERT-CONFIG-ID`.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )

    class TestGlobalAlertConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alert_config_id: str = Field(serialization_alias="ALERT-CONFIG-ID")
        r"""Unique 24-hexadecimal digit string that identifies the global alert configuration.
        """

        notification_id: str = Field(serialization_alias="NOTIFICATION-ID")
        r"""Unique 24-hexadecimal digit string that identifies the notification method within the global alert configuration.
        """

    def test_global_alert_configuration(
        self,
        path_params: TestGlobalAlertConfigurationPathParams,
    ) -> dict[str, Any]:
        r"""
        ## Test Global Alert Configuration
        ### Document:
        [Test Global Alert Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-test-one/)
        ### Endpoint:
        `POST /globalAlertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test`
        ### Description
        Triggers a test notification for a specific notification method in a global alert configuration. This endpoint sends a test payload with dummy data and rendered templates to validate your webhook configuration.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/globalAlertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test",
            path_params,
            None,
            None,
        )

    class EnableOrDisablePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        global_alert_config_id: str = Field(serialization_alias="GLOBAL-ALERT-CONFIG-ID")
        r"""Unique identifier of the global alert configuration you want to
enable or disable.
        """

    class EnableOrDisableQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    class EnableOrDisableBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        enabled: bool = Field(serialization_alias="enabled")
        r"""Toggle indicating whether the global alert configuration is
enabled or disabled:

- Set to `true` to enable a global alert configuration.
- Set to `false` to disable a global alert configuration.
        """

    def enable_or_disable(
        self,
        path_params: EnableOrDisablePathParams,
        query_params: Optional[EnableOrDisableQueryParams],
        body_params: EnableOrDisableBodyParams,
    ) -> dict[str, Any]:
        r"""
        ## Enable or Disable One Global Alert Configuration
        ### Document:
        [Enable or Disable](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-toggle-one/)
        ### Endpoint:
        `PATCH /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}`
        ### Description
        Enable or disable one global alert configuration identified by its
        `GLOBAL-ALERT-CONFIG-ID`.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        global_alert_config_id: str = Field(serialization_alias="GLOBAL-ALERT-CONFIG-ID")
        r"""Unique identifier of the global alert configuration you want to
update.
        """

    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        enabled: Optional[bool] = Field(default=None, serialization_alias="enabled")
        r"""Toggle that specifies whether the alert configuration is enabled.
        """

        event_type_name: EventTypeName = Field(serialization_alias="eventTypeName")
        r"""Type of event for which this alert configuration triggers
an alert.

To review the types of events that generate alerts, see
[Alert Types.](/docs/ops-manager/current/reference/alert-types/)

For a complete list of events included in the Ops Manager audit log, see
[Audit Events.](/docs/ops-manager/current/reference/audit-events/)
        """

        for_all_groups: bool = Field(serialization_alias="forAllGroups")
        r"""Toggle that specifies whether the global alert configuration
applies to all groups. Also affects whether you can use the
`tags` array to target the configuration to specific groups.

If `true`, the configuration applies to all groups. You can
target the alert configuration to specific groups through the
`tags` array.

If `false`, the configuration applies only to the groups
specified in the `groupIds` array. You must specify at
least one project in the `groupIds` array. You can't use the
`tags` array for this alert configuration.
        """

        group_ids: Optional[list[str]] = Field(default=None, serialization_alias="groupIds")
        r"""IDs of the groups to which this alert configuration applies.
This field applies only if `forAllGroups` is set to `false`.
        """

        class MatchersParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            field_name: Optional[MatcherFieldName] = Field(
                default=None, serialization_alias="fieldName"
            )
            r"""Name of the field in the target object on which to match.

- Host alerts support these fields:

  - `HOSTNAME`
  - `PORT`
  - `HOSTNAME_AND_PORT`
  - `REPLICA_SET_NAME`
  - `TYPE_NAME`
- Replica set alerts support these fields:

  - `REPLICA_SET_NAME`
  - `SHARD_NAME`
  - `CLUSTER_NAME`
- Sharded cluster alerts support these fields:

  - `CLUSTER_NAME`
  - `SHARD_NAME`

All other types of alerts do not support matchers.
            """

            operator: Optional[MatcherOperator] = Field(
                default=None, serialization_alias="operator"
            )
            r"""Operator to test the field's value. Accepted values are:

- `EQUALS`
- `NOT_EQUALS`
- `CONTAINS`
- `NOT_CONTAINS`
- `STARTS_WITH`
- `ENDS_WITH`
- `REGEX`
            """

            value: Optional[MatcherValue] = Field(default=None, serialization_alias="value")
            r"""Value to test with the specified operator.

If `matchers.fieldName` is set to `TYPE_NAME`, you can match on
the following values:

- `PRIMARY`
- `SECONDARY`
- `STANDALONE`
- `CONFIG`
- `MONGOS`
            """

        matchers: Optional[list[MatchersParams]] = Field(
            default=None, serialization_alias="matchers"
        )
        r"""Rules to apply when matching an object against this global alert
configuration. Ops Manager only checks entities that match *all* these
rules for an alert condition.

You can filter using the `matchers` array only when the
`eventTypeName` specifies an event for a host, replica set, or
sharded cluster.
        """

        class MetricThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            metric_name: Optional[str] = Field(default=None, serialization_alias="metricName")
            r"""Name of the metric to check. Supports the same values as the
`metricName` field of the `globalAlerts` resource. For a list
of possible values, see
[Measurement Types for Global Alerts.](/docs/ops-manager/current/reference/api/global-alerts/#std-label-measurement-types-for-global-alerts-api)
            """

            mode: Optional[str] = Field(default=None, serialization_alias="mode")
            r"""This is set to `AVERAGE` and computes the current metric value
as an average.
            """

            operator: Optional[ThresholdOperator] = Field(
                default=None, serialization_alias="operator"
            )
            r"""Operator to apply when checking the current metric value
against `metricThreshold.threshold`. Possible values are:

- `GREATER_THAN`
- `LESS_THAN`
            """

            threshold: Optional[int] = Field(default=None, serialization_alias="threshold")
            r"""Threshold value outside of which this alert configuration
triggers an alert.
            """

            units: Optional[Unit] = Field(default=None, serialization_alias="units")
            r"""Units for `metricThreshold.threshold`. The units depend on
the type of metric.

Accepted values are:

- `RAW`
- `BITS`
- `BYTES`
- `KILOBITS`
- `KILOBYTES`
- `MEGABITS`
- `MEGABYTES`
- `GIGABITS`
- `GIGABYTES`
- `TERABYTES`
- `PETABYTES`
- `MILLISECONDS`
- `SECONDS`
- `MINUTES`
- `HOURS`
- `DAYS`

For example, a metric that measures memory consumption can use `BYTES`,
while a metric that measures time can use `HOURS`.
            """

        metric_threshold: Optional[MetricThresholdParams] = Field(
            default=None, serialization_alias="metricThreshold"
        )
        r"""Threshold that causes this alert configuration to trigger
an alert. Only required if `eventTypeName` is set to
`OUTSIDE_METRIC_THRESHOLD`.
        """

        class NotificationsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            api_token: Optional[str] = Field(default=None, serialization_alias="apiToken")
            r"""Slack API token or Bot token. Only accepted for `SLACK`
notifications. If the token later becomes invalid, Ops Manager sends an
email to the project owner and removes the token.
            """

            channel_name: Optional[str] = Field(default=None, serialization_alias="channelName")
            r"""Slack channel name. Only accepted for `SLACK` notifications.
            """

            delay_min: Optional[int] = Field(default=None, serialization_alias="delayMin")
            r"""Number of minutes to wait after an alert condition is
detected before Ops Manager sends out the first notification.
            """

            email_address: Optional[Any] = Field(default=None, serialization_alias="emailAddress")
            r"""Email address to which to send notification. Only accepted for
`EMAIL` notifications.
            """

            email_enabled: Optional[bool] = Field(default=None, serialization_alias="emailEnabled")
            r"""Toggle specifying whether Ops Manager sends email notifications.
Only accepted for `GROUP` and `USER` notifications.
            """

            interval_min: Optional[int] = Field(default=None, serialization_alias="intervalMin")
            r"""Number of minutes to wait between successive notifications
for unacknowledged, unresolved alerts that this alert
configuration triggers.
            """

            microsoft_teams_webhook_url: Optional[str] = Field(
                default=None, serialization_alias="microsoftTeamsWebhookUrl"
            )
            r"""Microsoft Teams channel incoming webhook URL. Only accepted
for `MICROSOFT_TEAMS` notifications.
            """

            notification_token: Optional[str] = Field(
                default=None, serialization_alias="notificationToken"
            )
            r"""HipChat API token. Only accepted for `HIP_CHAT` notifications.
If the token later becomes invalid, Ops Manager sends an email to the
project owner and removes the token.
            """

            room_name: Optional[str] = Field(default=None, serialization_alias="roomName")
            r"""HipChat room name. Only accepted for `HIP_CHAT` notifications.
            """

            service_key: Optional[str] = Field(default=None, serialization_alias="serviceKey")
            r"""PagerDuty integration key. Only accepted for `PAGER_DUTY`
notifications. If the key later becomes invalid, Ops Manager sends an
email to the project owner and removes the key.

All new PagerDuty keys use their [Events API v2](https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgw-events-api-v2-overview).
If you have an Events API v1 key, you can continue to use that key
with Ops Manager.
            """

            sms_enabled: Optional[bool] = Field(default=None, serialization_alias="smsEnabled")
            r"""Toggle specifying whether Ops Manager sends SMS notifications. Only
accepted for `GROUP` and `USER` notifications.
            """

            type_name: NotificationsTypeName = Field(serialization_alias="typeName")
            r"""Type of alert notification this alert configuration triggers.
Accepted values are:

- `ADMIN`
- `GROUP`
- `USER`
- `EMAIL`
- `SMS` (Available only if Ops Manager is configured for [Twilio integration](/docs/ops-manager/current/reference/config/ui-settings/#std-label-twilio-sms-alert-settings).)
- `HIPCHAT`
- `SLACK`
- `PAGER_DUTY`
            """

            username: Optional[str] = Field(default=None, serialization_alias="username")
            r"""Name of the Ops Manager user to whom to send notifications. Only
present for `USER` notifications.
            """

            webhook_body_template: Optional[str] = Field(
                default=None, serialization_alias="webhookBodyTemplate"
            )
            r"""Template for the body content of webhook notifications.
You can use variables in the template that are replaced with
alert-specific values when the notification is sent.
            """

            webhook_headers_template: Optional[str] = Field(
                default=None, serialization_alias="webhookHeadersTemplate"
            )
            r"""Template for custom headers to include in webhook notifications.
You can use variables in the template that are replaced with
alert-specific values when the notification is sent.
            """

            webhook_secret: Optional[str] = Field(default=None, serialization_alias="webhookSecret")
            r"""A value used to authenticate with the Webhook that accepts and
forwards the notification. You can explicitly declare a secret
only in a request that has both:

- A `notifications.typeName` of `WEBHOOK`
- An explicitly declared `notifications.webhookURL`

You can configure a `webhookSecret` for a default
`webhookURL` only with the
[Admin Console.](/docs/ops-manager/current/tutorial/manage-global-alerts/#std-label-mms-manage-global-alerts)

To explicitly declare a `webhookURL` without a
`webhookSecret`, omit this field.
            """

            webhook_url: Optional[str] = Field(default=None, serialization_alias="webhookUrl")
            r"""URL for the webhook that triggers this notification. If you do
not explicitly declare a `webhookUrl`, your request will use
the default `webhookUrl` set in the
[Admin Console.](/docs/ops-manager/current/tutorial/manage-global-alerts/#std-label-mms-manage-global-alerts)
            """

        notifications: list[NotificationsParams] = Field(serialization_alias="notifications")
        r"""Notifications Ops Manager sends when it detects an alert that this
alert configuration describes.
        """

        tags: Optional[list[str]] = Field(default=None, serialization_alias="tags")
        r"""Tags associated with this alert configuration.
        """

        class ThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            operator: Optional[ThresholdOperator] = Field(
                default=None, serialization_alias="operator"
            )
            r"""Operator to apply when checking the current metric value against
`threshold.threshold`. Accepted values are:

- `GREATER_THAN`
- `LESS_THAN`
            """

            threshold: Optional[int] = Field(default=None, serialization_alias="threshold")
            r"""Threshold value outside of which this alert configuration
triggers an alert.
            """

        threshold: Optional[ThresholdParams] = Field(default=None, serialization_alias="threshold")
        r"""Threshold that causes this alert configuration to trigger
an alert. Only required if `eventTypeName` is set to one of the
following values:

- `TOO_FEW_HEALTHY_MEMBERS`
- `TOO_MANY_UNHEALTHY_MEMBERS`
        """

        type_name: Optional[str] = Field(default=None, serialization_alias="typeName")
        r"""*This field is deprecated and will be ignored.*
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        r"""
        ## Update One Global Alert Configuration
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-update-one/)
        ### Endpoint:
        `PUT /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}`
        ### Description
        Update one global alert configuration identified by its
        `GLOBAL-ALERT-CONFIG-ID`.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
