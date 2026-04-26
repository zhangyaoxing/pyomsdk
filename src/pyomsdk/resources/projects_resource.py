"""Auto-generated client for ProjectsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class ProjectsResource(BaseResource):
    """Client for ProjectsResource resource."""

    class AddExistingUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) The unique identifier for the project.
        """

    class AddExistingUsersQueryParams(BaseModel):
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

    class AddExistingUsersBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        id: Optional[str] = Field(None, serialization_alias="id")
        """The unique identifier for an existing user.
        """

        class RolesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            group_id: Optional[str] = Field(None, serialization_alias="groupId")
            """The unique identifier for the project role.
            """

            role_name: Optional[str] = Field(None, serialization_alias="roleName")
            """The display name for the user role.
            """

        roles: Optional[list[RolesParams]] = Field(None, serialization_alias="roles")
        """The roles to which this user is assigned.
        """

    def add_existing_users(
        self,
        path_params: AddExistingUsersPathParams,
        query_params: Optional[AddExistingUsersQueryParams],
        body_params: Optional[AddExistingUsersBodyParams],
    ) -> dict[str, Any]:
        """
        ## Add Existing Users to One Project
        ### Document:
        [Add Existing Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/add-users-to-one-group/)
        ### Endpoint:
        `POST /groups/{PROJECT-ID}/users`
        ### Description
        This resource adds users who exist in Ops Manager to another project. It does not create new users and add them to a project. By default, users first receive an invitation to the project. You can add users directly to a project only if you set the mms.user.bypassInviteForExistingUsers setting to true.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{PROJECT-ID}/users",
            path_params,
            query_params,
            body_params,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) The unique identifier for the project.
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

        ldap_group_mappings: Optional[list[dict]] = Field(
            None, serialization_alias="ldapGroupMappings"
        )
        """For LDAP-backed Ops Manager, the mappings of LDAP groups to Ops Manager project roles. Only accepted for LDAP-backed Ops Manager.
        """

        name: Optional[str] = Field(None, serialization_alias="name")
        """The new name for the project.
        """

        tags: Optional[list[str]] = Field(None, serialization_alias="tags")
        """The tags assigned to the project for use in programmatically identifying the project.

To view tags you must have either the Global Read Only or Global Owner role.

To create or edit tags, you must be a Global Owner.

A project can have up to 10 tags. Tags follow these rules:

Are case-sensitive

Can contain these characters:

A through Z

0 through 9

. (period)

_ (underscore)

- (dash)

