"""Auto-generated client for ImportDeploymentsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class ImportDeploymentsResource(BaseResource):
    """Client for ImportDeploymentsResource resource."""

    class CancelImportDeploymentRequestPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project.
        """

        request_id: str = Field(serialization_alias="REQUEST-ID")
        """Unique identifier of the import deployment request to cancel.
        """

    class CancelImportDeploymentRequestQueryParams(BaseModel):
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

    def cancel_import_deployment_request(
        self,
        path_params: CancelImportDeploymentRequestPathParams,
        query_params: Optional[CancelImportDeploymentRequestQueryParams],
    ) -> dict[str, Any]:
        """
        ## Cancel Import Deployment Request
        ### Document:
        [Cancel Import Deployment Request](https://www.mongodb.com/docs/ops-manager/current/reference/api/import-deployments/cancel/)
        ### Endpoint:
        `POST /automation/importDeployment/{PROJECT-ID}/{REQUEST-ID}/cancel`
        ### Description
        Cancel an in-progress import deployment request. This endpoint allows you to stop an import deployment request that is currently running. Once cancelled, the import process will stop and the request state will change to CANCELLED.
        """
        return self._request(
            "POST",
            "/automation/importDeployment/{PROJECT-ID}/{REQUEST-ID}/cancel",
            path_params,
            query_params,
            None,
        )

    class CreateImportDeploymentRequestPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that will own the imported deployments.
        """

    class CreateImportDeploymentRequestQueryParams(BaseModel):
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

    class CreateImportDeploymentRequestBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        admin_db: Optional[str] = Field(None, serialization_alias="adminDb")
        """Database to authenticate against. Default: admin.
        """

        admin_kerberos_keytab: Optional[str] = Field(
            None, serialization_alias="adminKerberosKeytab"
        )
        """Path to the Kerberos keytab file for GSSAPI authentication.
        """

        admin_ldap_group_dn: Optional[str] = Field(None, serialization_alias="adminLdapGroupDn")
        """LDAP group distinguished name for PLAIN authentication.
        """

        auth_mechanism: Optional[AuthMechanismName] = Field(
            None, serialization_alias="authMechanism"
        )
        """Authentication mechanism for connecting to the MongoDB processes. Possible values are:

MONGODB_CR (This covers SCRAM-SHA-1, SCRAM-SHA-256, and MONGODB-CR.)

GSSAPI

PLAIN

MONGODB_X509

NONE
        """

        ca_file_path: Optional[str] = Field(None, serialization_alias="caFilePath")
        """Path to the Certificate Authority file for TLS connections.
        """

        client_certificate_mode: Optional[str] = Field(
            None, serialization_alias="clientCertificateMode"
        )
        """Client certificate mode for TLS connections.
        """

        cluster_ca_file_path: Optional[str] = Field(None, serialization_alias="clusterCaFilePath")
        """Path to the cluster Certificate Authority file for TLS connections.
        """

        password: Optional[str] = Field(None, serialization_alias="password")
        """Password for authenticating to the MongoDB processes. Required if authMechanism is MONGODB_CR.

Ops Manager doesn't include this parameter in response documents.
        """

        pem_key_file_password: Optional[str] = Field(None, serialization_alias="pemKeyFilePassword")
        """Password for the PEM key file.

