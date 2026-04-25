"""Auto-generated client for UsersResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class UsersResource(BaseResource):
    """Client for UsersResource resource."""

    class CreateFirstUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        whitelist: Optional[str] = Field(None, serialization_alias="whitelist")
        """IP address that you want to add to the whitelist for the first Ops Manager user.

You can add more than one whitelist parameter and value.
        """

    class CreateFirstUserBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        email_address: Optional[str] = Field(None, serialization_alias="emailAddress")
        """Email address of the first Ops Manager user.
        """

        first_name: str = Field(serialization_alias="firstName")
        """First name of the first Ops Manager user.
        """

        last_name: str = Field(serialization_alias="lastName")
        """Last name of the first Ops Manager user.
        """

        password: str = Field(serialization_alias="password")
        """Password of the first Ops Manager user. This field is not included in the HTTP response body. Ops Manager sends this in the HTTP request only when creating the first Ops Manager user.
        """

        username: str = Field(serialization_alias="username")
        """Username of the first Ops Manager user. Validated depending on the value of the mms.email.validation property:

Value
	
Description



false

	

(Default) Username is not required to be an email address.




loose

	

Username must contain an @ symbol followed by a period.




strict

	

Username must adhere to a strict email address validation regular expression.

See mms.email.validation for details.

