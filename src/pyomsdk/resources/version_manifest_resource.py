"""Auto-generated client for VersionManifestResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class VersionManifestResource(BaseResource):
    """Client for VersionManifestResource resource."""

    class RetrieveQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

    def retrieve(
        self,
        query_params: Optional[RetrieveQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve the Ops Manager Version Manifest
        ### Document:
        [Retrieve](https://www.mongodb.com/docs/ops-manager/current/reference/api/version-manifest/get-om-version-manifest/)
        ### Endpoint:
        `GET /unauth/versionManifest`
        ### Description
        Use this resource to retrieve the version manifest that Ops Manager is configured to use.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/unauth/versionManifest",
            None,
            query_params,
            None,
        )

    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

    def update(
        self,
        query_params: Optional[UpdateQueryParams],
    ) -> dict[str, Any]:
        """
        ## Update the Version Manifest
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/version-manifest/update-version-manifest/)
        ### Endpoint:
        `PUT /versionManifest`
        ### Description
        Use this resource to upload the latest version manifest from MongoDB, Inc.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/versionManifest",
            None,
            query_params,
            None,
        )
