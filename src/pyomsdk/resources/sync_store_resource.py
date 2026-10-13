
r"""Auto-generated client for SyncStoreResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *

class SyncStoreResource(BaseResource):
    r"""Client for SyncStoreResource resource.
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
        r"""*Optional.* Flag indicating whether this sync store can be assigned backup jobs.
        """
        
        
        encrypted_credentials: Optional[bool] = Field(default=None, serialization_alias="encryptedCredentials")
        r"""*Optional.* Flag indicating whether the username and password for this sync store were encrypted using the [credentialstool.](/docs/ops-manager/current/tutorial/encrypt-user-credentials/)
        """
        
        
        id: Optional[str] = Field(default=None, serialization_alias="id")
        r"""The unique name that labels this sync store.
        """
        
        
        labels: Optional[list[str]] = Field(default=None, serialization_alias="labels")
        r"""*Optional.* Array of tags to manage which [backup jobs](/docs/ops-manager/current/reference/glossary/#std-term-backup-job) Ops Manager can assign to which [sync stores.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-sync-store)

Setting these tags limits which backup jobs this sync store can process. If omitted, this sync store can only process backup jobs for projects that do not use labels to filter their jobs.
        """
        
        
        max_capacity_gb: Optional[int] = Field(default=None, serialization_alias="maxCapacityGB")
        r"""*Optional.* The sync store’s expected maximum available capacity for use in the [OUTSIDE\_SPACE\_USED\_THRESHOLD](/docs/ops-manager/current/core/system-alerts/#std-label-blockstore) alert. `maxCapacityGB` does not enforce any limitation on the size of the backing database.
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
        r"""*Optional.* Flag indicating whether this sync store only accepts connections encrypted using TLS.
        """
        
        
        uri: Optional[str] = Field(default=None, serialization_alias="uri")
        r"""A comma-separated list of hosts in the `<hostname:port>` format that can be used to access this sync store.
        """
        
        
        write_concern: Optional[WriteConcern] = Field(default=None, serialization_alias="writeConcern")
        r"""*Optional.* The write concern used for this sync store.

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
## Create One Sync Store Configuration
### Document:
[Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoconfigs/create-one-sync-store-configuration/)
### Endpoint:
`POST /sync/mongoConfigs`
### Description
Configures one new sync store.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/admin/backup/sync/mongoConfigs",
            None,
            query_params,
            body_params,
        )
    
    
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        sync_store_config_id: str = Field(serialization_alias="SYNC-STORE-CONFIG-ID")
        r"""Unique identifier of this Sync Store configuration.
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
## Delete One Sync Store Configuration
### Document:
[Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoconfigs/delete-one-sync-store-configuration/)
### Endpoint:
`DELETE /sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}`
### Description
Deletes the configuration of one sync store.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/admin/backup/sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )
    
    
    
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        assignable_only: Optional[bool] = Field(default=True, serialization_alias="assignableOnly")
        r"""Indicates whether to return only sync stores to which you can assign new backup jobs.
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
## Get All Sync Store Configurations
### Document:
[Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoconfigs/get-all-sync-store-configurations/)
### Endpoint:
`GET /sync/mongoConfigs`
### Description
Retrieves the configurations of all sync stores.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/backup/sync/mongoConfigs",
            None,
            query_params,
            None,
        )
    
    
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        sync_store_config_id: str = Field(serialization_alias="SYNC-STORE-CONFIG-ID")
        r"""The unique identifier that represents this Oplog configuration.
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
## Get One Sync Store Configuration by ID
### Document:
[Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoconfigs/get-one-sync-store-configuration-by-id/)
### Endpoint:
`GET /sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}`
### Description
Retrieves the configuration of one sync store.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/backup/sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )
    
    
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        sync_store_config_id: str = Field(serialization_alias="SYNC-STORE-CONFIG-ID")
        r"""Unique identifier for this Sync Store configuration.
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
        r"""*Optional.* Flag indicating whether this sync store can be assigned backup jobs.
        """
        
        
        encrypted_credentials: Optional[bool] = Field(default=None, serialization_alias="encryptedCredentials")
        r"""*Optional.* Flag indicating whether the username and password for this sync store were encrypted using the [credentialstool.](/docs/ops-manager/current/tutorial/encrypt-user-credentials/)
        """
        
        
        labels: Optional[list[str]] = Field(default=None, serialization_alias="labels")
        r"""*Optional.* Array of tags to manage which [backup jobs](/docs/ops-manager/current/reference/glossary/#std-term-backup-job) Ops Manager can assign to which [sync stores.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-sync-store)

Setting these tags limits which backup jobs this sync store can process. If omitted, this sync store can only process backup jobs for projects that do not use labels to filter their jobs.
        """
        
        
        max_capacity_gb: Optional[int] = Field(default=None, serialization_alias="maxCapacityGB")
        r"""*Optional.* The sync store’s expected maximum available capacity for use in the [OUTSIDE\_SPACE\_USED\_THRESHOLD](/docs/ops-manager/current/core/system-alerts/#std-label-blockstore) alert. `maxCapacityGB` does not enforce any limitation on the size of the backing database.
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
        r"""*Optional.* Flag indicating whether this sync store only accepts connections encrypted using TLS.
        """
        
        
        uri: Optional[str] = Field(default=None, serialization_alias="uri")
        r"""A comma-separated list of hosts in the `<hostname:port>` format that can be used to access this sync store.
        """
        
        
        write_concern: Optional[WriteConcern] = Field(default=None, serialization_alias="writeConcern")
        r"""*Optional.* The write concern used for this sync store.

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
## Update One Sync Store Configuration
### Document:
[Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoconfigs/update-one-sync-store-configuration/)
### Endpoint:
`PUT /sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}`
### Description
Updates the configuration of one sync store.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/admin/backup/sync/mongoConfigs/{SYNC-STORE-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    
