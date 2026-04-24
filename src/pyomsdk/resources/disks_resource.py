"""Auto-generated client for DisksResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class DisksResource(BaseResource):
    """Client for DisksResource resource."""

    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """(Required.) Unique identifier of the host where the disk partition resides.
        """

        partition_name: str = Field(serialization_alias="PARTITION-NAME")
        """(Required.) The name of the disk partition that you want to retrieve.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) Unique identifier of the project where the disk partition resides.
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
        ## Get a Disk Partition
        ### Document:
        [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/disk-get-one/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/disks/{PARTITION-NAME}`
        ### Description
        Retrieves a disk partition.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/disks/{PARTITION-NAME}",
            path_params,
            query_params,
            None,
        )

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """(Required.) Unique identifier of the host where the disk partition resides.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) Unique identifier of the project where the disk partition resides.
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
        ## Get all Disk Partitions
        ### Document:
        [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/disks-get-all/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/disks`
        ### Description
        Retrieves all disk partitions on the specified host.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/disks",
            path_params,
            query_params,
            None,
        )
