"""Auto-generated client for SyncStoreResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class SyncStoreResource(BaseResource):
    """Client for SyncStoreResource resource."""

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
        """Optional. Flag indicating whether this sync store can be assigned backup jobs.
        """

        encrypted_credentials: Optional[bool] = Field(
            None, serialization_alias="encryptedCredentials"
        )
        """Optional. Flag indicating whether the username and password for this sync store were encrypted using the credentialstool.
        """

        id: Optional[str] = Field(None, serialization_alias="id")
        """The unique name that labels this sync store.
        """

        labels: Optional[list[str]] = Field(None, serialization_alias="labels")
        """Optional. Array of tags to manage which backup jobs Ops Manager can assign to which sync stores.

Setting these tags limits which backup jobs this sync store can process. If omitted, this sync store can only process backup jobs for projects that do not use labels to filter their jobs.
        """

        max_capacity_gb: Optional[int] = Field(None, serialization_alias="maxCapacityGB")
        """Optional. The sync store’s expected maximum available capacity for use in the OUTSIDE_SPACE_USED_THRESHOLD alert. maxCapacityGB does not enforce any limitation on the size of the backing database.
        """

        ssl: Optional[bool] = Field(None, serialization_alias="ssl")
        """Optional. Flag indicating whether this sync store only accepts connections encrypted using TLS.
        """

        uri: Optional[str] = Field(None, serialization_alias="uri")
        """A comma-separated list of hosts in the <hostname:port> format that can be used to access this sync store.
        """

        write_concern: Optional[WriteConcern] = Field(None, serialization_alias="writeConcern")
        """Optional. The write concern used for this sync store.

The accepted values for this option are:

ACKNOWLEDGED

W2

JOURNALED

MAJORITY

To learn about write acknowledgement levels in MongoDB, see Write Concern.
        """

    def create(
        self,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Create One Sync Store Configuration
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoConfigs/create-one-sync-store-configuration/)
        ### Endpoint:
        `POST /sync/mongoConfigs`
        ### Description
        Configures one new sync store.
        """
        return self._request(
            "POST",
            "/sync/mongoConfigs",
            None,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        sync_store_config_id: str = Field(serialization_alias="SYNC-STORE-CONFIG-ID")
        """Unique identifier of this Sync Store configuration.
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
        ## Delete One Sync Store Configuration
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoConfigs/delete-one-sync-store-configuration/)
        ### Endpoint:
        `DELETE /sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}`
        ### Description
        Deletes the configuration of one sync store.
        """
        return self._request(
            "DELETE",
            "/sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        assignable_only: Optional[bool] = Field(True, serialization_alias="assignableOnly")
        """Indicates whether this sync store can be assigned new backup jobs.
        """

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

    def get_all(
        self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Sync Store Configurations
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoConfigs/get-all-sync-store-configurations/)
        ### Endpoint:
        `GET /sync/mongoConfigs`
        ### Description
        Retrieves the configurations of all sync stores.
        """
        return self._request(
            "GET",
            "/sync/mongoConfigs",
            None,
            query_params,
            None,
        )

    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        sync_store_config_id: str = Field(serialization_alias="SYNC-STORE-CONFIG-ID")
        """The unique identifier that represents this Oplog configuration.
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
        ## Get One Sync Store Configuration by ID
        ### Document:
        [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoConfigs/get-one-sync-store-configuration-by-id/)
        ### Endpoint:
        `GET /sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}`
        ### Description
        Retrieves the configuration of one sync store.
        """
        return self._request(
            "GET",
            "/sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        sync_store_config_id: str = Field(serialization_alias="SYNC-STORE-CONFIG-ID")
        """Unique identifier for this Sync Store configuration.
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
        """Optional. Flag indicating whether this sync store can be assigned backup jobs.
        """

        encrypted_credentials: Optional[bool] = Field(
            None, serialization_alias="encryptedCredentials"
        )
        """Optional. Flag indicating whether the username and password for this sync store were encrypted using the credentialstool.
        """

        labels: Optional[list[str]] = Field(None, serialization_alias="labels")
        """Optional. Array of tags to manage which backup jobs Ops Manager can assign to which sync stores.

Setting these tags limits which backup jobs this sync store can process. If omitted, this sync store can only process backup jobs for projects that do not use labels to filter their jobs.
        """

        max_capacity_gb: Optional[int] = Field(None, serialization_alias="maxCapacityGB")
        """Optional. The sync store’s expected maximum available capacity for use in the OUTSIDE_SPACE_USED_THRESHOLD alert. maxCapacityGB does not enforce any limitation on the size of the backing database.
        """

        ssl: Optional[bool] = Field(None, serialization_alias="ssl")
        """Optional. Flag indicating whether this sync store only accepts connections encrypted using TLS.
        """

        uri: Optional[str] = Field(None, serialization_alias="uri")
        """A comma-separated list of hosts in the <hostname:port> format that can be used to access this sync store.
        """

        write_concern: Optional[WriteConcern] = Field(None, serialization_alias="writeConcern")
        """Optional. The write concern used for this sync store.

The accepted values for this option are:

ACKNOWLEDGED

W2

JOURNALED

MAJORITY

To learn about write acknowledgement levels in MongoDB, see Write Concern.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update One Sync Store Configuration
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoConfigs/update-one-sync-store-configuration/)
        ### Endpoint:
        `PUT /sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}`
        ### Description
        Updates the configuration of one sync store.
        """
        return self._request(
            "PUT",
            "/sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
