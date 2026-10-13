
r"""Auto-generated client for KeyVaultResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *

class KeyVaultResource(BaseResource):
    r"""Client for KeyVaultResource resource.
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
        
        
        class AuthParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            
            jwt_claims: Optional[dict] = Field(default=None, serialization_alias="jwtClaims")
            r"""Claims that Ops Manager sends when it requests a JWT login from HashiCorp Vault. Required when `auth.mechanism` is `JWT`. Include the `user` and `role` claims.
            """
            
            mechanism: str = Field(serialization_alias="mechanism")
            r"""Authentication method that Ops Manager uses to connect to HashiCorp Vault. Ops Manager accepts the following values:

- `TOKEN`
- `JWT`
            """
            
            secret: str = Field(serialization_alias="secret")
            r"""Credential that Ops Manager uses to authenticate to HashiCorp Vault.

When `auth.mechanism` is `TOKEN`, set this value to the Vault token. When `auth.mechanism` is `JWT`, set this value to the PEM-formatted RSA private key that signs the JWT.

Ops Manager encrypts this value at rest and redacts it in API responses.
            """
            
        
        auth: AuthParams = Field(serialization_alias="auth")
        r"""Authentication details that Ops Manager uses to connect to HashiCorp Vault.
        """
        
        
        class CustomCertificatesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            
            cert_string: Optional[str] = Field(default=None, serialization_alias="certString")
            r"""Contents of the Certificate Authority PEM file. Required for each entry in `customCertificates`. Ops Manager redacts this value in API responses.
            """
            
            filename: Optional[str] = Field(default=None, serialization_alias="filename")
            r"""Name that identifies the Certificate Authority PEM file. Required for each entry in `customCertificates`.
            """
            
        
        custom_certificates: Optional[list[CustomCertificatesParams]] = Field(default=None, serialization_alias="customCertificates")
        r"""List of custom Certificate Authority certificates that Ops Manager uses for TLS verification when it connects to the HashiCorp Vault server.
        """
        
        
        friendly_name: str = Field(serialization_alias="friendlyName")
        r"""Human-readable label that identifies this key vault configuration. Ops Manager displays this value in the Key Vault list and in the Vault Name field.
        """
        
        
        type: str = Field(serialization_alias="type")
        r"""Key vault provider type. Ops Manager accepts only `HASHI_CORP`, which represents HashiCorp Vault.
        """
        
        
        url: str = Field(serialization_alias="url")
        r"""Address of the HashiCorp Vault server that Ops Manager connects to, such as `https://localhost:8200/`.
        """
        
    
    def create(self,
        
        
        query_params: Optional[CreateQueryParams],
        
        
        body_params: CreateBodyParams,
        
    ) -> dict[str, Any]:
        r"""
## Create One Key Vault Configuration
### Document:
[Create](https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/admin/keyvault/create-one-key-vault-configuration/)
### Endpoint:
`POST /keyVault`
### Description
Creates one key vault configuration that Ops Manager uses to read credentials from HashiCorp Vault.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/admin/keyVault",
            None,
            query_params,
            body_params,
        )
    
    
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        key_vault_id: str = Field(serialization_alias="KEY-VAULT-ID")
        r"""Unique identifier of the key vault configuration to delete.
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
## Delete One Key Vault Configuration
### Document:
[Delete](https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/admin/keyvault/delete-one-key-vault-configuration/)
### Endpoint:
`DELETE /keyVault/{KEY-VAULT-ID}`
### Description
Deletes one key vault configuration.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/admin/keyVault/{KEY-VAULT-ID}",
            path_params,
            query_params,
            None,
        )
    
    
    
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
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
## Get All Key Vault Configurations
### Document:
[Get All](https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/admin/keyvault/get-all-key-vault-configurations/)
### Endpoint:
`GET /keyVault`
### Description
Retrieves the configurations of all key vaults.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/keyVault",
            None,
            query_params,
            None,
        )
    
    
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        key_vault_id: str = Field(serialization_alias="KEY-VAULT-ID")
        r"""Unique identifier of the key vault configuration to retrieve.
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
## Get One Key Vault Configuration by ID
### Document:
[Get by ID](https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/admin/keyvault/get-one-key-vault-configuration-by-id/)
### Endpoint:
`GET /keyVault/{KEY-VAULT-ID}`
### Description
Retrieves the configuration of one key vault.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/keyVault/{KEY-VAULT-ID}",
            path_params,
            query_params,
            None,
        )
    
    
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        key_vault_id: str = Field(serialization_alias="KEY-VAULT-ID")
        r"""Unique identifier of the key vault configuration to update.
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
        
        
        class AuthParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            
            jwt_claims: Optional[dict] = Field(default=None, serialization_alias="jwtClaims")
            r"""Claims that Ops Manager sends when it requests a JWT login from HashiCorp Vault. Required when `auth.mechanism` is `JWT`. Include the `user` and `role` claims.
            """
            
            mechanism: Optional[str] = Field(default=None, serialization_alias="mechanism")
            r"""Authentication method that Ops Manager uses to connect to HashiCorp Vault. Provide this field only when you change the authentication method. If you omit this field, Ops Manager keeps the stored mechanism. Ops Manager accepts the following values:

- `TOKEN`
- `JWT`
            """
            
            secret: Optional[str] = Field(default=None, serialization_alias="secret")
            r"""Credential that Ops Manager uses to authenticate to HashiCorp Vault. Required when you change `auth.mechanism`, because Ops Manager cannot reuse a credential across authentication methods.

When `auth.mechanism` is `TOKEN`, set this value to the Vault token. When `auth.mechanism` is `JWT`, set this value to the PEM-formatted RSA private key that signs the JWT.

When you don't change `auth.mechanism`, omit this field or send the redacted value that Ops Manager returns to keep the stored credential. Ops Manager encrypts this value at rest and redacts it in API responses.
            """
            
        
        auth: Optional[AuthParams] = Field(default=None, serialization_alias="auth")
        r"""Authentication details that Ops Manager uses to connect to HashiCorp Vault.
        """
        
        
        class CustomCertificatesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            
            cert_string: Optional[str] = Field(default=None, serialization_alias="certString")
            r"""Contents of the Certificate Authority PEM file. Required for each entry in `customCertificates`. To keep a stored certificate, send the redacted value that Ops Manager returns. Ops Manager redacts this value in API responses.
            """
            
            filename: Optional[str] = Field(default=None, serialization_alias="filename")
            r"""Name that identifies the Certificate Authority PEM file. Required for each entry in `customCertificates`.
            """
            
        
        custom_certificates: Optional[list[CustomCertificatesParams]] = Field(default=None, serialization_alias="customCertificates")
        r"""List of custom Certificate Authority certificates that Ops Manager uses for TLS verification when it connects to the HashiCorp Vault server.
        """
        
        
        friendly_name: Optional[str] = Field(default=None, serialization_alias="friendlyName")
        r"""Human-readable label that identifies this key vault configuration. Ops Manager displays this value in the Key Vault list and in the Vault Name field.
        """
        
        
        type: Optional[str] = Field(default=None, serialization_alias="type")
        r"""Key vault provider type. Ops Manager accepts only `HASHI_CORP`, which represents HashiCorp Vault.
        """
        
        
        url: Optional[str] = Field(default=None, serialization_alias="url")
        r"""Address of the HashiCorp Vault server that Ops Manager connects to, such as `https://localhost:8200/`.
        """
        
    
    def update(self,
        
        path_params: UpdatePathParams,
        
        
        query_params: Optional[UpdateQueryParams],
        
        
        body_params: Optional[UpdateBodyParams],
        
    ) -> dict[str, Any]:
        r"""
## Update One Key Vault Configuration
### Document:
[Update](https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/admin/keyvault/update-one-key-vault-configuration/)
### Endpoint:
`PATCH /keyVault/{KEY-VAULT-ID}`
### Description
Updates one key vault configuration. Ops Manager merges the fields that you send with the stored configuration and leaves the fields that you omit unchanged.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/admin/keyVault/{KEY-VAULT-ID}",
            path_params,
            query_params,
            body_params,
        )
    
