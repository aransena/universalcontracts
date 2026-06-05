# Guide: Building or Reviewing a General App Module

## Start With A Profile

Choose one profile first when it matches the module:

- `universal.profile.service_module.v1`
- `universal.profile.web_application.v1`
- `universal.profile.database_backed_module.v1`
- `universal.profile.event_producer_consumer.v1`
- `universal.profile.integration_connector.v1`
- `universal.profile.file_processing_pipeline.v1`

## Add Application-Service Contracts

Add only the contracts touched by the feature:

- `universal.app.user_account.v1`
- `universal.app.auth_identity.v1`
- `universal.app.access_control.v1`
- `universal.app.user_session.v1`
- `universal.app.notification.v1`
- `universal.app.file_upload.v1`
- `universal.app.payment_billing.v1`
- `universal.app.feature_flag.v1`
- `universal.app.cache_policy.v1`
- `universal.app.search_surface.v1`
- `universal.app.audit_log.v1`
- `universal.app.integration_connector.v1`
- `universal.app.localization.v1`

## Agent Checklist

1. Select the smallest matching profile from `contracts/catalog.json`.
2. Preserve identity, configuration, permissions, auth, lifecycle,
   observability, and provenance fields from the selected contracts.
3. Declare module handoff points: commands, APIs, data models, queries, events,
   storage, cache, search, audit, and background jobs.
4. Keep provider, framework, and tool details in local schemas or project
   profiles.
5. Report selected profile, selected contracts, local extensions, and validation.
