r"""Auto-generated client for MeasurementsResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class MeasurementsResource(BaseResource):
    r"""Client for MeasurementsResource resource."""

    class DatabasePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        database_name: str = Field(serialization_alias="DATABASE-NAME")
        r"""Unique identifier of the database on which the MongoDB
process is stored.
        """

        host_id: str = Field(serialization_alias="HOST-ID")
        r"""Unique identifier of the host that serves the MongoDB process.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project) that owns the host.
        """

    class DatabaseQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        end: Optional[str] = Field(default=None, serialization_alias="end")
        r"""Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC for the end of the period for which to retrieve
measurements. If you specify `end` you must also specify
`start`.
        """

        envelope: Optional[bool] = Field(default=None, serialization_alias="envelope")
        r"""Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `"envelope" : true` in the
query.

For endpoints that return one result, response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |

For endpoints that return a list of results, the `results`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        granularity: str = Field(serialization_alias="granularity")
        r"""Duration in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594#Durations) notation that specifies the interval between
measurement data points.

Measurement granularity can be expressed as days, hours, minutes, seconds and milliseconds using the following notation:

`P` (for *period*) followed by:

- `D` for *days* (if desired)
- `T` for *time* (after *days*)
- `H` for *hours*
- `M` for *minutes*
- `S` for *seconds*

For example:

| Notation | Duration |
| --- | --- |
| `PT30S` | 30 seconds |
| `P1T12H` | 1 day, 12 hours |
| `PT0.5S` | 500 milliseconds |
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        m: Optional[str] = Field(default=None, serialization_alias="m")
        r"""Measurements to return. If `m` is not specified, all
measurements are returned.

To specify multiple values for `m`, you must repeat the `m`
parameter.

For example:

```
|  |
| --- |
| ../measurements?m=CONNECTIONS&m=OPCOUNTER_CMD&m=OPCOUNTER_QUERY |
```

You must specify measurements that are valid for the host. Ops Manager
returns an error if any specified measurements are invalid
For available measurements, see [Measurement Types.](/docs/ops-manager/current/reference/api/measures/measurement-types/)
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""Page number (1-index based).
        """

        period: Optional[str] = Field(default=None, serialization_alias="period")
        r"""Duration in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594#Durations) notation that specifies how far back in the past to
retrieve measurements.

For example, to request the last 36 hours, include this query
parameter: `period=P1DT12H`.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

        start: Optional[str] = Field(default=None, serialization_alias="start")
        r"""Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC for the beginning of the period for which to
retrieve measurements. If you specify `start` you must also
specify `end`.
        """

    def database(
        self,
        path_params: DatabasePathParams,
        query_params: DatabaseQueryParams,
    ) -> dict[str, Any]:
        r"""
        ## Get Database Measurements
        ### Document:
        [Database](https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-database-measurements/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}/measurements`
        ### Description
        Database measurements provide statistics on database performance and
        storage. The Monitoring collects database measurements through
        the [dbStats](https://www.mongodb.com/docs/manual/reference/command/dbStats/) command.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}/measurements",
            path_params,
            query_params,
            None,
        )

    class DiskPartitionPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        r"""Unique identifier of the host that serves the MongoDB process.
        """

        partition_name: str = Field(serialization_alias="PARTITION-NAME")
        r"""Name of the disk partition on which the MongoDB
process is stored.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project) that owns the host.
        """

    class DiskPartitionQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        end: Optional[str] = Field(default=None, serialization_alias="end")
        r"""Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC for the end of the period for which to retrieve
measurements. If you specify `end` you must also specify
`start`.
        """

        envelope: Optional[bool] = Field(default=None, serialization_alias="envelope")
        r"""Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `"envelope" : true` in the
query.

For endpoints that return one result, response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |

For endpoints that return a list of results, the `results`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        granularity: str = Field(serialization_alias="granularity")
        r"""Duration in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594#Durations) notation that specifies the interval between
measurement data points.

Measurement granularity can be expressed as days, hours, minutes, seconds and milliseconds using the following notation:

`P` (for *period*) followed by:

- `D` for *days* (if desired)
- `T` for *time* (after *days*)
- `H` for *hours*
- `M` for *minutes*
- `S` for *seconds*

For example:

| Notation | Duration |
| --- | --- |
| `PT30S` | 30 seconds |
| `P1T12H` | 1 day, 12 hours |
| `PT0.5S` | 500 milliseconds |
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        m: Optional[str] = Field(default=None, serialization_alias="m")
        r"""Measurements to return. If `m` is not specified, all
