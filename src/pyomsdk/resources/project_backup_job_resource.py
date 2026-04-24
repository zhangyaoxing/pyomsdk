"""Auto-generated client for ProjectBackupJobResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class ProjectBackupJobResource(BaseResource):
    """Client for ProjectBackupJobResource resource."""

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

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
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Project Backup Jobs Configurations
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/groups/get-all-backup-group-configurations/)
        ### Endpoint:
        `GET /groups`
        ### Description
        Retrieves the configurations of all project's backup jobs.
        """
        return self._request(
            "GET",
            "/groups",
            None,
            query_params,
            None,
        )

    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """The unique identifier that represents this project and its backup job configuration.
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
        ## Get One Project Backup Jobs Configuration by ID
        ### Document:
        [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/groups/get-one-backup-group-configuration-by-id/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}`
        ### Description
        Retrieves the configuration of one project's backup jobs.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """The unique identifier that represents this project and its backup job configuration.
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

        class DaemonfilterParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            head_root_directory: Optional[str] = Field(
                serialization_alias="headRootDirectory"
            )
            """Optional. The root-relative path of the head directory on this Backup Daemon host.
            """

            machine: Optional[str] = Field(serialization_alias="machine")
            """The host address for one Backup Daemon host.
            """

        daemon_filter: Optional[list[DaemonfilterParams]] = Field(
            serialization_alias="daemonFilter"
        )
        """Optional. An array of pairs of Backup Daemon hosts and their head directories that to which this project's backup jobs are limited. If omitted, all available Backup Daemons are used.
        """

        id: Optional[str] = Field(serialization_alias="id")
        """The unique identifier that represents this project and its backup job configuration.
        """

        kmip_client_cert_password: Optional[str] = Field(
            serialization_alias="kmipClientCertPassword"
        )
        """Optional. The password that encrypts the KMIP client certificate.
        """

        kmip_client_cert_path: Optional[str] = Field(
            serialization_alias="kmipClientCertPath"
        )
        """Optional. The root-relative path on the Backup Daemon host that stores the KMIP client certificate.
        """

        label_filter: Optional[list[str]] = Field(serialization_alias="labelFilter")
        """Optional. An array of tags that limits which Backup Daemons and snapshot stores can process backup jobs for this project.

If a snapshot store or any Backup Daemon has the same labels set as this labelFilter, they can process backup jobs for this project.

If omitted, the project's backup jobs can use any available Backup Daemon or snapshot store.
        """

        class OplogstorefilterParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            id: Optional[str] = Field(serialization_alias="id")
            """Unique identifier representing an oplog store that may be used with this project's backup jobs.

Retrieve the id of the oplog store you want to use with Get All Oplog Configurations.
            """

            type: Optional[OplogStoreFilterType] = Field(serialization_alias="type")
            """Type of oplog store to use.

The accepted values are:

oplogStore

s3OplogStore

thirdPartyOplogStore
            """

        oplog_store_filter: Optional[list[OplogstorefilterParams]] = Field(
            serialization_alias="oplogStoreFilter"
        )
        """Optional. An array of unique identifiers representing Oplog stores that may be used with this project's backup jobs. If omitted, all available oplog stores may be used.
        """

        class SnapshotstorefilterParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            id: Optional[str] = Field(serialization_alias="id")
            """Optional. The unique identifier representing specific snapshot stores that can be used with this project's backup jobs.
            """

            type: Optional[SnapshotStoreFilterType] = Field(serialization_alias="type")
            """Optional. The type of the specific snapshot store given as snapshotStoreFilter.id.

The accepted values for this option are:

s3blockstore

blockstore

fileSystemStore
            """

        snapshot_store_filter: Optional[list[SnapshotstorefilterParams]] = Field(
            serialization_alias="snapshotStoreFilter"
        )
        """Optional. Array of unique identifiers representing specific snapshot stores and their types that can be used with this project's backup jobs. If omitted, all available snapshot stores are used.
        """

        sync_store_filter: Optional[list[str]] = Field(
            serialization_alias="syncStoreFilter"
        )
        """Optional. An array of sync store filters that can be used with this project's backup jobs. If omitted, all available sync stores are used.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update One Project Backup Jobs Configuration
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/groups/update-one-backup-group-configuration/)
        ### Endpoint:
        `PUT /groups/{PROJECT-ID}`
        ### Description
        Updates the configuration of one project's backup jobs.
        """
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}",
            path_params,
            query_params,
            body_params,
        )
