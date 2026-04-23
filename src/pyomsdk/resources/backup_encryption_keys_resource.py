"""Auto-generated client for BackupEncryptionKeysResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class BackupEncryptionKeysResource(BaseResource):
    """Client for BackupEncryptionKeysResource resource."""

    class RetrieveKmipMasterKeyIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster to which the encryption keys belongs.
        """

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique identifier of the project to which the encryption key belongs.
        """

    class RetrieveKmipMasterKeyIdQueryParams(BaseModel):
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

    def retrieve_kmip_master_key_id(
        self,
        path_params: RetrieveKmipMasterKeyIdPathParams,
        query_params: Optional[RetrieveKmipMasterKeyIdQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve the KMIP Master Key ID
        - Document: [Retrieve KMIP Master Key ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/kmip-keys/get-master-key/)
        - Resource: `GET /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/encryptionKey`
        - Description: Use the GET HTTP method with the same endpoint to retrieve the ID of the current KMIP master key.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/encryptionKey",
            path_params,
            query_params,
            None,
        )

    class RotateKmipMasterKeyIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster to which the encryption keys belongs.
        """

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique identifier of the project to which the encryption key belongs.
        """

    class RotateKmipMasterKeyIdQueryParams(BaseModel):
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

    def rotate_kmip_master_key_id(
        self,
        path_params: RotateKmipMasterKeyIdPathParams,
        query_params: Optional[RotateKmipMasterKeyIdQueryParams],
    ) -> dict[str, Any]:
        """
        ## Rotate the KMIP Master Key ID
        - Document: [Rotate KMIP Master Key ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/kmip-keys/rotate-master-key/)
        - Resource: `PUT /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/encryptionKey`
        - Description: Use the PUT HTTP method with the following endpoint to rotate the KMIP master key. Issue one PUT request for each shard and another PUT request for the config server replica set.
        """
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/encryptionKey",
            path_params,
            query_params,
            None,
        )
