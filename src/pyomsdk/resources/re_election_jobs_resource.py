
r"""Auto-generated client for ReElectionJobsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *

class ReElectionJobsResource(BaseResource):
    r"""Client for ReElectionJobsResource resource.
    """
    
    
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        group_id: str = Field(serialization_alias="GROUP-ID")
        r"""Unique 24-hexadecimal digit string that identifies your project.
        """
        
        rs_id: str = Field(serialization_alias="RS-ID")
        r"""Name of the replica set whose re-election jobs you want to list.
        """
        
    
    
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        envelope: Optional[bool] = Field(default=None, serialization_alias="envelope")
        r"""Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set `"envelope" : true` in the query.

For endpoints that return one result, response body includes:

- `status`: HTTP response code
- `content`: Expected response body

For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body.
        """
        
        
        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """
        
        
        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""Page number (1-index based).
        """
        
        
        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Indicates whether the response body should be in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """
        
    
    
    def get_all(self,
        
        path_params: GetAllPathParams,
        
        
        query_params: Optional[GetAllQueryParams],
        
        
    ) -> dict[str, Any]:
        r"""
## Get All Replica Set Re-Election Jobs
### Document:
[Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/re-election-jobs/re-election-jobs-get-all/)
### Endpoint:
`GET /groups/{GROUP-ID}/replicaSets/{RS-ID}/reElectionJobs`
### Description
Use this endpoint to retrieve every re-election job for a specific replica set.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{GROUP-ID}/replicaSets/{RS-ID}/reElectionJobs",
            path_params,
            query_params,
            None,
        )
    
    
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        group_id: str = Field(serialization_alias="GROUP-ID")
        r"""Unique 24-hexadecimal digit string that identifies your project.
        """
        
        reelection_job_id: str = Field(serialization_alias="REELECTION-JOB-ID")
        r"""Unique 24-hexadecimal digit string that identifies the re-election job, as returned by the step down or step up endpoint.
        """
        
        rs_id: str = Field(serialization_alias="RS-ID")
        r"""Name of the replica set that contains the re-election job.
        """
        
    
    
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set **envelope=true** in the query.

For endpoints that return one result, the response body includes:

- `status`: HTTP response code
- `content`: Expected response body
        """
        
        
        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body is in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """
        
    
    
    def get_one(self,
        
        path_params: GetOnePathParams,
        
        
        query_params: Optional[GetOneQueryParams],
        
        
    ) -> dict[str, Any]:
        r"""
## Get One Replica Set Re-Election Job
### Document:
[Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/re-election-jobs/re-election-jobs-get-one/)
### Endpoint:
`GET /groups/{GROUP-ID}/replicaSets/{RS-ID}/reElectionJobs/{REELECTION-JOB-ID}`
### Description
Use this endpoint to retrieve a single re-election job by its unique identifier. Poll this endpoint until the job reaches a terminal status.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{GROUP-ID}/replicaSets/{RS-ID}/reElectionJobs/{REELECTION-JOB-ID}",
            path_params,
            query_params,
            None,
        )
    
    
    class StepDownAPrimaryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        group_id: str = Field(serialization_alias="GROUP-ID")
        r"""Unique 24-hexadecimal digit string that identifies your project.
        """
        
        host_port: str = Field(serialization_alias="HOST-PORT")
        r"""Target process, as `hostname:port`. This process must currently be the replica set's primary.
        """
        
        rs_id: str = Field(serialization_alias="RS-ID")
        r"""Name of the replica set that contains the target process.
        """
        
    
    
    class StepDownAPrimaryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set **envelope=true** in the query.

For endpoints that return one result, the response body includes:

