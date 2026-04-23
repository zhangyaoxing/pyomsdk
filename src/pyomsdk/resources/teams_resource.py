"""Auto-generated client for TeamsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class TeamsResource(BaseResource):
    """Client for TeamsResource resource."""

    class AddUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field("None", serialization_alias="ORG-ID")
        """The unique identifier for the organization you want to associate the team with.
        """

        team_id: str = Field("None", serialization_alias="TEAM-ID")
        """The name of the team you want to add users to.
        """

    class AddUsersQueryParams(BaseModel):
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

    class AddUsersBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        id: Optional[str] = Field("None", serialization_alias="id")
        """The unique ID of the user you want to add to the team
        """

    def add_users(
        self,
        path_params: AddUsersPathParams,
        query_params: Optional[AddUsersQueryParams],
        body_params: list[Optional[AddUsersBodyParams]],
    ) -> dict[str, Any]:
        """
        ## Add Users to Team
        - Document: [Add Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-add-user/)
        - Resource: `POST /orgs/{ORG-ID}/teams/{TEAM-ID}/users`
        - Description: No description.
        """
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}/users",
            path_params,
            query_params,
            body_params,
        )

    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field("None", serialization_alias="ORG-ID")
        """The unique identifier for the organization with which you want to associate the team.
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

        name: Optional[str] = Field("None", serialization_alias="name")
        """The name of the team you want to create.
        """

    def create(
        self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Create a Team
        - Document: [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-create-one/)
        - Resource: `POST /orgs/{ORG-ID}/teams`
        - Description: No description.
        """
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/teams",
            path_params,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field("None", serialization_alias="ORG-ID")
        """The unique identifier for the organization associated with the team.
        """

        team_id: str = Field("None", serialization_alias="TEAM-ID")
        """The unique identifier of the team you want to delete.
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
        ## Delete One Team
        - Document: [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-delete-one/)
        - Resource: `DELETE /orgs/{ORG-ID}/teams/{TEAM-ID}`
        - Description: No description.
        """
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllTeamUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field("None", serialization_alias="ORG-ID")
        """The unique identifier for the organization associated with the team.
        """

        team_id: str = Field("None", serialization_alias="TEAM-ID")
        """The unique identifier of the team whose user membership you want to retrieve.
        """

    class GetAllTeamUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

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

    def get_all_team_users(
        self,
        path_params: GetAllTeamUsersPathParams,
        query_params: Optional[GetAllTeamUsersQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Users Assigned to a Team
        - Document: [Get All Team Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-all-users/)
        - Resource: `GET /orgs/{ORG-ID}/teams/{TEAM-ID}/users`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}/users",
            path_params,
            query_params,
            None,
        )

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field("None", serialization_alias="ORG-ID")
        """The unique identifier for the organization whose teams you want to retrieve.
        """

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

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
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Teams
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-all/)
        - Resource: `GET /orgs/{ORG-ID}/teams`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams",
            path_params,
            query_params,
            None,
        )

    class GetOneByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field("None", serialization_alias="ORG-ID")
        """The unique identifier for the organization associated with the team.
        """

        team_id: str = Field("None", serialization_alias="TEAM-ID")
        """The unique identifier of the team whose information you want to retrieve.
        """

    class GetOneByIdQueryParams(BaseModel):
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

    def get_one_by_id(
        self,
        path_params: GetOneByIdPathParams,
        query_params: Optional[GetOneByIdQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Team by ID
        - Document: [Get One by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-one-by-id/)
        - Resource: `GET /orgs/{ORG-ID}/teams/{TEAM-ID}`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            None,
        )

    class GetOneByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field("None", serialization_alias="ORG-ID")
        """The unique identifier for the organization associated with the team.
        """

        team_name: str = Field("None", serialization_alias="TEAM-NAME")
        """The name of the team whose information you want to retrieve.
        """

    class GetOneByNameQueryParams(BaseModel):
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

    def get_one_by_name(
        self,
        path_params: GetOneByNamePathParams,
        query_params: Optional[GetOneByNameQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Team by Name
        - Document: [Get One by Name](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-one-by-name/)
        - Resource: `GET /orgs/{ORG-ID}/teams/byName/{TEAM-NAME}`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams/byName/{TEAM-NAME}",
            path_params,
            query_params,
            None,
        )

    class RemoveUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field("None", serialization_alias="ORG-ID")
        """The unique identifier for the organization that contains the team from which you want to remove a MongoDB user.
        """

        team_id: str = Field("None", serialization_alias="TEAM-ID")
        """The unique identifier of the team from which you want to remove a MongoDB user.
        """

        user_id: str = Field("None", serialization_alias="USER-ID")
        """The unique identifier of the MongoDB user that you want to remove from the specified team.
        """

    class RemoveUserQueryParams(BaseModel):
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

    def remove_user(
        self,
        path_params: RemoveUserPathParams,
        query_params: Optional[RemoveUserQueryParams],
    ) -> dict[str, Any]:
        """
        ## Remove a User from a Team
        - Document: [Remove User](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-remove-user/)
        - Resource: `DELETE /orgs/{ORG-ID}/teams/{TEAM-ID}/users/{USER-ID}`
        - Description: No description.
        """
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}/users/{USER-ID}",
            path_params,
            query_params,
            None,
        )

    class RenamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field("None", serialization_alias="ORG-ID")
        """The unique identifier for the organization associated with the team that you want to rename.
        """

        team_id: str = Field("None", serialization_alias="TEAM-ID")
        """The unique identifier of the team that you want to rename.
        """

    class RenameQueryParams(BaseModel):
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

    class RenameBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        name: str = Field("None", serialization_alias="name")
        """The new name of the team.
        """

    def rename(
        self,
        path_params: RenamePathParams,
        query_params: Optional[RenameQueryParams],
        body_params: RenameBodyParams,
    ) -> dict[str, Any]:
        """
        ## Rename a Team
        - Document: [Rename](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-rename-one/)
        - Resource: `PATCH /orgs/{ORG-ID}/teams/{TEAM-ID}`
        - Description: No description.
        """
        return self._request(
            "PATCH",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            body_params,
        )

    class UpdateRolesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier of the project associated with this team.
        """

        team_id: str = Field("None", serialization_alias="TEAM-ID")
        """Unique identifier of the team for which you want to update roles.
        """

    class UpdateRolesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """Flag that specifies whether or not to wrap the response in an envelope.

Defaults to false.
        """

        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """Flag that specifies whether or not to return a "pretty-printed" JSON document.

Defaults to false.
        """

    class UpdateRolesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        role_names: GroupRole = Field(serialization_alias="roleNames")
        """Project roles you want to assign the given team.
        """

    def update_roles(
        self,
        path_params: UpdateRolesPathParams,
        query_params: Optional[UpdateRolesQueryParams],
        body_params: list[UpdateRolesBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update Team Roles in One Project
        - Document: [Update Roles](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-update-roles/)
        - Resource: `PATCH /groups/{PROJECT-ID}/teams/{TEAM-ID}`
        - Description: No description.
        """
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            body_params,
        )
