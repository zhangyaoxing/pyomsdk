from importlib.metadata import version
from httpx import Auth, DigestAuth, Client
from .resources import AccessListResource
from .resources import BackupDaemonResource
from .resources import ProjectBackupJobResource
from .resources import OplogStoreResource
from .resources import S3OplogResource
from .resources import FileSystemStoreResource
from .resources import BlockstoreResource
from .resources import S3CompatibleBlockstoreResource
from .resources import SyncStoreResource
from .resources import AgentsResource
from .resources import AlertConfigurationsResource
from .resources import AlertsResource
from .resources import GlobalAccessListResource
from .resources import GlobalApiKeysResource
from .resources import OrganizationApiKeysResource
from .resources import OrganizationAccessListsResource
from .resources import ApiKeysOnProjectsResource
from .resources import ConfigurationResource
from .resources import AutomationResource
from .resources import DeploymentRegionsResource
from .resources import BackupConfigurationsResource
from .resources import SnapshotScheduleResource
from .resources import MigrateToMongodbAtlasResource
from .resources import ClustersResource
from .resources import FeatureControlPoliciesResource
from .resources import DatabasesResource
from .resources import ServerUsageResource
from .resources import DisksResource
from .resources import EventsResource
from .resources import GlobalEventsResource
from .resources import GlobalAlertConfigurationsResource
from .resources import GlobalAlertsResource
from .resources import ProjectsResource
from .resources import HostsResource
from .resources import ImportDeploymentsResource
from .resources import OrganizationsResource
from .resources import BackupEncryptionKeysResource
from .resources import LogCollectionJobsResource
from .resources import MaintenanceWindowsResource
from .resources import MeasurementsResource
from .resources import PerformanceAdvisorResource
from .resources import RestoreJobsResource
from .resources import RootResource
from .resources import SnapshotsResource
from .resources import TeamsResource
from .resources import TelemetryResource
from .resources import IntegrationSettingsResource
from .resources import UsersResource
from .resources import VersionManifestResource


