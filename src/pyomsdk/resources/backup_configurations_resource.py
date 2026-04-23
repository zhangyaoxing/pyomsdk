"""Auto-generated client for BackupConfigurationsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class BackupConfigurationsResource(BaseResource):
    """Client for BackupConfigurationsResource resource."""

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique 24-hexadecimal digit string that identifies the project to which the backup configuration applies.
        """

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
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Backup Configurations for One Project
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-all-backup-configs-for-group/)
        - Resource: `GET /groups/{PROJECT-ID}/backupConfigs`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/backupConfigs",
            path_params,
            query_params,
            None,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique 24-hexadecimal digit string that identifies the cluster whose backup configuration you want to find.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique 24-hexadecimal digit string that identifies the project that holds the cluster with the backup configuration you want to find.
        """

    class GetOneQueryParams(BaseModel):
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

    def get_one(
        self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Backup Configuration from One Project
        - Document: [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-one-backup-config-by-cluster-id/)
        - Resource: `GET /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="clusterId")
        """Unique 24-hexadecimal digit string that identifies the cluster whose backup configuration you want to change.
        """

        project_id: str = Field(serialization_alias="projectId")
        """Unique 24-hexadecimal digit string that identifies the project that holds the cluster with the backup configuration you want to change.
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

        auth_mechanism_name: Optional[AuthMechanismName] = Field(
            serialization_alias="authMechanismName"
        )
        """Authentication mechanism needed to connect to the sync source database. Ops Manager requires this parameter if the sync store uses authentication. Ops Manager accepts:

MONGODB_CR (This covers SCRAM-SHA-1, SCRAM-SHA-256, and MONGODB-CR.)

GSSAPI

PLAIN

MONGODB_X509

NONE
        """

        encryption_enabled: Optional[bool] = Field(
            serialization_alias="encryptionEnabled"
        )
        """Flag that indicates if encryption is enabled for the backup configuration. You must include the syncSource parameter when enabling encryption for a backup configuration. For existing backups in a project, enabling encryption requires an initial sync to recreate the backups’ head databases.

FCV 4.2 and later use backup cursors instead of head databases. For more information, see Backup Daemon Service.

For more information on backup encryption for FCV 4.2 or later, see Encrypted Backup Snapshots.
        """

        excluded_namespaces: Optional[list[str]] = Field(
            serialization_alias="excludedNamespaces"
        )
        """List of database and collection names to omit from the backup. Each string represents one namespace. Namespaces use one of the following formats:

{database}

{database}.{collection}.

Ops Manager accepts this parameter for backup jobs running MongoDB FCV 4.0 or earlier. Ops Manager ignores this parameter when backing up MongoDB databases running FCV 4.2 or later.

This parameter must meet the following conditions:

Ops Manager accepts either this parameter or includedNamespaces, not both.

Ops Manager requires the new full list of excluded namespaces, including any already found in the array.

If your new list removes any namespaces from the existing array, set the syncSource parameter.

Removing an excluded namespace requires a full resync.

Without the syncSource parameter, the request fails.

If your new list only adds to the existing array, don't set syncSource.
        """

        included_namespaces: Optional[list[str]] = Field(
            serialization_alias="includedNamespaces"
        )
        """List of database and collection names to include from the backup. Each string represents one namespace. Namespaces use one of the following formats:

{database}

{database}.{collection}.

Ops Manager accepts this parameter for backup jobs running MongoDB FCV 4.0 or earlier. Ops Manager ignores this parameter when backing up MongoDB databases running FCV 4.2 or later.

This parameter must meet the following conditions:

Ops Manager accepts either this parameter or excludedNamespaces, not both.

Ops Manager requires the new full list of included namespaces, including any already found in the array.

If the new list adds any namespaces from existing array, set the syncSource parameter.

Adding an included namespace requires a full resync.

Without the syncSource parameter, the request fails.

If the new list only removes namespaces from the existing array, don't set syncSource.
        """

        password: Optional[str] = Field(serialization_alias="password")
        """Password to use to connect to the sync source database. Ops Manager requires this parameter when the sync store mongod instances require clients to authenticate.
        """

        preferred_member: Optional[str] = Field(serialization_alias="preferredMember")
        """Cluster member that a user designates as the preferred replica set member to create snapshots. You can set the preferred member using the console. View available replica set members that can act as a preferred member using the Get one backup config endpoint.
        """

        provisioned: Optional[bool] = Field(serialization_alias="provisioned")
        """Flag that indicates if Ops Manager has provisioned the resources needed to store a backup.
        """

        class SnapshotstoreParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            snapshot_store_id: Optional[str] = Field(
                serialization_alias="snapshotStoreId"
            )
            """String that identifies the S3 blockstore to transition to. New snapshots will be stored in this destination S3 blockstore. Existing snapshots remain in the original store until they expire based on your configured retention policy. If you provide the snapshotStore object, you must specify both the snapshotStoreType and snapshotStoreId parameters.
            """

            snapshot_store_type: Optional[str] = Field(
                serialization_alias="snapshotStoreType"
            )
            """String that identifies the snapshot store type. Currently, only an S3 bucket (S3 blockstore) is supported. Value must be s3blockstore. If you provide the snapshotStore object, you must specify both the snapshotStoreType and snapshotStoreId parameters.
            """

        snapshot_store: Optional[SnapshotstoreParams] = Field(
            serialization_alias="snapshotStore"
        )
        """Object that specifies the snapshot store to transition to. This object contains the snapshot store type and the ID of the S3 bucket (S3 blockstore). Existing snapshots remain in the original store until they expire based on your configured retention policy. You can also transition between S3-compatible snapshot stores from the Jobs page.
        """

        ssl_enabled: Optional[bool] = Field(serialization_alias="sslEnabled")
        """Flag that indicates if TLS is enabled for the sync source database.
        """

        status_name: Optional[BackupStatusName] = Field(
            serialization_alias="statusName"
        )
        """Current (or desired) status of the backup configuration. Ops Manager accepts:

INACTIVE

PROVISIONING

STARTED

STOPPED

TERMINATING
        """

        storage_engine_name: Optional[StorageEngineName] = Field(
            serialization_alias="storageEngineName"
        )
        """Storage engine used for the backup. Ops Manager accepts:

MEMORY_MAPPED

WIRED_TIGER
        """

        sync_source: Optional[str] = Field(serialization_alias="syncSource")
        """mongod instance from which you retrieve backup data. Ops Manager accepts either a specific hostname or one of: PRIMARY and SECONDARY.

Ops Manager requires this parameter if "storageEngineName" : "WIRED_TIGER".
        """

        username: Optional[str] = Field(serialization_alias="username")
        """Name of the user to use to connect to the sync source database. Ops Manager requires this parameter when the sync store mongod instances require clients to authenticate.

Send this parameter to Ops Manager when updating the backup configuration for a replica set or sharded cluster that Ops Manager doesn't manage.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update One Backup Configuration
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/update-backup-config/)
        - Resource: `PATCH /groups/{projectId}/backupConfigs/{clusterId}`
        - Description: No description.
        """
        return self._request(
            "PATCH",
            "/groups/{projectId}/backupConfigs/{clusterId}",
            path_params,
            query_params,
            body_params,
        )
