"""Auto-generated client for MaintenanceWindowsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class MaintenanceWindowsResource(BaseResource):
    """Client for MaintenanceWindowsResource resource."""

    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier of the project.
        """

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

        alert_type_names: list[str] = Field(serialization_alias="alertTypeNames")
        """Alert types to silence during maintenance window. For example: HOST, REPLICA_SET, CLUSTER, AGENT, BACKUP
        """

        description: Optional[str] = Field("None", serialization_alias="description")
        """Description of the maintenance window.
        """

        end_date: str = Field("None", serialization_alias="endDate")
        """Timestamp in ISO 8601 date and time format in UTC when the maintenance window ends.
        """

        start_date: str = Field("None", serialization_alias="startDate")
        """Timestamp in ISO 8601 date and time format in UTC when the maintenance window starts.
        """

    def create(
        self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Maintenance Window
        - Document: [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-create-one/)
        - Resource: `POST /groups/{PROJECT-ID}/maintenanceWindows/`
        - Description: Create one maintenance window. Ops Manager turns off alert notifications for certain alert types for a period of time you specify to allow maintenance to occur.
        """
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/maintenanceWindows/",
            path_params,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        mw_id: str = Field("None", serialization_alias="MW-ID")
        """Unique identifier of the maintenance window you want to delete.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier of the project.
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
        ## Delete One Maintenance Window
        - Document: [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-delete-one/)
        - Resource: `DELETE /groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}`
        - Description: Delete one maintenance window with an end date in the future.
        """
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier of the project.
        """

    class GetAllQueryParams(BaseModel):
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

    def get_all(
        self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Maintenance Windows
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-get-all/)
        - Resource: `GET /groups/{PROJECT-ID}/maintenanceWindows/`
        - Description: Retrieve all maintenance windows with end dates in the future.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/maintenanceWindows/",
            path_params,
            query_params,
            None,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        mw_id: str = Field("None", serialization_alias="MW-ID")
        """Unique identifier of the maintenance window you want to retrieve.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier of the project.
        """

    class GetOneQueryParams(BaseModel):
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

    def get_one(
        self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Maintenance Window
        - Document: [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-get-one/)
        - Resource: `GET /groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}`
        - Description: Retrieve one maintenance window with an end date in the future.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        mw_id: str = Field("None", serialization_alias="MW-ID")
        """Unique identifier of the maintenance window you want to update.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier of the project.
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

        alert_type_names: list[str] = Field(serialization_alias="alertTypeNames")
        """Alert types to silence during maintenance window. For example: HOST, REPLICA_SET, CLUSTER, AGENT, BACKUP
        """

        description: Optional[str] = Field("None", serialization_alias="description")
        """Description of the maintenance window.
        """

        end_date: str = Field("None", serialization_alias="endDate")
        """Timestamp in ISO 8601 date and time format in UTC when the maintenance window ends.
        """

        start_date: str = Field("None", serialization_alias="startDate")
        """Timestamp in ISO 8601 date and time format in UTC when the maintenance window starts.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Maintenance Window
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-update-one/)
        - Resource: `PATCH /groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}`
        - Description: Update one maintenance window with an end date in the future.
        """
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}",
            path_params,
            query_params,
            body_params,
        )
