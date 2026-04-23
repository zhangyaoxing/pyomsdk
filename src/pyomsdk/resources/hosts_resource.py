"""Auto-generated client for HostsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class HostsResource(BaseResource):
    """Client for HostsResource resource."""

    class BeginMonitoringPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns this MongoDB process.
        """

    class BeginMonitoringQueryParams(BaseModel):
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

    class BeginMonitoringBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alerts_enabled: Optional[bool] = Field(serialization_alias="alertsEnabled")
        """Set to true if alerts should be enabled for this MongoDB process.
        """

        auth_mechanism_name: Optional[AuthMechanismName] = Field(
            serialization_alias="authMechanismName"
        )
        """Specify which authentication mechanism should be used to connect to this MongoDB process. Possible values are:

MONGODB_CR (This covers SCRAM-SHA-1, SCRAM-SHA-256, and MONGODB-CR.)

GSSAPI

PLAIN

MONGODB_X509

NONE
        """

        hostname: str = Field(serialization_alias="hostname")
        """Set the primary hostname Ops Manager should use to connect to this MongoDB instance.
        """

        logs_enabled: Optional[bool] = Field(serialization_alias="logsEnabled")
        """Set to true if Ops Manager should collect logs for this MongoDB process.
        """

        password: Optional[str] = Field(serialization_alias="password")
        """Password associated with username for connecting to this MongoDB process.

Set this parameter if "authMechanismName" : "MONGODB_CR"

Ops Manager doesn't include this parameter in any Host || response.
        """

        port: float = Field(serialization_alias="port")
        """Port on which MongoDB process listens.
        """

        profiler_enabled: Optional[bool] = Field(serialization_alias="profilerEnabled")
        """Flag indicating whether Ops Manager collects profile information from this MongoDB process.
        """

        ssl_enabled: Optional[bool] = Field(serialization_alias="sslEnabled")
        """Flag indicating whether TLS should be enabled for this MongoDB process.

Set to true if "authMechanismName" : "MONGODB_X509".
        """

        username: Optional[str] = Field(serialization_alias="username")
        """Username needed to connect to this MongoDB process.

Required if "authMechanismName" : "MONGODB_CR"
        """

    def begin_monitoring(
        self,
        path_params: BeginMonitoringPathParams,
        query_params: Optional[BeginMonitoringQueryParams],
        body_params: BeginMonitoringBodyParams,
    ) -> dict[str, Any]:
        """
        ## Begin Monitoring One Host
        - Document: [Begin Monitoring](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/create-one-host/)
        - Resource: `POST /groups/{PROJECT-ID}/hosts`
        - Description: Start monitoring a new MongoDB process. The Monitoring starts monitoring the MongoDB process on the hostname and port you specify. Ops Manager knows only the information that you provide. The response document includes blank values until Ops Manager completes discovery of the MongoDB processes configuration.
        """
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/hosts",
            path_params,
            query_params,
            body_params,
        )

    class StopMonitoringPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """(Required.) Unique identifier of the host for the MongoDB process.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) Unique identifier of the project that owns this MongoDB host.
        """

    class StopMonitoringQueryParams(BaseModel):
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

    def stop_monitoring(
        self,
        path_params: StopMonitoringPathParams,
        query_params: Optional[StopMonitoringQueryParams],
    ) -> dict[str, Any]:
        """
        ## Stop Monitoring One Host
        - Document: [Stop Monitoring](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/delete-one-host/)
        - Resource: `DELETE /groups/{PROJECT-ID}/hosts/{HOST-ID}`
        - Description: Stops the Monitoring from monitoring the MongoDB process on the hostname and port you specify.
        """
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns this MongoDB host.
        """

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="clusterId")
        """Unique identifier of the cluster in which this MongoDB process belongs.
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

    def get_all(
        self,
        path_params: GetAllPathParams,
        query_params: GetAllQueryParams,
    ) -> dict[str, Any]:
        """
        ## Get All Hosts in One Project
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/get-all-hosts-in-group/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts`
        - Description: Get all MongoDB hosts in a project. Use the CLUSTER-ID query parameter to only get the hosts that belong to the specified cluster. The response sorts the hosts alphabetically by HOSTNAME:PORT.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts",
            path_params,
            query_params,
            None,
        )

    class GetByHostnamePortPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        hostname: str = Field(serialization_alias="HOSTNAME")
        """Primary hostname Ops Manager should use to connect to this MongoDB instance. This hostname can be a hostname, an FQDN, an IPv4 address, or an IPv6 address.
        """

        port: str = Field(serialization_alias="PORT")
        """Port on which the MongoDB process listens.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns this MongoDB process.
        """

    class GetByHostnamePortQueryParams(BaseModel):
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

    def get_by_hostname_port(
        self,
        path_params: GetByHostnamePortPathParams,
        query_params: Optional[GetByHostnamePortQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Host by Hostname and Port
        - Document: [Get by Hostname & Port](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/get-one-host-by-hostname-port/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/byName/{HOSTNAME}:{PORT}`
        - Description: Get a single MongoDB process by its hostname and port combination. You can specify either the primary hostname or an alias.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/byName/{HOSTNAME}:{PORT}",
            path_params,
            query_params,
            None,
        )

    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """Unique identifier of the host for the MongoDB process.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns this MongoDB process.
        """

    class GetByIdQueryParams(BaseModel):
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

    def get_by_id(
        self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Host by ID
        - Document: [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/get-one-host-by-id/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}`
        - Description: Get the MongoDB process with the specified host ID.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdateConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """Unique identifier of the host for the MongoDB process.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns this MongoDB process.
        """

    class UpdateConfigurationQueryParams(BaseModel):
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

    class UpdateConfigurationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        alerts_enabled: Optional[bool] = Field(serialization_alias="alertsEnabled")
        """Set to true if alerts should be enabled for this MongoDB process.
        """

        auth_mechanism_name: Optional[AuthMechanismName] = Field(
            serialization_alias="authMechanismName"
        )
        """Specify which authentication mechanism should be used to connect to this MongoDB process. Possible values are:

