"""Auto-generated client for ServerUsageResource resource.
Any manual changes to this file may be overwritten when the code is regenerated.
"""
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *


class ServerUsageResource(BaseResource):
    """Client for ServerUsageResource resource."""

    class GetDiagnosticArchivePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field(serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the diagnostics archive.
        """

    class GetDiagnosticArchiveQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        age_limit: Optional[int] = Field(7, serialization_alias="ageLimit")
        """Length of time in days to retrieve entries for the diagnostic archive.
        """

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope : true in the query.

For endpoints that return a list of results, the content object is an envelope. Ops Manager adds the status field to the response body.
        """

        items_per_page: Optional[int] = Field(100, serialization_alias="itemsPerPage")
        """Number of items to return per page, up to a maximum of 500.
        """

        limit: Optional[int] = Field(1000, serialization_alias="limit")
        """Maximum number of entries for the diagnostic archive.
        """

        minutes: Optional[int] = Field(1440, serialization_alias="minutes")
        """Time range of the diagnostic archive, beginning at the specified number of minutes in the past and ending at the present time.

For example, to retrieve a diagnostic archive with data for the last 10 minutes, specify minutes=10 in your request .
        """

        page_num: Optional[int] = Field(1, serialization_alias="pageNum")
        """One-based integer that returns a subsection of results.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag that indicates whether the response body should be in a prettyprint format.
        """

        size_limit: Optional[int] = Field(50000000, serialization_alias="sizeLimit")
        """Maximum file size of each file in the diagnostic archive expressed in the number of characters. This includes values up to the nearest whole value to this limit.
        """

    def get_diagnostic_archive(
        self,
        path_params: GetDiagnosticArchivePathParams,
        query_params: Optional[GetDiagnosticArchiveQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Project Diagnostic Archive
        ### Document:
        [Get Diagnostic Archive](https://www.mongodb.com/docs/ops-manager/current/reference/api/diagnostics/get-project-diagnostic-archive/)
        ### Endpoint:
        `GET /groups/{PROJECT-ID}/diagnostics`
        ### Description
        MongoDB engineers may request that Ops Manager administrators provide diagnostic archives for one project for debugging and troubleshooting. Project diagnostic archives also contain global system information about Ops Manager.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{PROJECT-ID}/diagnostics",
            path_params,
            query_params,
            None,
        )

    class CreatePhysicalHostQueryParams(BaseModel):
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

    class CreatePhysicalHostBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        name: str = Field(serialization_alias="name")
        """Label you gave to the physical host. This value must be unique.
        """

        server_type: ServerTypeName = Field(serialization_alias="serverType")
        """Server Type of the physical host. You can set this to one of the following values:

DEV_SERVER

TEST_SERVER

PRODUCTION_SERVER

RAM_POOL

To learn more, see MongoDB Usage Page.
        """

        class VirtualhostsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            group_id: Optional[str] = Field(None, serialization_alias="groupId")
            """Unique identifier of the project into which Ops Manager places this virtual host.
            """

            hostname: Optional[str] = Field(None, serialization_alias="hostname")
            """FQDN of the virtual host bound to the physical host.
            """

        virtual_hosts: list[VirtualhostsParams] = Field(serialization_alias="virtualHosts")
        """List of virtual hosts bound to the provided physical host.
        """

    def create_physical_host(
        self,
        query_params: Optional[CreatePhysicalHostQueryParams],
        body_params: CreatePhysicalHostBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Physical Host
        ### Document:
        [Create Physical Host](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/create-one-physical-host/)
        ### Endpoint:
        `POST /usage/groups`
        ### Description
        No description.
        """
        return self._request(
            "POST",
            "/api/public/v1.0/usage/groups",
            None,
            query_params,
            body_params,
        )

    class GetGlobalUsageReportArchiveQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        end_date: str = Field(serialization_alias="endDate")
        """Date in ISO 8601 date format when the report ends.
        """

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

        file_format: str = Field(serialization_alias="fileFormat")
        """Compression format of the resulting report. Ops Manager accepts zip or .tar.gz.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

        redact: Optional[bool] = Field(True, serialization_alias="redact")
        """Flag that indicates whether the response should censor all IP addresses, hostnames, organization names, and project names in the report.
        """

        start_date: str = Field(serialization_alias="startDate")
        """Date in ISO 8601 date format when the report starts.
        """

    def get_global_usage_report_archive(
        self,
        query_params: GetGlobalUsageReportArchiveQueryParams,
    ) -> dict[str, Any]:
        """
        ## Get One Global Usage Report Archive
        ### Document:
        [Get Global Usage Report Archive](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/create-one-report/)
        ### Endpoint:
        `GET /usage/report`
        ### Description
        Retrieve a compressed report, in zip or .tar.gz format, of server usage in a given timeframe.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/usage/report",
            None,
            query_params,
            None,
        )

    class GenerateUsageSnapshotQueryParams(BaseModel):
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

    def generate_usage_snapshot(
        self,
        query_params: Optional[GenerateUsageSnapshotQueryParams],
    ) -> dict[str, Any]:
        """
        ## Generate Daily Usage Snapshot
        ### Document:
        [Generate Usage Snapshot](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/generate-daily-usage-snapshot/)
        ### Endpoint:
        `POST /usage/dailyCapture`
        ### Description
        If MongoDB Usage UI is set to On, you can trigger this endpoint which tells Ops Manager to:
        """
        return self._request(
            "POST",
            "/api/public/v1.0/usage/dailyCapture",
            None,
            query_params,
            None,
        )

    class RetrieveAllPhysicalHostsQueryParams(BaseModel):
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

    def retrieve_all_physical_hosts(
        self,
        query_params: Optional[RetrieveAllPhysicalHostsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve All Physical Hosts
        ### Document:
        [Retrieve All Physical Hosts](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-all-physical-hosts/)
        ### Endpoint:
        `GET /usage/groups`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/usage/groups",
            None,
            query_params,
            None,
        )

    class GetServerTypeInOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="orgId")
        """Unique identifier of the organization.
        """

    class GetServerTypeInOneOrganizationQueryParams(BaseModel):
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

    def get_server_type_in_one_organization(
        self,
        path_params: GetServerTypeInOneOrganizationPathParams,
        query_params: Optional[GetServerTypeInOneOrganizationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Default Server Type For One Organization
        ### Document:
        [Get Server Type in One Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-default-server-type-for-one-organization/)
        ### Endpoint:
        `GET /usage/organizations/{orgId}/defaultServerType`
        ### Description
        Retrieve the default server type for one organization.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/usage/organizations/{orgId}/defaultServerType",
            path_params,
            query_params,
            None,
        )

    class GetDefaultServerTypePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="groupId")
        """Unique identifier of the project associated with the desired hosts.
        """

    class GetDefaultServerTypeQueryParams(BaseModel):
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

    def get_default_server_type(
        self,
        path_params: GetDefaultServerTypePathParams,
        query_params: Optional[GetDefaultServerTypeQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Default Server Type For One Project
        ### Document:
        [Get Default Server Type](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-default-server-type-for-one-project/)
        ### Endpoint:
        `GET /usage/groups/{groupId}/defaultServerType`
        ### Description
        Retrieve the default server type for one project.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/usage/groups/{groupId}/defaultServerType",
            path_params,
            query_params,
            None,
        )

    class RetreiveOnePhysicalHostPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        physical_host_id: str = Field(serialization_alias="physicalHostId")
        """Unique identifier of the physical host to be retrieved.
        """

    class RetreiveOnePhysicalHostQueryParams(BaseModel):
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

    def retreive_one_physical_host(
        self,
        path_params: RetreiveOnePhysicalHostPathParams,
        query_params: Optional[RetreiveOnePhysicalHostQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve One Physical Host
        ### Document:
        [Retreive One Physical Host](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-one-physical-host-by-host-id/)
        ### Endpoint:
        `GET /usage/groups/{physicalHostId}`
        ### Description
        No description.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/usage/groups/{physicalHostId}",
            path_params,
            query_params,
            None,
        )

    class ListHostAssignmentsInOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="orgId")
        """Unique identifier of the organization associated with the desired hosts.
        """

    class ListHostAssignmentsInOneOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        end_date: str = Field(serialization_alias="endDate")
        """Date in ISO 8601 date format when the list of host assignments ends.
        """

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

        items_per_page: int = Field(100, serialization_alias="itemsPerPage")
        """Number of host assignments to return in one group.
        """

        page_num: int = Field(serialization_alias="pageNum")
        """Starting group of host assignments to return. The group size is defined by itemsPerPage. This value starts with 1.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

        start_date: str = Field(serialization_alias="startDate")
        """Date in ISO 8601 date format when the list of host assignments starts.
        """

    def list_host_assignments_in_one_organization(
        self,
        path_params: ListHostAssignmentsInOneOrganizationPathParams,
        query_params: ListHostAssignmentsInOneOrganizationQueryParams,
    ) -> dict[str, Any]:
        """
        ## List All Host Assignments In One Organization
        ### Document:
        [List Host Assignments in One Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/list-all-host-assignments-in-one-organization/)
        ### Endpoint:
        `GET /usage/organizations/{orgId}/hosts`
        ### Description
        Retrieves all host assignments for one organization.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/usage/organizations/{orgId}/hosts",
            path_params,
            query_params,
            None,
        )

    class ListHostAssignmentsInOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="groupId")
        """Unique identifier of the project associated with the desired hosts.
        """

    class ListHostAssignmentsInOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        end_date: str = Field(serialization_alias="endDate")
        """Date in ISO 8601 date format when the list of host assignments ends.
        """

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

        items_per_page: int = Field(100, serialization_alias="itemsPerPage")
        """Number of host assignments to return in one group.
        """

        page_num: int = Field(serialization_alias="pageNum")
        """Starting group of host assignments to return. The group size is defined by itemsPerPage. This value starts with 1.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

        start_date: str = Field(serialization_alias="startDate")
        """Date in ISO 8601 date format when the list of host assignments starts.
        """

    def list_host_assignments_in_one_project(
        self,
        path_params: ListHostAssignmentsInOneProjectPathParams,
        query_params: ListHostAssignmentsInOneProjectQueryParams,
    ) -> dict[str, Any]:
        """
        ## List All Host Assignments In One Project
        ### Document:
        [List Host Assignments in One Project](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/list-all-host-assignments-in-one-project/)
        ### Endpoint:
        `GET /usage/groups/{groupId}/hosts`
        ### Description
        Retrieves all host assignments for one project.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/usage/groups/{groupId}/hosts",
            path_params,
            query_params,
            None,
        )

    class ListHostAssignmentsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        end_date: str = Field(serialization_alias="endDate")
        """Date in ISO 8601 date format when the list of host assignments ends.
        """

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

        items_per_page: int = Field(100, serialization_alias="itemsPerPage")
        """Number of host assignments to return in one group.
        """

        page_num: int = Field(serialization_alias="pageNum")
        """Starting group of host assignments to return. The group size is defined by itemsPerPage. This value starts with 1.
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

        start_date: str = Field(serialization_alias="startDate")
        """Date in ISO 8601 date format when the list of host assignments starts.
        """

    def list_host_assignments(
        self,
        query_params: ListHostAssignmentsQueryParams,
    ) -> dict[str, Any]:
        """
        ## List All Host Assignments
        ### Document:
        [List Host Assignments](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/list-all-host-assignments/)
        ### Endpoint:
        `GET /usage/assignments`
        ### Description
        Retrieves all host assignments.
        """
        return self._request(
            "GET",
            "/api/public/v1.0/usage/assignments",
            None,
            query_params,
            None,
        )

    class RemovePhysicalHostPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        physical_host_id: str = Field(serialization_alias="physicalHostId")
        """Unique identifier of the physical host.
        """

    class RemovePhysicalHostQueryParams(BaseModel):
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

    def remove_physical_host(
        self,
        path_params: RemovePhysicalHostPathParams,
        query_params: Optional[RemovePhysicalHostQueryParams],
    ) -> dict[str, Any]:
        """
        ## Remove One Physical Host
        ### Document:
        [Remove Physical Host](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/remove-one-physical-host/)
        ### Endpoint:
        `DELETE /usage/groups/{physicalHostId}`
        ### Description
        No description.
        """
        return self._request(
            "DELETE",
            "/api/public/v1.0/usage/groups/{physicalHostId}",
            path_params,
            query_params,
            None,
        )

    class UpdateServerTypeForOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        org_id: str = Field(serialization_alias="orgId")
        """Unique identifier of the organization.
        """

    class UpdateServerTypeForOneOrganizationQueryParams(BaseModel):
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

    class UpdateServerTypeForOneOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        class ServertypeParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            label: Optional[ServerTypeLabel] = Field(None, serialization_alias="label")
            """Server Type label for the physical host.

You can set this to one of the following values:

Dev Server

Test Server

Production Server

Ram Pool

To learn more, see MongoDB Usage Page.
            """

            name: ServerTypeName = Field(serialization_alias="name")
            """Server Type value for the physical host.

You can set this to one of the following values:

DEV_SERVER

TEST_SERVER

PRODUCTION_SERVER

RAM_POOL

To learn more, see MongoDB Usage Page.
            """

        server_type: ServertypeParams = Field(serialization_alias="serverType")
        """Server Type of the physical host.
        """

    def update_server_type_for_one_organization(
        self,
        path_params: UpdateServerTypeForOneOrganizationPathParams,
        query_params: Optional[UpdateServerTypeForOneOrganizationQueryParams],
        body_params: UpdateServerTypeForOneOrganizationBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update Default Server Type For One Organization
        ### Document:
        [Update Server Type for One Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-default-server-type-for-one-organization/)
        ### Endpoint:
        `PUT /usage/organizations/{orgId}/defaultServerType`
        ### Description
        Update the default server type for one organization.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/usage/organizations/{orgId}/defaultServerType",
            path_params,
            query_params,
            body_params,
        )

    class UpdateDefaultServerTypePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        group_id: str = Field(serialization_alias="groupId")
        """Unique identifier of the project associated with the desired hosts.
        """

    class UpdateDefaultServerTypeQueryParams(BaseModel):
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

    class UpdateDefaultServerTypeBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        class ServertypeParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            label: Optional[ServerTypeLabel] = Field(None, serialization_alias="label")
            """Server Type label for the physical host.

You can set this to one of the following values:

Dev Server

Test Server

Production Server

Ram Pool

To learn more, see MongoDB Usage Page.
            """

            name: ServerTypeName = Field(serialization_alias="name")
            """Server Type value for the physical host.

You can set this to one of the following values:

DEV_SERVER

TEST_SERVER

PRODUCTION_SERVER

RAM_POOL

To learn more, see MongoDB Usage Page.
            """

        server_type: ServertypeParams = Field(serialization_alias="serverType")
        """Server Type of the physical host.
        """

    def update_default_server_type(
        self,
        path_params: UpdateDefaultServerTypePathParams,
        query_params: Optional[UpdateDefaultServerTypeQueryParams],
        body_params: UpdateDefaultServerTypeBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update Default Server Type For One Project
        ### Document:
        [Update Default Server Type](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-default-server-type-for-one-project/)
        ### Endpoint:
        `PUT /usage/groups/{groupId}/defaultServerType`
        ### Description
        Update the default server type for one project.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/usage/groups/{groupId}/defaultServerType",
            path_params,
            query_params,
            body_params,
        )

    class UpdatePhysicalHostPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        physical_host_id: str = Field(serialization_alias="physicalHostId")
        """Unique identifier of the physical host.
        """

    class UpdatePhysicalHostQueryParams(BaseModel):
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

    class UpdatePhysicalHostBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        name: str = Field(serialization_alias="name")
        """Label you gave to the physical host. This value must be unique.
        """

        server_type: ServerTypeName = Field(serialization_alias="serverType")
        """Server Type of the physical host. You can set this to one of the following values:

DEV_SERVER

TEST_SERVER

PRODUCTION_SERVER

RAM_POOL

To learn more, see MongoDB Usage Page.
        """

        class VirtualhostsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            group_id: Optional[str] = Field(None, serialization_alias="groupId")
            """Unique identifier of the project into which Ops Manager places this virtual host.
            """

            hostname: Optional[str] = Field(None, serialization_alias="hostname")
            """FQDN of the virtual host bound to the physical host.
            """

        virtual_hosts: list[VirtualhostsParams] = Field(serialization_alias="virtualHosts")
        """List of virtual hosts bound to the provided physical host.
        """

    def update_physical_host(
        self,
        path_params: UpdatePhysicalHostPathParams,
        query_params: Optional[UpdatePhysicalHostQueryParams],
        body_params: UpdatePhysicalHostBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Physical Host
        ### Document:
        [Update Physical Host](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-one-physical-host/)
        ### Endpoint:
        `PUT /usage/groups/{physicalHostId}`
        ### Description
        No description.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/usage/groups/{physicalHostId}",
            path_params,
            query_params,
            body_params,
        )

    class UpdateServerTypePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field(serialization_alias="hostId")
        """Unique identifier of the host.
        """

    class UpdateServerTypeQueryParams(BaseModel):
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

    class UpdateServerTypeBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        class ServertypeParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            label: Optional[ServerTypeLabel] = Field(None, serialization_alias="label")
            """Server Type label for the physical host.

You can set this to one of the following values:

Dev Server

Test Server

Production Server

Ram Pool

To learn more, see MongoDB Usage Page.
            """

            name: ServerTypeName = Field(serialization_alias="name")
            """Server Type value for the physical host.

You can set this to one of the following values:

DEV_SERVER

TEST_SERVER

PRODUCTION_SERVER

RAM_POOL

To learn more, see MongoDB Usage Page.
            """

        server_type: ServertypeParams = Field(serialization_alias="serverType")
        """Server Type of the physical host.
        """

    def update_server_type(
        self,
        path_params: UpdateServerTypePathParams,
        query_params: Optional[UpdateServerTypeQueryParams],
        body_params: UpdateServerTypeBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update Server Type for One Host
        ### Document:
        [Update Server Type](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-server-type-for-one-host/)
        ### Endpoint:
        `PUT /usage/hosts/{hostId}`
        ### Description
        Update one default server type for one host.
        """
        return self._request(
            "PUT",
            "/api/public/v1.0/usage/hosts/{hostId}",
            path_params,
            query_params,
            body_params,
        )
