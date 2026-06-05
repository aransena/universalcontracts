# Deployment Contract v1

Contract ID: `universal.ops.deployment.v1`

## Purpose

Describe a deployed instance of an application, service, job, model, plugin, or
workflow in a specific environment.

## Required Shape

A deployment descriptor should include:

- `schema`: `universal.ops.deployment.v1`.
- `id`: stable deployment ID.
- `kind`: `deployment`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: deployment tool, project, and version.
- `subject`: release, artifact, image, service, model, or workflow deployed.
- `environment`: target environment, region, cluster, account, or host.
- `configuration`: configuration files, secrets, feature flags, and overrides.
- `status`: active, inactive, failed, rolling, rollback, or unknown.
- `observability`: health, logs, metrics, traces, and dashboard references.

## Extension Points

Projects may add orchestrator metadata, replica counts, traffic routing, canary
state, autoscaling, cost, or cloud-provider IDs.

## Invariants

- Deployed subject and environment are explicit.
- Runtime configuration differs from source configuration only through declared
  overrides.
- Health and rollback paths are discoverable.
- Secrets are referenced, not embedded.

## Validation Rules

- Resolve local release, configuration, and observability references.
- Warn when active deployments omit health checks.
- Warn when rollback behavior is missing.

## Agent Implementation Notes

Use this contract when connecting releases, operations, monitoring, incidents,
and integration tests.