Ops Manager doesn't include this parameter in response documents.
        """

        pem_key_file_path: Optional[str] = Field(None, serialization_alias="pemKeyFilePath")
        """Path to the PEM key file for TLS client authentication.
        """

        required_processes: list[Any] = Field(serialization_alias="requiredProcesses")
        """Array of hostname:port strings representing MongoDB processes that must be discovered before the import can proceed.
        """

        sasl_service_name: Optional[str] = Field(None, serialization_alias="saslServiceName")
        """SASL service name for GSSAPI authentication.
        """

        seed_hostport: str = Field(serialization_alias="seedHostport")
        """Hostname and port of the seed MongoDB process to connect to for discovery (e.g., mongodb1.example.com:27017).
        """

        class TimeoutsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            automation_imported: Optional[float] = Field(
                None, serialization_alias="automationImported"
            )
            """Timeout in seconds for completing the automation import. Range: 60-86400 seconds. Default uses system settings.
            """

            goal_state_sec: Optional[float] = Field(None, serialization_alias="goalStateSec")
            """Timeout in seconds for reaching automation goal state. Range: 60-86400 seconds. Default uses system settings.
            """

            processes_discovery_sec: Optional[float] = Field(
                None, serialization_alias="processesDiscoverySec"
            )
            """Timeout in seconds for discovering all required processes. Range: 60-86400 seconds. Default uses system settings.
            """

            seed_host_connection_sec: Optional[float] = Field(
                None, serialization_alias="seedHostConnectionSec"
            )
            """Timeout in seconds for connecting to the seed host. Range: 60-86400 seconds. Default uses system settings.
            """

        timeouts: Optional[TimeoutsParams] = Field(None, serialization_alias="timeouts")
        """Timeout settings for various import phases.
        """

        username: Optional[str] = Field(None, serialization_alias="username")
        """Username for authenticating to the MongoDB processes. Required if authMechanism is specified.
        """

    def create_import_deployment_request(
        self,
        path_params: CreateImportDeploymentRequestPathParams,
        query_params: Optional[CreateImportDeploymentRequestQueryParams],
        body_params: CreateImportDeploymentRequestBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create Import Deployment Request
        ### Document:
        [Create Import Deployment Request](https://www.mongodb.com/docs/ops-manager/current/reference/api/import-deployments/create/)
        ### Endpoint:
        `POST /automation/importDeployment/{PROJECT-ID}`
        ### Description
        Create a new import deployment request to add existing MongoDB processes to Ops Manager automation. This endpoint initiates the process of importing multiple MongoDB processes into both monitoring and automation management.
        """
        return self._request(
            "POST",
            "/automation/importDeployment/{PROJECT-ID}",
            path_params,
            query_params,
            body_params,
        )

    class DeleteImportDeploymentRequestPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project.
        """

        request_id: str = Field(serialization_alias="REQUEST-ID")
        """Unique identifier of the import deployment request to delete.
        """

    class DeleteImportDeploymentRequestQueryParams(BaseModel):
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

    def delete_import_deployment_request(
        self,
        path_params: DeleteImportDeploymentRequestPathParams,
        query_params: Optional[DeleteImportDeploymentRequestQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete Import Deployment Request
        ### Document:
        [Delete Import Deployment Request](https://www.mongodb.com/docs/ops-manager/current/reference/api/import-deployments/delete/)
        ### Endpoint:
        `DELETE /automation/importDeployment/{PROJECT-ID}/{REQUEST-ID}`
        ### Description
        Delete a failed import deployment request and clean up any partially imported resources. This endpoint removes the import deployment request record and performs cleanup of any resources that were partially imported during the failed import process.
        """
        return self._request(
            "DELETE",
            "/automation/importDeployment/{PROJECT-ID}/{REQUEST-ID}",
            path_params,
            query_params,
            None,
        )

    class GetImportDeploymentRequestsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project.
        """

    class GetImportDeploymentRequestsQueryParams(BaseModel):
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

    def get_import_deployment_requests(
        self,
        path_params: GetImportDeploymentRequestsPathParams,
        query_params: Optional[GetImportDeploymentRequestsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Import Deployment Requests
        ### Document:
        [Get Import Deployment Requests](https://www.mongodb.com/docs/ops-manager/current/reference/api/import-deployments/get-all/)
        ### Endpoint:
        `GET /automation/importDeployment/{PROJECT-ID}`
        ### Description
        Retrieve all import deployment requests for a project. This endpoint returns a list of all import deployment requests that have been created for the specified project, including their current status and history.
        """
        return self._request(
            "GET",
            "/automation/importDeployment/{PROJECT-ID}",
            path_params,
            query_params,
            None,
        )

    class GetImportDeploymentRequestStatusPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        import_process_id: str = Field(serialization_alias="IMPORT-PROCESS-ID")
        """Unique identifier of the import deployment request.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project.
        """

    class GetImportDeploymentRequestStatusQueryParams(BaseModel):
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

    def get_import_deployment_request_status(
        self,
        path_params: GetImportDeploymentRequestStatusPathParams,
        query_params: Optional[GetImportDeploymentRequestStatusQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Import Deployment Request Status
        ### Document:
        [Get Import Deployment Request Status](https://www.mongodb.com/docs/ops-manager/current/reference/api/import-deployments/get-status/)
        ### Endpoint:
        `GET /automation/importDeployment/{PROJECT-ID}/{IMPORT-PROCESS-ID}`
        ### Description
        Retrieve the status of a specific import deployment request. This endpoint provides detailed information about the current state and history of a single import deployment request.
        """
        return self._request(
            "GET",
            "/automation/importDeployment/{PROJECT-ID}/{IMPORT-PROCESS-ID}",
            path_params,
            query_params,
            None,
        )
