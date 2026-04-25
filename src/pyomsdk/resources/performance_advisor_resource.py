"""Auto-generated client for PerformanceAdvisorResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class PerformanceAdvisorResource(BaseResource):
    """Client for PerformanceAdvisorResource resource."""

    class GetSlowQueryLogsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """(Required.) Unique identifier of the host for the MongoDB process.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) Unique identifier of the project that owns this MongoDB process.
        """

    class GetSlowQueryLogsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        duration: Optional[int] = Field(None, serialization_alias="duration")
        """Length of time in milliseconds during which to find slow query logs among the managed namespaces in the cluster.
        """

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Indicates whether or not to wrap the response in an envelope.
        """

        n_logs: Optional[int] = Field(20000, serialization_alias="nLogs")
        """Maximum number of log lines to return.
        """

        namespaces: Optional[str] = Field("all", serialization_alias="namespaces")
        """Namespaces from which to retrieve suggested slow query logs. A namespace consists of the database and collection resource separated by a ., such as <database>.<collection>.

To specify multiple namespaces, pass the parameter multiple times using an ampersand (&) as a delimiter, once for each namespace.

For example:

?namespaces=data.stocks&namespaces=data.zips&pretty=true
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

        since: Optional[int] = Field(None, serialization_alias="since")
        """Point in time from which to retrieve slow query logs, stated in milliseconds since epoch.
        """

    def get_slow_query_logs(
        self,
        path_params: GetSlowQueryLogsPathParams,
        query_params: Optional[GetSlowQueryLogsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Slow Query Logs
        ### Document:
        [Get Slow Query Logs](https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/get-slow-queries/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/slowQueryLogs`
        ### Description
        Retrieves log lines for slow queries as determined by the Performance Advisor.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/slowQueryLogs",
            path_params,
            query_params,
            None,
        )

    class GetSuggestedIndexesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """(Required.) Unique identifier of the host for the MongoDB process.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """(Required.) Unique identifier of the project that owns this MongoDB process.
        """

    class GetSuggestedIndexesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        duration: Optional[int] = Field(None, serialization_alias="duration")
        """Length of time in milliseconds during which to find suggested indexes among the managed namespaces in the cluster.
        """

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Indicates whether or not to wrap the response in an envelope.
        """

        n_examples: Optional[int] = Field(5, serialization_alias="nExamples")
        """Maximum number of examples queries to provide that will be improved by a suggested index.
        """

        n_indexes: Optional[int] = Field(None, serialization_alias="nIndexes")
        """Maximum number of indexes to suggest.
        """

        namespaces: Optional[str] = Field("all", serialization_alias="namespaces")
        """Namespaces from which to retrieve suggested indexes. A namespace consists of the database and collection resource separated by a ., such as <database>.<collection>.

To specify multiple namespaces, pass the parameter multiple times using an ampersand (&) as a delimiter, once for each namespace.

For example:

?namespaces=data.stocks&namespaces=data.zips&pretty=true
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format.
        """

        since: Optional[int] = Field(None, serialization_alias="since")
        """Point in time from which to retrieve suggested indexes, stated in milliseconds since epoch.
        """

    def get_suggested_indexes(
        self,
        path_params: GetSuggestedIndexesPathParams,
        query_params: Optional[GetSuggestedIndexesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Suggested Indexes
        ### Document:
        [Get Suggested Indexes](https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/get-suggested-indexes/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/suggestedIndexes`
        ### Description
        Retrieves suggested indexes as determined by the Performance Advisor.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/suggestedIndexes",
            path_params,
            query_params,
            None,
        )

    class GetNamespacesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="HOST-ID")
        """The unique identifier for the host of a MongoDB process. For information about retrieving host ids, see Get All Hosts in One Project.
        """

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """The unique identifier for the project where the MongoDB host resides.
        """

    class GetNamespacesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        duration: Optional[int] = Field(None, serialization_alias="duration")
        """Length of time from the since parameter, in milliseconds, for which you want to receive results. If you do not also specify the since parameter, the endpoint returns results from the number of milliseconds specified by duration before the current time until now.
        """

        envelope: Optional[bool] = Field(None, serialization_alias="envelope")
        """Specifies whether or not to wrap the response in an envelope. The default is false.
        """

        pretty: Optional[bool] = Field(None, serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format. The default value is false.
        """

        since: Optional[int] = Field(None, serialization_alias="since")
        """Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive results. If you do not also specify the duration parameter, the endpoint returns results from since until the current time.
        """

    def get_namespaces(
        self,
        path_params: GetNamespacesPathParams,
        query_params: Optional[GetNamespacesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Namespaces for a Project
        ### Document:
        [Get Namespaces](https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/pa-namespaces-get-all/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/namespaces`
        ### Description
        Retrieve namespaces for collections experiencing slow queries on a specified host. Namespaces appear in the following format: {database}.{collection}.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/namespaces",
            path_params,
            query_params,
            None,
        )
