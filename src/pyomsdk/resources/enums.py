from enum import Enum


class ServerTypeName(str, Enum):
    """Enum for server type names."""

    DEV_SERVER = "DEV_SERVER"
    TEST_SERVER = "TEST_SERVER"
    PRODUCTION_SERVER = "PRODUCTION_SERVER"
    RAM_POOL = "RAM_POOL"


class ServerTypeLabel(str, Enum):
    """Enum for server type labels."""

    DEV_SERVER = "Dev Server"
    TEST_SERVER = "Test Server"
    PRODUCTION_SERVER = "Production Server"
    RAM_POOL = "Ram Pool"


class Policy(str, Enum):
    """Enum for [feature control policies](https://www.mongodb.com/docs/ops-manager/current/reference/api/feature-control-policies/)."""

    EXTERNALLY_MANAGED_LOCK = "EXTERNALLY_MANAGED_LOCK"
    """Users can't use Ops Manager to manage other settings given in the policies.policy[n] array. These same users may use a configured external system, like the Kubernetes Operator to manage these settings."""

    DISABLE_USER_MANAGEMENT = "DISABLE_USER_MANAGEMENT"
    """Users can't manage users or roles."""

    DISABLE_AUTHENTICATION_MECHANISMS = "DISABLE_AUTHENTICATION_MECHANISMS"
    """Users can't change authentication settings."""

    DISABLE_SET_MONGOD_CONFIG = "DISABLE_SET_MONGOD_CONFIG"
    """Users can't change any mongod settings listed in the policies[n].disabledParams array."""

    DISABLE_SET_MONGOD_VERSION = "DISABLE_SET_MONGOD_VERSION"
    """Users can't change the version of any mongod or mongos."""

    DISABLE_BACKUP_AGENT = "DISABLE_BACKUP_AGENT"
    """Users can't enable or disable the Backup agent."""

    DISABLE_MONGOD_LOG_MANAGEMENT = "DISABLE_MONGOD_LOG_MANAGEMENT"
    """Users can't change log management settings."""

    DISABLE_IMPORT_TO_AUTOMATION = "DISABLE_IMPORT_TO_AUTOMATION"
    """Users can't manage deployments using Automation."""

    DISABLE_AGENT_API_KEY_MANAGEMENT = "DISABLE_AGENT_API_KEY_MANAGEMENT"
    """Users can't create or update Agent API keys."""

    DISABLE_MONGOD_HOST_MANAGEMENT = "DISABLE_MONGOD_HOST_MANAGEMENT"
    """Users can't change the server type of hosts."""


class HeadDiskType(str, Enum):
    """Type of disk used to store the head directory."""

    HDD = "HDD"
    SSD = "SSD"


class OplogStoreFilterType(str, Enum):
    """Type of oplog store to use."""

    OPLOG_STORE = "oplogStore"
    S3_OPLOG_STORE = "s3OplogStore"
    THIRD_PARTY_OPLOG_STORE = "thirdPartyOplogStore"


class SnapshotStoreFilterType(str, Enum):
    """The type of the specific snapshot store given as `snapshotStoreFilter.id`."""

    S3_BLOCK_STORE = "s3blockstore"
    BLOCK_STORE = "blockstore"
    FILE_SYSTEM_STORE = "fileSystemStore"


class WriteConcern(str, Enum):
    """Enum for write concern levels."""

    ACKNOWLEDGED = "ACKNOWLEDGED"
    W2 = "W2"
    JOURNALED = "JOURNALED"
    MAJORITY = "MAJORITY"


class S3AuthMethod(str, Enum):
    """Enum for S3 authentication methods."""

    KEYS = "KEYS"
    """Ops Manager uses awsAccessKey and awsSecretKey to authorize access to S3-compatible storage bucket specified in s3BucketName."""
    IAM_ROLE = "IAM_ROLE"
    """Ops Manager uses an AWS IAM role to authorize access to S3-compatible storage bucket specified in s3BucketName. awsAccessKey and awsSecretKey fields are ignored. To learn more, see the AWS documentation"""


