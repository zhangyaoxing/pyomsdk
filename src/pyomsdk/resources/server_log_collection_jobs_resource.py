"""Auto-generated client for ServerLogCollectionJobsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class ServerLogCollectionJobsResource(BaseResource):
    """Client for ServerLogCollectionJobsResource resource."""

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique 24-hexadecimal digit string that identifies the Ops Manager server log collection job. To find a job ID, call Get All Ops Manager Server Log Collection Jobs.
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
        ## Delete an Ops Manager Server Log Collection Job
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/om-log-collections/om-log-collections-delete-one/)
        ### Endpoint:
        `DELETE /admin/omLogCollectionJobs/{JOB-ID}`
        ### Description
        Use this endpoint to delete an Ops Manager server log collection job and its archive. Ops Manager removes the job, all task summaries, and every collected log file from the Application Database immediately. You cannot delete a job that is still in progress.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/admin/omLogCollectionJobs/{JOB-ID}",
            path_params,
            query_params,
            None,
        )

    class DownloadLogsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique 24-hexadecimal digit string that identifies the Ops Manager server log collection job. To find a job ID, call Get All Ops Manager Server Log Collection Jobs.
        """

    class DownloadLogsQueryParams(BaseModel):
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

    def download_logs(
        self,
        path_params: DownloadLogsPathParams,
        query_params: Optional[DownloadLogsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Download Ops Manager Server Logs
        ### Document:
        [Download Logs](https://www.mongodb.com/docs/ops-manager/current/reference/api/om-log-collections/om-log-collections-download-job/)
        ### Endpoint:
        `GET /admin/omLogCollectionJobs/{JOB-ID}:download`
        ### Description
        Use this endpoint to download a .tar.gz archive that contains every log file that Ops Manager collected for the specified job. You cannot download from a job whose status is IN_PROGRESS or EXPIRED. If a job partially failed, the archive includes only the log files that Ops Manager collected successfully.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/omLogCollectionJobs/{JOB-ID}:download",
            path_params,
            query_params,
            None,
        )

    class GetAllJobsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether to wrap the response in an envelope. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

        verbose: Optional[bool] = Field(False, serialization_alias="verbose")
        """Flag that indicates whether to include all child jobs in the response. Each Ops Manager server log collection job has a child job for each combination of server and log type included in the request.
        """

    def get_all_jobs(
        self,
        query_params: Optional[GetAllJobsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Ops Manager Server Log Collection Jobs
        ### Document:
        [Get All Jobs](https://www.mongodb.com/docs/ops-manager/current/reference/api/om-log-collections/om-log-collections-get-all/)
        ### Endpoint:
        `GET /admin/omLogCollectionJobs`
        ### Description
        Use this endpoint to retrieve every Ops Manager server log collection job.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/omLogCollectionJobs",
            None,
            query_params,
            None,
        )

    class GetOneJobPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique 24-hexadecimal digit string that identifies the Ops Manager server log collection job. To find a job ID, call Get All Ops Manager Server Log Collection Jobs.
        """

    class GetOneJobQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether to wrap the response in an envelope. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

        verbose: Optional[bool] = Field(False, serialization_alias="verbose")
        """Flag that indicates whether to include all child jobs in the response.
        """

    def get_one_job(
        self,
        path_params: GetOneJobPathParams,
        query_params: Optional[GetOneJobQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Ops Manager Server Log Collection Job
        ### Document:
        [Get One Job](https://www.mongodb.com/docs/ops-manager/current/reference/api/om-log-collections/om-log-collections-get-one/)
        ### Endpoint:
        `GET /admin/omLogCollectionJobs/{JOB-ID}`
        ### Description
        Use this endpoint to retrieve a single Ops Manager server log collection job by its identifier.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/omLogCollectionJobs/{JOB-ID}",
            path_params,
            query_params,
            None,
        )

    class ListActiveServersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether to wrap the response in an envelope. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

        status: Optional[str] = Field("active", serialization_alias="status")
        """Server status to filter by. Currently the only valid value is active. Any other value returns 400 INVALID_SERVER_STATUS. If you omit this parameter, Ops Manager returns active servers.
        """

        type: Optional[str] = Field("All types", serialization_alias="type")
        """Server type to filter by. Pass this parameter multiple times to include several types (?type=VALUE_1&type=VALUE_2). The currently supported value is MMS_SERVER, which represents the Ops Manager application server. If you omit this parameter, Ops Manager returns all types (currently only MMS_SERVER).
        """

    def list_active_servers(
        self,
        query_params: Optional[ListActiveServersQueryParams],
    ) -> dict[str, Any]:
        """
        ## List Active Ops Manager Servers
        ### Document:
        [List Active Servers](https://www.mongodb.com/docs/ops-manager/current/reference/api/om-log-collections/om-log-collections-list-servers/)
        ### Endpoint:
        `GET /admin/servers`
        ### Description
        Returns a list of all active Ops Manager servers. Ops Manager considers a server active if it sent a heartbeat to the Application Database within the last 20 seconds. Use this endpoint to discover valid serverId values before you submit a log collection request.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/servers",
            None,
            query_params,
            None,
        )

    class RetryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique 24-hexadecimal digit string that identifies the Ops Manager server log collection job. To find a job ID, call Get All Ops Manager Server Log Collection Jobs.
        """

    class RetryQueryParams(BaseModel):
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

    def retry(
        self,
        path_params: RetryPathParams,
        query_params: Optional[RetryQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retry an Ops Manager Server Log Collection Job
        ### Document:
        [Retry](https://www.mongodb.com/docs/ops-manager/current/reference/api/om-log-collections/om-log-collections-retry/)
        ### Endpoint:
        `POST /admin/omLogCollectionJobs/{JOB-ID}:retry`
        ### Description
        Use this endpoint to retry the failed tasks in an Ops Manager server log collection job. Ops Manager reruns only the child tasks whose status is FAILURE and preserves the tasks that succeeded.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/admin/omLogCollectionJobs/{JOB-ID}:retry",
            path_params,
            query_params,
            None,
        )

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

        eachvalueinserversmustidentifyaregisteredactive_ops_managerserver: Optional[Any] = Field(
            None,
            serialization_alias="Each value in servers must identify a registered, active Ops Manager server",
        )
        """400
        """

        theestimatedstoragemustnotexceedthestoragelimitthatthe_ops_manageradministratorhasconfiguredforlogcollection: Optional[
            Any
        ] = Field(
            None,
            serialization_alias="The estimated storage must not exceed the storage limit that the Ops Manager administrator has configured for log collection",
        )
        """413
        """

        thenumberofconcurrentjobsmustnotexceed4: Optional[Any] = Field(
            None, serialization_alias="The number of concurrent jobs must not exceed 4"
        )
        """429
        """

        thetimerangemustnotexceed7days: Optional[Any] = Field(
            None, serialization_alias="The time range must not exceed 7 days"
        )
        """400
        """

        thetimerangemustnotstartearlierthanthemaximumloghistorythatthe_ops_manageradministratorhasconfigured: Optional[
            Any
        ] = Field(
            None,
            serialization_alias="The time range must not start earlier than the maximum log history that the Ops Manager administrator has configured",
        )
        """400
        """

        log_collection_from_date: Optional[str] = Field(
            None, serialization_alias="logCollectionFromDate"
        )
        """Start of the time range to collect, in ISO 8601 UTC format. If you set this field, you must also set logCollectionToDate.
        """

        log_collection_from_dateandlog_collection_to_datemustbesettogether: Optional[Any] = Field(
            None,
            serialization_alias="logCollectionFromDate and logCollectionToDate must be set together",
        )
        """400
        """

        log_collection_from_datemustnotbeinthefuture: Optional[Any] = Field(
            None, serialization_alias="logCollectionFromDate must not be in the future"
        )
        """400
        """

        log_collection_from_datemustprecedelog_collection_to_date: Optional[Any] = Field(
            None, serialization_alias="logCollectionFromDate must precede logCollectionToDate"
        )
        """400
        """

        log_collection_to_date: Optional[str] = Field(
            None, serialization_alias="logCollectionToDate"
        )
        """End of the time range to collect, in ISO 8601 UTC format. If you set this field, you must also set logCollectionFromDate.
        """

        log_types: Optional[list[LogType]] = Field(None, serialization_alias="logTypes")
        """Log types to collect. Each element must be one of the following values:

APPLICATION

HTTP_ACCESS

MIGRATION

If you omit this field or pass an empty array, Ops Manager collects every log type.
        """

        servers: Optional[list[str]] = Field(None, serialization_alias="servers")
        """List of serverId values returned by List Active Ops Manager Servers. If you omit this field or pass an empty array, Ops Manager collects logs from every active server.
        """

        size_requested_per_file_bytes: Optional[int] = Field(
            None, serialization_alias="sizeRequestedPerFileBytes"
        )
        """Maximum uncompressed size, in bytes, per log type per server. Must be greater than 0. If you omit this field, Ops Manager auto-allocates the remaining configured storage across the requested servers and log types.
        """

        size_requested_per_file_bytesmustbegreaterthan0: Optional[Any] = Field(
            None, serialization_alias="sizeRequestedPerFileBytes must be greater than 0"
        )
        """400
        """

    def create(
        self,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Create an Ops Manager Server Log Collection Job
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/om-log-collections/om-log-collections-submit/)
        ### Endpoint:
        `POST /admin/omLogCollectionJobs`
        ### Description
        When you create an Ops Manager server log collection job, Ops Manager starts background tasks to collect the requested logs from the target servers. Each server collects its logs locally, compresses and encrypts them, and stores the result in the Application Database. Use this endpoint to create a new job.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/admin/omLogCollectionJobs",
            None,
            query_params,
            body_params,
        )

    class ExtendExpirationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique 24-hexadecimal digit string that identifies the Ops Manager server log collection job. To find a job ID, call Get All Ops Manager Server Log Collection Jobs.
        """

    class ExtendExpirationQueryParams(BaseModel):
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

    class ExtendExpirationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        expiration_date: str = Field(serialization_alias="expirationDate")
        """New expiration timestamp, in ISO 8601 UTC format. The timestamp must be no more than 28 days after the job creation date and no earlier than the time of the request.
        """

    def extend_expiration(
        self,
        path_params: ExtendExpirationPathParams,
        query_params: Optional[ExtendExpirationQueryParams],
        body_params: ExtendExpirationBodyParams,
    ) -> dict[str, Any]:
        """
        ## Extend an Ops Manager Server Log Collection Job Expiration
        ### Document:
        [Extend Expiration](https://www.mongodb.com/docs/ops-manager/current/reference/api/om-log-collections/om-log-collections-update-one/)
        ### Endpoint:
        `PATCH /admin/omLogCollectionJobs/{JOB-ID}`
        ### Description
        Ops Manager sets the default expiration of every job to 7 days from the job creation date. Use this endpoint to extend the expiration of an existing job. The new expiration date must be no more than 28 days after the original creation date. You cannot extend a job that has already expired.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/admin/omLogCollectionJobs/{JOB-ID}",
            path_params,
            query_params,
            body_params,
        )
