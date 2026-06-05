# Service Health Contract v1

Contract ID: `universal.ops.service_health.v1`

## Purpose

Describe current or historical health for a service, deployment, workflow, model
endpoint, or integration.

## Required Shape

A service health descriptor should include:

- `schema`: `universal.ops.service_health.v1`.
- `id`: stable health record ID.
- `kind`: `service_health`.
- `created_at`: ISO 8601 UTC timestamp.
- `subject`: service, deployment, job, endpoint, or environment reference.
- `status`: healthy, degraded, unavailable, maintenance, unknown, or custom.
- `checks`: readiness, liveness, dependency, smoke, or synthetic check results.
- `metrics`: key service indicators, units, and thresholds.
- `incidents`: related incident or alert references.

## Extension Points

Projects may add SLO windows, error budgets, synthetic traces, dependency maps,
regional status, or customer-facing messages.

## Invariants

- Health status is machine-readable.
- Check meanings and thresholds are discoverable.
- Dependency failures are distinguishable from local failures.
- Maintenance is not reported as healthy unless explicitly intended.

## Validation Rules

- Resolve local check, metric, and incident references.
- Warn when status lacks supporting checks.
- Warn when metrics omit units or thresholds.

## Agent Implementation Notes

Use this contract to connect monitoring, deployment gates, incident response,
and automated remediation.