class OpsManagerClient:
    def __init__(
        self, base_url: str, public_key: str, private_key: str, timeout: float = 30.0
    ) -> None:
        ver_num: str = version("ops-manager-sdk")
        assert (
            base_url and public_key and private_key
        ), "Base URL, public key, and private key are required to initialize the OpsManagerClient."
        auth: Auth = DigestAuth(public_key, private_key)
        self._client = Client(
            base_url=f"{base_url.rstrip('/')}/api/public/v1.0",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": f"ops-manager-sdk-python/{ver_num}",
            },
            timeout=timeout,
            auth=auth,
        )

    @property
    def access_list_resource(self) -> AccessListResource:
        """Get the client for AccessListResource resource."""
        return AccessListResource(self._client)

    @property
    def backup_daemon_resource(self) -> BackupDaemonResource:
        """Get the client for BackupDaemonResource resource."""
        return BackupDaemonResource(self._client)

    @property
    def project_backup_job_resource(self) -> ProjectBackupJobResource:
        """Get the client for ProjectBackupJobResource resource."""
        return ProjectBackupJobResource(self._client)

    @property
    def oplog_store_resource(self) -> OplogStoreResource:
        """Get the client for OplogStoreResource resource."""
        return OplogStoreResource(self._client)

    @property
    def s3_oplog_resource(self) -> S3OplogResource:
        """Get the client for S3OplogResource resource."""
        return S3OplogResource(self._client)

    @property
    def file_system_store_resource(self) -> FileSystemStoreResource:
        """Get the client for FileSystemStoreResource resource."""
        return FileSystemStoreResource(self._client)

    @property
    def blockstore_resource(self) -> BlockstoreResource:
        """Get the client for BlockstoreResource resource."""
        return BlockstoreResource(self._client)

    @property
    def s3_compatible_blockstore_resource(self) -> S3CompatibleBlockstoreResource:
        """Get the client for S3CompatibleBlockstoreResource resource."""
        return S3CompatibleBlockstoreResource(self._client)

    @property
    def sync_store_resource(self) -> SyncStoreResource:
        """Get the client for SyncStoreResource resource."""
        return SyncStoreResource(self._client)

    @property
    def agents_resource(self) -> AgentsResource:
        """Get the client for AgentsResource resource."""
        return AgentsResource(self._client)

    @property
    def alert_configurations_resource(self) -> AlertConfigurationsResource:
        """Get the client for AlertConfigurationsResource resource."""
        return AlertConfigurationsResource(self._client)

    @property
    def alerts_resource(self) -> AlertsResource:
        """Get the client for AlertsResource resource."""
        return AlertsResource(self._client)

    @property
    def global_access_list_resource(self) -> GlobalAccessListResource:
        """Get the client for GlobalAccessListResource resource."""
        return GlobalAccessListResource(self._client)

    @property
    def global_api_keys_resource(self) -> GlobalApiKeysResource:
        """Get the client for GlobalApiKeysResource resource."""
        return GlobalApiKeysResource(self._client)

    @property
    def organization_api_keys_resource(self) -> OrganizationApiKeysResource:
        """Get the client for OrganizationApiKeysResource resource."""
        return OrganizationApiKeysResource(self._client)

    @property
    def organization_access_lists_resource(self) -> OrganizationAccessListsResource:
        """Get the client for OrganizationAccessListsResource resource."""
        return OrganizationAccessListsResource(self._client)

    @property
    def api_keys_on_projects_resource(self) -> ApiKeysOnProjectsResource:
        """Get the client for ApiKeysOnProjectsResource resource."""
        return ApiKeysOnProjectsResource(self._client)

    @property
    def configuration_resource(self) -> ConfigurationResource:
        """Get the client for ConfigurationResource resource."""
        return ConfigurationResource(self._client)

    @property
    def automation_resource(self) -> AutomationResource:
        """Get the client for AutomationResource resource."""
        return AutomationResource(self._client)

    @property
    def deployment_regions_resource(self) -> DeploymentRegionsResource:
        """Get the client for DeploymentRegionsResource resource."""
        return DeploymentRegionsResource(self._client)

    @property
    def backup_configurations_resource(self) -> BackupConfigurationsResource:
        """Get the client for BackupConfigurationsResource resource."""
        return BackupConfigurationsResource(self._client)

    @property
    def snapshot_schedule_resource(self) -> SnapshotScheduleResource:
        """Get the client for SnapshotScheduleResource resource."""
        return SnapshotScheduleResource(self._client)

    @property
    def migrate_to_mongodb_atlas_resource(self) -> MigrateToMongodbAtlasResource:
        """Get the client for MigrateToMongodbAtlasResource resource."""
        return MigrateToMongodbAtlasResource(self._client)

    @property
    def clusters_resource(self) -> ClustersResource:
        """Get the client for ClustersResource resource."""
        return ClustersResource(self._client)

    @property
    def feature_control_policies_resource(self) -> FeatureControlPoliciesResource:
        """Get the client for FeatureControlPoliciesResource resource."""
        return FeatureControlPoliciesResource(self._client)

    @property
    def databases_resource(self) -> DatabasesResource:
        """Get the client for DatabasesResource resource."""
        return DatabasesResource(self._client)

    @property
    def server_usage_resource(self) -> ServerUsageResource:
        """Get the client for ServerUsageResource resource."""
        return ServerUsageResource(self._client)

    @property
    def disks_resource(self) -> DisksResource:
        """Get the client for DisksResource resource."""
        return DisksResource(self._client)

    @property
    def events_resource(self) -> EventsResource:
        """Get the client for EventsResource resource."""
        return EventsResource(self._client)

    @property
    def global_events_resource(self) -> GlobalEventsResource:
        """Get the client for GlobalEventsResource resource."""
        return GlobalEventsResource(self._client)

    @property
    def global_alert_configurations_resource(self) -> GlobalAlertConfigurationsResource:
        """Get the client for GlobalAlertConfigurationsResource resource."""
        return GlobalAlertConfigurationsResource(self._client)

    @property
    def global_alerts_resource(self) -> GlobalAlertsResource:
        """Get the client for GlobalAlertsResource resource."""
        return GlobalAlertsResource(self._client)

    @property
    def projects_resource(self) -> ProjectsResource:
        """Get the client for ProjectsResource resource."""
        return ProjectsResource(self._client)

    @property
    def hosts_resource(self) -> HostsResource:
        """Get the client for HostsResource resource."""
        return HostsResource(self._client)

    @property
    def import_deployments_resource(self) -> ImportDeploymentsResource:
        """Get the client for ImportDeploymentsResource resource."""
        return ImportDeploymentsResource(self._client)

    @property
    def organizations_resource(self) -> OrganizationsResource:
        """Get the client for OrganizationsResource resource."""
        return OrganizationsResource(self._client)

    @property
    def backup_encryption_keys_resource(self) -> BackupEncryptionKeysResource:
        """Get the client for BackupEncryptionKeysResource resource."""
        return BackupEncryptionKeysResource(self._client)

    @property
    def log_collection_jobs_resource(self) -> LogCollectionJobsResource:
        """Get the client for LogCollectionJobsResource resource."""
        return LogCollectionJobsResource(self._client)

    @property
    def maintenance_windows_resource(self) -> MaintenanceWindowsResource:
        """Get the client for MaintenanceWindowsResource resource."""
        return MaintenanceWindowsResource(self._client)

    @property
    def measurements_resource(self) -> MeasurementsResource:
        """Get the client for MeasurementsResource resource."""
        return MeasurementsResource(self._client)

    @property
    def performance_advisor_resource(self) -> PerformanceAdvisorResource:
        """Get the client for PerformanceAdvisorResource resource."""
        return PerformanceAdvisorResource(self._client)

    @property
    def restore_jobs_resource(self) -> RestoreJobsResource:
        """Get the client for RestoreJobsResource resource."""
        return RestoreJobsResource(self._client)

    @property
    def root_resource(self) -> RootResource:
        """Get the client for RootResource resource."""
        return RootResource(self._client)

    @property
    def snapshots_resource(self) -> SnapshotsResource:
        """Get the client for SnapshotsResource resource."""
        return SnapshotsResource(self._client)

    @property
    def teams_resource(self) -> TeamsResource:
        """Get the client for TeamsResource resource."""
        return TeamsResource(self._client)

    @property
    def telemetry_resource(self) -> TelemetryResource:
        """Get the client for TelemetryResource resource."""
        return TelemetryResource(self._client)

    @property
    def integration_settings_resource(self) -> IntegrationSettingsResource:
        """Get the client for IntegrationSettingsResource resource."""
        return IntegrationSettingsResource(self._client)

    @property
    def users_resource(self) -> UsersResource:
        """Get the client for UsersResource resource."""
        return UsersResource(self._client)

    @property
    def version_manifest_resource(self) -> VersionManifestResource:
        """Get the client for VersionManifestResource resource."""
        return VersionManifestResource(self._client)