Are limited to 32 characters
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update One Project
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/change-one-group-name/)
        ### Endpoint:
        `PATCH /groups/{PROJECT-ID}`
        ### Description
        Use this endpoint to make any of the following changes to one project:
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/groups/{PROJECT-ID}",
            path_params,
            query_params,
            body_params,
        )

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

        name: str = Field(serialization_alias="name")
        """Human-readable label that identifies the project.
        """

        org_id: str = Field(serialization_alias="orgId")
        """Unique 24-hexadecimal digit string that identifies the organization within which to create the project.

Ops Manager set the oldest Organization Owner of the specified organization as a Project Owner for the new project.
        """

    def create(
        self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Project
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/create-one-group/)
        ### Endpoint:
        `POST /groups`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/groups",
            None,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) The unique identifier for the project.
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
        ## Delete One Project
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/delete-one-group/)
        ### Endpoint:
        `DELETE /groups/{PROJECT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/groups/{PROJECT-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
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
        ## Get All Projects for the Current User
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-all-groups-for-current-user/)
        ### Endpoint:
        `GET /groups`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups",
            None,
            query_params,
            None,
        )

    class GetBySpecificTagsForTheCurrentUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        tag: Optional[str] = Field(None, serialization_alias="tag")
        """The tags assigned to the project for use in programmatically identifying the project.

To view tags you must have the Project Read Only role.

To create or edit tags you must have the Project Automation Admin role.
        """

    def get_by_specific_tags_for_the_current_user(
        self,
        query_params: Optional[GetBySpecificTagsForTheCurrentUserQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Projects with Specific Tags for the Current User
        ### Document:
        [Get by Specific Tags for the Current User](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-all-groups-with-specific-tags-for-current-user/)
        ### Endpoint:
        `GET /groups`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups",
            None,
            query_params,
            None,
        )

    class GetAllUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for the project.
        """

    class GetAllUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        flatten_teams: Optional[bool] = Field(None, serialization_alias="flattenTeams")
        """Flag that indicates whether the returned list should include users who belong to a team assigned a role in this project. You may not have assigned the individual users a role in this project.

If this flag is set to false, the endpoint returns only users that were assigned a role in the project.

If this flag is set to true, the endpoint returns both users that were assigned roles in the project and users who are members of teams that were assigned roles in the project.
        """

        include_org_users: Optional[bool] = Field(None, serialization_alias="includeOrgUsers")
        """Flag that indicates whether the returned list should include users with implicit access to the project through the Organization Owner or Organization Read Only role. You might not have assigned the individual users a role in this project.

If this flag is set to false, the endpoint returns only users who are assigned a role in the project.

If this flag is set to true, the endpoint returns both users who are assigned roles in the project and users who have implicit access to the project through their organization role.

The default value is false.
        """

    def get_all_users(
        self,
        path_params: GetAllUsersPathParams,
        query_params: Optional[GetAllUsersQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Users in One Project
        ### Document:
        [Get All Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-all-users-in-one-group/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/users`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/users",
            path_params,
            query_params,
            None,
        )

    class GetByAgentApiKeyPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        agent_api_key: str = Field(serialization_alias="AGENT-API-KEY")
        """(Required.) The agent API key
        """

    class GetByAgentApiKeyQueryParams(BaseModel):
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

    def get_by_agent_api_key(
        self,
        path_params: GetByAgentApiKeyPathParams,
        query_params: Optional[GetByAgentApiKeyQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Project by Agent API Key
        ### Document:
        [Get by Agent API Key](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-one-group-by-agent-api-key/)
        ### Endpoint:
        `GET /groups/byAgentApiKey/{AGENT-API-KEY}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/byAgentApiKey/{AGENT-API-KEY}",
            path_params,
            query_params,
            None,
        )

    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) The unique identifier for the project.
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
        ## Get One Project by ID
        ### Document:
        [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-one-group-by-id/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}",
            path_params,
            query_params,
            None,
        )

    class GetByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_name: str = Field(serialization_alias="GROUP-NAME")
        """(Required.) The name of the project.
        """

    class GetByNameQueryParams(BaseModel):
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

    def get_by_name(
        self,
        path_params: GetByNamePathParams,
        query_params: Optional[GetByNameQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Project by Name
        ### Document:
        [Get by Name](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-one-group-by-name/)
        ### Endpoint:
        `GET /groups/byName/{GROUP-NAME}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/byName/{GROUP-NAME}",
            path_params,
            query_params,
            None,
        )

    class AddTeamsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """The unique identifier for the project to which you are adding the team or teams.
        """

    class AddTeamsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag that indicates whether the response body should be in a prettyprint format.
        """

    class AddTeamsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        role_names: Optional[GroupRole] = Field(None, serialization_alias="roleNames")
        """Each object in the array represents a project role you want to assign to the team.

The valid roles and their associated mappings are:

GROUP_OWNER - Project Owner

GROUP_READ_ONLY - Project Read Only

GROUP_DATA_ACCESS_ADMIN - Project Data Access Admin

GROUP_DATA_ACCESS_READ_WRITE - Project Data Access Read/Write

GROUP_DATA_ACCESS_READ_ONLY - Project Data Access Read Only

GROUP_MONITORING_ADMIN - Project Monitoring Admin

GROUP_BACKUP_ADMIN - Project Backup Admin

GROUP_AUTOMATION_ADMIN - Project Automation Admin

GROUP_USER_ADMIN - Project User Admin
        """

        team_id: Optional[str] = Field(None, serialization_alias="teamId")
        """The unique identifier of the team you want to associate with the project. The team and project must share the same parent organization.
        """

    def add_teams(
        self,
        path_params: AddTeamsPathParams,
        query_params: Optional[AddTeamsQueryParams],
        body_params: list[Optional[AddTeamsBodyParams]],
    ) -> dict[str, Any]:
        """
        ## Add Teams to a Project
        ### Document:
        [Add Teams](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/project-add-team/)
        ### Endpoint:
        `POST /groups/{PROJECT-ID}/teams`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{PROJECT-ID}/teams",
            path_params,
            query_params,
            body_params,
        )

    class GetAllTeamsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """The unique identifier for the project.
        """

    class GetAllTeamsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag that indicates whether the response body should be in a prettyprint format.
        """

    def get_all_teams(
        self,
        path_params: GetAllTeamsPathParams,
        query_params: Optional[GetAllTeamsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Teams in One Project
        ### Document:
        [Get All Teams](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/project-get-teams/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/teams`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/teams",
            path_params,
            query_params,
            None,
        )

    class RemoveUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) The unique identifier for the project.
        """

        user_id: str = Field(serialization_alias="USER-ID")
        """(Required.) The unique identifier for the user in {PROJECT-ID}.
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
        ## Remove One User from One Project
        ### Document:
        [Remove User](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/remove-one-user-from-one-group/)
        ### Endpoint:
        `DELETE /groups/{PROJECT-ID}/users/{USER-ID}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/groups/{PROJECT-ID}/users/{USER-ID}",
            path_params,
            query_params,
            None,
        )

    class CreateInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the project.
        """

    class CreateInvitationQueryParams(BaseModel):
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

    class CreateInvitationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        roles: Optional[list[str]] = Field(None, serialization_alias="roles")
        """List of Ops Manager project roles to assign to the invited user. If the user accepts the invitation, Ops Manager assigns these roles to them. Specify one or more of the following values:

Role Value in API
	
Role



GROUP_AUTOMATION_ADMIN

	

Project Automation Admin




GROUP_BACKUP_ADMIN

	

Project Backup Admin




GROUP_DATA_ACCESS_ADMIN

	

Project Data Access Admin




GROUP_DATA_ACCESS_READ_ONLY

	

Project Data Access Read Only




GROUP_DATA_ACCESS_READ_WRITE

	

Project Data Access Read/Write




GROUP_MONITORING_ADMIN

	

Project Monitoring Admin




GROUP_OWNER

	

Project Owner




GROUP_READ_ONLY

	

Project Read Only




GROUP_USER_ADMIN

	

Project User Admin
        """

        username: Optional[str] = Field(None, serialization_alias="username")
        """Email address to which Ops Manager sent the invitation. The user uses this email address as their Ops Manager username if they accept this invitation.
        """

    def create_invitation(
        self,
        path_params: CreateInvitationPathParams,
        query_params: Optional[CreateInvitationQueryParams],
        body_params: Optional[CreateInvitationBodyParams],
    ) -> dict[str, Any]:
        """
        ## Create One Project Invitation
        ### Document:
        [Create Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/create-one-invitation/)
        ### Endpoint:
        `POST /groups/{GROUP-ID}/invites/`
        ### Description
        Retrieve details for one pending invitation to the specified Ops Manager project.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{GROUP-ID}/invites/",
            path_params,
            query_params,
            body_params,
        )

    class DeleteInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the project.
        """

        invitation_id: str = Field(serialization_alias="INVITATION-ID")
        """Unique 24-hexadecimal digit string that identifies the invitation.
        """

    class DeleteInvitationQueryParams(BaseModel):
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

    def delete_invitation(
        self,
        path_params: DeleteInvitationPathParams,
        query_params: Optional[DeleteInvitationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Project Invitation
        ### Document:
        [Delete Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/delete-one-invitation/)
        ### Endpoint:
        `DELETE /groups/{GROUP-ID}/invites/{INVITATION-ID}`
        ### Description
        Deletes one pending invitation to the Ops Manager project that you specify. You can't delete an invitation that a user has accepted.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/groups/{GROUP-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllInvitationsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the project.
        """

    class GetAllInvitationsQueryParams(BaseModel):
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

        username: Optional[str] = Field(None, serialization_alias="username")
        """Email address of the invited user. This is the address to which Ops Manager sent the invite.

If omitted, Ops Manager returns all pending invitations.
        """

    def get_all_invitations(
        self,
        path_params: GetAllInvitationsPathParams,
        query_params: Optional[GetAllInvitationsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Project Invitations
        ### Document:
        [Get All Invitations](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/get-all-invitations/)
        ### Endpoint:
        `GET /groups/{GROUP-ID}/invites`
        ### Description
        Retrieves all pending invitations to the specified Ops Manager project.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{GROUP-ID}/invites",
            path_params,
            query_params,
            None,
        )

    class GetOneInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the project.
        """

        invitation_id: str = Field(serialization_alias="INVITATION-ID")
        """Unique 24-hexadecimal digit string that identifies the invitation.
        """

    class GetOneInvitationQueryParams(BaseModel):
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

    def get_one_invitation(
        self,
        path_params: GetOneInvitationPathParams,
        query_params: Optional[GetOneInvitationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Project Invitation
        ### Document:
        [Get One Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/get-one-invitation/)
        ### Endpoint:
        `GET /groups/{GROUP-ID}/invites/{INVITATION-ID}`
        ### Description
        Retrieve details for one pending invitation to the specified Ops Manager project.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{GROUP-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdateInvitationByInvitationIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the project.
        """

        invitation_id: str = Field(serialization_alias="INVITATION-ID")
        """Unique 24-hexadecimal digit string that identifies the invitation.
        """

    class UpdateInvitationByInvitationIdQueryParams(BaseModel):
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

    class UpdateInvitationByInvitationIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        roles: list[str] = Field(serialization_alias="roles")
        """Ops Manager roles to assign to the invited user.

If the user accepts the invitation, Ops Manager assigns these roles to them.

IMPORTANT: Ops Manager replaces the roles in the invitation with the roles that you provide in this request. Ensure that you include all roles that you want to assign the user in this request.
        """

    def update_invitation_by_invitation_id(
        self,
        path_params: UpdateInvitationByInvitationIdPathParams,
        query_params: Optional[UpdateInvitationByInvitationIdQueryParams],
        body_params: UpdateInvitationByInvitationIdBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Project Invitation by Invitation ID
        ### Document:
        [Update Invitation by Invitation ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/update-one-invitation-by-id/)
        ### Endpoint:
        `PATCH /groups/{GROUP-ID}/invites/{INVITATION-ID}`
        ### Description
        Updates one pending invitation by {INVITATION-ID} to the Ops Manager project that you specify.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/groups/{GROUP-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            body_params,
        )

    class UpdateInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique 24-hexadecimal digit string that identifies the project.
        """

    class UpdateInvitationQueryParams(BaseModel):
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

    class UpdateInvitationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        roles: list[str] = Field(serialization_alias="roles")
        """Ops Manager roles to assign to the invited user.

If the user accepts the invitation, Ops Manager assigns these roles to them.

IMPORTANT: Ops Manager replaces the roles in the invitation with the roles that you provide in this request. Ensure that you include all roles that you want to assign the user in this request.
        """

        username: str = Field(serialization_alias="username")
        """Username of the user whose invitation you want to update. In Ops Manager, an invited user's username is the email address to which Ops Manager sent the invitation.
        """

    def update_invitation(
        self,
        path_params: UpdateInvitationPathParams,
        query_params: Optional[UpdateInvitationQueryParams],
        body_params: UpdateInvitationBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Project Invitation
        ### Document:
        [Update Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/update-one-invitation/)
        ### Endpoint:
        `PATCH /groups/{GROUP-ID}/invites`
        ### Description
        Updates one pending invitation to the Ops Manager project that you specify.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/groups/{GROUP-ID}/invites",
            path_params,
            query_params,
            body_params,
        )

    class RemoveTeamPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """The unique identifier of the group from which you want to remove a team.
        """

        team_id: str = Field(serialization_alias="TEAM-ID")
        """The unique identifier of the team that you want to remove from the specified project.
        """

    class RemoveTeamQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(None, serialization_alias="envelope")
        """Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set "envelope" : true in the query.

For endpoints that return one result, response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body

For endpoints that return a list of results, the results object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
        """Page number (1-index based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

    def remove_team(
        self,
        path_params: RemoveTeamPathParams,
        query_params: Optional[RemoveTeamQueryParams],
    ) -> dict[str, Any]:
        """
        ## Remove One Team From One Project
        ### Document:
        [Remove Team](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-remove-from-project/)
        ### Endpoint:
        `DELETE /groups/{PROJECT-ID}/teams/{TEAM-ID}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/groups/{PROJECT-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            None,
        )
