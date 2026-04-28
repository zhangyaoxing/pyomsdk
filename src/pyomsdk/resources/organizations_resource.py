"""Auto-generated client for OrganizationsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class OrganizationsResource(BaseResource):
    """Client for OrganizationsResource resource."""

    class InviteUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        """Unique 24-hexadecimal digit string that identifies the organization.
        """

    class InviteUserQueryParams(BaseModel):
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

    class InviteUserBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        roles: list[OrgRole] = Field(serialization_alias="roles")
        """Ops Manager roles to assign to the invited user.

If the user accepts the invitation, Ops Manager assigns these roles to them.
        """

        team_ids: Optional[list[str]] = Field(None, serialization_alias="teamIds")
        """Unique 24-hexadecimal digit strings that identify the teams that you invite the user to join.
        """

        username: str = Field(serialization_alias="username")
        """Email address of the invited user. This is the address to which Ops Manager sends the invite.

If the user accepts the invitation, they log in to Ops Manager with this username.
        """

    def invite_user(
        self,
        path_params: InviteUserPathParams,
        query_params: Optional[InviteUserQueryParams],
        body_params: InviteUserBodyParams,
    ) -> dict[str, Any]:
        """
        ## Invite One User to an Ops Manager Organization
        ### Document:
        [Invite User](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/create-one-invitation/)
        ### Endpoint:
        `POST /orgs/{ORG-ID}/invites`
        ### Description
        Invites one user to the Ops Manager organization that you specify.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/orgs/{ORG-ID}/invites",
            path_params,
            query_params,
            body_params,
        )

    class DeleteInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        invitation_id: str = Field(serialization_alias="INVITATION-ID")
        """Unique 24-hexadecimal digit string that identifies the invitation.
        """

        org_id: str = Field(serialization_alias="ORG-ID")
        """Unique 24-hexadecimal digit string that identifies the organization.
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
        ## Delete One Organization Invitation
        ### Document:
        [Delete Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/delete-one-invitation/)
        ### Endpoint:
        `DELETE /orgs/{ORG-ID}/invites/{INVITATION-ID}`
        ### Description
        Deletes one pending invitation to the specified Ops Manager organization. You can't delete an invitation that a user has accepted.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/orgs/{ORG-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllInvitationsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        """Unique 24-hexadecimal digit string that identifies the organization.
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
        ## Get All Organization Invitations
        ### Document:
        [Get All Invitations](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/get-all-invitations/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}/invites`
        ### Description
        Retrieves all pending invitations to the specified Ops Manager organization.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{ORG-ID}/invites",
            path_params,
            query_params,
            None,
        )

    class GetOneInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        invitation_id: str = Field(serialization_alias="INVITATION-ID")
        """Unique 24-hexadecimal digit string that identifies the invitation.
        """

        org_id: str = Field(serialization_alias="ORG-ID")
        """Unique 24-hexadecimal digit string that identifies the organization.
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
        ## Get One Organization Invitation
        ### Document:
        [Get One Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/get-one-invitation/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}/invites/{INVITATION-ID}`
        ### Description
        Retrieve details for one pending invitation to the specified Ops Manager organization.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{ORG-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdateByInvitationIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        invitation_id: str = Field(serialization_alias="INVITATION-ID")
        """Unique 24-hexadecimal digit string that identifies the invitation.
        """

        org_id: str = Field(serialization_alias="ORG-ID")
        """Unique 24-hexadecimal digit string that identifies the organization.
        """

    class UpdateByInvitationIdQueryParams(BaseModel):
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

    class UpdateByInvitationIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        roles: list[OrgRole] = Field(serialization_alias="roles")
        """Ops Manager roles to assign to the invited user.

If the user accepts the invitation, Ops Manager assigns these roles to them.

IMPORTANT: Ops Manager replaces the roles in the invitation with the roles that you provide in this request. Ensure that you include all roles that you want to assign the user in this request.
        """

    def update_by_invitation_id(
        self,
        path_params: UpdateByInvitationIdPathParams,
        query_params: Optional[UpdateByInvitationIdQueryParams],
        body_params: UpdateByInvitationIdBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Organization Invitation by Invitation ID
        ### Document:
        [Update by Invitation ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/update-one-invitation-by-id/)
        ### Endpoint:
        `PATCH /orgs/{ORG-ID}/invites/{INVITATION-ID}`
        ### Description
        Updates one pending invitation by {INVITATION-ID} to the Ops Manager organization that you specify.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/orgs/{ORG-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            body_params,
        )

    class UpdateInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        """Unique 24-hexadecimal digit string that identifies the organization.
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

        roles: list[OrgRole] = Field(serialization_alias="roles")
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
        ## Update One Organization Invitation
        ### Document:
        [Update Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/update-one-invitation/)
        ### Endpoint:
        `PATCH /orgs/{ORG-ID}/invites`
        ### Description
        Updates one pending invitation to the Ops Manager organization that you specify.
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/orgs/{ORG-ID}/invites",
            path_params,
            query_params,
            body_params,
        )

    class CreateOrganizationQueryParams(BaseModel):
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

    class CreateOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        class LdapGroupMappingsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            ldap_groups: Optional[list[Any]] = Field(None, serialization_alias="ldapGroups")
            """LDAP group(s) that map to associate to the roleName.
            """

            role_name: Optional[OrgRole] = Field(None, serialization_alias="roleName")
            """Ops Manager organization role to map. Can specify from the following list:

ORG_READ_ONLY

ORG_MEMBER

ORG_OWNER

You cannot specify a global role, project role, or an organization billing admin role.
            """

        ldap_group_mappings: Optional[list[LdapGroupMappingsParams]] = Field(
            None, serialization_alias="ldapGroupMappings"
        )
        """Requires LDAP integration for Ops Manager.

Array of documents that specify the mapping between the Ops Manager Organization Roles and the LDAP groups.

If specifying ldapGroupMappings, mapping for ORG_OWNER role is required.
        """

        name: str = Field(serialization_alias="name")
        """Name of the organization you want to create.
        """

    def create_organization(
        self,
        query_params: Optional[CreateOrganizationQueryParams],
        body_params: CreateOrganizationBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Organization
        ### Document:
        [Create Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-create-one/)
        ### Endpoint:
        `POST /orgs`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/orgs",
            None,
            query_params,
            body_params,
        )

    class DeleteOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        """The unique identifier for the organization to delete.
        """

    class DeleteOrganizationQueryParams(BaseModel):
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

    def delete_organization(
        self,
        path_params: DeleteOrganizationPathParams,
        query_params: Optional[DeleteOrganizationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Organization
        ### Document:
        [Delete Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-delete-one/)
        ### Endpoint:
        `DELETE /orgs/{ORG-ID}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/orgs/{ORG-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllProjectsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        """The unique identifier for the organization whose information you want to retrieve.
        """

    class GetAllProjectsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Specifies whether or not to wrap the response in an envelope.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        name: Optional[str] = Field(None, serialization_alias="name")
        """Human-readable label of the project to use to filter the returned list. Performs a case-insensitive search for a project, which is prefixed by the specified name, within the organization.

For example, if you specify a name query parameter of project1, Ops Manager returns the project named project1, but would not return a project named project123.
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
        """Page number (1-based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Displays response in a prettyprint format.
        """

    def get_all_projects(
        self,
        path_params: GetAllProjectsPathParams,
        query_params: Optional[GetAllProjectsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Projects in an Organization
        ### Document:
        [Get All Projects](https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-all-projects/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}/groups`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{ORG-ID}/groups",
            path_params,
            query_params,
            None,
        )

    class GetAllUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        """The unique identifier for the organization whose user information you want to retrieve.
        """

    class GetAllUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(None, serialization_alias="envelope")
        """A boolean that specifies whether or not to wrap the response in an envelope.

Defaults to false.
        """

        items_per_page: Optional[int] = Field(None, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.

Defaults to 100.
        """

        page_num: Optional[int] = Field(None, serialization_alias="pageNum")
        """The page to return.

Defaults to 1.
        """

        pretty: Optional[bool] = Field(None, serialization_alias="pretty")
        """A boolean that specifies whether or not to return a "pretty-printed" JSON document.

Defaults to false.
        """

    def get_all_users(
        self,
        path_params: GetAllUsersPathParams,
        query_params: Optional[GetAllUsersQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Organization Users
        ### Document:
        [Get All Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-all-users/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}/users`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{ORG-ID}/users",
            path_params,
            query_params,
            None,
        )

    class GetAllOrganizationsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Specifies whether or not to wrap the response in an envelope.
        """

        include_deleted_orgs: Optional[bool] = Field(True, serialization_alias="includeDeletedOrgs")
        """Flag indicating whether the response body contains deleted organizations.

Ops Manager honors the value of this parameter only if the user who makes the request has a global role.

If set to true or omitted, users assigned a global role receive deleted projects in the response. If set to false or if the user does not have a global owner role, the response does not contain deleted organizations.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        name: Optional[str] = Field(None, serialization_alias="name")
        """Filters results based on the specified organization name. Performs a case-insensitive search for organizations which exactly match the specified name.

For example, if you specify a name query parameter of org1, Ops Manager returns organizations named org1 and Org1, but would not return an organization named org123.
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
        """Page number (1-based).
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Displays response in a prettyprint format.
        """

    def get_all_organizations(
        self,
        query_params: Optional[GetAllOrganizationsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Organizations
        ### Document:
        [Get All Organizations](https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-all/)
        ### Endpoint:
        `GET /orgs`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs",
            None,
            query_params,
            None,
        )

    class GetOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        """(Required.) The unique identifier for the organization whose information you want to retrieve.
        """

    class GetOneOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag indicating whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query.

For endpoints that return one result, the response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body
        """

        include_deleted_orgs: Optional[bool] = Field(True, serialization_alias="includeDeletedOrgs")
        """Flag indicating whether the response body contains deleted organizations.

Ops Manager honors the value of this parameter only if the user who makes the request has a global role.

If set to true or omitted, users assigned a global role receive deleted projects in the response. If set to false or if the user does not have a global owner role, the response does not contain deleted organizations.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

    def get_one_organization(
        self,
        path_params: GetOneOrganizationPathParams,
        query_params: Optional[GetOneOrganizationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Organization
        ### Document:
        [Get One Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-one/)
        ### Endpoint:
        `GET /orgs/{ORG-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/orgs/{ORG-ID}",
            path_params,
            query_params,
            None,
        )

    class RenameOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="ORG-ID")
        """The unique identifier of the organization.
        """

    class RenameOrganizationQueryParams(BaseModel):
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

    class RenameOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        ldap_group_mappings: Optional[list[dict]] = Field(
            None, serialization_alias="ldapGroupMappings"
        )
        """For LDAP-backed Ops Manager, the mappings of LDAP groups to Ops Manager organization roles. Only accepted for LDAP-backed Ops Manager.
        """

        name: Optional[str] = Field(None, serialization_alias="name")
        """The new name for the organization.
        """

    def rename_organization(
        self,
        path_params: RenameOrganizationPathParams,
        query_params: Optional[RenameOrganizationQueryParams],
        body_params: Optional[RenameOrganizationBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update One Organization
        ### Document:
        [Rename Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-rename/)
        ### Endpoint:
        `PATCH /orgs/{ORG-ID}`
        ### Description
        Use this endpoint to make any of the following changes to one organization:
        """
        return self._request(
            "PATCH",
            "/api/public/v1.0/orgs/{ORG-ID}",
            path_params,
            query_params,
            body_params,
        )
