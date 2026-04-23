"""Auto-generated client for AgentsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class AgentsResource(BaseResource):
    """Client for AgentsResource resource."""

    class CreateApiKeyPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the Agent API Key.
        """

    class CreateApiKeyQueryParams(BaseModel):
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

    class CreateApiKeyBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        desc: Optional[str] = Field(serialization_alias="desc")
        """Label for this Agent API Key.
        """

    def create_api_key(
        self,
        path_params: CreateApiKeyPathParams,
        query_params: Optional[CreateApiKeyQueryParams],
        body_params: Optional[CreateApiKeyBodyParams],
    ) -> dict[str, Any]:
        """
        ## Create One Agent API Key
        - Document: [Create API Key](https://www.mongodb.com/docs/ops-manager/current/reference/api/agentapikeys/create-one-agent-api-key/)
        - Resource: `POST /groups/{PROJECT-ID}/agentapikeys`
        - Description: No description.
        """
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/agentapikeys",
            path_params,
            query_params,
            body_params,
        )

    class RemoveApiKeyPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        api_agent_key_id: str = Field(serialization_alias="API-AGENT-KEY-ID")
        """Unique identifier of Agent API Key.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the Agent API Key.
        """

    class RemoveApiKeyQueryParams(BaseModel):
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

    def remove_api_key(
        self,
        path_params: RemoveApiKeyPathParams,
        query_params: Optional[RemoveApiKeyQueryParams],
    ) -> dict[str, Any]:
        """
        ## Remove One Agent API Key
        - Document: [Remove API Key](https://www.mongodb.com/docs/ops-manager/current/reference/api/agentapikeys/delete-one-agent-api-key/)
        - Resource: `DELETE /groups/{PROJECT-ID}/agentapikeys/{API-AGENT-KEY-ID}`
        - Description: No description.
        """
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/agentapikeys/{API-AGENT-KEY-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllApiKeysPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the Agent API Key.
        """

    class GetAllApiKeysQueryParams(BaseModel):
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

    def get_all_api_keys(
        self,
        path_params: GetAllApiKeysPathParams,
        query_params: Optional[GetAllApiKeysQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Agent API Keys for One Project
        - Document: [Get All API Keys](https://www.mongodb.com/docs/ops-manager/current/reference/api/agentapikeys/get-all-agent-api-keys-for-project/)
        - Resource: `GET /groups/{PROJECT-ID}/agentapikeys`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agentapikeys",
            path_params,
            query_params,
            None,
        )

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the Agent API Key.
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
        ## Get Links to Agent Resources for a Project
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/agents-get-all/)
        - Resource: `GET /groups/{PROJECT-ID}/agents`
        - Description: Get links to Monitoring, Backup, and Automation Agent resources for a project.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agents",
            path_params,
            query_params,
            None,
        )

    class GetByTypePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the Agent API Key.
        """

        type: AgentType = Field(serialization_alias="TYPE")
        """The agent type to retrieve. TYPE can be one of the following values:

MONITORING

BACKUP

AUTOMATION
        """

    class GetByTypeQueryParams(BaseModel):
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

    def get_by_type(
        self,
        path_params: GetByTypePathParams,
        query_params: Optional[GetByTypeQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Agents by Type for One Project
        - Document: [Get by Type](https://www.mongodb.com/docs/ops-manager/current/reference/api/agents-get-by-type/)
        - Resource: `GET /groups/{PROJECT-ID}/agents/{TYPE}`
        - Description: Get all agents of a specified type (i.e. Monitoring, Backup, or Automation) for a project.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agents/{TYPE}",
            path_params,
            query_params,
            None,
        )

    class RetrieveAllVersionsQueryParams(BaseModel):
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

    def retrieve_all_versions(
        self,
        query_params: Optional[RetrieveAllVersionsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve All Agent Versions
        - Document: [Retrieve All Versions](https://www.mongodb.com/docs/ops-manager/current/reference/api/agents/get-agent-versions-global/)
        - Resource: `GET /softwareComponents/versions/`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/softwareComponents/versions/",
            None,
            query_params,
            None,
        )

    class RetrieveForOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project.
        """

    class RetrieveForOneProjectQueryParams(BaseModel):
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

    def retrieve_for_one_project(
        self,
        path_params: RetrieveForOneProjectPathParams,
        query_params: Optional[RetrieveForOneProjectQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve All Agent Versions for One Project
        - Document: [Retrieve for One Project](https://www.mongodb.com/docs/ops-manager/current/reference/api/agents/get-agent-versions-per-project/)
        - Resource: `GET /groups/{PROJECT-ID}/agents/versions`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agents/versions",
            path_params,
            query_params,
            None,
        )
