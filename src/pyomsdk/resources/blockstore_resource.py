"""Auto-generated client for BlockstoreResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class BlockstoreResource(BaseResource):
    """Client for BlockstoreResource resource."""

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
        """Optional. Flag indicating whether this blockstore can be assigned backup jobs.
        """

        encrypted_credentials: Optional[bool] = Field(
            None, serialization_alias="encryptedCredentials"
        )
        """Optional. Flag indicating whether the username and password for this blockstore were encrypted using the credentialstool.
        """

        id: Optional[str] = Field(None, serialization_alias="id")
        """The unique name that labels this blockstore.
        """

        labels: Optional[list[str]] = Field(None, serialization_alias="labels")
        """Optional. Array of tags to manage which backup jobs Ops Manager can assign to which blockstores.

Setting these tags limits which backup jobs this blockstore can process. If omitted, this blockstore can only process backup jobs for projects that do not use labels to filter their jobs.
        """

        load_factor: Optional[int] = Field(None, serialization_alias="loadFactor")
        """Optional. A positive, non-zero integer that expresses how much backup work this snapshot store should perform compared to another snapshot store. This option is needed only if more than one snapshot store is in use.

To learn more about Load Factor, see Edit One Existing Blockstore.
        """

        max_capacity_gb: Optional[int] = Field(None, serialization_alias="maxCapacityGB")
        """Optional. The blockstore’s expected maximum available capacity for use in the OUTSIDE_SPACE_USED_THRESHOLD alert. maxCapacityGB does not enforce any limitation on the size of the backing database.
        """

        ssl: Optional[bool] = Field(None, serialization_alias="ssl")
        """Optional. Flag indicating whether this blockstore only accepts connections encrypted using TLS.
        """

        uri: Optional[str] = Field(None, serialization_alias="uri")
        """A comma-separated list of hosts in the <hostname:port> format that can be used to access this blockstore.
        """

        write_concern: Optional[WriteConcern] = Field(None, serialization_alias="writeConcern")
        """Optional. The write concern used for this blockstore.

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
        ## Create One Blockstore Configuration
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/create-one-blockstore-configuration/)
        ### Endpoint:
        `POST /snapshot/mongoConfigs`
        ### Description
        Configures one new blockstore.
        """
        return self._request(
            "POST",
            "/snapshot/mongoConfigs",
            None,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        blockstore_id: str = Field(serialization_alias="BLOCKSTORE-ID")
        """Unique name that labels this blockstore configuration.
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
        ## Delete One Blockstore Configuration
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/delete-one-blockstore-configuration/)
        ### Endpoint:
        `DELETE /snapshot/mongoConfigs/{BLOCKSTORE-ID}`
        ### Description
        Deletes the configuration of one blockstore.
        """
        return self._request(
            "DELETE",
            "/snapshot/mongoConfigs/{BLOCKSTORE-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        assignable_only: Optional[bool] = Field(True, serialization_alias="assignableOnly")
        """Indicates whether this blockstore can be assigned new backup jobs.
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
        ## Get All Blockstore Configurations
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/get-all-blockstore-configurations/)
        ### Endpoint:
        `GET /snapshot/mongoConfigs`
        ### Description
        Retrieves the configurations of all blockstores.
        """
        return self._request(
            "GET",
            "/snapshot/mongoConfigs",
            None,
            query_params,
            None,
        )

    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        blockstore_id: str = Field(serialization_alias="BLOCKSTORE-ID")
        """The unique name that labels this blockstore configuration.
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
        ## Get One Blockstore Configuration by ID
        ### Document:
        [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/get-one-blockstore-configuration-by-id/)
        ### Endpoint:
        `GET /snapshot/mongoConfigs/{BLOCKSTORE-ID}`
        ### Description
        Retrieves the configuration of one blockstore.
        """
        return self._request(
            "GET",
            "/snapshot/mongoConfigs/{BLOCKSTORE-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        blockstore_id: str = Field(serialization_alias="BLOCKSTORE-ID")
        """The unique name that labels this blockstore configuration.
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
        """Optional. Flag indicating whether this blockstore can be assigned backup jobs.
        """

        encrypted_credentials: Optional[bool] = Field(
            None, serialization_alias="encryptedCredentials"
        )
        """Optional. Flag indicating whether the username and password for this blockstore were encrypted using the credentialstool.
        """

        labels: Optional[list[str]] = Field(None, serialization_alias="labels")
        """Optional. Array of tags to manage which backup jobs Ops Manager can assign to which blockstores.

Setting these tags limits which backup jobs this blockstore can process. If omitted, this blockstore can only process backup jobs for projects that do not use labels to filter their jobs.
        """

        load_factor: Optional[int] = Field(None, serialization_alias="loadFactor")
        """Optional. A positive, non-zero integer that expresses how much backup work this snapshot store should perform compared to another snapshot store. This option is needed only if more than one snapshot store is in use.

To learn more about Load Factor, see Edit One Existing Blockstore.
        """

        max_capacity_gb: Optional[int] = Field(None, serialization_alias="maxCapacityGB")
        """Optional. The blockstore’s expected maximum available capacity for use in the OUTSIDE_SPACE_USED_THRESHOLD alert. maxCapacityGB does not enforce any limitation on the size of the backing database.
        """

        ssl: Optional[bool] = Field(None, serialization_alias="ssl")
        """Optional. Flag indicating whether this blockstore only accepts connections encrypted using TLS.
        """

        uri: Optional[str] = Field(None, serialization_alias="uri")
        """A comma-separated list of hosts in the <hostname:port> format that can be used to access this blockstore.
        """

        write_concern: Optional[WriteConcern] = Field(None, serialization_alias="writeConcern")
        """Optional. The write concern used for this blockstore.

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
        ## Update One Blockstore Configuration
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/update-one-blockstore-configuration/)
        ### Endpoint:
        `PUT /snapshot/mongoConfigs/{BLOCKSTORE-ID}`
        ### Description
        Updates the configuration of one blockstore.
        """
        return self._request(
            "PUT",
            "/snapshot/mongoConfigs/{BLOCKSTORE-ID}",
            path_params,
            query_params,
            body_params,
        )