class AgentType(str, Enum):
    """Enum for agent types."""

    MONITORING = "MONITORING"
    BACKUP = "BACKUP"
    AUTOMATION = "AUTOMATION"


class EventTypeName(str, Enum):
    """Enum for event type names."""

    AUTOMATION_AGENT_DOWN = "AUTOMATION_AGENT_DOWN"
    AUTOMATION_AGENT_UP = "AUTOMATION_AGENT_UP"
    BACKUP_AGENT_CONF_CALL_FAILURE = "BACKUP_AGENT_CONF_CALL_FAILURE"
    BACKUP_AGENT_DOWN = "BACKUP_AGENT_DOWN"
    BACKUP_AGENT_UP = "BACKUP_AGENT_UP"
    BACKUP_AGENT_VERSION_BEHIND = "BACKUP_AGENT_VERSION_BEHIND"
    BACKUP_AGENT_VERSION_CURRENT = "BACKUP_AGENT_VERSION_CURRENT"
    MONITORING_AGENT_DOWN = "MONITORING_AGENT_DOWN"
    MONITORING_AGENT_UP = "MONITORING_AGENT_UP"
    MONITORING_AGENT_VERSION_BEHIND = "MONITORING_AGENT_VERSION_BEHIND"
    MONITORING_AGENT_VERSION_CURRENT = "MONITORING_AGENT_VERSION_CURRENT"
    NEW_AGENT = "NEW_AGENT"
    AUTOMATION_CONFIG_PUBLISHED_AUDIT = "AUTOMATION_CONFIG_PUBLISHED_AUDIT"
    BAD_CLUSTERSHOTS = "BAD_CLUSTERSHOTS"
    CLUSTER_BLACKLIST_UPDATED_AUDIT = "CLUSTER_BLACKLIST_UPDATED_AUDIT"
    CLUSTER_CHECKKPOINT_UPDATED_AUDIT = "CLUSTER_CHECKKPOINT_UPDATED_AUDIT"
    CLUSTER_CREDENTIAL_UPDATED_AUDIT = "CLUSTER_CREDENTIAL_UPDATED_AUDIT"
    CLUSTER_SNAPSHOT_SCHEDULE_UPDATED_AUDIT = "CLUSTER_SNAPSHOT_SCHEDULE_UPDATED_AUDIT"
    CLUSTER_STATE_CHANGED_AUDIT = "CLUSTER_STATE_CHANGED_AUDIT"
    CLUSTER_STORAGE_ENGINE_UPDATED_AUDIT = "CLUSTER_STORAGE_ENGINE_UPDATED_AUDIT"
    CLUSTERSHOT_DELETED_AUDIT = "CLUSTERSHOT_DELETED_AUDIT"
    CLUSTERSHOT_EXPIRY_UPDATED_AUDIT = "CLUSTERSHOT_EXPIRY_UPDATED_AUDIT"
    CONSISTENT_BACKUP_CONFIGURATION = "CONSISTENT_BACKUP_CONFIGURATION"
    GOOD_CLUSTERSHOT = "GOOD_CLUSTERSHOT"
    INCONSISTENT_BACKUP_CONFIGURATION = "INCONSISTENT_BACKUP_CONFIGURATION"
    INITIAL_SYNC_FINISHED_AUDIT = "INITIAL_SYNC_FINISHED_AUDIT"
    INITIAL_SYNC_STARTED_AUDIT = "INITIAL_SYNC_STARTED_AUDIT"
    OPLOG_BEHIND = "OPLOG_BEHIND"
    OPLOG_CURRENT = "OPLOG_CURRENT"
    RESTORE_REQUESTED_AUDIT = "RESTORE_REQUESTED_AUDIT"
    RESYNC_PERFORMED = "RESYNC_PERFORMED"
    RESYNC_REQUIRED = "RESYNC_REQUIRED"
    RS_BLACKLIST_UPDATED_AUDIT = "RS_BLACKLIST_UPDATED_AUDIT"
    RS_CREDENTIAL_UPDATED_AUDIT = "RS_CREDENTIAL_UPDATED_AUDIT"
    RS_ROTATE_MASTER_KEY_AUDIT = "RS_ROTATE_MASTER_KEY_AUDIT"
    RS_SNAPSHOT_SCHEDULE_UPDATED_AUDIT = "RS_SNAPSHOT_SCHEDULE_UPDATED_AUDIT"
    RS_STATE_CHANGED_AUDIT = "RS_STATE_CHANGED_AUDIT"
    RS_STORAGE_ENGINE_UPDATED_AUDIT = "RS_STORAGE_ENGINE_UPDATED_AUDIT"
    SNAPSHOT_DELETED_AUDIT = "SNAPSHOT_DELETED_AUDIT"
    SNAPSHOT_EXPIRY_UPDATED_AUDIT = "SNAPSHOT_EXPIRY_UPDATED_AUDIT"
    SYNC_PENDING_AUDIT = "SYNC_PENDING_AUDIT"
    SYNC_REQUIRED_AUDIT = "SYNC_REQUIRED_AUDIT"
    BI_CONNECTOR_DOWN = "BI_CONNECTOR_DOWN"
    BI_CONNECTOR_UP = "BI_CONNECTOR_UP"
    CLUSTER_MONGOS_IS_MISSING = "CLUSTER_MONGOS_IS_MISSING"
    CLUSTER_MONGOS_IS_PRESENT = "CLUSTER_MONGOS_IS_PRESENT"
    SHARD_ADDED = "SHARD_ADDED"
    SHARD_REMOVED = "SHARD_REMOVED"
    DATA_EXPLORER = "DATA_EXPLORER"
    DATA_EXPLORER_CRUD = "DATA_EXPLORER_CRUD"
    ADD_HOST_AUDIT = "ADD_HOST_AUDIT"
    ADD_HOST_TO_REPLICA_SET_AUDIT = "ADD_HOST_TO_REPLICA_SET_AUDIT"
    DELETE_HOST_AUDIT = "DELETE_HOST_AUDIT"
    HOST_DOWN = "HOST_DOWN"
    HOST_RECOVERING = "HOST_RECOVERING"
    HOST_RESTARTED = "HOST_RESTARTED"
    HOST_ROLLBACK = "HOST_ROLLBACK"
    HOST_SSL_CERTIFICATE_STALE = "HOST_SSL_CERTIFICATE_STALE"
    OUTSIDE_METRIC_THRESHOLD = "OUTSIDE_METRIC_THRESHOLD"
    REMOVE_HOST_FROM_REPLICA_SET_AUDIT = "REMOVE_HOST_FROM_REPLICA_SET_AUDIT"
    UNDELETE_HOST_AUDIT = "UNDELETE_HOST_AUDIT"
    VERSION_BEHIND = "VERSION_BEHIND"
    ALL_ORG_USERS_HAVE_MFA = "ALL_ORG_USERS_HAVE_MFA"
    ORG_API_KEY_ADDED = "ORG_API_KEY_ADDED"
    ORG_API_KEY_DELETED = "ORG_API_KEY_DELETED"
    ORG_EMPLOYEE_ACCESS_RESTRICTED = "ORG_EMPLOYEE_ACCESS_RESTRICTED"
    ORG_EMPLOYEE_ACCESS_UNRESTRICTED = "ORG_EMPLOYEE_ACCESS_UNRESTRICTED"
    ORG_PUBLIC_API_ACCESS_LIST_NOT_REQUIRED = "ORG_PUBLIC_API_ACCESS_LIST_NOT_REQUIRED"
    ORG_PUBLIC_API_ACCESS_LIST_REQUIRED = "ORG_PUBLIC_API_ACCESS_LIST_REQUIRED"
    ORG_RENAMED = "ORG_RENAMED"
    ORG_TWO_FACTOR_AUTH_OPTIONAL = "ORG_TWO_FACTOR_AUTH_OPTIONAL"
    ORG_TWO_FACTOR_AUTH_REQUIRED = "ORG_TWO_FACTOR_AUTH_REQUIRED"
    ORG_USERS_WITHOUT_MFA = "ORG_USERS_WITHOUT_MFA"
    ALL_USERS_HAVE_MULTI_FACTOR_AUTH = "ALL_USERS_HAVE_MULTI_FACTOR_AUTH"
    USERS_WITHOUT_MULTI_FACTOR_AUTH = "USERS_WITHOUT_MULTI_FACTOR_AUTH"
    CONFIGURATION_CHANGED = "CONFIGURATION_CHANGED"
    ENOUGH_HEALTHY_MEMBERS = "ENOUGH_HEALTHY_MEMBERS"
    MEMBER_ADDED = "MEMBER_ADDED"
    MEMBER_REMOVED = "MEMBER_REMOVED"
    MULTIPLE_PRIMARIES = "MULTIPLE_PRIMARIES"
    NO_PRIMARY = "NO_PRIMARY"
    ONE_PRIMARY = "ONE_PRIMARY"
    PRIMARY_ELECTED = "PRIMARY_ELECTED"
    TOO_FEW_HEALTHY_MEMBERS = "TOO_FEW_HEALTHY_MEMBERS"
    TOO_MANY_ELECTIONS = "TOO_MANY_ELECTIONS"
    TOO_MANY_UNHEALTHY_MEMBERS = "TOO_MANY_UNHEALTHY_MEMBERS"
    TEAM_ADDED_TO_GROUP = "TEAM_ADDED_TO_GROUP"
    TEAM_CREATED = "TEAM_CREATED"
    TEAM_DELETED = "TEAM_DELETED"
    TEAM_NAME_CHANGED = "TEAM_NAME_CHANGED"
    TEAM_REMOVED_FROM_GROUP = "TEAM_REMOVED_FROM_GROUP"
    TEAM_ROLES_MODIFIED = "TEAM_ROLES_MODIFIED"
    TEAM_UPDATED = "TEAM_UPDATED"
    USER_ADDED_TO_TEAM = "USER_ADDED_TO_TEAM"
    INVITED_TO_GROUP = "INVITED_TO_GROUP"
    INVITED_TO_ORG = "INVITED_TO_ORG"
    JOIN_GROUP_REQUEST_APPROVED_AUDIT = "JOIN_GROUP_REQUEST_APPROVED_AUDIT"
    JOIN_GROUP_REQUEST_DENIED_AUDIT = "JOIN_GROUP_REQUEST_DENIED_AUDIT"
    JOINED_GROUP = "JOINED_GROUP"
    JOINED_ORG = "JOINED_ORG"
    JOINED_TEAM = "JOINED_TEAM"
    REMOVED_FROM_GROUP = "REMOVED_FROM_GROUP"
    REMOVED_FROM_ORG = "REMOVED_FROM_ORG"
    REMOVED_FROM_TEAM = "REMOVED_FROM_TEAM"
    REQUESTED_TO_JOIN_GROUP = "REQUESTED_TO_JOIN_GROUP"
    USER_ROLES_CHANGED_AUDIT = "USER_ROLES_CHANGED_AUDIT"