The username is usually an email address. If you set this value to an email address, you do not need to set the emailAddress value explicitly.
        """

    def create_first_user(
        self,
        query_params: Optional[CreateFirstUserQueryParams],
        body_params: CreateFirstUserBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create the First User
        ### Document:
        [Create First User](https://www.mongodb.com/docs/ops-manager/current/reference/api/user-create-first/)
        ### Endpoint:
        `POST /unauth/users`
        ### Description
        Create the first Ops Manager user. You can call this endpoint without having an API key.
        """
        return self._request(
            "POST",
            "/unauth/users",
            None,
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

        email_address: Optional[str] = Field(None, serialization_alias="emailAddress")
        """Email address of the Ops Manager user.
        """

        first_name: Optional[str] = Field(None, serialization_alias="firstName")
        """First name of the Ops Manager user.
        """

        last_name: Optional[str] = Field(None, serialization_alias="lastName")
        """Last name of the Ops Manager user.
        """

        mobile_number: Optional[str] = Field(None, serialization_alias="mobileNumber")
        """Mobile telephone number of the Ops Manager user.
        """

        password: Optional[str] = Field(None, serialization_alias="password")
        """Password of the Ops Manager user.

This field is not included in the entity returned from the server. It can be sent only in the entity body when you create a new user.
        """

        class RolesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            group_id: Optional[str] = Field(None, serialization_alias="groupId")
            """Unique identifier of the group in which the Ops Manager user has the specified role.

For the "global" roles (those whose name starts with GLOBAL_) there is no groupId since these roles are not tied to a group.
            """

            org_id: Optional[str] = Field(None, serialization_alias="orgId")
            """Unique identifier of the organization in which the Ops Manager user has the specified role.
            """

            role_name: Optional[AllRole] = Field(None, serialization_alias="roleName")
            """Name of the role. Accepted values are:

Value
	
Description



ORG_MEMBER

	

Organization Member




ORG_READ_ONLY

	

Organization Read Only




ORG_GROUP_CREATOR

	

Organization Project Creator




ORG_OWNER

	

Organization Owner




GROUP_AUTOMATION_ADMIN

	

Project Automation Admin




GROUP_BACKUP_ADMIN

	

Project Backup Admin




GROUP_MONITORING_ADMIN

	

Project Monitoring Admin




GROUP_OWNER

	

Project Owner




GROUP_READ_ONLY

	

Project Read Only




GROUP_USER_ADMIN

	

Project User Admin




GROUP_DATA_ACCESS_ADMIN

	

Project Data Access Admin




GROUP_DATA_ACCESS_READ_ONLY

	

Project Data Access Read Only




GROUP_DATA_ACCESS_READ_WRITE

	

Project Data Access Read/Write




GLOBAL_AUTOMATION_ADMIN

	

Global Automation Admin




GLOBAL_BACKUP_ADMIN

	

Global Backup Admin




GLOBAL_MONITORING_ADMIN

	

Global Monitoring Admin




GLOBAL_OWNER

	

Global Owner




GLOBAL_READ_ONLY

	

Global Read Only




GLOBAL_USER_ADMIN

	

Global User Admin
            """

        roles: Optional[list[RolesParams]] = Field(None, serialization_alias="roles")
        """Role assignments of the Ops Manager user.
        """

        username: str = Field(serialization_alias="username")
        """Username of the Ops Manager user. Validated depending on the value of the mms.email.validation property:

Value
	
Description



false

	

(Default) Username is not required to be an email address.




loose

	

Username must contain an @ symbol followed by a period.




strict

	

Username must adhere to a strict email address validation regular expression.

See mms.email.validation for details.
        """

    def create(
        self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One User
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/user-create/)
        ### Endpoint:
        `POST /users`
        ### Description
        Create a new user. By default, any non-global organization and project roles in the payload send users an invitation to the organization or project first.
        """
        return self._request(
            "POST",
            "/users",
            None,
            query_params,
            body_params,
        )

    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        user_id: str = Field(serialization_alias="USER-ID")
        """(Required.) Unique identifier of the user that you want to retrieve. To retrieve the USER-ID for a user, see Get All Users in One Project.
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
        ## Get a User by ID
        ### Document:
        [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/user-get-by-id/)
        ### Endpoint:
        `GET /users/{USER-ID}`
        ### Description
        You can always retrieve your own user account. Otherwise, you must be a global user or you must have the Project User Admin role in at least one project that is common between you and the user you are retrieving.
        """
        return self._request(
            "GET",
            "/users/{USER-ID}",
            path_params,
            query_params,
            None,
        )

    class GetByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        user_name: str = Field(serialization_alias="USER-NAME")
        """(Required.) Username of the MongoDB user that you want to retrieve.
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
        ## Get a User by Name
        ### Document:
        [Get by Name](https://www.mongodb.com/docs/ops-manager/current/reference/api/user-get-by-name/)
        ### Endpoint:
        `GET /users/byName/{USER-NAME}`
        ### Description
        You can always retrieve your own user account. Otherwise, you must be a global user or you must have the Project User Admin role in at least one project that is common between you and the user you are retrieving.
        """
        return self._request(
            "GET",
            "/users/byName/{USER-NAME}",
            path_params,
            query_params,
            None,
        )

    class UpdateRolesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        user_id: str = Field(serialization_alias="USER-ID")
        """Unique identifier of the user that you want to retrieve. To retrieve the USER-ID for a user, see Get All Users in One Project.
        """

    class UpdateRolesQueryParams(BaseModel):
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

    class UpdateRolesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        class RolesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            group_id: Optional[str] = Field(None, serialization_alias="groupId")
            """Unique identifier of the project in which the Ops Manager user has the specified role.

Roles that start with GLOBAL_ don't require a groupId. These roles aren't tied to a project.
            """

            org_id: Optional[str] = Field(None, serialization_alias="orgId")
            """Unique identifier of the organization in which the Ops Manager user has the specified role.
            """

            role_name: Optional[AllRole] = Field(None, serialization_alias="roleName")
            """Name of the role. Accepted values are:

Value
	
Description



ORG_MEMBER

	

Organization Member




ORG_READ_ONLY

	

Organization Read Only




ORG_GROUP_CREATOR

	

Organization Project Creator




ORG_OWNER

	

Organization Owner




GROUP_AUTOMATION_ADMIN

	

Project Automation Admin




GROUP_BACKUP_ADMIN

	

Project Backup Admin




GROUP_MONITORING_ADMIN

	

Project Monitoring Admin




GROUP_OWNER

	

Project Owner




GROUP_READ_ONLY

	

Project Read Only




GROUP_USER_ADMIN

	

Project User Admin




GROUP_DATA_ACCESS_ADMIN

	

Project Data Access Admin




GROUP_DATA_ACCESS_READ_ONLY

	

Project Data Access Read Only




GROUP_DATA_ACCESS_READ_WRITE

	

Project Data Access Read/Write




GLOBAL_AUTOMATION_ADMIN

	

Global Automation Admin




GLOBAL_BACKUP_ADMIN

	

Global Backup Admin




GLOBAL_MONITORING_ADMIN

	

Global Monitoring Admin




GLOBAL_OWNER

	

Global Owner




GLOBAL_READ_ONLY

	

Global Read Only




GLOBAL_USER_ADMIN

	

Global User Admin
            """

        roles: list[RolesParams] = Field(serialization_alias="roles")
        """Role assigned to the Ops Manager user.
        """

    def update_roles(
        self,
        path_params: UpdateRolesPathParams,
        query_params: Optional[UpdateRolesQueryParams],
        body_params: UpdateRolesBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update Roles for One User
        ### Document:
        [Update Roles](https://www.mongodb.com/docs/ops-manager/current/reference/api/user-update/)
        ### Endpoint:
        `PATCH /users/{USER-ID}`
        ### Description
        Add, update, or remove a user's roles within an organization or project. By default, any new non-global organization and project roles in the payload send users an invitation to the organization or project first. You can add users directly to an organization or project only if you set the mms.user.bypassInviteForExistingUsers setting to true.
        """
        return self._request(
            "PATCH",
            "/users/{USER-ID}",
            path_params,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        user_id: str = Field(serialization_alias="USER-ID")
        """Unique identifier of the user.
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
        ## Remove One User
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/users/delete-one-user/)
        ### Endpoint:
        `DELETE /users/{USER-ID}`
        ### Description
        Removes one user from Ops Manager by user ID.
        """
        return self._request(
            "DELETE",
            "/users/{USER-ID}",
            path_params,
            query_params,
            None,
        )
