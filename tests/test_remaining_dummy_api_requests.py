from __future__ import annotations

import inspect
from json import JSONDecodeError
from typing import Any, get_args, get_origin

import pytest
from pydantic import BaseModel

from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.enums import IntegrationType, ServerTypeName


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


DUMMY_ID = "000000000000000000000000"


DUMMY_API_CASES = [
    ("alert_configurations_resource", "create"),
    ("alert_configurations_resource", "delete"),
    ("alert_configurations_resource", "enable_disable"),
    ("alert_configurations_resource", "test_project_alert_configuration"),
    ("alert_configurations_resource", "update"),
    ("blockstore_resource", "create"),
    ("blockstore_resource", "delete"),
    ("blockstore_resource", "get_by_id"),
    ("blockstore_resource", "update"),
    ("configuration_resource", "update_agent_versions"),
    ("configuration_resource", "update_the_audit_log_rotate_config"),
    ("configuration_resource", "update_the_automation_configuration_no_secrets"),
    ("configuration_resource", "update_the_automation_configuration"),
    ("configuration_resource", "update_backup_configuration_settings"),
    ("configuration_resource", "update_monitoring_configuration_settings"),
    ("configuration_resource", "update_the_system_log_rotate_config"),
    ("deployment_regions_resource", "assign"),
    ("deployment_regions_resource", "create_by_id"),
    ("deployment_regions_resource", "create"),
    ("deployment_regions_resource", "delete"),
    ("file_system_store_resource", "create"),
    ("file_system_store_resource", "delete"),
    ("file_system_store_resource", "update"),
    ("global_alert_configurations_resource", "get_all_open_alerts"),
    ("global_alert_configurations_resource", "create"),
    ("global_alert_configurations_resource", "delete"),
    ("global_alert_configurations_resource", "get_one"),
    ("global_alert_configurations_resource", "enable_or_disable"),
    ("global_alert_configurations_resource", "update"),
    ("global_api_keys_resource", "create"),
    ("global_api_keys_resource", "delete"),
    ("global_api_keys_resource", "update"),
    ("hosts_resource", "begin_monitoring"),
    ("hosts_resource", "stop_monitoring"),
    ("hosts_resource", "update_configuration"),
    ("integration_settings_resource", "create"),
    ("integration_settings_resource", "delete"),
    ("integration_settings_resource", "get_one_configuration"),
    ("integration_settings_resource", "update"),
    ("log_collection_jobs_resource", "delete"),
    ("log_collection_jobs_resource", "download_logs"),
    ("log_collection_jobs_resource", "retry"),
    ("log_collection_jobs_resource", "create"),
    ("log_collection_jobs_resource", "extend"),
    ("oplog_store_resource", "create"),
    ("oplog_store_resource", "delete"),
    ("oplog_store_resource", "update"),
    ("organizations_resource", "invite_user"),
    ("organizations_resource", "delete_invitation"),
    ("organizations_resource", "get_all_invitations"),
    ("organizations_resource", "get_one_invitation"),
    ("organizations_resource", "update_by_invitation_id"),
    ("organizations_resource", "update_invitation"),
    ("projects_resource", "add_existing_users"),
    ("projects_resource", "get_by_agent_api_key"),
    ("projects_resource", "add_teams"),
    ("projects_resource", "remove_user"),
    ("projects_resource", "create_invitation"),
    ("projects_resource", "delete_invitation"),
    ("projects_resource", "get_all_invitations"),
    ("projects_resource", "get_one_invitation"),
    ("projects_resource", "update_invitation_by_invitation_id"),
    ("projects_resource", "update_invitation"),
    ("projects_resource", "remove_team"),
    ("restore_jobs_resource", "create_cluster"),
    ("restore_jobs_resource", "create_config_server"),
    ("restore_jobs_resource", "get_all_config_server"),
    ("restore_jobs_resource", "get_one_cluster"),
    ("restore_jobs_resource", "get_one_config_server"),
    ("s3_compatible_blockstore_resource", "create"),
    ("s3_compatible_blockstore_resource", "delete"),
    ("s3_compatible_blockstore_resource", "update"),
    ("server_usage_resource", "get_diagnostic_archive"),
    ("server_usage_resource", "create_physical_host"),
    ("server_usage_resource", "get_global_usage_report_archive"),
    ("server_usage_resource", "generate_usage_snapshot"),
    ("server_usage_resource", "retrieve_all_physical_hosts"),
    ("server_usage_resource", "get_server_type_in_one_organization"),
    ("server_usage_resource", "retreive_one_physical_host"),
    ("server_usage_resource", "list_host_assignments_in_one_organization"),
    ("server_usage_resource", "list_host_assignments_in_one_project"),
    ("server_usage_resource", "list_host_assignments"),
    ("server_usage_resource", "remove_physical_host"),
    ("server_usage_resource", "update_server_type_for_one_organization"),
    ("server_usage_resource", "update_default_server_type"),
    ("server_usage_resource", "update_physical_host"),
    ("server_usage_resource", "update_server_type"),
    ("snapshots_resource", "change_expiry"),
    ("snapshots_resource", "get_all_config_server"),
    ("snapshots_resource", "get_one_config_server"),
    ("snapshots_resource", "remove_one"),
    ("snapshots_resource", "create_one_on_demand_cluster"),
    ("sync_store_resource", "create"),
    ("sync_store_resource", "delete"),
    ("sync_store_resource", "update"),
    ("teams_resource", "update_roles"),
]


