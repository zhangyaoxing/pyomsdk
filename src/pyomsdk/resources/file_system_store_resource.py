"""Auto-generated client for FileSystemStoreResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class FileSystemStoreResource(BaseResource):
    """Client for FileSystemStoreResource resource."""

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

        assignment_enabled: Optional[bool] = Field(
            serialization_alias="assignmentEnabled"
        )
        """Flag that indicates whether this file system store can be assigned backup jobs.
        """

        id: str = Field(serialization_alias="id")
        """Unique identifier of this file system store.
        """

        labels: Optional[list[str]] = Field(serialization_alias="labels")
        """Tags to manage which backup jobs Ops Manager can assign to which file system stores.

Setting these tags limits which backup jobs this file system store can process. If omitted, this file system store can only process backup jobs for projects that do not use labels to filter their jobs.
        """

        load_factor: Optional[float] = Field(serialization_alias="loadFactor")
        """Positive, non-zero integer that expresses how much backup work this snapshot store should perform compared to another snapshot store. Set this option only if you're using more than one snapshot store.

To learn more about Load Factor, see Edit One Existing Blockstore.
        """

        mmapv1_compression_setting: Optional[str] = Field(
            serialization_alias="mmapv1CompressionSetting"
        )
        """Compression setting if you use the MMAPv1 storage engine for your snaphots.

Ops Manager accepts NONE or GZIP.

If the MongoDB runs FCV 4.2 or later, MongoDB Atlas ignores this setting.

IMPORTANT: MongoDB removed support for the MMAPv1 storage engine in MongoDB 4.2. If you edit your deployment's configuration to change your storage engine to WiredTiger Storage Engine, Ops Manager restarts the MongoDB processes.
        """

        store_path: str = Field(serialization_alias="storePath")
        """Location where file system-based backups are stored on the file system store host.
        """

        wt_compression_setting: Optional[str] = Field(
            serialization_alias="wtCompressionSetting"
        )
        """Compression setting if you use the WiredTiger storage engine for your snaphots.

Ops Manager accepts NONE or GZIP.

If the MongoDB runs FCV 4.2 or later, MongoDB Atlas ignores this setting.
        """

    def create(
        self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One File System Store Configuration
        - Document: [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/create-one-file-system-store-configuration/)
        - Resource: `POST /snapshot/fileSystemConfigs`
        - Description: Configures one new file system store.
        """
        return self._request(
            "POST",
            "/snapshot/fileSystemConfigs",
            None,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        file_system_config_id: str = Field(serialization_alias="FILE-SYSTEM-CONFIG-ID")
        """Unique identifier that labels this file system store configuration.
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
        ## Delete One File System Store Configuration
        - Document: [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/delete-one-file-system-store-configuration/)
        - Resource: `DELETE /snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}`
        - Description: Deletes the configuration of one file system store.
        """
        return self._request(
            "DELETE",
            "/snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        assignable_only: Optional[bool] = Field(
            True, serialization_alias="assignableOnly"
        )
        """Flag that indicates whether this file system store can be assigned new backup jobs.
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
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All File System Store Configurations
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/get-all-file-system-store-configurations/)
        - Resource: `GET /snapshot/fileSystemConfigs`
        - Description: Retrieves the configurations of all file system stores.
        """
        return self._request(
            "GET",
            "/snapshot/fileSystemConfigs",
            None,
            query_params,
            None,
        )

    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        file_system_config_id: str = Field(serialization_alias="FILE-SYSTEM-CONFIG-ID")
        """Unique name that labels this file system store configuration.
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
        ## Get One File System Store Configuration by ID
        - Document: [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/get-one-file-system-store-configuration-by-id/)
        - Resource: `GET /snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}`
        - Description: Retrieves the configuration of one file system store.
        """
        return self._request(
            "GET",
            "/snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        file_system_config_id: str = Field(serialization_alias="FILE-SYSTEM-CONFIG-ID")
        """Unique identifier that labels this file system store configuration.
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

        assignment_enabled: Optional[bool] = Field(
            serialization_alias="assignmentEnabled"
        )
        """Flag that indicates whether this file system store can be assigned backup jobs.
        """

        labels: Optional[list[str]] = Field(serialization_alias="labels")
        """Tags to manage which backup jobs Ops Manager can assign to which file system stores.

Setting these tags limits which backup jobs this file system store can process. If omitted, this file system store can only process backup jobs for projects that do not use labels to filter their jobs.
        """

        load_factor: Optional[float] = Field(serialization_alias="loadFactor")
        """Positive, non-zero integer that expresses how much backup work this snapshot store should perform compared to another snapshot store. Set this option only if you're using more than one snapshot store.

To learn more about Load Factor, see Edit One Existing Blockstore.
        """

        mmapv1_compression_setting: Optional[str] = Field(
            serialization_alias="mmapv1CompressionSetting"
        )
        """Compression setting if you use the MMAPv1 storage engine for your snaphots.

Ops Manager accepts NONE or GZIP. Ops Manager sets this value to NONE by default.

If the MongoDB runs FCV 4.2 or later, Ops Manager ignores this setting.

IMPORTANT: MongoDB removed support for the MMAPv1 storage engine in MongoDB 4.2. If you edit your deployment's configuration to change your storage engine to WiredTiger Storage Engine, Ops Manager restarts the MongoDB processes.
        """

        store_path: str = Field(serialization_alias="storePath")
        """Location where file system-based backups are stored on the file system store host.
        """

        wt_compression_setting: Optional[str] = Field(
            serialization_alias="wtCompressionSetting"
        )
        """Compression setting if you use the WiredTiger storage engine for your snaphots.

Ops Manager accepts NONE or GZIP. Ops Manager sets this value to GZIP by default.

If the MongoDB runs FCV 4.2 or later, Ops Manager ignores this setting.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One File System Store Configuration
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/update-one-file-system-store-configuration/)
        - Resource: `PUT /snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}`
        - Description: Updates the configuration of one file system store.
        """
        return self._request(
            "PUT",
            "/snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
