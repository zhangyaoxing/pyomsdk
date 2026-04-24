"""Auto-generated client for S3CompatibleBlockstoreResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class S3CompatibleBlockstoreResource(BaseResource):
    """Client for S3CompatibleBlockstoreResource resource."""

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

        accepted_tos: bool = Field(serialization_alias="acceptedTos")
        """Flag that indicates whether or not you accepted the terms of service for using S3-compatible storage stores with Ops Manager. You must set this to true to create an S3-compatible storage store.

If you set this to false, Ops Manager returns an error. The error states that Ops Manager can't create the S3-compatible storage store.
        """

        assignment_enabled: Optional[bool] = Field(
            serialization_alias="assignmentEnabled"
        )
        """Flag that indicates whether you can assign backup jobs to this data store.
        """

        aws_access_key: Optional[str] = Field(serialization_alias="awsAccessKey")
        """AWS Access Key ID that can access the S3-compatible storage bucket specified in s3BucketName.

If "s3AuthMethod" : "IAM_ROLE", then you don't need to include awsAccessKey.
        """

        aws_secret_key: Optional[str] = Field(serialization_alias="awsSecretKey")
        """AWS Secret Access Key that can access the S3-compatible storage bucket specified in <s3BucketName>.

If "s3AuthMethod" : "IAM_ROLE", then you don't need to include awsSecretKey.
        """

        class CustomcertificatesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            cert_string: Optional[str] = Field(serialization_alias="certString")
            """Contents of the Certificate Authority PEM file that comprise your Certificate Authority chain.
            """

            filename: Optional[str] = Field(serialization_alias="filename")
            """Name that identifies the Certificate Authority PEM file.
            """

        custom_certificates: Optional[list[CustomcertificatesParams]] = Field(
            serialization_alias="customCertificates"
        )
        """List of valid Certificate Authority certificates that apply to the associated S3-compatible storage bucket.
        """

        disable_proxy_s3: Optional[bool] = Field(serialization_alias="disableProxyS3")
        """Flag that indicates whether the HTTP proxy should be used when connecting to S3-compatible storage. You don't need to set this value unless you configured Ops Manager to use the HTTP proxy.
        """

        encrypted_credentials: Optional[bool] = Field(
            serialization_alias="encryptedCredentials"
        )
        """Flag that indicates whether the username and password for this S3-compatible storage blockstore were encrypted using the credentialstool.
        """

        id: str = Field(serialization_alias="id")
        """Name that uniquely identifies this S3 Snapshot Store.
        """

        labels: Optional[list[str]] = Field(serialization_alias="labels")
        """Array of tags to manage which backup jobs Ops Manager can assign to which S3 blockstores.

Setting these tags limits which backup jobs this S3-compatible storage blockstore can process. If omitted, this S3-compatible storage blockstore can only process backup jobs for projects that do not use labels to filter their jobs.
        """

        load_factor: Optional[float] = Field(serialization_alias="loadFactor")
        """Positive, non-zero integer that expresses how much backup work this snapshot store performs compared to another snapshot store. This option is needed only if more than one snapshot store is in use.

To learn more about Load Factor, see Edit One Existing Blockstore.
        """

        object_lock_enabled: Optional[bool] = Field(
            serialization_alias="objectLockEnabled"
        )
        """Flag that indicates whether object lock is enabled to prevent the objects in an S3 bucket from being deleted.
        """

        path_style_access_enabled: bool = Field(
            serialization_alias="pathStyleAccessEnabled"
        )
        """Flag that indicates the style of this endpoint.

Value
	
S3 Blockstore Endpoint Style
	
Example



true

	

Path-style URL endpoint

	

s3.amazonaws.com/<bucket>




false

	

Virtual-host-style URL endpoint

	

<bucket>.s3.amazonaws.com

To review the S3-compatible storage bucket URL conventions, see the AWS S3 documentation.
        """

        s3_auth_method: Optional[S3AuthMethod] = Field(
            serialization_alias="s3AuthMethod"
        )
        """Method used to authorize access to the S3-compatible storage bucket specified in s3BucketName.

Accepted values for this option are: KEYS, IAM_ROLE.

KEYS or None

	

Ops Manager uses awsAccessKey and awsSecretKey to authorize access to S3-compatible storage bucket specified in s3BucketName.




IAM_ROLE

	