- `status`: HTTP response code
- `content`: Expected response body
        """
        
        
        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body is in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """
        
    
    
    class StepDownAPrimaryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        expires_after_seconds: Optional[int] = Field(default=300, serialization_alias="expiresAfterSeconds")
        r"""Number of seconds the request stays queued for an Automation Agent to pick up before the job expires. Must be greater than `0`.
        """
        
        
        secondary_catch_up_period_secs: Optional[int] = Field(default=None, serialization_alias="secondaryCatchUpPeriodSecs")
        r"""Number of seconds to wait for a lagging secondary to catch up before the primary steps down. Must be greater than or equal to `0`. If you omit this field, `mongod` applies its own default.
        """
        
        
        step_down_secs: Optional[int] = Field(default=60, serialization_alias="stepDownSecs")
        r"""Number of seconds the stepped-down primary remains ineligible for re-election. Must be greater than `0`.
        """
        
    
    def step_down_a_primary(self,
        
        path_params: StepDownAPrimaryPathParams,
        
        
        query_params: Optional[StepDownAPrimaryQueryParams],
        
        
        body_params: Optional[StepDownAPrimaryBodyParams],
        
    ) -> dict[str, Any]:
        r"""
## Request a Replica Set Primary Step Down
### Document:
[Step Down a Primary](https://www.mongodb.com/docs/ops-manager/current/reference/api/re-election-jobs/re-election-jobs-step-down/)
### Endpoint:
`POST /groups/{GROUP-ID}/replicaSets/{RS-ID}/process/{HOST-PORT}:stepDown`
### Description
Use this endpoint to request that the current primary of a replica set step down, triggering a new election. Ops Manager queues a background job for the target host's Automation Agent to run on its next check-in.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{GROUP-ID}/replicaSets/{RS-ID}/process/{HOST-PORT}:stepDown",
            path_params,
            query_params,
            body_params,
        )
    
    
    class StepUpASecondaryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        group_id: str = Field(serialization_alias="GROUP-ID")
        r"""Unique 24-hexadecimal digit string that identifies your project.
        """
        
        host_port: str = Field(serialization_alias="HOST-PORT")
        r"""Target process, as `hostname:port`. This process must currently be an active, electable secondary.
        """
        
        rs_id: str = Field(serialization_alias="RS-ID")
        r"""Name of the replica set that contains the target process.
        """
        
    
    
    class StepUpASecondaryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        envelope: Optional[bool] = Field(default=False, serialization_alias="envelope")
        r"""Flag that indicates whether to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set **envelope=true** in the query.

For endpoints that return one result, the response body includes:

- `status`: HTTP response code
- `content`: Expected response body
        """
        
        
        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Flag indicating whether the response body is in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """
        
    
    
    class StepUpASecondaryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        
        
        expires_after_seconds: Optional[int] = Field(default=None, serialization_alias="expiresAfterSeconds")
        r"""Number of seconds the request stays queued for an Automation Agent to pick up before the job expires. Must be greater than `0`.
        """
        
        
        freeze_secs: Optional[int] = Field(default=None, serialization_alias="freezeSecs")
        r"""Number of seconds Ops Manager freezes the other electable secondaries so that the target wins the election. Must be greater than `0` and greater than or equal to `stepDownSecs`.
        """
        
        
        secondary_catch_up_period_secs: Optional[int] = Field(default=None, serialization_alias="secondaryCatchUpPeriodSecs")
        r"""Number of seconds to wait for a lagging secondary to catch up before the primary steps down. Must be greater than or equal to `0`. If you omit this field, `mongod` applies its own default.
        """
        
        
        step_down_secs: Optional[int] = Field(default=60, serialization_alias="stepDownSecs")
        r"""Number of seconds the outgoing primary remains ineligible for re-election. Must be greater than `0`.
        """
        
    
    def step_up_a_secondary(self,
        
        path_params: StepUpASecondaryPathParams,
        
        
        query_params: Optional[StepUpASecondaryQueryParams],
        
        
        body_params: Optional[StepUpASecondaryBodyParams],
        
    ) -> dict[str, Any]:
        r"""
## Request a Replica Set Secondary Step Up
### Document:
[Step Up a Secondary](https://www.mongodb.com/docs/ops-manager/current/reference/api/re-election-jobs/re-election-jobs-step-up/)
### Endpoint:
`POST /groups/{GROUP-ID}/replicaSets/{RS-ID}/process/{HOST-PORT}:stepUp`
### Description
Use this endpoint to request that a specific secondary of a replica set step up to become primary. Ops Manager freezes the other electable secondaries so that the target process, not another member, wins the election. The target host's Automation Agent runs the freeze and step-down procedure on its next check-in.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{GROUP-ID}/replicaSets/{RS-ID}/process/{HOST-PORT}:stepUp",
            path_params,
            query_params,
            body_params,
        )
    
