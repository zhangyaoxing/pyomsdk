
r"""Auto-generated client for S3CompatibleBlockstoreV20Resource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *

class S3CompatibleBlockstoreV20Resource(BaseResource):
    r"""Client for S3CompatibleBlockstoreV20Resource resource.
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
        
        
        accepted_tos: bool = Field(serialization_alias="acceptedTos")
        r"""Flag that indicates whether you accepted the terms of service for using S3-compatible storage stores with Ops Manager. You must set this to `true` to create an S3-compatible storage store.

If you set this to `false`, Ops Manager returns an error. The error states that Ops Manager can't create the S3-compatible storage store.
        """
        
        
        assignment_enabled: Optional[bool] = Field(default=None, serialization_alias="assignmentEnabled")
        r"""Flag that indicates whether you can assign backup jobs to this data store.
        """
        
        
        aws_access_key: Optional[str] = Field(default=None, serialization_alias="awsAccessKey")
        r"""AWS Access Key ID that can access the S3-compatible storage bucket specified in **s3BucketName**.

If `"s3AuthMethod" : "IAM_ROLE"`, then you don't need to include **awsAccessKey**.
        """
        
        
        aws_secret_key: Optional[str] = Field(default=None, serialization_alias="awsSecretKey")
        r"""AWS Secret Access Key that can access the S3-compatible storage bucket specified in `<s3BucketName>`.

If `"s3AuthMethod" : "IAM_ROLE"`, then you don't need to include **awsSecretKey**.
        """
        
        
        class CustomCertificatesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            
            cert_string: Optional[str] = Field(default=None, serialization_alias="certString")
            r"""Contents of the Certificate Authority PEM file that comprise your Certificate Authority chain.
            """
            
            filename: Optional[str] = Field(default=None, serialization_alias="filename")
            r"""Name that identifies the Certificate Authority PEM file.
            """
            
        
        custom_certificates: Optional[list[CustomCertificatesParams]] = Field(default=None, serialization_alias="customCertificates")
        r"""List of valid Certificate Authority certificates that apply to the associated S3-compatible storage bucket.
        """
        
        
        disable_proxy_s3: bool = Field(serialization_alias="disableProxyS3")
        r"""When connecting to S3-compatible storage, indicates whether to use the [HTTP proxy](/docs/ops-manager/current/tutorial/use-with-http-proxy/). You must include this field in every request to create or update an S3-compatible storage blockstore, even if you haven't configured Ops Manager to use the HTTP proxy.
        """
        
        
        encrypted_credentials: Optional[bool] = Field(default=None, serialization_alias="encryptedCredentials")
        r"""Flag that indicates whether the username and password for this S3-compatible storage blockstore were encrypted using the [credentialstool.](/docs/ops-manager/current/tutorial/encrypt-user-credentials/)
        """
        
        
        id: str = Field(serialization_alias="id")
        r"""Name that uniquely identifies this [S3 Snapshot Store.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-S3-Snapshot-Store)
        """
        
        
        class KeyVaultParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            
            aws_access_key_path: Optional[str] = Field(default=None, serialization_alias="awsAccessKeyPath")
            r"""Path to the AWS access key in the key vault, in the form `<secret-path>/<key>`. Ops Manager reads the value of the `<key>` field from the Vault KV version 2 secret at `<secret-path>`. For example, `secret/data/s3/aws-access-key` reads the `aws-access-key` field from the secret at `secret/data/s3`. Include the `/data/` segment that KV version 2 requires. Don't include the `/v1/` API prefix. Ops Manager adds the prefix automatically. Required when you provide `keyVault`.
            """
            
            aws_secret_key_path: Optional[str] = Field(default=None, serialization_alias="awsSecretKeyPath")
            r"""Path to the AWS secret key in the key vault. Uses the same `<secret-path>/<key>` format as `keyVault.awsAccessKeyPath`. Required when you provide `keyVault`.
            """
            
            vault_id: Optional[str] = Field(default=None, serialization_alias="vaultId")
            r"""Unique identifier of the key vault configuration that stores the credentials. This value matches the `id` of a key vault configuration. Required when you provide `keyVault`.
            """
            
        
        key_vault: Optional[KeyVaultParams] = Field(default=None, serialization_alias="keyVault")
        r"""Vault-backed credential source for this S3-compatible snapshot store. When `s3AuthMethod` is `KEYS`, provide either the `keyVault` object or both `awsAccessKey` and `awsSecretKey`, but not both. To learn more, see [HashiCorp Vault for Snapshot Store Credentials.](/docs/ops-manager/current/tutorial/vault-snapshot-store-credentials/#std-label-om-vault-snapshot-store-credentials)
        """
        
        
        labels: Optional[list[str]] = Field(default=None, serialization_alias="labels")
        r"""Array of tags to manage which [backup jobs](/docs/ops-manager/current/reference/glossary/#std-term-backup-job) Ops Manager can assign to which [S3 blockstores.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-S3-Snapshot-Store)

Setting these tags limits which backup jobs this S3-compatible storage blockstore can process. If omitted, this S3-compatible storage blockstore can only process backup jobs for projects that do not use labels to filter their jobs.
        """
        
        
        load_factor: Optional[int] = Field(default=None, serialization_alias="loadFactor")
        r"""Positive, non-zero integer that expresses how much backup work this [snapshot store](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-snapshot-store) performs compared to another snapshot store. This option is needed only if more than one snapshot store is in use.

To learn more about Load Factor, see [Edit One Existing Blockstore.](/docs/ops-manager/current/tutorial/manage-blockstore-storage/#std-label-edit-blockstore)
        """
        
        
        object_lock_enabled: Optional[bool] = Field(default=None, serialization_alias="objectLockEnabled")
        r"""Flag that indicates whether object lock is enabled to prevent the objects in an S3 bucket from being deleted.
        """
        
        
        oidc: Optional[dict] = Field(default=None, serialization_alias="oidc")
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
        
        
        path_style_access_enabled: bool = Field(serialization_alias="pathStyleAccessEnabled")
        r"""Flag that indicates the style of this endpoint.

- `true`: path-style URL endpoint. For example, `s3.amazonaws.com/<bucket>`.
- `false`: virtual-host-style URL endpoint. For example, `<bucket>.s3.amazonaws.com`.

To review the S3-compatible storage bucket URL conventions, see the [AWS S3 documentation.](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#access-bucket-intro)
        """
        
        
        s3_auth_method: Optional[S3AuthMethod] = Field(default=None, serialization_alias="s3AuthMethod")
        r"""Method used to authorize access to the S3-compatible storage bucket specified in **s3BucketName**.

Accepted values for this option are:

- `KEYS` or None: Ops Manager uses **awsAccessKey** and **awsSecretKey** to authorize access to S3-compatible storage bucket specified in **s3BucketName**.
- `IAM_ROLE`: Ops Manager uses an AWS IAM role to authorize access to S3-compatible storage bucket specified in **s3BucketName**. **awsAccessKey** and **awsSecretKey** fields are ignored. To learn more, see the [AWS documentation](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#attach-iam-role)
        """
        
        
        s3_bucket_endpoint: str = Field(serialization_alias="s3BucketEndpoint")
        r"""URL used to access this S3-compatible storage bucket.
        """
        
        
        s3_bucket_name: str = Field(serialization_alias="s3BucketName")
        r"""Name of the S3-compatible storage bucket that hosts the S3-compatible storage blockstore.
        """
        
        
        s3_max_connections: int = Field(serialization_alias="s3MaxConnections")
        r"""Positive integer indicating the maximum number of connections to this S3-compatible storage blockstore.
        """
        
        
        s3_region_override: Optional[str] = Field(default=None, serialization_alias="s3RegionOverride")
        r"""Region where your S3-compatible storage bucket resides.

Use this field only if your S3-compatible storage store's **s3BucketEndpoint** doesn't support region scoping. Don't use this field with AWS S3 buckets.
        """
        
        
        sse_enabled: bool = Field(serialization_alias="sseEnabled")
        r"""Flag that indicates whether this S3-compatible storage blockstore enables [server-side encryption.](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html)
        """
        
        
        ssl: Optional[bool] = Field(default=None, serialization_alias="ssl")
        r"""Flag that indicates whether this S3-compatible storage blockstore only accepts connections encrypted using TLS.
        """
        
        
        uri: str = Field(serialization_alias="uri")
        r"""[Connection String](https://www.mongodb.com/docs/manual/reference/connection-string/#std-label-mongodb-uri) that connects to the metadata database for this S3-compatible storage blockstore. This database stores the locations of the blocks in the AWS S3-compatible storage bucket.
        """
        
        
        write_concern: Optional[WriteConcern] = Field(default=None, serialization_alias="writeConcern")
        r"""Write concern used for this blockstore.

Ops Manager accepts the following values:

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
## Create One S3 Blockstore Configuration (v2.0)
### Document:
[Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3configs-v2/create-one-s3-blockstore-configuration/)
### Endpoint:
`POST /snapshot/s3Configs`
### Description
Configures one new S3-compatible storage blockstore. The v2.0 resource adds the `keyVault` object. With this object, the S3-compatible storage blockstore reads its AWS credentials from HashiCorp Vault. To learn more, see [HashiCorp Vault for Snapshot Store Credentials.](/docs/ops-manager/current/tutorial/vault-snapshot-store-credentials/#std-label-om-vault-snapshot-store-credentials)
        """
        return self._request(
            "POST",
            "/api/public/v2.0/admin/backup/snapshot/s3Configs",
            None,
            query_params,
            body_params,
        )
    
    
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        s3_blockstore_config_id: str = Field(serialization_alias="S3-BLOCKSTORE-CONFIG-ID")
        r"""The unique name that labels this S3-compatible storage blockstore configuration.
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
## Delete One S3 Blockstore Configuration (v2.0)
### Document:
[Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3configs-v2/delete-one-s3-blockstore-configuration/)
### Endpoint:
`DELETE /snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}`
### Description
Deletes the configuration of one S3-compatible storage blockstore.
        """
        return self._request(
            "DELETE",
            "/api/public/v2.0/admin/backup/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )
    
    
    
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        assignable_only: Optional[bool] = Field(default=True, serialization_alias="assignableOnly")
        r"""Indicates whether to return only S3-compatible storage blockstores to which you can assign new backup jobs.
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
## Get All S3 Blockstore Configurations (v2.0)
### Document:
[Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3configs-v2/get-all-s3-blockstore-configurations/)
### Endpoint:
`GET /snapshot/s3Configs`
### Description
Retrieves the configurations of all S3-compatible storage blockstores. The v2.0 resource returns the `keyVault` object for each S3-compatible storage blockstore that reads its AWS credentials from HashiCorp Vault.
        """
        return self._request(
            "GET",
            "/api/public/v2.0/admin/backup/snapshot/s3Configs",
            None,
            query_params,
            None,
        )
    
    
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        s3_blockstore_config_id: str = Field(serialization_alias="S3-BLOCKSTORE-CONFIG-ID")
        r"""The unique name that labels this S3-compatible storage blockstore configuration.
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
## Get One S3 Blockstore Configuration by ID (v2.0)
### Document:
[Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3configs-v2/get-one-s3-blockstore-configuration-by-id/)
### Endpoint:
`GET /snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}`
### Description
Retrieves the configuration of one S3-compatible storage blockstore. The v2.0 resource returns the `keyVault` object when the S3-compatible storage blockstore reads its AWS credentials from HashiCorp Vault.
        """
        return self._request(
            "GET",
            "/api/public/v2.0/admin/backup/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )
    
    
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        s3_blockstore_config_id: str = Field(serialization_alias="S3-BLOCKSTORE-CONFIG-ID")
        r"""The unique name that labels this S3-compatible storage blockstore configuration.
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
        
        
        accepted_tos: bool = Field(serialization_alias="acceptedTos")
        r"""Flag that indicates whether you accepted the terms of service for using S3-compatible storage stores with Ops Manager. You must set this to `true` to create an S3-compatible storage store.

If you set this to `false`, Ops Manager returns an error. The error states that Ops Manager can't create the S3-compatible storage store.
        """
        
        
        assignment_enabled: Optional[bool] = Field(default=None, serialization_alias="assignmentEnabled")
        r"""Flag that indicates whether you can assign backup jobs to this data store.
        """
        
        
        aws_access_key: Optional[str] = Field(default=None, serialization_alias="awsAccessKey")
        r"""AWS Access Key ID that can access the S3-compatible storage bucket specified in **s3BucketName**.

If `"s3AuthMethod" : "IAM_ROLE"`, then you don't need to include **awsAccessKey**.
        """
        
        
        aws_secret_key: Optional[str] = Field(default=None, serialization_alias="awsSecretKey")
        r"""AWS Secret Access Key that can access the S3-compatible storage bucket specified in `<s3BucketName>`.

If `"s3AuthMethod" : "IAM_ROLE"`, then you don't need to include **awsSecretKey**.
        """
        
        
        class CustomCertificatesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            
            cert_string: Optional[str] = Field(default=None, serialization_alias="certString")
            r"""Contents of the Certificate Authority PEM file that comprise your Certificate Authority chain.
            """
            
            filename: Optional[str] = Field(default=None, serialization_alias="filename")
            r"""Name that identifies the Certificate Authority PEM file.
            """
            
        
        custom_certificates: Optional[list[CustomCertificatesParams]] = Field(default=None, serialization_alias="customCertificates")
        r"""List of valid Certificate Authority certificates that apply to the associated S3-compatible storage bucket.
        """
        
        
        disable_proxy_s3: bool = Field(serialization_alias="disableProxyS3")
        r"""When connecting to S3-compatible storage, indicates whether to use the [HTTP proxy](/docs/ops-manager/current/tutorial/use-with-http-proxy/). You must include this field in every request to create or update an S3-compatible storage blockstore, even if you haven't configured Ops Manager to use the HTTP proxy.
        """
        
        
        encrypted_credentials: Optional[bool] = Field(default=None, serialization_alias="encryptedCredentials")
        r"""Flag that indicates whether the username and password for this S3-compatible storage blockstore were encrypted using the [credentialstool.](/docs/ops-manager/current/tutorial/encrypt-user-credentials/)
        """
        
        
        class KeyVaultParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            
            aws_access_key_path: Optional[str] = Field(default=None, serialization_alias="awsAccessKeyPath")
            r"""Path to the AWS access key in the key vault, in the form `<secret-path>/<key>`. Ops Manager reads the value of the `<key>` field from the Vault KV version 2 secret at `<secret-path>`. For example, `secret/data/s3/aws-access-key` reads the `aws-access-key` field from the secret at `secret/data/s3`. Include the `/data/` segment that KV version 2 requires. Don't include the `/v1/` API prefix. Ops Manager adds the prefix automatically. Required when you provide `keyVault`.
            """
            
            aws_secret_key_path: Optional[str] = Field(default=None, serialization_alias="awsSecretKeyPath")
            r"""Path to the AWS secret key in the key vault. Uses the same `<secret-path>/<key>` format as `keyVault.awsAccessKeyPath`. Required when you provide `keyVault`.
            """
            
            vault_id: Optional[str] = Field(default=None, serialization_alias="vaultId")
            r"""Unique identifier of the key vault configuration that stores the credentials. This value matches the `id` of a key vault configuration. Required when you provide `keyVault`.
            """
            
        
        key_vault: Optional[KeyVaultParams] = Field(default=None, serialization_alias="keyVault")
        r"""Vault-backed credential source for this S3-compatible snapshot store. When `s3AuthMethod` is `KEYS`, provide either the `keyVault` object or both `awsAccessKey` and `awsSecretKey`, but not both. To learn more, see [HashiCorp Vault for Snapshot Store Credentials.](/docs/ops-manager/current/tutorial/vault-snapshot-store-credentials/#std-label-om-vault-snapshot-store-credentials)
        """
        
        
        labels: Optional[list[str]] = Field(default=None, serialization_alias="labels")
        r"""Array of tags to manage which [backup jobs](/docs/ops-manager/current/reference/glossary/#std-term-backup-job) Ops Manager can assign to which [S3 blockstores.](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-S3-Snapshot-Store)

Setting these tags limits which backup jobs this S3-compatible storage blockstore can process. If omitted, this S3-compatible storage blockstore can only process backup jobs for projects that do not use labels to filter their jobs.
        """
        
        
        load_factor: Optional[int] = Field(default=None, serialization_alias="loadFactor")
        r"""Positive, non-zero integer that expresses how much backup work this [snapshot store](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-snapshot-store) performs compared to another snapshot store. This option is needed only if more than one snapshot store is in use.

To learn more about Load Factor, see [Edit One Existing Blockstore.](/docs/ops-manager/current/tutorial/manage-blockstore-storage/#std-label-edit-blockstore)
        """
        
        
        object_lock_enabled: Optional[bool] = Field(default=None, serialization_alias="objectLockEnabled")
        r"""Flag that indicates whether object lock is enabled to prevent the objects in an S3 bucket from being deleted.
        """
        
        
        oidc: Optional[dict] = Field(default=None, serialization_alias="oidc")
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

If you update this store and omit the `oidc` object from the request, Ops Manager removes the existing OIDC configuration. To preserve the existing configuration, include the current `oidc` object in every update request.

`clientSecret` is the one exception. If you omit `clientSecret` from the `oidc` object, or submit the redacted value returned by a previous `GET` request, Ops Manager preserves the existing secret. To change the secret, submit the new plaintext value.
        """
        
        
        path_style_access_enabled: bool = Field(serialization_alias="pathStyleAccessEnabled")
        r"""Flag that indicates the style of this endpoint.

- `true`: path-style URL endpoint. For example, `s3.amazonaws.com/<bucket>`.
- `false`: virtual-host-style URL endpoint. For example, `<bucket>.s3.amazonaws.com`.

To review the S3-compatible storage bucket URL conventions, see the [AWS S3 documentation.](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#access-bucket-intro)
        """
        
        
        s3_auth_method: Optional[S3AuthMethod] = Field(default=None, serialization_alias="s3AuthMethod")
        r"""Method used to authorize access to the S3-compatible storage bucket specified in **s3BucketName**.

Ops Manager accepts the following values:

- `KEYS` or None: Ops Manager uses **awsAccessKey** and **awsSecretKey** to authorize access to S3-compatible storage bucket specified in **s3BucketName**.
- `IAM_ROLE`: Ops Manager uses an AWS IAM role to authorize access to S3-compatible storage bucket specified in **s3BucketName**. **awsAccessKey** and **awsSecretKey** fields are ignored. To learn more, see the [AWS documentation](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#attach-iam-role)
        """
        
        
        s3_bucket_endpoint: str = Field(serialization_alias="s3BucketEndpoint")
        r"""URL used to access this S3-compatible storage bucket.
        """
        
        
        s3_bucket_name: str = Field(serialization_alias="s3BucketName")
        r"""Name of the S3-compatible storage bucket that hosts the S3-compatible storage blockstore.
        """
        
        
        s3_max_connections: int = Field(serialization_alias="s3MaxConnections")
        r"""Positive integer indicating the maximum number of connections to this S3-compatible storage blockstore.
        """
        
        
        s3_region_override: Optional[str] = Field(default=None, serialization_alias="s3RegionOverride")
        r"""Region where your S3-compatible storage bucket resides.

Use this field only if your S3-compatible storage store's **s3BucketEndpoint** doesn't support region scoping. Don't use this field with AWS S3 buckets.
        """
        
        
        sse_enabled: bool = Field(serialization_alias="sseEnabled")
        r"""Flag that indicates whether this S3-compatible storage blockstore enables [server-side encryption.](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html)
        """
        
        
        ssl: Optional[bool] = Field(default=None, serialization_alias="ssl")
        r"""Flag that indicates whether this S3-compatible storage blockstore only accepts connections encrypted using TLS.
        """
        
        
        uri: str = Field(serialization_alias="uri")
        r"""Comma-separated list of hosts in the `<hostname:port>` format that can access this S3-compatible storage blockstore.
        """
        
        
        write_concern: Optional[WriteConcern] = Field(default=None, serialization_alias="writeConcern")
        r"""Write concern used for this blockstore.

Ops Manager accepts the following values:

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
## Update One S3 Blockstore Configuration (v2.0)
### Document:
[Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3configs-v2/update-one-s3-blockstore-configuration/)
### Endpoint:
`PUT /snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}`
### Description
Updates one S3-compatible storage blockstore configuration. The v2.0 resource adds the `keyVault` object. With this object, the S3-compatible storage blockstore reads its AWS credentials from HashiCorp Vault. To learn more, see [HashiCorp Vault for Snapshot Store Credentials.](/docs/ops-manager/current/tutorial/vault-snapshot-store-credentials/#std-label-om-vault-snapshot-store-credentials)
        """
        return self._request(
            "PUT",
            "/api/public/v2.0/admin/backup/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    
