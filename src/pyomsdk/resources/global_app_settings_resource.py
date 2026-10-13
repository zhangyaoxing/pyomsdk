
r"""Auto-generated client for GlobalAppSettingsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *

class GlobalAppSettingsResource(BaseResource):
    r"""Client for GlobalAppSettingsResource resource.
    """
    
    
    
    class GetSettingsQueryParams(BaseModel):
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
        
    
    
    def get_settings(self,
        
        
        query_params: Optional[GetSettingsQueryParams],
        
        
    ) -> dict[str, Any]:
        r"""
## Get Global App Settings
### Document:
[Get Settings](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/settings/get-global-app-settings/)
### Endpoint:
`GET /admin/settings`
### Description
Retrieves the global application settings for an Ops Manager installation.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/admin/settings",
            None,
            query_params,
            None,
        )
    
    
    
    class UpdateSettingsQueryParams(BaseModel):
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
        
    
    
    class UpdateSettingsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        db_properties: dict = Field(serialization_alias="dbProperties")
        r"""Key-value pairs of global app settings to update or add. Settings not included in the request remain unchanged. To remove a setting, set its value to `null`.
        """
        
    
    def update_settings(self,
        
        
        query_params: Optional[UpdateSettingsQueryParams],
        
        
        body_params: UpdateSettingsBodyParams,
        
    ) -> dict[str, Any]:
        r"""
## Update Global App Settings
### Document:
[Update Settings](https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/settings/update-global-app-settings/)
### Endpoint:
`PATCH /admin/settings`
### Description
Updates the global application settings for an Ops Manager installation. Include only the settings you want to change. Ops Manager leaves all other settings unchanged.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/admin/settings",
            None,
            query_params,
            body_params,
        )
    
