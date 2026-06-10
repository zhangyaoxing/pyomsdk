from pyomsdk.ops_manager_client import OpsManagerClient
from pyomsdk.resources.configuration_resource import ConfigurationResource


# Pylint does not understand pytest fixture injection and reports false positives.
# pylint: disable=redefined-outer-name


def test_configuration_get_the_automation_configuration(
    client: OpsManagerClient, project_with_cluster
) -> None:
    resource = client.configuration_resource
    path_params = ConfigurationResource.GetTheAutomationConfigurationPathParams(
        project_id=project_with_cluster["id"]
    )

    result = resource.get_the_automation_configuration(path_params, None)
    assert result is not None
    assert "processes" in result


def test_configuration_get_the_automation_configuration_no_secrets(
    client: OpsManagerClient, project_with_cluster
) -> None:
    resource = client.configuration_resource
    path_params = ConfigurationResource.GetTheAutomationConfigurationNoSecretsPathParams(
        project_id=project_with_cluster["id"]
    )

    result = resource.get_the_automation_configuration_no_secrets(path_params, None)
    assert result is not None
    assert "error" not in result


def test_configuration_get_log_and_agent_configuration_settings(
    client: OpsManagerClient, project_with_cluster
) -> None:
    resource = client.configuration_resource
    project_id = project_with_cluster["id"]

    audit = resource.get_the_audit_log_rotate_configuration(
        ConfigurationResource.GetTheAuditLogRotateConfigurationPathParams(project_id=project_id),
        None,
    )
    assert audit is not None
    assert "error" not in audit

    backup = resource.get_backup_configuration_settings(
        ConfigurationResource.GetBackupConfigurationSettingsPathParams(project_id=project_id),
        None,
    )
    assert backup is not None
    assert "error" not in backup

    monitoring = resource.get_monitoring_configuration_settings(
        ConfigurationResource.GetMonitoringConfigurationSettingsPathParams(project_id=project_id),
        None,
    )
    assert monitoring is not None
    assert "error" not in monitoring

    system = resource.get_the_system_log_rotate_configuration(
        ConfigurationResource.GetTheSystemLogRotateConfigurationPathParams(project_id=project_id),
        None,
    )
    assert system is not None
    assert "error" not in system