Ops Manager uses an AWS IAM role to authorize access to S3-compatible storage bucket specified in s3BucketName. awsAccessKey and awsSecretKey fields are ignored. To learn more, see the AWS documentation
        """

        s3_bucket_endpoint: str = Field(serialization_alias="s3BucketEndpoint")
        """URL used to access this S3-compatible storage bucket.
        """

        s3_bucket_name: str = Field(serialization_alias="s3BucketName")
        """Name of the S3-compatible storage bucket that hosts the S3-compatible storage blockstore.
        """

        s3_max_connections: float = Field(serialization_alias="s3MaxConnections")
        """Positive integer indicating the maximum number of connections to this S3-compatible storage blockstore.
        """

        s3_region_override: Optional[str] = Field(
            serialization_alias="s3RegionOverride"
        )
        """Region where your S3-compatible storage bucket resides.

Use this field only if your S3-compatible storage store's s3BucketEndpoint doesn't support region scoping. Don't use this field with AWS S3 buckets.
        """

        sse_enabled: bool = Field(serialization_alias="sseEnabled")
        """Flag that indicates whether this S3-compatible storage blockstore enables server-side encryption.
        """

        ssl: Optional[bool] = Field(serialization_alias="ssl")
        """Flag that indicates whether this S3-compatible storage blockstore only accepts connections encrypted using TLS.
        """

        uri: str = Field(serialization_alias="uri")
        """Connection String that connects to the metadata database for this S3-compatible storage blockstore. This database stores the locations of the blocks in the AWS S3-compatible storage bucket.
        """

        write_concern: Optional[WriteConcern] = Field(
            serialization_alias="writeConcern"
        )
        """Write concern used for this blockstore.

Ops Manager accepts the following values:

ACKNOWLEDGED

W2

JOURNALED

MAJORITY