class MatcherFieldName(str, Enum):
    """Enum for field name matchers."""

    HOSTNAME = "HOSTNAME"
    PORT = "PORT"
    HOSTNAME_AND_PORT = "HOSTNAME_AND_PORT"
    REPLICA_SET_NAME = "REPLICA_SET_NAME"
    TYPE_NAME = "TYPE_NAME"
    SHARD_NAME = "SHARD_NAME"
    CLUSTER_NAME = "CLUSTER_NAME"


class MatcherOperator(str, Enum):
    """Enum for operator matchers."""

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    REGEX = "REGEX"


class MatcherValue(str, Enum):
    """Enum for value matchers."""

    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    STANDALONE = "STANDALONE"
    CONFIG = "CONFIG"
    MONGOS = "MONGOS"


class ThresholdOperator(str, Enum):
    """Enum for metric threshold operators."""

    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"


class Unit(str, Enum):
    """Enum for metric threshold units."""

    RAW = "RAW"
    BITS = "BITS"
    BYTES = "BYTES"
    KILOBITS = "KILOBITS"
    KILOBYTES = "KILOBYTES"
    MEGABITS = "MEGABITS"
    MEGABYTES = "MEGABYTES"
    GIGABITS = "GIGABITS"
    GIGABYTES = "GIGABYTES"
    TERABYTES = "TERABYTES"
    PETABYTES = "PETABYTES"
    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"


