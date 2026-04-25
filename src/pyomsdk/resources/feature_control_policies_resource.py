"""Auto-generated client for FeatureControlPoliciesResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class FeatureControlPoliciesResource(BaseResource):
    """Client for FeatureControlPoliciesResource resource."""

    class RetrieveAllQueryParams(BaseModel):
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

    def retrieve_all(
        self,
        query_params: Optional[RetrieveAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve All Feature Policies
        ### Document:
        [Retrieve All](https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/get-all-feature-control-policies/)
        ### Endpoint:
        `GET /groups/availablePolicies`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/availablePolicies",
            None,
            query_params,
            None,
        )

    class RetrieveForOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that has the controlled features.
        """

    class RetrieveForOneProjectQueryParams(BaseModel):
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

    def retrieve_for_one_project(
        self,
        path_params: RetrieveForOneProjectPathParams,
        query_params: Optional[RetrieveForOneProjectQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve Feature Policies for One Project
        ### Document:
        [Retrieve for One Project](https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/get-controlled-features-for-one-project/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/controlledFeature`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/controlledFeature",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that has the controlled features.
        """

    class UpdateQueryParams(BaseModel):
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

    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        class ExternalmanagementsystemParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            name: Optional[str] = Field(None, serialization_alias="name")
            """Identifying label for the external system that manages this Ops Manager Project.
            """

            system_id: Optional[str] = Field(None, serialization_alias="systemId")
            """Unique identifier of the external system that manages this Ops Manager Project.
            """

            version: Optional[str] = Field(None, serialization_alias="version")
            """Active release of the external system that manages this Ops Manager Project.
            """

        external_management_system: Optional[ExternalmanagementsystemParams] = Field(
            None, serialization_alias="externalManagementSystem"
        )
        """Identifying parameters for the external system that manages this Ops Manager Project.
        """

        class PoliciesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            disabled_params: Optional[list[Any]] = Field(None, serialization_alias="disabledParams")
            """List of mongod settings to disable when you apply the DISABLE_SET_MONGOD_CONFIG policy. Automation doesn't support all MongoDB options, which can result in failed import attempts. To learn more, see MongoDB Settings and Automation Support.
            """

            policy: Optional[Policy] = Field(None, serialization_alias="policy")
            """Single policy set for this Ops Manager Project. This parameter can be set one or more times in the policies array.

Accepted values are:

Value
	
Purpose



EXTERNALLY_MANAGED_LOCK

	

Users can't use Ops Manager to manage other settings given in the policies.policy[n] array. These same users may use a configured external system, like the Kubernetes Operator to manage these settings.




DISABLE_USER_MANAGEMENT

	

Users can't manage users or roles.



DISABLE_AUTHENTICATION_
MECHANISMS
	

Users can't change authentication settings.



DISABLE_SET_MONGOD_
CONFIG
	

Users can't change any mongod settings listed in the policies[n].disabledParams array.



DISABLE_SET_MONGOD_
VERSION
	

Users can't change the version of any mongod or mongos.




DISABLE_BACKUP_AGENT

	

Users can't enable or disable the Backup agent.



DISABLE_MONGOD_LOG_
MANAGEMENT
	

Users can't change log management settings.



DISABLE_IMPORT_TO_
AUTOMATION
	

Users can't manage deployments using Automation.



DISABLE_AGENT_API_KEY_
MANAGEMENT
	

Users can't create or update Agent API keys.



DISABLE_MONGOD_HOST_
MANAGEMENT
	

Users can't change the server type of hosts.
            """

        policies: Optional[list[PoliciesParams]] = Field(None, serialization_alias="policies")
        """List of policies that the external system applies to this Ops Manager Project.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update Feature Policies for One Project
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/update-controlled-features-for-one-project/)
        ### Endpoint:
        `PUT /groups/{PROJECT-ID}/controlledFeature`
        ### Description
        No description.
        """
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/controlledFeature",
            path_params,
            query_params,
            body_params,
        )
