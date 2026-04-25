"""Auto-generated client for DeploymentRegionsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class DeploymentRegionsResource(BaseResource):
    """Client for DeploymentRegionsResource resource."""

    class AssignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique 24-hexadecimal digit string that identifies the cluster whose backup configuration you want to find.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique 24-hexadecimal digit string that identifies the project that holds the cluster with the backup configuration you want to find.
        """

    class AssignQueryParams(BaseModel):
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

    class AssignBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        class DeploymentconfigsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            deployment_id: str = Field(serialization_alias="deploymentId")
            """Unique identifier that references the deployment region to assign to the shard.
            """

            rs_id: str = Field(serialization_alias="rsId")
            """Replica set label that identifies the shard.
            """

        deployment_configs: list[DeploymentconfigsParams] = Field(
            serialization_alias="deploymentConfigs"
        )
        """Specification objects for the cluster members for which to assign deployment regions.
        """

        multi_region_backup_enabled: bool = Field(serialization_alias="multiRegionBackupEnabled")
        """Flag that indicates whether multi-region backup is enabled for the cluster.
        """

    def assign(
        self,
        path_params: AssignPathParams,
        query_params: Optional[AssignQueryParams],
        body_params: AssignBodyParams,
    ) -> dict[str, Any]:
        """
        ## Assign Deployment Region to One Shard
        ### Document:
        [Assign](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/assign-deployment-region/)
        ### Endpoint:
        `PATCH /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}`
        ### Description
        No description.
        """
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}",
            path_params,
            query_params,
            body_params,
        )

    class CreateByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        deployment_id: str = Field(serialization_alias="DEPLOYMENT-ID")
        """Unique identifier that references this deployment region in configurations.
        """

    class CreateByIdQueryParams(BaseModel):
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

    class CreateByIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        assignment_enabled: Optional[bool] = Field(None, serialization_alias="assignmentEnabled")
        """Flag indicating whether you can assign Deployment Regions to backup resources.
        """

        bq_proxy_endpoint: str = Field(serialization_alias="bqProxyEndpoint")
        """Ops Manager instance that serves Queryable Backup requests. Value is in the following format: domain:port. For example, localhost:8080.
        """

        deployment_description: str = Field(serialization_alias="deploymentDescription")
        """String that describes the purpose of the deployment region.
        """

        ingestion_endpoint: Optional[str] = Field(None, serialization_alias="ingestionEndpoint")
        """Ops Manager instance to which the Backup Agent writes snapshot or oplog data. Value is a valid URL such as http://www.mongodb.com. Supports both HTTP and HTTPS.
        """

        restore_endpoint: str = Field(serialization_alias="restoreEndpoint")
        """Ops Manager instance that serves restore requests.
        """

    def create_by_id(
        self,
        path_params: CreateByIdPathParams,
        query_params: Optional[CreateByIdQueryParams],
        body_params: CreateByIdBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Deployment Region by ID
        ### Document:
        [Create by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/create-one-deployment-region-by-id/)
        ### Endpoint:
        `PUT /admin/backup/backupDeployments/{DEPLOYMENT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "PUT",
            "/admin/backup/backupDeployments/{DEPLOYMENT-ID}",
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

        assignment_enabled: Optional[bool] = Field(None, serialization_alias="assignmentEnabled")
        """Flag indicating whether you can assign Deployment Regions to backup resources.
        """

        bq_proxy_endpoint: str = Field(serialization_alias="bqProxyEndpoint")
        """Ops Manager instance that serves Queryable Backup requests. Value is in the following format: domain:port. For example, localhost:8080.
        """

        deployment_description: str = Field(serialization_alias="deploymentDescription")
        """String that describes the purpose of the deployment region.
        """

        id: Optional[str] = Field(None, serialization_alias="id")
        """Unique identifier that references this deployment region in configurations.
        """

        ingestion_endpoint: Optional[str] = Field(None, serialization_alias="ingestionEndpoint")
        """Ops Manager instance to which the Backup Agent writes snapshot or oplog data. Value is a valid URL such as http://www.mongodb.com. Supports both HTTP and HTTPS.
        """

        restore_endpoint: str = Field(serialization_alias="restoreEndpoint")
        """Ops Manager instance that serves restore requests.
        """

    def create(
        self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Deployment Region
        ### Document:
        [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/create-one-deployment-region/)
        ### Endpoint:
        `POST /admin/backup/backupDeployments`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/admin/backup/backupDeployments",
            None,
            query_params,
            body_params,
        )

    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        deployment_id: str = Field(serialization_alias="DEPLOYMENT-ID")
        """Unique identifier that references the deployment region in configurations.
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
        ## Delete One Deployment Region by ID
        ### Document:
        [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/delete-one-deployment-region-by-id/)
        ### Endpoint:
        `DELETE /admin/backup/backupDeployments/{DEPLOYMENT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/admin/backup/backupDeployments/{DEPLOYMENT-ID}",
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

        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
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
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Deployment Regions
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-all-deployment-regions/)
        ### Endpoint:
        `GET /admin/backup/backupDeployments`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/admin/backup/backupDeployments",
            None,
            query_params,
            None,
        )

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        deployment_id: str = Field(serialization_alias="DEPLOYMENT-ID")
        """Unique identifier that references the deployment region in configurations.
        """

    class GetOneQueryParams(BaseModel):
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

    def get_one(
        self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Deployment Region
        ### Document:
        [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-one-deployment-region-by-id/)
        ### Endpoint:
        `GET /admin/backup/backupDeployments/{DEPLOYMENT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/admin/backup/backupDeployments/{DEPLOYMENT-ID}",
            path_params,
            query_params,
            None,
        )