class NotificationsTypeName(str, Enum):
    """Enum for notifications type names."""

    DATADOG = "DATADOG"
    EMAIL = "EMAIL"
    GROUP = "GROUP"
    HIPCHAT = "HIPCHAT"
    ORG = "ORG"
    PAGER_DUTY = "PAGER_DUTY"
    SLACK = "SLACK"
    SMS = "SMS"
    USER = "USER"
    WEBHOOK = "WEBHOOK"


class AlertStatus(str, Enum):
    """Enum for alert statuses."""

    OPEN = "OPEN"
    """To return all open alerts."""
    CLOSED = "CLOSED"
    """To return all closed alerts."""
    TRACKING = "TRACKING"
    """To return alerts with TRACKING status. If an alert's configuration specifies a notification delay, Ops Manager assigns the alert the TRACKING status until the delay period ends. After the delay, Ops Manager sets the status to OPEN, if the condition persists.

If an alert's configuration has multiple notifications, each with its own notification delay, Ops Manager uses the smallest delay value to determine when to move the alert from TRACKING to OPEN."""


class GlobalRole(str, Enum):
    """Enum for Ops Manager roles."""

    GLOBAL_AUTOMATION_ADMIN = "GLOBAL_AUTOMATION_ADMIN"
    GLOBAL_BACKUP_ADMIN = "GLOBAL_BACKUP_ADMIN"
    GLOBAL_MONITORING_ADMIN = "GLOBAL_MONITORING_ADMIN"
    GLOBAL_OWNER = "GLOBAL_OWNER"
    GLOBAL_READ_ONLY = "GLOBAL_READ_ONLY"
    GLOBAL_USER_ADMIN = "GLOBAL_USER_ADMIN"