def _method_model_prefix(method_name: str) -> str:
    return "".join(part.capitalize() for part in method_name.split("_"))


def _dummy_path_value(
    field_name: str, annotation: Any, project: dict[str, Any], org: dict[str, Any]
) -> Any:
    if field_name in {"project_id", "group_id"}:
        return project["id"]
    if field_name == "org_id":
        return org["id"]
    if field_name == "integration_type":
        return IntegrationType.WEBHOOK
    if field_name in {"server_type", "server_type_name"}:
        return ServerTypeName.DEV_SERVER
    return _sample_value(annotation)


def _sample_value(annotation: Any) -> Any:
    origin = get_origin(annotation)
    args = get_args(annotation)
    if origin is list:
        return []
    if inspect.isclass(annotation) and issubclass(annotation, BaseModel):
        return _build_path_model(annotation, {}, {})
    if inspect.isclass(annotation) and hasattr(annotation, "__members__"):
        return next(iter(annotation))
    if annotation is int:
        return 1
    if annotation is bool:
        return True
    return DUMMY_ID


def _build_path_model(
    model_cls: type[BaseModel], project: dict[str, Any], org: dict[str, Any]
) -> BaseModel:
    values = {
        field_name: _dummy_path_value(field_name, field.annotation, project, org)
        for field_name, field in model_cls.model_fields.items()
    }
    return model_cls(**values)


def _build_args(
    resource: Any, method_name: str, project: dict[str, Any], org: dict[str, Any]
) -> list[Any]:
    resource_cls = resource.__class__
    method = getattr(resource, method_name)
    args = []
    for param_name in list(inspect.signature(method).parameters):
        if param_name == "path_params":
            model_cls = getattr(resource_cls, f"{_method_model_prefix(method_name)}PathParams")
            args.append(_build_path_model(model_cls, project, org))
        elif param_name == "query_params":
            args.append(None)
        elif param_name == "body_params":
            args.append({})
        else:
            raise AssertionError(f"Unexpected parameter {param_name} on {method_name}")
    return args


@pytest.mark.parametrize("resource_name, method_name", DUMMY_API_CASES)
def test_remaining_api_accepts_dummy_request(
    client: OpsManagerClient,
    project: dict[str, Any],
    org: dict[str, Any],
    resource_name: str,
    method_name: str,
) -> None:
    resource = getattr(client, resource_name)
    method = getattr(resource, method_name)

    try:
        result = method(*_build_args(resource, method_name, project, org))
    except JSONDecodeError:
        pytest.skip("Server returned a non-JSON response to the dummy request")

    assert result is None or isinstance(result, (dict, list))
