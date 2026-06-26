r"""Auto-generated client for TeamsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class TeamsResource(BaseResource):
    r"""Client for TeamsResource resource."""

    class AddUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        r"""The unique identifier for the
[organization](/docs/ops-manager/current/organizations-projects/#std-label-organizations)
you want to associate the team with.
        """

        team_id: str = Field(serialization_alias="TEAM-ID")
        r"""The name of the [team](/docs/ops-manager/current/organizations-projects/#std-label-teams) you want to add
users to.
        """

    class AddUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    class AddUsersBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        id: Optional[str] = Field(default=None, serialization_alias="id")
        r"""The unique ID of the user you want to add to the team
        """

    def add_users(
        self,
        path_params: AddUsersPathParams,
        query_params: Optional[AddUsersQueryParams],
        body_params: list[Optional[AddUsersBodyParams]],
    ) -> dict[str, Any]:
        r"""
        ## Add Users to Team
        ### Document:
        [Add Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-add-user/)
        ### Endpoint:
        `POST /orgs/{ORG-ID}/teams/{TEAM-ID}/users`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}/users",
            path_params,
            query_params,
            body_params,
        )

    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        r"""The unique identifier for the
[organization](/docs/ops-manager/current/organizations-projects/#std-label-organizations)
with which you want to associate the team.
        """

    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        name: Optional[str] = Field(default=None, serialization_alias="name")
        r"""The name of the [team](/docs/ops-manager/current/organizations-projects/#std-label-teams) you want to create.
        """

    def create(
        self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        r"""
        ## Create a Team
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-create-one/)
        ### Endpoint:
        `POST /orgs/{ORG-ID}/teams`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/orgs/{ORG-ID}/teams",
            path_params,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        r"""The unique identifier for the
[organization](/docs/ops-manager/current/organizations-projects/#std-label-organizations)
associated with the team.
        """

        team_id: str = Field(serialization_alias="TEAM-ID")
        r"""The unique identifier of the [team](/docs/ops-manager/current/organizations-projects/#std-label-teams) you want
to delete.
        """

    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def delete(
        self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Delete One Team
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-delete-one/)
        ### Endpoint:
        `DELETE /orgs/{ORG-ID}/teams/{TEAM-ID}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllTeamUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        r"""The unique identifier for the
[organization](/docs/ops-manager/current/tutorial/manage-organizations/) associated
with the team.
        """

        team_id: str = Field(serialization_alias="TEAM-ID")
        r"""The unique identifier of the [team](/docs/ops-manager/current/tutorial/manage-users/#std-label-manage-teams)
whose user membership you want to retrieve.
        """

    class GetAllTeamUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `envelope : true` in the
query.

For endpoints that return a list of results, the `content`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag that indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_all_team_users(
        self,
        path_params: GetAllTeamUsersPathParams,
        query_params: Optional[GetAllTeamUsersQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get All Users Assigned to a Team
        ### Document:
        [Get All Team Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-all-users/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}/teams/{TEAM-ID}/users`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}/users",
            path_params,
            query_params,
            None,
        )

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        r"""The unique identifier for the
[organization](/docs/ops-manager/current/organizations-projects/#std-label-organizations) whose teams you want
to retrieve.
        """

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `envelope : true` in the
query.

For endpoints that return a list of results, the `content`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag that indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_all(
        self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get All Teams
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-all/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}/teams`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{ORG-ID}/teams",
            path_params,
            query_params,
            None,
        )

    class GetOneByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        r"""The unique identifier for the
[organization](/docs/ops-manager/current/organizations-projects/#std-label-organizations)
associated with the team.
        """

        team_id: str = Field(serialization_alias="TEAM-ID")
        r"""The unique identifier of the [team](/docs/ops-manager/current/organizations-projects/#std-label-teams)
whose information you want to retrieve.
        """

    class GetOneByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_one_by_id(
        self,
        path_params: GetOneByIdPathParams,
        query_params: Optional[GetOneByIdQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get One Team by ID
        ### Document:
        [Get One by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-one-by-id/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}/teams/{TEAM-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            None,
        )

    class GetOneByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        r"""The unique identifier for the
[organization](/docs/ops-manager/current/organizations-projects/#std-label-organizations)
associated with the team.
        """

        team_name: str = Field(serialization_alias="TEAM-NAME")
        r"""The name of the [team](/docs/ops-manager/current/organizations-projects/#std-label-teams) whose
information you want to retrieve.
        """

    class GetOneByNameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def get_one_by_name(
        self,
        path_params: GetOneByNamePathParams,
        query_params: Optional[GetOneByNameQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Get One Team by Name
        ### Document:
        [Get One by Name](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-one-by-name/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}/teams/byName/{TEAM-NAME}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{ORG-ID}/teams/byName/{TEAM-NAME}",
            path_params,
            query_params,
            None,
        )

    class RemoveUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        r"""The unique identifier for the [organization](/docs/ops-manager/current/organizations-projects/#std-label-organizations)
that contains the team from which you want to remove a MongoDB
user.
        """

        team_id: str = Field(serialization_alias="TEAM-ID")
        r"""The unique identifier of the [team](/docs/ops-manager/current/organizations-projects/#std-label-teams) from which you want to remove
a MongoDB user.
        """

        user_id: str = Field(serialization_alias="USER-ID")
        r"""The unique identifier of the MongoDB [user](/docs/ops-manager/current/tutorial/manage-users/#std-label-add-users) that
you want to remove from the specified team.
        """

    class RemoveUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    def remove_user(
        self,
        path_params: RemoveUserPathParams,
        query_params: Optional[RemoveUserQueryParams],
    ) -> dict[str, Any]:
        r"""
        ## Remove a User from a Team
        ### Document:
        [Remove User](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-remove-user/)
        ### Endpoint:
        `DELETE /orgs/{ORG-ID}/teams/{TEAM-ID}/users/{USER-ID}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}/users/{USER-ID}",
            path_params,
            query_params,
            None,
        )

    class RenamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        r"""The unique identifier for the
[organization](/docs/ops-manager/current/tutorial/manage-organizations/) associated
with the team that you want to rename.
        """

        team_id: str = Field(serialization_alias="TEAM-ID")
        r"""The unique identifier of the [team](/docs/ops-manager/current/tutorial/manage-users/) that you want to rename.
        """

    class RenameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether or not to wrap the response in an
envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set **envelope=true** in the
query.

For endpoints that return one result, the response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

    class RenameBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        name: str = Field(serialization_alias="name")
        r"""The new name of the team.
        """

    def rename(
        self,
        path_params: RenamePathParams,
        query_params: Optional[RenameQueryParams],
        body_params: RenameBodyParams,
    ) -> dict[str, Any]:
        r"""
        ## Rename a Team
        ### Document:
        [Rename](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-rename-one/)
        ### Endpoint:
        `PATCH /orgs/{ORG-ID}/teams/{TEAM-ID}`
        ### Description
        No description.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            body_params,
        )

    class UpdateRolesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the
[project](/docs/ops-manager/current/tutorial/manage-projects/)
associated with this team.
        """

        team_id: str = Field(serialization_alias="TEAM-ID")
        r"""Unique identifier of the [team](/docs/ops-manager/current/tutorial/manage-users/#std-label-manage-teams) for which
you want to update roles.
        """

    class UpdateRolesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(default=None, serialization_alias="envelope")
        r"""Flag that specifies whether or not to wrap the response in an
[envelope.](/docs/ops-manager/current/core/api/#std-label-api-envelope)

Defaults to `false`.
        """

        pretty: Optional[bool] = Field(default=None, serialization_alias="pretty")
        r"""Flag that specifies whether or not to return a "pretty-printed"
JSON document.

Defaults to `false`.
        """

    class UpdateRolesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        role_names: list[GroupRole] = Field(serialization_alias="roleNames")
        r"""[Project roles](/docs/ops-manager/current/reference/user-roles/) you want to
assign the given team.
        """

    def update_roles(
        self,
        path_params: UpdateRolesPathParams,
        query_params: Optional[UpdateRolesQueryParams],
        body_params: list[UpdateRolesBodyParams],
    ) -> dict[str, Any]:
        r"""
        ## Update Team Roles in One Project
        ### Document:
        [Update Roles](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-update-roles/)
        ### Endpoint:
        `PATCH /groups/{PROJECT-ID}/teams/{TEAM-ID}`
        ### Description
        No description.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/groups/{PROJECT-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            body_params,
        )
