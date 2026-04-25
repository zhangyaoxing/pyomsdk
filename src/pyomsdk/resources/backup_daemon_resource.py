"""Auto-generated client for BackupDaemonResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class BackupDaemonResource(BaseResource):
    """Client for BackupDaemonResource resource."""

    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        machine: str = Field(serialization_alias="MACHINE")
        """Hostname or IP address of the machine that serves the Backup Daemon.
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

        assignment_enabled: Optional[bool] = Field(None, serialization_alias="assignmentEnabled")
        """Flag indicating whether this Backup Daemon can be assigned backup jobs.
        """

        backup_jobs_enabled: Optional[bool] = Field(None, serialization_alias="backupJobsEnabled")
        """Flag indicating whether this Backup Daemon can be used to backup databases.
        """

        configured: Optional[bool] = Field(None, serialization_alias="configured")
        """Flag indicating whether this Backup Daemon is ready to use.
        """

        garbage_collection_enabled: Optional[bool] = Field(
            None, serialization_alias="garbageCollectionEnabled"
        )
        """Flag indicating whether this Backup Daemon has garbage collection set.
        """

        head_disk_type: Optional[HeadDiskType] = Field(None, serialization_alias="headDiskType")
        """Type of disk used to store the head directory.

The accepted values for this option are:

HDD

SSD
        """

        labels: Optional[list[str]] = Field(None, serialization_alias="labels")
        """Array of tags to manage which backup jobs Ops Manager can assign to which Backup Daemons.

Setting these tags limits which backup jobs this Backup Daemon can process. If omitted, this Backup Daemon can only process backup jobs for projects that do not use labels to filter their jobs.
        """

        class MachineParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            head_root_directory: Optional[str] = Field(
                None, serialization_alias="headRootDirectory"
            )
            """Root-relative path of the head directory on this Backup Daemon host. This directory must end with a slash (/). If you omit the slash, the Backup Daemon generates a Java Exception error.
            """

            machine: str = Field(serialization_alias="machine")
            """Hostname or IP address of the Backup Daemon host.
            """

        machine: MachineParams = Field(serialization_alias="machine")
        """Backup Daemon host and its head directories.
        """

        num_workers: Optional[int] = Field(None, serialization_alias="numWorkers")
        """Number of worker processes that can perform tasks (i.e. backup, restore, or groom) for the Backup Daemon.
        """

        resource_usage_enabled: Optional[bool] = Field(
            None, serialization_alias="resourceUsageEnabled"
        )
        """Flag indicating whether this Backup Daemon has its resource usage monitored.
        """

        restore_queryable_jobs_enabled: Optional[bool] = Field(
            None, serialization_alias="restoreQueryableJobsEnabled"
        )
        """Flag indicating whether this Backup Daemon can perform queryable restores.
        """

    def create(
        self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Backup Daemon Configuration
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/create-one-backup-daemon-configuration/)
        ### Endpoint:
        `PUT /daemon/configs/{MACHINE}`
        ### Description
        Configures a new Backup Daemon.
        """
        return self._request(
            "PUT",
            "/daemon/configs/{MACHINE}",
            path_params,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        head_root_directory: str = Field(serialization_alias="HEAD-ROOT-DIRECTORY")
        """Root-relative URL-encoded path of the head directory on this Backup Daemon host. May be omitted if the Backup Daemon has not been configured.
        """

        machine: str = Field(serialization_alias="MACHINE")
        """Hostname or IP address of the machine that serves the Backup Daemon.
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
        ## Delete One Backup Daemon Configuration
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/delete-one-backup-daemon-configuration/)
        ### Endpoint:
        `DELETE /daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}`
        ### Description
        Deletes the configuration of one backup daemon.
        """
        return self._request(
            "DELETE",
            "/daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}",
            path_params,
            query_params,
            None,
        )

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        backup_jobs_enabled_only: Optional[bool] = Field(
            True, serialization_alias="backupJobsEnabledOnly"
        )
        """Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to false to include daemon configurations with the backupJobsEnabled flag set to false.
        """

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the results object is an envelope. Ops Manager adds the status field to the response body.
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

    def get_all(
        self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Backup Daemon Configurations
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/get-all-backup-daemon-configurations/)
        ### Endpoint:
        `GET /daemon/configs`
        ### Description
        Retrieves the configurations of all backup daemons.
        """
        return self._request(
            "GET",
            "/daemon/configs",
            None,
            query_params,
            None,
        )

    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        head_root_directory: str = Field(serialization_alias="HEAD-ROOT-DIRECTORY")
        """Root-relative URL-encoded path of the head directory on this Backup Daemon host. May be omitted if the Backup Daemon has not been configured.
        """

        machine: str = Field(serialization_alias="MACHINE")
        """Hostname or IP address of the machine that serves the Backup Daemon.
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
        ## Get One Backup Daemon Configuration by ID
        ### Document:
        [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/get-one-backup-daemon-configuration-by-host/)
        ### Endpoint:
        `GET /daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}`
        ### Description
        Retrieves the configuration of one backup daemon.
        """
        return self._request(
            "GET",
            "/daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        head_root_directory: str = Field(serialization_alias="HEAD-ROOT-DIRECTORY")
        """Root-relative URL-encoded path of the head directory on this Backup Daemon host.

Requests encode slashes in the URL path. For example, for Linux platforms, you should add the head directory in this format:

http://localhost:8080/api/public/v1.0/admin/backup/
daemon/config/localhost/%2Fdata%2Fbackup%2F
        """

        machine: str = Field(serialization_alias="MACHINE")
        """Hostname or IP address of the machine that serves the Backup Daemon.
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

        assignment_enabled: Optional[bool] = Field(None, serialization_alias="assignmentEnabled")
        """Flag indicating whether this Backup Daemon can be assigned backup jobs.
        """

        backup_jobs_enabled: Optional[bool] = Field(None, serialization_alias="backupJobsEnabled")
        """Flag indicating whether this Backup Daemon can be used to backup databases.
        """

        configured: Optional[bool] = Field(None, serialization_alias="configured")
        """Flag indicating whether this Backup Daemon is ready to use.
        """

        garbage_collection_enabled: Optional[bool] = Field(
            None, serialization_alias="garbageCollectionEnabled"
        )
        """Flag indicating whether this Backup Daemon has garbage collection set.
        """

        head_disk_type: Optional[HeadDiskType] = Field(None, serialization_alias="headDiskType")
        """Type of disk used to store the head directory.

The accepted values for this option are:

HDD

SSD
        """

        labels: Optional[list[str]] = Field(None, serialization_alias="labels")
        """Array of tags to manage which backup jobs Ops Manager can assign to which Backup Daemons.

Setting these tags limits which backup jobs this Backup Daemon can process. If omitted, this Backup Daemon can only process backup jobs for projects that do not use labels to filter their jobs.
        """

        class MachineParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            head_root_directory: Optional[str] = Field(
                None, serialization_alias="headRootDirectory"
            )
            """Root-relative path of the head directory on this Backup Daemon host. This directory must end with a slash (/). If you omit the slash, the Backup Daemon generates a Java Exception error.
            """

            machine: str = Field(serialization_alias="machine")
            """Hostname or IP address of the Backup Daemon host.
            """

        machine: MachineParams = Field(serialization_alias="machine")
        """Backup Daemon host and its head directories.
        """

        num_workers: Optional[int] = Field(None, serialization_alias="numWorkers")
        """Number of worker processes that can perform tasks (i.e. backup, restore, or groom) for the Backup Daemon.
        """

        resource_usage_enabled: Optional[bool] = Field(
            None, serialization_alias="resourceUsageEnabled"
        )
        """Flag indicating whether this Backup Daemon has its resource usage monitored.
        """

        restore_queryable_jobs_enabled: Optional[bool] = Field(
            None, serialization_alias="restoreQueryableJobsEnabled"
        )
        """Flag indicating whether this Backup Daemon can perform queryable restores.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Backup Daemon Configuration
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/update-one-backup-daemon-configuration/)
        ### Endpoint:
        `PUT /daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}`
        ### Description
        Updates the configuration of one Backup Daemon.
        """
        return self._request(
            "PUT",
            "/daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}",
            path_params,
            query_params,
            body_params,
        )
