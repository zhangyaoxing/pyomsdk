
r"""Auto-generated client for BlockstoreResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *

class BlockstoreResource(BaseResource):
    r"""Client for BlockstoreResource resource.
    """
    
    
    
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set **envelope=true** in the query.

For endpoints that return one result, the response body includes:

- `status`: HTTP response code
- `content`: Expected response body
        """
        
        
        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body is in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """
        
    
    
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        assignment_enabled: Optional[bool] = Field(default=None, serialization_alias="assignmentEnabled")
        r"""*Optional.* Flag indicating whether this [blockstore](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-blockstore-database) can be assigned backup jobs.
        """
        
        
        encrypted_credentials: Optional[bool] = Field(default=None, serialization_alias="encryptedCredentials")
        r"""*Optional.* Flag indicating whether the username and password for this blockstore were encrypted using the [credentialstool.](/docs/ops-manager/v8.0/tutorial/encrypt-user-credentials/)
        """
        
        
        id: Optional[str] = Field(default=None, serialization_alias="id")
        r"""The unique name that labels this [blockstore.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-blockstore-database)
        """
        
        
        labels: Optional[list[str]] = Field(default=None, serialization_alias="labels")
        r"""*Optional.* Array of tags to manage which [backup jobs](/docs/ops-manager/v8.0/reference/glossary/#std-term-backup-job) Ops Manager can assign to which [blockstores.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-blockstore-database)

Setting these tags limits which backup jobs this blockstore can process. If omitted, this blockstore can only process backup jobs for projects that do not use labels to filter their jobs.
        """
        
        
        load_factor: Optional[int] = Field(default=None, serialization_alias="loadFactor")
        r"""*Optional.* A positive, non-zero integer that expresses how much backup work this [snapshot store](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-snapshot-store) should perform compared to another snapshot store. This option is needed only if more than one snapshot store is in use.

To learn more about Load Factor, see [Edit One Existing Blockstore.](/docs/ops-manager/v8.0/tutorial/manage-blockstore-storage/#std-label-edit-blockstore)
        """
        
        
        max_capacity_gb: Optional[int] = Field(default=None, serialization_alias="maxCapacityGB")
        r"""*Optional.* The blockstore’s expected maximum available capacity for use in the [OUTSIDE\_SPACE\_USED\_THRESHOLD](/docs/ops-manager/v8.0/core/system-alerts/#std-label-blockstore) alert. `maxCapacityGB` does not enforce any limitation on the size of the backing database.
        """
        
        
        oidc: dict = Field(serialization_alias="oidc")
        r"""*Optional.* OIDC authentication settings for this store. The `oidc` object accepts the following fields:

- `enabled`: boolean. Enables OIDC authentication for this store.
- `method`: string. One of `callback`, `azure`, `gcp`, or `k8s`.
- `tokenUri`: string. The IdP token endpoint. Required when `method` is `callback`.
- `clientId`: string. The client ID registered with the IdP. Required when `method` is `callback`; optional when `method` is `azure`.
- `clientSecret`: string. The client secret registered with the IdP. Required when `method` is `callback`. If you edit an existing store and omit this field or submit the redacted value returned by a previous `GET` request, Ops Manager preserves the existing secret.
- `scope`: string. The OAuth2 scope requested from the IdP. Used only when `method` is `callback`.
- `tokenResource`: string. The audience or resource identifier for the workload identity token. Required when `method` is `azure` or `gcp`. This value must match the `audience` configured for this IdP in the target MongoDB deployment's `oidcIdentityProviders` setting.

The `callback`, `azure`, `gcp`, and `k8s` methods do not all require the same fields. The `azure`, `gcp`, and `k8s` methods do not require `clientSecret`.

When `oidc.enabled` is `true`, provide only hosts and connection options in the store's `uri` field. Ops Manager ignores any username or password embedded in the URI.

To switch a store from OIDC to another authentication mechanism, submit `oidc: {enabled: false}` in the request instead of omitting the `oidc` object.
        """
        
        
        ssl: Optional[bool] = Field(default=None, serialization_alias="ssl")
        r"""*Optional.* Flag indicating whether this blockstore only accepts connections encrypted using TLS.
        """
        
        
        uri: Optional[str] = Field(default=None, serialization_alias="uri")
        r"""A comma-separated list of hosts in the `<hostname:port>` format that can be used to access this [blockstore.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-blockstore-database)
        """
        
        
        write_concern: Optional[WriteConcern] = Field(default=None, serialization_alias="writeConcern")
        r"""*Optional.* The write concern used for this [blockstore.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-blockstore-database)

The accepted values for this option are:

- `ACKNOWLEDGED`
- `W2`
- `JOURNALED`
- `MAJORITY`

To learn about write acknowledgement levels in MongoDB, see [Write Concern.](https://www.mongodb.com/docs/manual/reference/write-concern/#std-label-write-operations-write-concern)
        """
        
    
    def create(self,
        
        
        query_params: Optional[CreateQueryParams],
        
        
        body_params: CreateBodyParams,
        
    ) -> dict[str, Any]:
        r"""
## Create One Blockstore Configuration
### Document:
[Create](https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/admin/backup/snapshot/mongoconfigs/create-one-blockstore-configuration/)
### Endpoint:
`POST /snapshot/mongoConfigs`
### Description
Configures one new blockstore.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/admin/backup/snapshot/mongoConfigs",
            None,
            query_params,
            body_params,
        )
    
    
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        blockstore_id: str = Field(serialization_alias="BLOCKSTORE-ID")
        r"""Unique name that labels this blockstore configuration.
        """
        
    
    
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set **envelope=true** in the query.

For endpoints that return one result, the response body includes:

- `status`: HTTP response code
- `content`: Expected response body
        """
        
        
        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body is in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """
        
    
    
    def delete(self,
        
        path_params: DeletePathParams,
        
        
        query_params: Optional[DeleteQueryParams],
        
        
    ) -> dict[str, Any]:
        r"""
## Delete One Blockstore Configuration
### Document:
[Delete](https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/admin/backup/snapshot/mongoconfigs/delete-one-blockstore-configuration/)
### Endpoint:
`DELETE /snapshot/mongoConfigs/{BLOCKSTORE-ID}`
### Description
Deletes the configuration of one blockstore.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/admin/backup/snapshot/mongoConfigs/{BLOCKSTORE-ID}",
            path_params,
            query_params,
            None,
        )
    
    
    
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        assignable_only: Optional[bool] = Field(default=True, serialization_alias="assignableOnly")
        r"""Indicates whether to return only blockstores to which you can assign new backup jobs.
        """
        
        
        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set `envelope : true` in the query.

For endpoints that return a list of results, the `content` object is an envelope. Ops Manager adds the `status` field to the response body.
        """
        
        
        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """
        
        
        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""One-based integer that returns a subsection of results.
        """
        
        
        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag that indicates whether the response body should be in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """
        
    
    
    def get_all(self,
        
        
        query_params: Optional[GetAllQueryParams],
        
        
    ) -> dict[str, Any]:
        r"""
## Get All Blockstore Configurations
### Document:
[Get All](https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/admin/backup/snapshot/mongoconfigs/get-all-blockstore-configurations/)
### Endpoint:
`GET /snapshot/mongoConfigs`
### Description
Retrieves the configurations of all blockstores.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/backup/snapshot/mongoConfigs",
            None,
            query_params,
            None,
        )
    
    
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        blockstore_id: str = Field(serialization_alias="BLOCKSTORE-ID")
        r"""The unique name that labels this blockstore configuration.
        """
        
    
    
    class GetByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set **envelope=true** in the query.

For endpoints that return one result, the response body includes:

- `status`: HTTP response code
- `content`: Expected response body
        """
        
        
        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body is in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """
        
    
    
    def get_by_id(self,
        
        path_params: GetByIdPathParams,
        
        
        query_params: Optional[GetByIdQueryParams],
        
        
    ) -> dict[str, Any]:
        r"""
## Get One Blockstore Configuration by ID
### Document:
[Get by ID](https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/admin/backup/snapshot/mongoconfigs/get-one-blockstore-configuration-by-id/)
### Endpoint:
`GET /snapshot/mongoConfigs/{BLOCKSTORE-ID}`
### Description
Retrieves the configuration of one blockstore.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/backup/snapshot/mongoConfigs/{BLOCKSTORE-ID}",
            path_params,
            query_params,
            None,
        )
    
    
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        blockstore_id: str = Field(serialization_alias="BLOCKSTORE-ID")
        r"""The unique name that labels this blockstore configuration.
        """
        
    
    
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set **envelope=true** in the query.

For endpoints that return one result, the response body includes:

- `status`: HTTP response code
- `content`: Expected response body
        """
        
        
        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body is in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """
        
    
    
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        assignment_enabled: Optional[bool] = Field(default=None, serialization_alias="assignmentEnabled")
        r"""*Optional.* Flag indicating whether this [blockstore](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-blockstore-database) can be assigned backup jobs.
        """
        
        
        encrypted_credentials: Optional[bool] = Field(default=None, serialization_alias="encryptedCredentials")
        r"""*Optional.* Flag indicating whether the username and password for this blockstore were encrypted using the [credentialstool.](/docs/ops-manager/v8.0/tutorial/encrypt-user-credentials/)
        """
        
        
        labels: Optional[list[str]] = Field(default=None, serialization_alias="labels")
        r"""*Optional.* Array of tags to manage which [backup jobs](/docs/ops-manager/v8.0/reference/glossary/#std-term-backup-job) Ops Manager can assign to which [blockstores.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-blockstore-database)

Setting these tags limits which backup jobs this blockstore can process. If omitted, this blockstore can only process backup jobs for projects that do not use labels to filter their jobs.
        """
        
        
        load_factor: Optional[int] = Field(default=None, serialization_alias="loadFactor")
        r"""*Optional.* A positive, non-zero integer that expresses how much backup work this [snapshot store](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-snapshot-store) should perform compared to another snapshot store. This option is needed only if more than one snapshot store is in use.

To learn more about Load Factor, see [Edit One Existing Blockstore.](/docs/ops-manager/v8.0/tutorial/manage-blockstore-storage/#std-label-edit-blockstore)
        """
        
        
        max_capacity_gb: Optional[int] = Field(default=None, serialization_alias="maxCapacityGB")
        r"""*Optional.* The blockstore’s expected maximum available capacity for use in the [OUTSIDE\_SPACE\_USED\_THRESHOLD](/docs/ops-manager/v8.0/core/system-alerts/#std-label-blockstore) alert. `maxCapacityGB` does not enforce any limitation on the size of the backing database.
        """
        
        
        oidc: dict = Field(serialization_alias="oidc")
        r"""*Optional.* OIDC authentication settings for this store. The `oidc` object accepts the following fields:

- `enabled`: boolean. Enables OIDC authentication for this store.
- `method`: string. One of `callback`, `azure`, `gcp`, or `k8s`.
- `tokenUri`: string. The IdP token endpoint. Required when `method` is `callback`.
- `clientId`: string. The client ID registered with the IdP. Required when `method` is `callback`; optional when `method` is `azure`.
- `clientSecret`: string. The client secret registered with the IdP. Required when `method` is `callback`. If you edit an existing store and omit this field or submit the redacted value returned by a previous `GET` request, Ops Manager preserves the existing secret.
- `scope`: string. The OAuth2 scope requested from the IdP. Used only when `method` is `callback`.
- `tokenResource`: string. The audience or resource identifier for the workload identity token. Required when `method` is `azure` or `gcp`. This value must match the `audience` configured for this IdP in the target MongoDB deployment's `oidcIdentityProviders` setting.

The `callback`, `azure`, `gcp`, and `k8s` methods do not all require the same fields. The `azure`, `gcp`, and `k8s` methods do not require `clientSecret`.

When `oidc.enabled` is `true`, provide only hosts and connection options in the store's `uri` field. Ops Manager ignores any username or password embedded in the URI.

To switch a store from OIDC to another authentication mechanism, submit `oidc: {enabled: false}` in the request instead of omitting the `oidc` object.
        """
        
        
        ssl: Optional[bool] = Field(default=None, serialization_alias="ssl")
        r"""*Optional.* Flag indicating whether this blockstore only accepts connections encrypted using TLS.
        """
        
        
        uri: Optional[str] = Field(default=None, serialization_alias="uri")
        r"""A comma-separated list of hosts in the `<hostname:port>` format that can be used to access this [blockstore.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-blockstore-database)
        """
        
        
        write_concern: Optional[WriteConcern] = Field(default=None, serialization_alias="writeConcern")
        r"""*Optional.* The write concern used for this [blockstore.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-backup-blockstore-database)

The accepted values for this option are:

- `ACKNOWLEDGED`
- `W2`
- `JOURNALED`
- `MAJORITY`

To learn about write acknowledgement levels in MongoDB, see [Write Concern.](https://www.mongodb.com/docs/manual/reference/write-concern/#std-label-write-operations-write-concern)
        """
        
    
    def update(self,
        
        path_params: UpdatePathParams,
        
        
        query_params: Optional[UpdateQueryParams],
        
        
        body_params: UpdateBodyParams,
        
    ) -> dict[str, Any]:
        r"""
## Update One Blockstore Configuration
### Document:
[Update](https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/admin/backup/snapshot/mongoconfigs/update-one-blockstore-configuration/)
### Endpoint:
`PUT /snapshot/mongoConfigs/{BLOCKSTORE-ID}`
### Description
Updates the configuration of one blockstore.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/admin/backup/snapshot/mongoConfigs/{BLOCKSTORE-ID}",
            path_params,
            query_params,
            body_params,
        )
    
