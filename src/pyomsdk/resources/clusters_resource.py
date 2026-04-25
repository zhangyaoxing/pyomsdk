"""Auto-generated client for ClustersResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class ClustersResource(BaseResource):
    """Client for ClustersResource resource."""

    class GetAllFromAllProjectsQueryParams(BaseModel):
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

    def get_all_from_all_projects(
        self,
        query_params: Optional[GetAllFromAllProjectsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Clusters in All Projects
        ### Document:
        [Get All from All Projects](https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-get-all-key/)
        ### Endpoint:
        `GET /api/public/v1.0/clusters`
        ### Description
        Get details for all clusters in all projects available to the programmatic API key making the request.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/clusters",
            None,
            query_params,
            None,
        )

    class GetAllFromOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for the project.
        """

    class GetAllFromOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag that indicates whether the response body should be in a prettyprint format.
        """

    def get_all_from_one_project(
        self,
        path_params: GetAllFromOneProjectPathParams,
        query_params: Optional[GetAllFromOneProjectQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Clusters in One Project
        ### Document:
        [Get All from One Project](https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-get-all/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/clusters`
        ### Description
        Retrieve details for all clusters in one project.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters",
            path_params,
            query_params,
            None,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier for the cluster you want to retrieve.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for the project.
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
        ## Get One Cluster in One Project
        ### Document:
        [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-get-one/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}`
        ### Description
        Retrieve details for one cluster in one project.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier for the cluster you want to retrieve.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for the project.
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

        cluster_name: str = Field(serialization_alias="clusterName")
        """Name to assign to the cluster.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Cluster
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-update-one/)
        ### Endpoint:
        `PATCH /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}`
        ### Description
        Update one cluster in one project.
        """
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}",
            path_params,
            query_params,
            body_params,
        )
