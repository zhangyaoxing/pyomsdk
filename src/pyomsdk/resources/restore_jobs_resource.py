"""Auto-generated client for RestoreJobsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class RestoreJobsResource(BaseResource):
    """Client for RestoreJobsResource resource."""

    class CreateClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster that the job represents.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the job.
        """

    class CreateClusterQueryParams(BaseModel):
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

    def create_cluster(
        self,
        path_params: CreateClusterPathParams,
        query_params: Optional[CreateClusterQueryParams],
    ) -> dict[str, Any]:
        """
        ## Create One Restore Job for One Cluster
        ### Document:
        [Create (Cluster)](https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/create-one-restore-job-for-one-cluster/)
        ### Endpoint:
        `POST /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs",
            path_params,
            query_params,
            None,
        )

    class CreateConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """Unique identifier of the mirrored config server (SCCC) that the job represents.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the job.
        """

    class CreateConfigServerQueryParams(BaseModel):
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

    class CreateConfigServerBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        checkpoint_id: Optional[str] = Field(None, serialization_alias="checkpointId")
        """Unique identifier for the sharded cluster checkpoint that represents the point in time to which your data will be restored.

Conditions include:

Set "delivery.methodName" : "AUTOMATED_RESTORE".

Can't set oplogInc, oplogTs, or pointInTimeUTCMillis.

If you provide this setting, this endpoint restores all data up to this checkpoint to the database you specified in the delivery object.
        """

        class DeliveryParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            expiration_hours: Optional[float] = Field(None, serialization_alias="expirationHours")
            """Number of hours the download URL is valid once the restore job is complete.

delivery.methodName" : "HTTP"
            """

            expires: Optional[str] = Field(None, serialization_alias="expires")
            """Timestamp in ISO 8601 date and time format in UTC after which the URL is no longer available.

delivery.methodName" : "HTTP"
            """

            max_downloads: Optional[float] = Field(None, serialization_alias="maxDownloads")
            """Number of times the download URL can be used. This must be 1 or greater.

delivery.methodName" : "HTTP"
            """

            method_name: DeliveryMethodName = Field(serialization_alias="methodName")
            """Means by which Ops Manager delivers the data. Accepted values are:

AUTOMATED_RESTORE

HTTP

If you set "delivery.methodName" : "AUTOMATED_RESTORE", you must also set:

delivery.targetGroupId and

delivery.targetClusterId

In addition, the response shows the delivery.methodName as HTTP. An automated restore uses the HTTP method to deliver the restore job to the target host.

IMPORTANT: Restore delivery using SCP was removed in Ops Manager 4.0.
            """

            target_cluster_id: Optional[str] = Field(None, serialization_alias="targetClusterId")
            """Unique identifier of the target cluster. Use the clusterId returned in the response body of the Get All Snapshots and Get a Snapshot endpoints.

delivery.methodName" : "AUTOMATED_RESTORE".

If backup is not enabled on the target cluster, the Get All Snapshots endpoint returns an empty results array without clusterId elements, and the Get a Snapshot endpoint also does not return a clusterId element.
            """

            target_group_id: Optional[str] = Field(None, serialization_alias="targetGroupId")
            """Unique identifier of the project that contains the destination cluster for the restore job.

delivery.methodName" : "AUTOMATED_RESTORE"
            """

        delivery: DeliveryParams = Field(serialization_alias="delivery")
        """Method and details of how the restored snapshot data is delivered.
        """

        oplog_inc: Optional[str] = Field(None, serialization_alias="oplogInc")
        """32-bit incrementing ordinal that represents operations within a given second. When paired with oplogTs, they represent the point in time to which your data will be restored.

"delivery.methodName" : "AUTOMATED_RESTORE" for Replica Sets Only.

If you set oplogInc, you:

Must set oplogTs.

Cannot set checkpointId or pointInTimeUTCMillis.

If you provide this setting, this endpoint restores all data up to and including this Oplog timestamp to the database you specified in the delivery object.
        """

        oplog_ts: Optional[str] = Field(None, serialization_alias="oplogTs")
        """Oplog timestamp given as a Timestamp in the number of seconds that have elapsed since the UNIX epoch. When paired with oplogInc, they represent the point in time to which your data will be restored.

