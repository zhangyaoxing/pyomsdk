"""Auto-generated client for LogCollectionJobsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class LogCollectionJobsResource(BaseResource):
    """Client for LogCollectionJobsResource resource."""

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the log collection request job.
        """

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique 24-hexadecimal digit string that identifies the log collection job to retry. Use the Get All Log Collection Jobs for One Project endpoint to obtain the IDs associated with your project.
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
        ## Delete a Log Collection Job
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-delete-one/)
        ### Endpoint:
        `DELETE /groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}`
        ### Description
        When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to delete a specified log collection job. You can delete both in-progress jobs and completed jobs.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}",
            path_params,
            query_params,
            None,
        )

    class DownloadLogsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the log collection request job.
        """

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique identifier of the job for which to download the logs. You can obtain the JOB-IDs associated with your project by using the Get All Log Collection Jobs for One Project endpoint.
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
        ## Download Logs from a Log Collection Job
        ### Document:
        [Download Logs](https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-download-job/)
        ### Endpoint:
        `GET /groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}/download`
        ### Description
        When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to download a .tar.gz file stream for all logs associated with the specified job.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}/download",
            path_params,
            query_params,
            None,
        )

    class GetAllJobsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the log collection request job.
        """

    class GetAllJobsQueryParams(BaseModel):
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

        verbose: Optional[bool] = Field(False, serialization_alias="verbose")
        """Flag that indicates whether to include all child jobs in the response. Each log collection job contains child jobs for each log type and MongoDB process included in the request.
        """

    def get_all_jobs(
        self,
        path_params: GetAllJobsPathParams,
        query_params: Optional[GetAllJobsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Log Collection Jobs for One Project
        ### Document:
        [Get All Jobs](https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-get-all/)
        ### Endpoint:
        `GET /groups/{GROUP-ID}/logCollectionJobs`
        ### Description
        When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to retrieve all log collection jobs for a specified Ops Manager project.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs",
            path_params,
            query_params,
            None,
        )

    class GetJobPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(
            "Unique 24-hexadecimal digit string that identifies the log collection request job.",
            serialization_alias="GROUP-ID",
        )
        """Unique 24-hexadecimal digit string that identifies the log collection request job.
        """

        job_id: str = Field(
            "Unique 24-hexadecimal digit string that identifies the log collection job to retry. Use the Get All Log Collection Jobs for One Project endpoint to obtain the IDs associated with your project.",
            serialization_alias="JOB-ID",
        )
        """Unique 24-hexadecimal digit string that identifies the log collection job to retry. Use the Get All Log Collection Jobs for One Project endpoint to obtain the IDs associated with your project.
        """

    class GetJobQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(None, serialization_alias="envelope")
        """Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set "envelope" : true in the query.

For endpoints that return one result, response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body

For endpoints that return a list of results, the results object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
        """Page number (1-index based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

        verbose: Optional[bool] = Field(False, serialization_alias="verbose")
        """If true, returns all child jobs in the response. A log collection job contains child jobs for each log type and MongoDB process included in the request.
        """

    def get_job(
        self,
        path_params: GetJobPathParams,
        query_params: Optional[GetJobQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Log Collection Job
        ### Document:
        [Get Job](https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-get-one/)
        ### Endpoint:
        `GET /groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}`
        ### Description
        When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to retrieve a single log collection job by its unique identifier.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}",
            path_params,
            query_params,
            None,
        )

    class RetryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the log collection request job.
        """

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique 24-hexadecimal digit string that identifies the log collection job to retry. Use the Get All Log Collection Jobs for One Project endpoint to obtain the IDs associated with your project.
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
        ## Retry a Failed Log Collection Job
        ### Document:
        [Retry](https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-retry/)
        ### Endpoint:
        `PUT /groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}/retry`
        ### Description
        When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to retry a single failed log collection job.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}/retry",
            path_params,
            query_params,
            None,
        )

    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the log collection request job.
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

        log_types: list[LogType] = Field(serialization_alias="logTypes")
        """Array of strings specifying the types of logs to collect. Each array element must be one of the following values:

AUTOMATION_AGENT

BACKUP_AGENT

MONITORING_AGENT

MONGODB

FTDC
        """

        redacted: bool = Field(serialization_alias="redacted")
        """If set to true, emails, hostnames, IP addresses, and namespaces in API responses involving this job are replaced with random string values.
        """

        resource_name: str = Field(serialization_alias="resourceName")
        """Name of the resource from which to collect logs. The resource type defines the value:

For the CLUSTER resourceType, the value is the name of the deployment or the CLUSTER-ID. For example, my-deployment.

To obtain this value, use the /groups/{GROUP-ID}/clusters/{CLUSTER-ID} endpoint.

For the PROCESS resourceType, the value is the name of the replica set followed by the node name. For example, Cluster0-shard-1-node-0.

To obtain this value, use the /groups/{PROJECT-ID}/automationConfig endpoint. The value is located in the processes.name parameter.

To obtain the name of the replica set, the list of nodes, and other information, access the cluster and run rs.conf()._id and rs.status().

For the REPLICASET resourceType, the value is the name of the replica set in the cluster followed by the shard name. For example, test-123abc-shard-0.
        """

        resource_type: ResourceType = Field(serialization_alias="resourceType")
        """Type of resource from which to collect logs. Must be one of the following values:

CLUSTER, for a sharded cluster.

PROCESS, for a node in the replica set.

REPLICASET, for a replica set.`
        """

        size_requested_per_file_bytes: int = Field(serialization_alias="sizeRequestedPerFileBytes")
        """Size for each log file in bytes.
        """

    def create(
        self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create a Log Collection Job
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-submit/)
        ### Endpoint:
        `POST /groups/{GROUP-ID}/logCollectionJobs`
        ### Description
        When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to create a new log collection job.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs",
            path_params,
            query_params,
            body_params,
        )

    class ExtendPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the log collection request job.
        """

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique 24-hexadecimal digit string that identifies the log collection job to retry. Use the Get All Log Collection Jobs for One Project endpoint to obtain the IDs associated with your project.
        """

    class ExtendQueryParams(BaseModel):
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

    class ExtendBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        expiration_date: str = Field(serialization_alias="expirationDate")
        """Timestamp, in the number of seconds that have elapsed since the UNIX epoch when this job expires. This can be up to 6 months from the time the job was created. You cannot specify a date which precedes the time the request is made.
        """

    def extend(
        self,
        path_params: ExtendPathParams,
        query_params: Optional[ExtendQueryParams],
        body_params: ExtendBodyParams,
    ) -> dict[str, Any]:
        """
        ## Extend a Log Collection Job
        ### Document:
        [Extend](https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-update-one/)
        ### Endpoint:
        `PATCH /groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}`
        ### Description
        When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Each job is created with a specified expiration date. Use this endpoint to extend the expiration date of an existing log collection job.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}",
            path_params,
            query_params,
            body_params,
        )