measurements are returned.

To specify multiple values for `m`, you must repeat the `m`
parameter.

For example:

```
|  |
| --- |
| ../measurements?m=CONNECTIONS&m=OPCOUNTER_CMD&m=OPCOUNTER_QUERY |
```

You must specify measurements that are valid for the host. Ops Manager
returns an error if any specified measurements are invalid
For available measurements, see [Measurement Types.](/docs/ops-manager/current/reference/api/measures/measurement-types/)
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""Page number (1-index based).
        """

        period: Optional[str] = Field(default=None, serialization_alias="period")
        r"""Duration in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594#Durations) notation that specifies how far back in the past to
retrieve measurements.

For example, to request the last 36 hours, include this query
parameter: `period=P1DT12H`.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

        start: Optional[str] = Field(default=None, serialization_alias="start")
        r"""Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC for the beginning of the period for which to
retrieve measurements. If you specify `start` you must also
specify `end`.
        """

    def disk_partition(
        self,
        path_params: DiskPartitionPathParams,
        query_params: DiskPartitionQueryParams,
    ) -> dict[str, Any]:
        r"""
        ## Get Disk Partition Measurements
        ### Document:
        [Disk Partition](https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-disk-measurements/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/disks/{PARTITION-NAME}/measurements`
        ### Description
        Disk measurements provide data on IOPS, disk use, and disk latency on
        the disk partitions for hosts running MongoDB that the Automations collect. You must run Ops Manager Automation to retrieve disk measurements.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/disks/{PARTITION-NAME}/measurements",
            path_params,
            query_params,
            None,
        )

    class HostPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        r"""Unique identifier of the host that serves the MongoDB process.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project) that owns the host.
        """

    class HostQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        end: Optional[str] = Field(default=None, serialization_alias="end")
        r"""Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC for the end of the period for which to retrieve
measurements. If you specify `end` you must also specify
`start`.
        """

        envelope: Optional[bool] = Field(default=None, serialization_alias="envelope")
        r"""Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `"envelope" : true` in the
query.

For endpoints that return one result, response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |

For endpoints that return a list of results, the `results`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        granularity: str = Field(serialization_alias="granularity")
        r"""Duration in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594#Durations) notation that specifies the interval between
measurement data points.

Measurement granularity can be expressed as days, hours, minutes, seconds and milliseconds using the following notation:

`P` (for *period*) followed by:

- `D` for *days* (if desired)
- `T` for *time* (after *days*)
- `H` for *hours*
- `M` for *minutes*
- `S` for *seconds*

For example:

| Notation | Duration |
| --- | --- |
| `PT30S` | 30 seconds |
| `P1T12H` | 1 day, 12 hours |
| `PT0.5S` | 500 milliseconds |
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        m: Optional[str] = Field(default=None, serialization_alias="m")
        r"""Measurements to return. If `m` is not specified, all
measurements are returned.

To specify multiple values for `m`, you must repeat the `m`
parameter.

For example:

```
|  |
| --- |
| ../measurements?m=CONNECTIONS&m=OPCOUNTER_CMD&m=OPCOUNTER_QUERY |
```

You must specify measurements that are valid for the host. Ops Manager
returns an error if any specified measurements are invalid
For available measurements, see [Measurement Types.](/docs/ops-manager/current/reference/api/measures/measurement-types/)
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""Page number (1-index based).
        """

        period: Optional[str] = Field(default=None, serialization_alias="period")
        r"""Duration in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594#Durations) notation that specifies how far back in the past to
retrieve measurements.