MONGODB_CR (This covers SCRAM-SHA-1, SCRAM-SHA-256, and MONGODB-CR.)

GSSAPI

PLAIN

MONGODB_X509

NONE
        """

        logs_enabled: Optional[bool] = Field(serialization_alias="logsEnabled")
        """Set to true if Ops Manager should collect logs for this MongoDB process.
        """

        password: Optional[str] = Field(serialization_alias="password")
        """Password for connecting to this MongoDB process. Specify if "authMechanismName" : "MONGODB_CR" or "authMechanismName" : "SCRAM_SHA_1". However, it will never be exposed when a host entity is returned.
        """

        profiler_enabled: Optional[bool] = Field(serialization_alias="profilerEnabled")
        """Set to true if Ops Manager collects profile information from this MongoDB process.
        """

        ssl_enabled: Optional[bool] = Field(serialization_alias="sslEnabled")
        """Set to true if TLS/SSL should be enabled for this MongoDB process. Set to true if "authMechanismName" : "MONGODB_X509".
        """

        username: Optional[str] = Field(serialization_alias="username")
        """Username needed to connect to this MongoDB process. Specify if "authMechanismName" : "MONGODB_CR" or "authMechanismName" : "SCRAM_SHA_1".
        """

    def update_configuration(
        self,
        path_params: UpdateConfigurationPathParams,
        query_params: Optional[UpdateConfigurationQueryParams],
        body_params: Optional[UpdateConfigurationBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update Configuration of One Monitored Host
        - Document: [Update Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/update-one-host/)
        - Resource: `PATCH /groups/{PROJECT-ID}/hosts/{HOST-ID}`
        - Description: Update the configuration of a monitored MongoDB process.
        """
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}",
            path_params,
            query_params,
            body_params,
        )
