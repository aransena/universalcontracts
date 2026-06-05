# Ops Environment Contract v1

Contract ID: `universal.ops.environment.v1`

## Purpose

Describe an operational environment such as development, staging, production,
edge, lab, or customer-hosted infrastructure.

## Required Shape

An ops environment descriptor should include:

- `schema`: `universal.ops.environment.v1`.
- `id`: stable environment ID.
- `kind`: `ops_environment`.
- `tier`: development, test, staging, production, edge, lab, or custom.
- `runtime`: infrastructure, cluster, host, account, region, or network.
- `services`: databases, queues, APIs, object stores, and dependencies.
- `configuration`: environment configuration, secrets, and policy references.
- `permissions`: access roles, approvals, and break-glass behavior.

## Extension Points

Projects may add IaC state, cloud provider IDs, network diagrams, compliance
zones, maintenance windows, or data residency rules.

## Invariants

- Environment purpose and risk tier are explicit.
- Access and secret handling are documented.
- Dependencies are discoverable before deployment.
- Production-like environments are distinguishable from disposable ones.

## Validation Rules

- Resolve local infrastructure, configuration, and permission references.
- Warn when production environments omit access or observability details.
- Warn when dependencies are undocumented.

## Agent Implementation Notes

Use this contract before deploying, testing, migrating, or debugging operational
systems.
