"""Auto-generated client for SnapshotsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class SnapshotsResource(BaseResource):
    """Client for SnapshotsResource resource."""

    class ChangeExpiryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster that the snapshot represents.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the snapshot.
        """

        snapshot_id: str = Field(serialization_alias="SNAPSHOT-ID")
        """Unique identifier of the snapshot.
        """

    class ChangeExpiryQueryParams(BaseModel):
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

    class ChangeExpiryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        do_not_delete: Optional[bool] = Field(serialization_alias="doNotDelete")
        """Indicator that the snapshot cannot be deleted.

IMPORTANT: You cannot set doNotDelete to true and set a timestamp for expires in the same request. If you do, Ops Manager returns an error: Cannot modify snapshot because of invalid fields.
        """

        expires: Optional[str] = Field(serialization_alias="expires")
        """The date in ISO 8601 date and time format at UTC after which this snapshot can be deleted.

If doNotDelete is set to true, any existing value in expires is removed.

If expires is set to a timestamp at or before the current date and time, Ops Manager deletes the snapshot at its next opportunity. There is no guarantee that the snapshot would be deleted immediately.

If the current expires timestamp has already passed, it cannot be edited.
        """

    def change_expiry(
        self,
        path_params: ChangeExpiryPathParams,
        query_params: Optional[ChangeExpiryQueryParams],
        body_params: Optional[ChangeExpiryBodyParams],
    ) -> dict[str, Any]:
        """
        ## Change the Expiry of One Snapshot
        ### Document:
        [Change Expiry](https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/change-expiry-for-one-snapshot/)
        ### Endpoint:
        `PATCH /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}",
            path_params,
            query_params,
            body_params,
        )

    class GetAllConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """Unique identifier of the host that that the snapshot represents.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the snapshot.
        """

    class GetAllConfigServerQueryParams(BaseModel):
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

    def get_all_config_server(
        self,
        path_params: GetAllConfigServerPathParams,
        query_params: Optional[GetAllConfigServerQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Snapshots for One Config Server
        ### Document:
        [Get All (Config Server)](https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/get-all-snapshots-for-config-server/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/snapshots`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/snapshots",
            path_params,
            query_params,
            None,
        )

    class GetAllClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster that the snapshot represents.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the snapshot.
        """

    class GetAllClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        completed: Optional[SnapshotCompletedState] = Field(
            SnapshotCompletedState("true"), serialization_alias="completed"
        )
        """String that indicates whether to return completed or incomplete snapshots:

true: Return only completed snapshots

false: Return only incomplete snapshots

all: Return both completed and incomplete snapshots
        """

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the results object is an envelope. Ops Manager adds the status field to the response body.
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

    def get_all_cluster(
        self,
        path_params: GetAllClusterPathParams,
        query_params: Optional[GetAllClusterQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Snapshots for One Cluster
        ### Document:
        [Get All (Cluster)](https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/get-all-snapshots-for-one-cluster/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots",
            path_params,
            query_params,
            None,
        )

    class GetOneConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster that the snapshot represents.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the snapshot.
        """

        snapshot_id: str = Field(serialization_alias="SNAPSHOT-ID")
        """Unique identifier of the snapshot.
        """

    class GetOneConfigServerQueryParams(BaseModel):
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

    def get_one_config_server(
        self,
        path_params: GetOneConfigServerPathParams,
        query_params: Optional[GetOneConfigServerQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Snapshot for One Config Server
        ### Document:
        [Get One (Config Server)](https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/get-one-snapshot-for-config-server/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/snapshots/{SNAPSHOT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/snapshots/{SNAPSHOT-ID}",
            path_params,
            query_params,
            None,
        )

    class GetOneClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster that the snapshot represents.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the snapshot.
        """

        snapshot_id: str = Field(serialization_alias="SNAPSHOT-ID")
        """Unique identifier of the snapshot.
        """

    class GetOneClusterQueryParams(BaseModel):
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

    def get_one_cluster(
        self,
        path_params: GetOneClusterPathParams,
        query_params: Optional[GetOneClusterQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Snapshot for One Cluster
        ### Document:
        [Get One (Cluster)](https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/get-one-snapshot-for-one-cluster/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}",
            path_params,
            query_params,
            None,
        )

    class RemoveOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster that the snapshot represents.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the snapshot.
        """

        snapshot_id: str = Field(serialization_alias="SNAPSHOT-ID")
        """Unique identifier of the snapshot.
        """

    class RemoveOneQueryParams(BaseModel):
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

    def remove_one(
        self,
        path_params: RemoveOnePathParams,
        query_params: Optional[RemoveOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Remove One Snapshot from a Cluster
        ### Document:
        [Remove One](https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/remove-one-snapshot-from-one-cluster/)
        ### Endpoint:
        `DELETE /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}",
            path_params,
            query_params,
            None,
        )

    class CreateOneOnDemandClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster that the snapshot represents.
        """

        group_id: str = Field(serialization_alias="GROUP-ID")
        """Unique identifier of your project from your project settings.
        """

    class CreateOneOnDemandClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the results object is an envelope. Ops Manager adds the status field to the response body.
        """

        retention_days: float = Field(serialization_alias="retentionDays")
        """Integer that indicates the number of days the on-demand snapshot will be retained. Must be greater than 0.
        """

    def create_one_on_demand_cluster(
        self,
        path_params: CreateOneOnDemandClusterPathParams,
        query_params: CreateOneOnDemandClusterQueryParams,
    ) -> dict[str, Any]:
        """
        ## Create an On-Demand Snapshot
        ### Document:
        [Create One On-Demand (Cluster)](https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/take-an-on-demand-snapshot/)
        ### Endpoint:
        `POST /groups/{groupId}/clusters/{clusterId}/snapshots/onDemandSnapshot`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/groups/{groupId}/clusters/{clusterId}/snapshots/onDemandSnapshot",
            path_params,
            query_params,
            None,
        )