To learn about write acknowledgement levels in MongoDB, see Write Concern.
        """

    def create(
        self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One S3 Blockstore Configuration
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/create-one-s3-blockstore-configuration/)
        ### Endpoint:
        `POST /snapshot/s3Configs`
        ### Description
        Configures one new s3 blockstore.
        """
        return self._request(
            "POST",
            "/snapshot/s3Configs",
            None,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        s3_blockstore_config_id: str = Field(
            serialization_alias="S3-BLOCKSTORE-CONFIG-ID"
        )
        """The unique name that labels this S3 blockstore configuration.
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
        ## Delete One S3-Compatible Blockstore Configuration
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/delete-one-s3-blockstore-configuration/)
        ### Endpoint:
        `DELETE /snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}`
        ### Description
        Deletes the configuration of one s3 blockstore.
        """
        return self._request(
            "DELETE",
            "/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        assignable_only: Optional[bool] = Field(
            True, serialization_alias="assignableOnly"
        )
        """Flag indicating whether this S3 blockstore can be assigned new backup jobs.
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
        ## Get All S3 Blockstore Configurations
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/get-all-s3-blockstore-configurations/)
        ### Endpoint:
        `GET /snapshot/s3Configs`
        ### Description
        Retrieves the configurations of all S3 blockstores.
        """
        return self._request(
            "GET",
            "/snapshot/s3Configs",
            None,
            query_params,
            None,
        )

    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        s3_blockstore_config_id: str = Field(
            serialization_alias="S3-BLOCKSTORE-CONFIG-ID"
        )
        """The unique name that labels this S3 blockstore configuration.
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
        ## Get One S3 Blockstore Configuration by ID
        ### Document:
        [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/get-one-s3-blockstore-configuration-by-id/)
        ### Endpoint:
        `GET /snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}`
        ### Description
        Retrieves the configuration of one S3 blockstore.
        """
        return self._request(
            "GET",
            "/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        s3_blockstore_config_id: str = Field(
            serialization_alias="S3-BLOCKSTORE-CONFIG-ID"
        )
        """The unique name that labels this S3 blockstore configuration.
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

        accepted_tos: bool = Field(serialization_alias="acceptedTos")
        """Flag that indicates whether or not you accepted the terms of service for using S3-compatible storage stores with Ops Manager. You must set this to true to create an S3-compatible storage store.

If you set this to false, Ops Manager returns an error. The error states that Ops Manager can't create the S3-compatible storage store.
        """

        assignment_enabled: Optional[bool] = Field(
            serialization_alias="assignmentEnabled"
        )
        """Flag that indicates whether you can assign backup jobs to this data store.
        """

        aws_access_key: Optional[str] = Field(serialization_alias="awsAccessKey")
        """AWS Access Key ID that can access the S3-compatible storage bucket specified in s3BucketName.

If "s3AuthMethod" : "IAM_ROLE", then you don't need to include awsAccessKey.
        """

        aws_secret_key: Optional[str] = Field(serialization_alias="awsSecretKey")
        """AWS Secret Access Key that can access the S3-compatible storage bucket specified in <s3BucketName>.

If "s3AuthMethod" : "IAM_ROLE", then you don't need to include awsSecretKey.
        """

        class CustomcertificatesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            cert_string: Optional[str] = Field(serialization_alias="certString")
            """Contents of the Certificate Authority PEM file that comprise your Certificate Authority chain.
            """

            filename: Optional[str] = Field(serialization_alias="filename")
            """Name that identifies the Certificate Authority PEM file.
            """

        custom_certificates: Optional[list[CustomcertificatesParams]] = Field(
            serialization_alias="customCertificates"
        )
        """List of valid Certificate Authority certificates that apply to the associated S3-compatible storage bucket.
        """

        disable_proxy_s3: Optional[bool] = Field(serialization_alias="disableProxyS3")
        """Flag that indicates whether the HTTP proxy should be used when connecting to S3-compatible storage. You don't need to set this value unless you configured Ops Manager to use the HTTP proxy.
        """

        encrypted_credentials: Optional[bool] = Field(
            serialization_alias="encryptedCredentials"
        )
        """Flag that indicates whether the username and password for this S3-compatible storage blockstore were encrypted using the credentialstool.
        """

        labels: Optional[list[str]] = Field(serialization_alias="labels")
        """Array of tags to manage which backup jobs Ops Manager can assign to which S3 blockstores.

Setting these tags limits which backup jobs this S3-compatible storage blockstore can process. If omitted, this S3-compatible storage blockstore can only process backup jobs for projects that do not use labels to filter their jobs.
        """

        load_factor: Optional[float] = Field(serialization_alias="loadFactor")
        """Positive, non-zero integer that expresses how much backup work this snapshot store performs compared to another snapshot store. This option is needed only if more than one snapshot store is in use.

To learn more about Load Factor, see Edit One Existing Blockstore.
        """

        object_lock_enabled: Optional[bool] = Field(
            serialization_alias="objectLockEnabled"
        )
        """Flag that indicates whether object lock is enabled to prevent the objects in an S3 bucket from being deleted.
        """

        path_style_access_enabled: bool = Field(
            serialization_alias="pathStyleAccessEnabled"
        )
        """Flag that indicates the style of this endpoint.

Value
	
S3 Blockstore Endpoint Style
	
Example



true

	

Path-style URL endpoint

	

s3.amazonaws.com/<bucket>




false

	

Virtual-host-style URL endpoint

	

<bucket>.s3.amazonaws.com

To review the S3-compatible storage bucket URL conventions, see the AWS S3 documentation.
        """

        s3_auth_method: Optional[S3AuthMethod] = Field(
            serialization_alias="s3AuthMethod"
        )
        """Method used to authorize access to the S3-compatible storage bucket specified in s3BucketName.

Ops Manager accepts the following values:

KEYS or None

	

Ops Manager uses awsAccessKey and awsSecretKey to authorize access to S3-compatible storage bucket specified in s3BucketName.




IAM_ROLE

	

Ops Manager uses an AWS IAM role to authorize access to S3-compatible storage bucket specified in s3BucketName. awsAccessKey and awsSecretKey fields are ignored. To learn more, see the AWS documentation
        """

        s3_bucket_endpoint: str = Field(serialization_alias="s3BucketEndpoint")
        """URL used to access this S3-compatible storage bucket.
        """

        s3_bucket_name: str = Field(serialization_alias="s3BucketName")
        """Name of the S3-compatible storage bucket that hosts the S3-compatible storage blockstore.
        """

        s3_max_connections: float = Field(serialization_alias="s3MaxConnections")
        """Positive integer indicating the maximum number of connections to this S3-compatible storage blockstore.
        """

        s3_region_override: Optional[str] = Field(
            serialization_alias="s3RegionOverride"
        )
        """Region where your S3-compatible storage bucket resides.

Use this field only if your S3-compatible storage store's s3BucketEndpoint doesn't support region scoping. Don't use this field with AWS S3 buckets.
        """

        sse_enabled: bool = Field(serialization_alias="sseEnabled")
        """Flag that indicates whether this S3-compatible storage blockstore enables server-side encryption.
        """

        ssl: Optional[bool] = Field(serialization_alias="ssl")
        """Flag that indicates whether this S3-compatible storage blockstore only accepts connections encrypted using TLS.
        """

        uri: str = Field(serialization_alias="uri")
        """Comma-separated list of hosts in the <hostname:port> format that can access this S3-compatible storage blockstore.
        """

        write_concern: Optional[WriteConcern] = Field(
            serialization_alias="writeConcern"
        )
        """Write concern used for this blockstore.

Ops Manager accepts the following values:

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
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One S3 Blockstore Configuration
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/update-one-s3-blockstore-configuration/)
        ### Endpoint:
        `PUT /snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}`
        ### Description
        Updates the configuration of one s3 blockstore.
        """
        return self._request(
            "PUT",
            "/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