For example, to request the last 36 hours, include this query
parameter: `period=P1DT12H`.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

        start: Optional[str] = Field(default=None, serialization_alias="start")
        r"""Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC for the beginning of the period for which to
retrieve measurements. If you specify `start` you must also
specify `end`.
        """

    def host(
        self,
        path_params: HostPathParams,
        query_params: HostQueryParams,
    ) -> dict[str, Any]:
        r"""
        ## Get Host, Process, System Measurements
        ### Document:
        [Host](https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-host-process-system-measurements/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements?granularity={ISO-8601-PERIOD}&period={ISO-8601-PERIOD}`
        ### Description
        Host measurements provide data on the state of the MongoDB process.
        The Monitoring collects host measurements through the MongoDB
        [serverStatus](https://www.mongodb.com/docs/manual/reference/command/serverStatus/) and
        [dbStats](https://www.mongodb.com/docs/manual/reference/command/dbStats/) commands.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements?granularity={ISO-8601-PERIOD}&period={ISO-8601-PERIOD}",
            path_params,
            query_params,
            None,
        )

    class GetTypesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        r"""Unique identifier of the host that serves the MongoDB process.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        r"""Unique identifier of the [project](https://www.mongodb.com/docs/ops-manager/current/reference/glossary/#std-term-project) that owns the host.
        """

    class GetTypesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        end: Optional[str] = Field(default=None, serialization_alias="end")
        r"""Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC for the end of the period for which to retrieve
measurements. If you specify `end` you must also specify
`start`.
        """

        envelope: Optional[bool] = Field(default=None, serialization_alias="envelope")
        r"""Indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or
status code. To remediate this, set `"envelope" : true` in the
query.

For endpoints that return one result, response body
includes:

| Name | Description |
| --- | --- |
| `status` | HTTP response code |
| `content` | Expected response body |

For endpoints that return a list of results, the `results`
object is an envelope. Ops Manager adds the `status` field to the
response body.
        """

        granularity: str = Field(serialization_alias="granularity")
        r"""Duration in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594#Durations) notation that specifies the interval between
measurement data points.

Measurement granularity can be expressed as days, hours, minutes, seconds and milliseconds using the following notation:

`P` (for *period*) followed by:

- `D` for *days* (if desired)
- `T` for *time* (after *days*)
- `H` for *hours*
- `M` for *minutes*
- `S` for *seconds*

For example:

| Notation | Duration |
| --- | --- |
| `PT30S` | 30 seconds |
| `P1T12H` | 1 day, 12 hours |
| `PT0.5S` | 500 milliseconds |
        """

        items_per_page: Optional[int] = Field(default=100, serialization_alias="itemsPerPage")
        r"""Number of items to return per page, up to a maximum of 500.
        """

        m: Optional[str] = Field(default=None, serialization_alias="m")
        r"""Measurements to return. If `m` is not specified, all
measurements are returned.

To specify multiple values for `m`, you must repeat the `m`
parameter.

For example:

```
|  |
| --- |
| ../measurements?m=CONNECTIONS&m=OPCOUNTER_CMD&m=OPCOUNTER_QUERY |
```

You must specify measurements that are valid for the host. Ops Manager
returns an error if any specified measurements are invalid
For available measurements, see [Measurement Types.](/docs/ops-manager/current/reference/api/measures/measurement-types/)
        """

        page_num: Optional[int] = Field(default=1, serialization_alias="pageNum")
        r"""Page number (1-index based).
        """

        period: Optional[str] = Field(default=None, serialization_alias="period")
        r"""Duration in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594#Durations) notation that specifies how far back in the past to
retrieve measurements.

For example, to request the last 36 hours, include this query
parameter: `period=P1DT12H`.
        """

        pretty: Optional[bool] = Field(default=False, serialization_alias="pretty")
        r"""Indicates whether the response body should be in a
[prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
        """

        start: Optional[str] = Field(default=None, serialization_alias="start")
        r"""Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=960381594) date and time format in UTC for the beginning of the period for which to
retrieve measurements. If you specify `start` you must also
specify `end`.
        """

    def get_types(
        self,
        path_params: GetTypesPathParams,
        query_params: GetTypesQueryParams,
    ) -> dict[str, Any]:
        r"""
        ## Get Measurement Types
        ### Document:
        [Get Types](https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-measurement-types/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements`
        ### Description
        To retrieve the [Measurement Types](/docs/ops-manager/current/reference/api/measures/measurement-types/) that
        apply to a specific measurement without returning a large document,
        issue the following `GET` command with a value of `PT5M` for both
        the `granularity` and `period`. This returns a document with only
        one data point for each measurement.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements",
            path_params,
            query_params,
            None,
        )
