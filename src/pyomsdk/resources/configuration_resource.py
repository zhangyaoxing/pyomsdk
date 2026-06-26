r"""Auto-generated client for ConfigurationResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class ConfigurationResource(BaseResource):
    r"""Client for ConfigurationResource resource."""

    class GetTheAuditLogRotateConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project)
that owns the automation configuration.
        """

    class GetTheAuditLogRotateConfigurationQueryParams(BaseModel):
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

    def get_the_audit_log_rotate_configuration(
        self,
        path_params: GetTheAuditLogRotateConfigurationPathParams,
        query_params: Optional[GetTheAuditLogRotateConfigurationQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get the Audit Log Rotate Configuration
        ### Document:
        [Get the Audit Log Rotate Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-audit-log-rotate-config/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/automationConfig/auditLogRotateConfig`
        ### Description
        This endpoint returns the current audit log rotation configuration.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/auditLogRotateConfig",
            path_params,
            query_params,
            None,
        )

    class GetTheAutomationConfigurationNoSecretsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [group](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-group) that owns the automation
configuration.
        """

    class GetTheAutomationConfigurationNoSecretsQueryParams(BaseModel):
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

    def get_the_automation_configuration_no_secrets(
        self,
        path_params: GetTheAutomationConfigurationNoSecretsPathParams,
        query_params: Optional[GetTheAutomationConfigurationNoSecretsQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get the Automation Configuration (Redacted Secrets)
        ### Document:
        [Get the Automation Configuration (No Secrets)](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-automation-config-no-secrets/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/automationConfig/noSecrets`
        ### Description
        A project's [automation configuration](/docs/ops-manager/current/reference/cluster-configuration/#std-label-automation-configuration-ref) determines the goal state of its MongoDB
        processes and agents. The MongoDB Agent builds the deployment according
        to the goals specified.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/noSecrets",
            path_params,
            query_params,
            None,
        )

    class GetTheAutomationConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [group](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-group) that owns the automation
configuration.
        """

    class GetTheAutomationConfigurationQueryParams(BaseModel):
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

    def get_the_automation_configuration(
        self,
        path_params: GetTheAutomationConfigurationPathParams,
        query_params: Optional[GetTheAutomationConfigurationQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get the Automation Configuration
        ### Document:
        [Get the Automation Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-automation-config/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/automationConfig`
        ### Description
        A project's [automation configuration](/docs/ops-manager/current/reference/cluster-configuration/#std-label-automation-configuration-ref) determines the goal state of its MongoDB
        processes and agents. The MongoDB Agent builds the deployment according
        to the goals specified.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig",
            path_params,
            query_params,
            None,
        )

    class GetBackupConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique 24-hexadecimal digit string that identifies the
[project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project) that owns the configuration.
        """

    class GetBackupConfigurationSettingsQueryParams(BaseModel):
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

    def get_backup_configuration_settings(
        self,
        path_params: GetBackupConfigurationSettingsPathParams,
        query_params: Optional[GetBackupConfigurationSettingsQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get Backup Configuration Settings
        ### Document:
        [Get Backup Configuration Settings](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-backup-log-attributes/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/automationConfig/backupAgentConfig`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/backupAgentConfig",
            path_params,
            query_params,
            None,
        )

    class GetMonitoringConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique 24-hexadecimal digit string that identifies the
[project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project) that owns the configuration.
        """

    class GetMonitoringConfigurationSettingsQueryParams(BaseModel):
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

    def get_monitoring_configuration_settings(
        self,
        path_params: GetMonitoringConfigurationSettingsPathParams,
        query_params: Optional[GetMonitoringConfigurationSettingsQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get Monitoring Configuration Settings
        ### Document:
        [Get Monitoring Configuration Settings](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-monitoring-log-attributes/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig",
            path_params,
            query_params,
            None,
        )

    class GetTheSystemLogRotateConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project)
that owns the automation configuration.
        """

    class GetTheSystemLogRotateConfigurationQueryParams(BaseModel):
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

    def get_the_system_log_rotate_configuration(
        self,
        path_params: GetTheSystemLogRotateConfigurationPathParams,
        query_params: Optional[GetTheSystemLogRotateConfigurationQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get the System Log Rotate Configuration
        ### Document:
        [Get the System Log Rotate Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-system-log-rotate-config/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/automationConfig/systemLogRotateConfig`
        ### Description
        This endpoint returns the current system log rotation configuration.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/systemLogRotateConfig",
            path_params,
            query_params,
            None,
        )

    class UpdateAgentVersionsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [group](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-group) that owns the automation
configuration.
        """

    class UpdateAgentVersionsQueryParams(BaseModel):
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

    class UpdateAgentVersionsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        automation_agent_version: Optional[str] = Field(
            default=None, serialization_alias="automationAgentVersion"
        )
        r"""Version to which you want to update the MongoDB Agent.
        """

        bi_connector_version: Optional[str] = Field(
            default=None, serialization_alias="biConnectorVersion"
        )
        r"""Version to which you want to update the [BI Connector](https://www.mongodb.com/docs/bi-connector/current/).
        """

        mongo_db_tools_version: Optional[str] = Field(
            default=None, serialization_alias="mongoDbToolsVersion"
        )
        r"""Version to which you want to update the
[MongoDB Database Tools](https://www.mongodb.com/docs/database-tools/)
        """

    def update_agent_versions(
        self,
        path_params: UpdateAgentVersionsPathParams,
        query_params: Optional[UpdateAgentVersionsQueryParams],
        body_params: Optional[UpdateAgentVersionsBodyParams],
    ) -> dict[str, Any]:
        r"""
        ## Update Agent Versions
        ### Document:
        [Update Agent Versions](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-agent-versions/)
        ### Endpoint:
        `POST /groups/{PROJECT-ID}/automationConfig/updateAgentVersions`
        ### Description
        This endpoint updates the MongoDB Agent and tools to the latest
        versions available at the time of the request:
        """
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/updateAgentVersions",
            path_params,
            query_params,
            body_params,
        )

    class UpdateTheAuditLogRotateConfigPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project)
that owns the automation configuration.
        """

    class UpdateTheAuditLogRotateConfigQueryParams(BaseModel):
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

    class UpdateTheAuditLogRotateConfigBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        num_total: Optional[Any] = Field(default=None, serialization_alias="numTotal")
        r"""Total number of log files. If the number of log files on disk is
greater than this number, the oldest files will be deleted.
If a number is not specified, defaults to 0 and is determined
by other settings.
        """

        num_uncompressed: Optional[Any] = Field(default=None, serialization_alias="numUncompressed")
        r"""Maximum number of total log files to leave uncompressed,
including the current log file. The default is `5`. If number of log
files is more than max uncompressed, sort by date, and then keep
compressing the oldest file until the restraint is met.
        """

        percent_of_diskspace: Optional[Any] = Field(
            default=None, serialization_alias="percentOfDiskspace"
        )
        r"""Maximum percentage of total disk space all log files
should take up before deletion. The default is `.02`. If log files
size is taking up more than max percent of total disk space, sort by
date, and then keep deleting the oldest file until the restraint is met.
        """

        size_threshold_mb: Optional[Any] = Field(
            default=None, serialization_alias="sizeThresholdMB"
        )
        r"""Maximum size in MB for an individual log file before rotation.
NOTE: this parameter is required unless you are passing an empty request body
to disable log rotation.
        """

        time_threshold_hrs: Optional[Any] = Field(
            default=None, serialization_alias="timeThresholdHrs"
        )
        r"""Maximum time in hours for an individual log file before rotation.
NOTE: this parameter is required unless you are passing an empty request body
to disable log rotation.
        """

    def update_the_audit_log_rotate_config(
        self,
        path_params: UpdateTheAuditLogRotateConfigPathParams,
        query_params: Optional[UpdateTheAuditLogRotateConfigQueryParams],
        body_params: Optional[UpdateTheAuditLogRotateConfigBodyParams],
    ) -> dict[str, Any]:
        r"""
        ## Update the Audit Log Rotate Config
        ### Document:
        [Update the Audit Log Rotate Config](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-audit-log-rotate-config/)
        ### Endpoint:
        `PUT /groups/{PROJECT-ID}/automationConfig/auditLogRotateConfig`
        ### Description
        This endpoint updates the MongoDB Agent audit log rotation configuration.
        After this request completes, Ops Manager modifies the agent configuration
        and saves the updated version.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/auditLogRotateConfig",
            path_params,
            query_params,
            body_params,
        )

    class UpdateTheAutomationConfigurationNoSecretsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [group](https://www.mongodb.com/docs/cloud-manager/reference/glossary/#std-term-group) that owns the automation
configuration.
        """

    class UpdateTheAutomationConfigurationNoSecretsQueryParams(BaseModel):
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

    class UpdateTheAutomationConfigurationNoSecretsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True, extra="allow")

    def update_the_automation_configuration_no_secrets(
        self,
        path_params: UpdateTheAutomationConfigurationNoSecretsPathParams,
        query_params: Optional[UpdateTheAutomationConfigurationNoSecretsQueryParams],
        body_params: Optional[UpdateTheAutomationConfigurationNoSecretsBodyParams],
    ) -> dict[str, Any]:
        r"""
        ## Update Automation Config Without Sensitive Fields
        ### Document:
        [Update the Automation Configuration (No Secrets)](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-automation-config-no-secrets/)
        ### Endpoint:
        `PUT /groups/{PROJECT-ID}/automationConfig/noSecrets`
        ### Description
        A project's [automation configuration](/docs/ops-manager/current/reference/cluster-configuration/#std-label-automation-configuration-ref) determines the goal state of its MongoDB
        processes and agents. The MongoDB Agent builds the deployment according
        to the goals specified.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/noSecrets",
            path_params,
            query_params,
            body_params,
        )

    class UpdateTheAutomationConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [group](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-group) that owns the automation
configuration.
        """

    class UpdateTheAutomationConfigurationQueryParams(BaseModel):
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

    class UpdateTheAutomationConfigurationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True, extra="allow")

    def update_the_automation_configuration(
        self,
        path_params: UpdateTheAutomationConfigurationPathParams,
        query_params: Optional[UpdateTheAutomationConfigurationQueryParams],
        body_params: Optional[UpdateTheAutomationConfigurationBodyParams],
    ) -> dict[str, Any]:
        r"""
        ## Update the Automation Configuration
        ### Document:
        [Update the Automation Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-automation-config/)
        ### Endpoint:
        `PUT /groups/{PROJECT-ID}/automationConfig`
        ### Description
        A project's [automation configuration](/docs/ops-manager/current/reference/cluster-configuration/#std-label-automation-configuration-ref) determines the goal state of its MongoDB
        processes and agents. The MongoDB Agent builds the deployment according
        to the goals specified.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig",
            path_params,
            query_params,
            body_params,
        )

    class UpdateBackupConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique 24-hexadecimal digit string that identifies the
[project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project) that owns the configuration.
        """

    class UpdateBackupConfigurationSettingsQueryParams(BaseModel):
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

    class UpdateBackupConfigurationSettingsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        config_overrides: Optional[dict] = Field(
            default=None, serialization_alias="configOverrides"
        )
        r"""List of MongoDB Agent settings that you need to change because
your backup settings differ from those of the
[MongoDB Agent](/docs/ops-manager/current/reference/mongodb-agent-settings/#std-label-mongodb-agent-settings-main). Configure this
option when upgrading from legacy agents to the MongoDB Agent.

| Setting | Data Type |
| --- | --- |
| [`mmsGroupId`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.mmsGroupId) | string |
| [`mmsApiKey`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.mmsApiKey) | string |
| [`mothership`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.mothership) | string |
| [`mothershipResponseHeaderTimeout`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.mothershipResponseHeaderTimeout) | integer |
| [`https`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.https) | boolean |
| [`httpProxy`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.httpProxy) | string |
| [`krb5Principal`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.krb5Principal) | string |
| [`krb5Keytab`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.krb5Keytab) | string |
| [`krb5ConfigLocation`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.krb5ConfigLocation) | string |
| [`gsapiServiceName`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.gsapiServiceName) | string |
| [`sslClientCertificate`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.sslClientCertificate) | string |
| [`sslClientCertificatePassword`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.sslClientCertificatePassword) | string |
| [`sslTrustedServerCertificates`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.sslTrustedServerCertificates) | string |
| [`sslRequireValidServerCertificates`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.sslRequireValidServerCertificates) | boolean |
| [`sslTrustedMMSBackupServerCertificate`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-bsetting-bsetting.sslTrustedMMSBackupServerCertificate) | string |
        """

        log_path: Optional[str] = Field(default=None, serialization_alias="logPath")
        r"""Absolute file path to which this MongoDB Agent writes its logs.
If this is not specified, the log writes to standard error
(`stderr`) on UNIX- and Linux-based systems and to the Event
Log on Windows systems.
        """

        class LogRotateParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            size_threshold_mb: Optional[int] = Field(
                default=None, serialization_alias="sizeThresholdMB"
            )
            r"""Maximum size, in MB, of a log file before this MongoDB Agent
rotates the logs.
            """

            time_duration_hrs: Optional[int] = Field(
                default=None, serialization_alias="timeDurationHrs"
            )
            r"""Number of hours after which this MongoDB Agent rotates the log
file.
            """

        log_rotate: Optional[LogRotateParams] = Field(default=None, serialization_alias="logRotate")
        r"""Thresholds after which this MongoDB Agent rotates the backup log.
        """

        username: Optional[str] = Field(default=None, serialization_alias="username")
        r"""MongoDB user in the application database that manages the
backup logs.

If you use the API to enable authentication for the
MongoDB Agent, set this parameter to **mms-automation** when
executing this endpoint.
        """

    def update_backup_configuration_settings(
        self,
        path_params: UpdateBackupConfigurationSettingsPathParams,
        query_params: Optional[UpdateBackupConfigurationSettingsQueryParams],
        body_params: Optional[UpdateBackupConfigurationSettingsBodyParams],
    ) -> dict[str, Any]:
        r"""
        ## Update Backup Configuration Settings
        ### Document:
        [Update Backup Configuration Settings](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-backup-log-attributes/)
        ### Endpoint:
        `PUT /groups/{PROJECT-ID}/automationConfig/backupAgentConfig`
        ### Description
        No description.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/backupAgentConfig",
            path_params,
            query_params,
            body_params,
        )

    class UpdateMonitoringConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique 24-hexadecimal digit string that identifies the
[project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project) that owns the configuration.
        """

    class UpdateMonitoringConfigurationSettingsQueryParams(BaseModel):
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

    class UpdateMonitoringConfigurationSettingsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        config_overrides: Optional[dict] = Field(
            default=None, serialization_alias="configOverrides"
        )
        r"""List of MongoDB Agent settings that you need to change because
your monitoring settings differ from those of the
[MongoDB Agent](/docs/ops-manager/current/reference/mongodb-agent-settings/#std-label-mongodb-agent-settings-main). Configure
this option when upgrading from legacy agents to the
MongoDB Agent.

| Setting | Data Type |
| --- | --- |
| [`mmsGroupId`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.mmsGroupId) | string |
| [`mmsApiKey`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.mmsApiKey) | string |
| [`mmsBaseUrl`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.mmsBaseUrl) | string |
| [`httpProxy`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.httpProxy) | string |
| [`krb5Principal`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.krb5Principal) | string |
| [`krb5Keytab`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.krb5Keytab) | string |
| [`krb5ConfigLocation`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.krb5ConfigLocation) | string |
| [`gssapiServiceName`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.gssapiServiceName) | string |
| [`useSslForAllConnections`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.useSslForAllConnections) | boolean |
| [`sslClientCertificate`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.sslClientCertificate) | string |
| [`sslClientCertificatePassword`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.sslClientCertificatePassword) | string |
| [`sslTrustedServerCertificates`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.sslTrustedServerCertificates) | string |
| [`sslRequireValidServerCertificates`](/docs/ops-manager/current/reference/mongodb-agent-settings/#mongodb-msetting-msetting.sslRequireValidServerCertificates) | boolean |
| `enableMunin` | boolean |
        """

        log_path: Optional[str] = Field(default=None, serialization_alias="logPath")
        r"""Absolute file path to which this MongoDB Agent writes its logs.
If this is not specified, the log writes to standard error
(`stderr`) on UNIX- and Linux-based systems and to the Event
Log on Windows systems.
        """

        class LogRotateParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            size_threshold_mb: Optional[int] = Field(
                default=None, serialization_alias="sizeThresholdMB"
            )
            r"""Maximum size, in MB, of a log file before this MongoDB Agent
rotates the logs.
            """

            time_duration_hrs: Optional[int] = Field(
                default=None, serialization_alias="timeDurationHrs"
            )
            r"""Number of hours after which this MongoDB Agent rotates the log
file.
            """

        log_rotate: Optional[LogRotateParams] = Field(default=None, serialization_alias="logRotate")
        r"""Thresholds after which this MongoDB Agent rotates the monitoring
log.
        """

        username: Optional[str] = Field(default=None, serialization_alias="username")
        r"""MongoDB user in the application database that manages the
monitoring logs.

If you use the API to enable authentication for the
MongoDB Agent, set this parameter to **mms-automation** when
executing this endpoint.
        """

    def update_monitoring_configuration_settings(
        self,
        path_params: UpdateMonitoringConfigurationSettingsPathParams,
        query_params: Optional[UpdateMonitoringConfigurationSettingsQueryParams],
        body_params: Optional[UpdateMonitoringConfigurationSettingsBodyParams],
    ) -> dict[str, Any]:
        r"""
        ## Update Monitoring Configuration Settings
        ### Document:
        [Update Monitoring Configuration Settings](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-monitoring-log-attributes/)
        ### Endpoint:
        `PUT /groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig`
        ### Description
        No description.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig",
            path_params,
            query_params,
            body_params,
        )

    class UpdateTheSystemLogRotateConfigPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project)
that owns the automation configuration.
        """

    class UpdateTheSystemLogRotateConfigQueryParams(BaseModel):
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

    class UpdateTheSystemLogRotateConfigBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        num_total: Optional[Any] = Field(default=None, serialization_alias="numTotal")
        r"""Total number of log files. If the number of log files on disk is
greater than this number, the oldest files will be deleted.
If a number is not specified, defaults to 0 and is determined
by other settings.
        """

        num_uncompressed: Optional[Any] = Field(default=None, serialization_alias="numUncompressed")
        r"""Maximum number of total log files to leave uncompressed,
including the current log file. The default is `5`. If number of log
files is more than max uncompressed, sort by date, and then keep
compressing the oldest file until the restraint is met.
        """

        percent_of_diskspace: Optional[Any] = Field(
            default=None, serialization_alias="percentOfDiskspace"
        )
        r"""Maximum percentage of total disk space all log files
should take up before deletion. The default is `.02`. If log files
size is taking up more than max percent of total disk space, sort by
date, and then keep deleting the oldest file until the restraint is met.
        """

        size_threshold_mb: Optional[Any] = Field(
            default=None, serialization_alias="sizeThresholdMB"
        )
        r"""Maximum size in MB for an individual log file before rotation.
NOTE: this parameter is required unless you are passing an empty request body
to disable log rotation.
        """

        time_threshold_hrs: Optional[Any] = Field(
            default=None, serialization_alias="timeThresholdHrs"
        )
        r"""Maximum time in hours for an individual log file before rotation.
NOTE: this parameter is required unless you are passing an empty request body
to disable log rotation.
        """

    def update_the_system_log_rotate_config(
        self,
        path_params: UpdateTheSystemLogRotateConfigPathParams,
        query_params: Optional[UpdateTheSystemLogRotateConfigQueryParams],
        body_params: Optional[UpdateTheSystemLogRotateConfigBodyParams],
    ) -> dict[str, Any]:
        r"""
        ## Update the System Log Rotate Config
        ### Document:
        [Update the System Log Rotate Config](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-system-log-rotate-config/)
        ### Endpoint:
        `PUT /groups/{PROJECT-ID}/automationConfig/systemLogRotateConfig`
        ### Description
        This endpoint updates the MongoDB Agent system log rotation configuration.
        After this request completes, Ops Manager modifies the agent configuration
        and saves the updated version.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/systemLogRotateConfig",
            path_params,
            query_params,
            body_params,
        )