class AuthMechanismName(str, Enum):
    """Enum for authentication mechanism names."""

    MONGODB_CR = "MONGODB_CR"
    """This covers SCRAM-SHA-1, SCRAM-SHA-256, and MONGODB-CR."""
    GSSAPI = "GSSAPI"
    PLAIN = "PLAIN"
    MONGODB_X509 = "MONGODB_X509"
    NONE = "NONE"


class BackupStatusName(str, Enum):
    """Enum for backup status names."""

    INACTIVE = "INACTIVE"
    PROVISIONING = "PROVISIONING"
    STARTED = "STARTED"
    STOPPED = "STOPPED"
    TERMINATING = "TERMINATING"


class StorageEngineName(str, Enum):
    """Enum for storage engine names."""

    MEMORY_MAPPED = "MEMORY_MAPPED"
    WIRED_TIGER = "WIRED_TIGER"


class GroupRole(str, Enum):
    """Enum for role names."""

    GROUP_OWNER = "GROUP_OWNER"
    GROUP_READ_ONLY = "GROUP_READ_ONLY"
    GROUP_DATA_ACCESS_ADMIN = "GROUP_DATA_ACCESS_ADMIN"
    GROUP_DATA_ACCESS_READ_WRITE = "GROUP_DATA_ACCESS_READ_WRITE"
    GROUP_DATA_ACCESS_READ_ONLY = "GROUP_DATA_ACCESS_READ_ONLY"
    GROUP_MONITORING_ADMIN = "GROUP_MONITORING_ADMIN"
    GROUP_BACKUP_ADMIN = "GROUP_BACKUP_ADMIN"
    GROUP_AUTOMATION_ADMIN = "GROUP_AUTOMATION_ADMIN"
    GROUP_USER_ADMIN = "GROUP_USER_ADMIN"


class ResourceType(str, Enum):
    """Enum for resource types."""

    CLUSTER = "CLUSTER"
    """For a sharded cluster."""
    PROCESS = "PROCESS"
    """For a node in the replica set."""
    REPLICASET = "REPLICASET"
    """For a replica set."""


