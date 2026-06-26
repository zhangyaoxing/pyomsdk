r"""Auto-generated client for ProjectBackupJobResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class ProjectBackupJobResource(BaseResource):
    r"""Client for ProjectBackupJobResource resource."""

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `envelope : true` in the
query.

For endpoints that return a list of results, the `content`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag that indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_all(
        self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        r"""
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
            "/api/public/v1.0/admin/backup/groups",
            None,
            query_params,
            None,
        )

    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""The unique identifier that represents this project and its backup
job configuration.
        """

    class GetByIdQueryParams(BaseModel):
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

    def get_by_id(
        self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
    ) -> dict[str, Any]:
        r"""
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
            "/api/public/v1.0/admin/backup/groups/{PROJECT-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""The unique identifier that represents this project and its
backup job configuration.
        """

    class UpdateQueryParams(BaseModel):
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

    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        class DaemonFilterParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            head_root_directory: Optional[str] = Field(
                default=None, serialization_alias="headRootDirectory"
            )
            r"""*Optional.* The root-relative path of the [head directory](/docs/ops-manager/current/reference/glossary/#std-term-head-directory)
on this [Backup Daemon](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-daemon) host.
            """

            machine: Optional[str] = Field(default=None, serialization_alias="machine")
            r"""The host address for one [Backup Daemon](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-daemon) host.
            """

        daemon_filter: Optional[list[DaemonFilterParams]] = Field(
            default=None, serialization_alias="daemonFilter"
        )
        r"""*Optional.* An array of pairs of [Backup Daemon](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-daemon) hosts and
their [head directories](/docs/ops-manager/current/reference/glossary/#std-term-head-directory) that to which
this project's backup jobs are limited. If omitted, all available
Backup Daemons are used.
        """

        id: Optional[str] = Field(default=None, serialization_alias="id")
        r"""The unique identifier that represents this project and its
backup job configuration.
        """

        kmip_client_cert_password: Optional[str] = Field(
            default=None, serialization_alias="kmipClientCertPassword"
        )
        r"""*Optional.* The password that encrypts the
KMIP
client certificate.
        """

        kmip_client_cert_path: Optional[str] = Field(
            default=None, serialization_alias="kmipClientCertPath"
        )
        r"""*Optional.* The root-relative path on the [Backup Daemon](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-daemon)
host that stores the
KMIP
client certificate.
        """

        label_filter: Optional[list[str]] = Field(default=None, serialization_alias="labelFilter")
        r"""*Optional.* An array of tags that limits which
[Backup Daemons](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-Backup-Daemon) and
[snapshot stores](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-snapshot-store) can process
[backup jobs](/docs/ops-manager/current/reference/glossary/#std-term-backup-job) for this project.

If a snapshot store or any Backup Daemon has the same `labels`
set as this `labelFilter`, they can process backup jobs for
this project.

If omitted, the project's backup jobs can use any available
Backup Daemon or snapshot store.
        """

        class OplogStoreFilterParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            id: Optional[str] = Field(default=None, serialization_alias="id")
            r"""Unique identifier representing an
[oplog store](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-Oplog-Store-Database) that may be used
with this project's backup jobs.

Retrieve the `id` of the oplog store you want to use with
[Get All Oplog Configurations.](/docs/ops-manager/current/reference/api/admin/backup/oplog/mongoConfigs/get-all-oplog-configurations/#std-label-get-all-oplog-configs-response)
            """

            type: Optional[OplogStoreFilterType] = Field(default=None, serialization_alias="type")
            r"""Type of [oplog store](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-Oplog-Store-Database) to use.

The accepted values are:

- `oplogStore`
- `s3OplogStore`
- `thirdPartyOplogStore`
            """

        oplog_store_filter: Optional[list[OplogStoreFilterParams]] = Field(
            default=None, serialization_alias="oplogStoreFilter"
        )
        r"""*Optional.* An array of unique identifiers representing
[Oplog stores](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-Oplog-Store-Database) that may
be used with this project's backup jobs. If omitted, all
available oplog stores may be used.
        """

        class SnapshotStoreFilterParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            id: Optional[str] = Field(default=None, serialization_alias="id")
            r"""*Optional.* The unique identifier representing specific
[snapshot stores](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-snapshot-store) that can be
used with this project's backup jobs.
            """

            type: Optional[SnapshotStoreFilterType] = Field(
                default=None, serialization_alias="type"
            )
            r"""*Optional.* The type of the specific snapshot store given as
`snapshotStoreFilter.id`.

The accepted values for this option are:

- `s3blockstore`
- `blockstore`
- `fileSystemStore`
            """

        snapshot_store_filter: Optional[list[SnapshotStoreFilterParams]] = Field(
            default=None, serialization_alias="snapshotStoreFilter"
        )
        r"""*Optional.* Array of unique identifiers representing specific
[snapshot stores](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-snapshot-store) and their types that can
be used with this project's backup jobs. If omitted, all
available snapshot stores are used.
        """

        sync_store_filter: Optional[list[str]] = Field(
            default=None, serialization_alias="syncStoreFilter"
        )
        r"""*Optional.* An array of sync store filters that can be used with
this project's backup jobs. If omitted, all available sync stores
are used.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        r"""
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
            "/api/public/v1.0/admin/backup/groups/{PROJECT-ID}",
            path_params,
            query_params,
            body_params,
        )
