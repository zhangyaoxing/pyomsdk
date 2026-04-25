from typing import Literal, Optional
from pydantic import Field
from .enums import IntegrationType, PrometheusScheme, PrometheusServiceDiscoveryType
from .integration_settings_resource import IntegrationSettingsResource

BodyParamsA = IntegrationSettingsResource.CreateBodyParams
BodyParamsB = IntegrationSettingsResource.UpdateBodyParams


class PagerDutyIntegrationSettings(BodyParamsA, BodyParamsB):
    """Client for PagerDuty integration settings resource."""

    type: Literal[IntegrationType.PAGER_DUTY] = Field(
        IntegrationType.PAGER_DUTY, serialization_alias="type"
    )
    service_key: str = Field(None, serialization_alias="serviceKey")
    """Your Integration Key.

**IMPORTANT**: Changing the Integration Key doesn't change any alerts that use this integration. Those alerts still use the previous Integration Key. Remove and re-add each PagerDuty notification to use the new key.

All new PagerDuty keys use their Events API v2. If you have an Events API v1 key, you can continue to use that key with Ops Manager.

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

- View or edit the alert through the UI.
- Query the third-party integration settings through the API."""


class SlackIntegrationSettings(BodyParamsA, BodyParamsB):
    """Client for Slack integration settings resource."""

    type: Literal[IntegrationType.SLACK] = Field(IntegrationType.SLACK, serialization_alias="type")
    api_token: str = Field(None, serialization_alias="apiToken")
    """Your API Token.

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

- View or edit the alert through the UI.
- Query the third-party integration settings through the API."""
    team_name: str = Field(None, serialization_alias="teamName")
    """Your team name."""
    channel_name: Optional[str] = Field(None, serialization_alias="channelName")
    """Your channel name."""


class DatadogIntegrationSettings(BodyParamsA, BodyParamsB):
    """Client for Datadog integration settings resource."""

    type: Literal[IntegrationType.DATADOG] = Field(
        IntegrationType.DATADOG, serialization_alias="type"
    )
    api_key: str = Field(None, serialization_alias="apiKey")
    """Your API Key.

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

- View or edit the alert through the UI.
- Query the third-party integration settings through the API."""


class HipChatIntegrationSettings(BodyParamsA, BodyParamsB):
    """Client for HipChat integration settings resource."""

    type: Literal[IntegrationType.HIP_CHAT] = Field(
        IntegrationType.HIP_CHAT, serialization_alias="type"
    )
    notification_token: str = Field(None, serialization_alias="notificationToken")
    """Notification token for your HipChat user account.

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

- View or edit the alert through the UI.
- Query the third-party integration settings through the API."""
    room_name: str = Field(None, serialization_alias="roomName")
    """Your HipChat room name."""


class OpsgenieIntegrationSettings(BodyParamsA, BodyParamsB):
    """Client for Opsgenie integration settings resource."""

    type: Literal[IntegrationType.OPS_GENIE] = Field(
        IntegrationType.OPS_GENIE, serialization_alias="type"
    )
    api_key: str = Field(None, serialization_alias="apiKey")
    """Your API Key.

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

- View or edit the alert through the UI.
- Query the third-party integration settings through the API."""
    region: str = Field(None, serialization_alias="region")
    """Indicates which API URL is used, either US or EU. Opsgenie will use US by default."""


class VictorOpsIntegrationSettings(BodyParamsA, BodyParamsB):
    """Client for VictorOps integration settings resource."""

    type: Literal[IntegrationType.VICTOR_OPS] = Field(
        IntegrationType.VICTOR_OPS, serialization_alias="type"
    )
    api_key: str = Field(None, serialization_alias="apiKey")
    """Your API Key.

After you create a third-party integration that requires an API or integration key, the key appears partially redacted when you:

- View or edit the alert through the UI.
- Query the third-party integration settings through the API."""
    routing_key: Optional[str] = Field(None, serialization_alias="routingKey")
    """An optional field for your Routing Key."""


class WebhookIntegrationSettings(BodyParamsA, BodyParamsB):
    """Client for Webhook integration settings resource."""

    type: Literal[IntegrationType.WEBHOOK] = Field(
        IntegrationType.WEBHOOK, serialization_alias="type"
    )
    url: str = Field(None, serialization_alias="url")
    """Your webhook URL."""
    secret: Optional[str] = Field(None, serialization_alias="secret")
    """An optional field for your webhook secret.

After creating a webhook notification, the URL is partially redacted when you view or edit the alert, and the secret is completely redacted."""


class MicrosoftTeamsIntegrationSettings(BodyParamsA, BodyParamsB):
    """Client for Microsoft Teams integration settings resource."""

    type: Literal[IntegrationType.MICROSOFT_TEAMS] = Field(
        IntegrationType.MICROSOFT_TEAMS, serialization_alias="type"
    )
    microsoft_teams_webhook_url: str = Field(None, serialization_alias="microsoftTeamsWebhookUrl")
    """Your Microsoft Teams incoming webhook URL.

When you view or edit the alert for a webhook notification, the URL appears partially redacted, and the secret appears completely redacted."""


class PrometheusIntegrationSettings(BodyParamsA, BodyParamsB):
    """Client for Prometheus integration settings resource."""

    type: Literal[IntegrationType.PROMETHEUS] = Field(
        IntegrationType.PROMETHEUS, serialization_alias="type"
    )
    username: str = Field(None, serialization_alias="username")
    """Your Prometheus username."""
    password: str = Field(None, serialization_alias="password")
    """Your Prometheus password."""
    listen_address: str = Field(None, serialization_alias="listenAddress")
    """The IP address and port your Prometheus instance will reach out to."""
    service_discovery: PrometheusServiceDiscoveryType = Field(
        None, serialization_alias="serviceDiscovery"
    )
    """Indicates which service discovery method is used, either file or http."""
    scheme: PrometheusScheme = Field(None, serialization_alias="scheme")
    """Your Prometheus protocol scheme configured for requests, either http or https. If you configure https, you must specify tlsPemPath."""
    enabled: bool = Field(True, serialization_alias="enabled")
    """Whether your cluster has Prometheus enabled."""
    tls_pem_password: Optional[str] = Field(None, serialization_alias="tlsPemPassword")
    """An optional field for the password to your PEM file."""
    tls_pem_path: Optional[str] = Field(None, serialization_alias="tlsPemPath")
    """An optional field for the absolute path to your PEM file."""