Run a query against local.oplog.rs on your replica set to find the desired timestamp.

"delivery.methodName" : "AUTOMATED_RESTORE" for Replica Sets Only.

If you set oplogTs, you:

Must set oplogInc.

Cannot set checkpointId or pointInTimeUTCMillis.

If you provide this setting, this endpoint restores all data up to and including this Oplog timestamp to the database you specified in the delivery object.
        """

        point_in_time_utc_millis: Optional[int] = Field(
            None, serialization_alias="pointInTimeUTCMillis"
        )
        """timestamp in the number of milliseconds that have elapsed since the UNIX epoch that represents the point in time to which your data will be restored. This timestamp must be within last 24 hours of the current time.

If you provide this setting, this endpoint restores all data up to this Point in Time to the database you specified in the delivery object.

"delivery.methodName" : "AUTOMATED_RESTORE" for Replica Sets Only.

If you set pointInTimeUTCMillis, you cannot set oplogInc, oplogTs, or checkpointId.
        """

        snapshot_id: Optional[str] = Field(None, serialization_alias="snapshotId")
        """Unique identifier of the snapshot to restore.
        """

    def create_config_server(
        self,
        path_params: CreateConfigServerPathParams,
        query_params: Optional[CreateConfigServerQueryParams],
        body_params: CreateConfigServerBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Restore Job for One Legacy Mirrored Config Server
        ### Document:
        [Create (Config Server)](https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/create-one-restore-job-for-one-sccc-config-server/)
        ### Endpoint:
        `POST /groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs",
            path_params,
            query_params,
            body_params,
        )

    class GetAllClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster that the snapshot represents.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the snapshot.
        """

    class GetAllClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        batch_id: Optional[str] = Field(None, serialization_alias="BATCH-ID")
        """Unique identifier of the batch.
        """

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag that indicates whether the response body should be in a prettyprint format.
        """

    def get_all_cluster(
        self,
        path_params: GetAllClusterPathParams,
        query_params: Optional[GetAllClusterQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Restore Jobs for One Cluster
        ### Document:
        [Get All (Cluster)](https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-all-restore-jobs-for-one-cluster/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs`
        ### Description
        Get all restore jobs for a cluster. CLUSTER-ID must be the ID of either a replica set or a sharded cluster.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs",
            path_params,
            query_params,
            None,
        )

    class GetAllConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """Unique identifier of the host that the job represents.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the job.
        """

    class GetAllConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag that indicates whether the response body should be in a prettyprint format.
        """

    def get_all_config_server(
        self,
        path_params: GetAllConfigServerPathParams,
        query_params: Optional[GetAllConfigServerQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Restore Jobs for One Legacy Mirrored Config Server
        ### Document:
        [Get All (Config Server)](https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-all-restore-jobs-for-one-sccc-config-server/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs",
            path_params,
            query_params,
            None,
        )

    class GetOneClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster that the restore job represents.
        """

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique identifier of the restore job.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the restore job.
        """

    class GetOneClusterQueryParams(BaseModel):
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

    def get_one_cluster(
        self,
        path_params: GetOneClusterPathParams,
        query_params: Optional[GetOneClusterQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Restore Job for One Cluster
        ### Document:
        [Get One (Cluster)](https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-one-single-restore-job-for-one-cluster/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs/{JOB-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs/{JOB-ID}",
            path_params,
            query_params,
            None,
        )

    class GetOneConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """Unique identifier of the mirrored config server (SCCC) that the restore job represents.
        """

        job_id: str = Field(serialization_alias="JOB-ID")
        """Unique identifier of the restore job.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the restore job.
        """

    class GetOneConfigServerQueryParams(BaseModel):
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

    def get_one_config_server(
        self,
        path_params: GetOneConfigServerPathParams,
        query_params: Optional[GetOneConfigServerQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Restore Job for One Legacy Mirrored Config Server
        ### Document:
        [Get One (Config Server)](https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-one-single-restore-job-for-one-sccc-config-server/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs/{JOB-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs/{JOB-ID}",
            path_params,
            query_params,
            None,
        )