class LogType(str, Enum):
    """Enum for log types."""

    AUTOMATION_AGENT = "AUTOMATION_AGENT"
    BACKUP_AGENT = "BACKUP_AGENT"
    MONITORING_AGENT = "MONITORING_AGENT"
    MONGODB = "MONGODB"
    FTDC = "FTDC"


class OrgRole(str, Enum):
    """Enum for organization role names."""

    ORG_OWNER = "ORG_OWNER"
    ORG_READ_ONLY = "ORG_READ_ONLY"
    ORG_MEMBER = "ORG_MEMBER"
    ORG_GROUP_CREATOR = "ORG_GROUP_CREATOR"


class DeliveryMethodName(str, Enum):
    """Enum for delivery method names."""

    AUTOMATED_RESTORE = "AUTOMATED_RESTORE"
    HTTP = "HTTP"


class SnapshotCompletedState(str, Enum):
    """Enum for snapshot completed values."""

    TRUE = "true"
    """Return only completed snapshots"""
    FALSE = "false"
    """Return only incomplete snapshots"""
    ALL = "all"
    """Return both completed and incomplete snapshots"""


class IntegrationType(str, Enum):
    """Enum for integration types."""

    DATADOG = "DATADOG"
    HIP_CHAT = "HIP_CHAT"
    PAGER_DUTY = "PAGER_DUTY"
    SLACK = "SLACK"
    NEW_RELIC = "NEW_RELIC"
    OPS_GENIE = "OPS_GENIE"
    VICTOR_OPS = "VICTOR_OPS"
    WEBHOOK = "WEBHOOK"
    MICROSOFT_TEAMS = "MICROSOFT_TEAMS"
    PROMETHEUS = "PROMETHEUS"


class AllRole(str, Enum):
    """Enum for all role names."""

    GLOBAL_AUTOMATION_ADMIN = GlobalRole.GLOBAL_AUTOMATION_ADMIN.value
    GLOBAL_BACKUP_ADMIN = GlobalRole.GLOBAL_BACKUP_ADMIN.value
    GLOBAL_MONITORING_ADMIN = GlobalRole.GLOBAL_MONITORING_ADMIN.value
    GLOBAL_OWNER = GlobalRole.GLOBAL_OWNER.value
    GLOBAL_READ_ONLY = GlobalRole.GLOBAL_READ_ONLY.value
    GLOBAL_USER_ADMIN = GlobalRole.GLOBAL_USER_ADMIN.value
    ORG_OWNER = OrgRole.ORG_OWNER.value
    ORG_READ_ONLY = OrgRole.ORG_READ_ONLY.value
    ORG_MEMBER = OrgRole.ORG_MEMBER.value
    ORG_GROUP_CREATOR = OrgRole.ORG_GROUP_CREATOR.value
    GROUP_OWNER = GroupRole.GROUP_OWNER.value
    GROUP_READ_ONLY = GroupRole.GROUP_READ_ONLY.value
    GROUP_DATA_ACCESS_ADMIN = GroupRole.GROUP_DATA_ACCESS_ADMIN.value
    GROUP_DATA_ACCESS_READ_WRITE = GroupRole.GROUP_DATA_ACCESS_READ_WRITE.value
    GROUP_DATA_ACCESS_READ_ONLY = GroupRole.GROUP_DATA_ACCESS_READ_ONLY.value
    GROUP_MONITORING_ADMIN = GroupRole.GROUP_MONITORING_ADMIN.value
    GROUP_BACKUP_ADMIN = GroupRole.GROUP_BACKUP_ADMIN.value
    GROUP_AUTOMATION_ADMIN = GroupRole.GROUP_AUTOMATION_ADMIN.value
    GROUP_USER_ADMIN = GroupRole.GROUP_USER_ADMIN.value


class PrometheusServiceDiscoveryType(str, Enum):
    """Enum for Prometheus service discovery types."""

    FILE = "file"
    HTTP = "http"


class PrometheusScheme(str, Enum):
    """Enum for Prometheus schemes."""

    HTTP = "http"
    HTTPS = "https"
