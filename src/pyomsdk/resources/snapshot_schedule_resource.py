"""Auto-generated client for SnapshotScheduleResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class SnapshotScheduleResource(BaseResource):
    """Client for SnapshotScheduleResource resource."""

    class GetSchedulePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster whose snapshot schedule you want to get.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for the project that holds the cluster with the snapshot schedule you want to get.
        """

    class GetScheduleQueryParams(BaseModel):
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

    def get_schedule(
        self,
        path_params: GetSchedulePathParams,
        query_params: Optional[GetScheduleQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get the Snapshot Schedule
        ### Document:
        [Get Schedule](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-snapshot-schedule/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/backupConfigs/CLUSTER-ID/snapshotSchedule`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/backupConfigs/CLUSTER-ID/snapshotSchedule",
            path_params,
            query_params,
            None,
        )

    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        cluster_id: str = Field(serialization_alias="CLUSTER-ID")
        """Unique identifier of the cluster whose snapshot schedule you want to update.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier for the project that holds the cluster with the snapshot schedule you want to update.
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

        cluster_checkpoint_interval_min: Optional[int] = Field(
            None, serialization_alias="clusterCheckpointIntervalMin"
        )
        """Number of minutes between successive cluster checkpoints. This only applies to sharded clusters. This number determines the granularity of point-in-time restores for sharded clusters. You can set a value of 15, 30, or 60.
        """

        cluster_id: Optional[str] = Field(None, serialization_alias="clusterId")
        """Unique identifier of the cluster to which this backup configuration applies.
        """

        daily_snapshot_retention_days: Optional[int] = Field(
            None, serialization_alias="dailySnapshotRetentionDays"
        )
        """Number of days to retain daily snapshots. Accepted values are: 0, 3, 4, 5, 6, 7, 15, 30, 60, 90, 120, 180, 360.

Setting dailySnapshotRetentionDays to 0 disables this rule.
        """

        full_incremental_day_of_week: Optional[str] = Field(
            None, serialization_alias="fullIncrementalDayOfWeek"
        )
        """Day of the week when Ops Manager takes a full snapshot. This ensures a recent complete backup. Ops Manager sets the default value to SUNDAY.
        """

        group_id: Optional[str] = Field(None, serialization_alias="groupId")
        """Unique identifier of the project that owns the backup configuration.
        """

        links: Optional[list[dict]] = Field(None, serialization_alias="links")
        """One or more links to sub-resources or related resources. All links arrays in responses include at least one link called self. The relationships between URLs are explained in the Web Linking Specification.
        """

        monthly_snapshot_retention_months: Optional[int] = Field(
            None, serialization_alias="monthlySnapshotRetentionMonths"
        )
        """Number of months to retain monthly snapshots. You can set a value between 1 and 36, inclusive.

Setting monthlySnapshotRetentionMonths to 0 disables this rule.
        """

        point_in_time_window_hours: Optional[int] = Field(
            None, serialization_alias="pointInTimeWindowHours"
        )
        """Number of hours in the past for which a point-in-time snapshot can be created.
        """

        reference_hour_of_day: Optional[int] = Field(None, serialization_alias="referenceHourOfDay")
        """Hour of the day to schedule snapshots using a 24 hour clock. You can set a value between 0 and 23, inclusive.
        """

        reference_minute_of_hour: Optional[int] = Field(
            None, serialization_alias="referenceMinuteOfHour"
        )
        """Minute of the hour to schedule snapshots. You can set a value between 0 and 59, inclusive.
        """

        reference_time_zone_offset: Optional[str] = Field(
            None, serialization_alias="referenceTimeZoneOffset"
        )
        """The ISO-8601 timezone offset where the Ops Manager host resides. To avoid problems with daylight saving time, use UTC. The default is +0000, which is equivalent to UTC. Z is also a supported value and equivalent to UTC.

Ops Manager converts any offset other than +0000 to +0000 before storing it, and adjusts the referenceHourOfDay value accordingly.

For example, you pass in a request with a referenceHourOfDay of 5 and a referenceTimeZoneOffset of "+0200". |onprem| stores a ``referenceHourOfDay of 3 and a referenceTimeZoneOffset of "+0000".
        """

        snapshot_interval_hours: Optional[int] = Field(
            None, serialization_alias="snapshotIntervalHours"
        )
        """Number of hours between snapshots. You can set a value of 6, 8, 12, or 24.
        """

        snapshot_retention_days: Optional[int] = Field(
            None, serialization_alias="snapshotRetentionDays"
        )
        """Number of days to keep recent snapshots. You can set a value between 2 and 5, inclusive.
        """

        weekly_snapshot_retention_weeks: Optional[int] = Field(
            None, serialization_alias="weeklySnapshotRetentionWeeks"
        )
        """Number of weeks to retain weekly snapshots. You can set a value between 1 and 52, inclusive.

Setting weeklySnapshotRetentionWeeks to 0 disables this rule.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update the Snapshot Schedule
        ### Document:
        [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/update-one-snapshot-schedule-by-cluster-id/)
        ### Endpoint:
        `PATCH /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/snapshotSchedule`
        ### Description
        No description.
        """
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/snapshotSchedule",
            path_params,
            query_params,
            body_params,
        )
