# Observability Contract v1

Contract ID: `universal.core.observability.v1`

## Purpose

Describe logs, metrics, traces, health checks, alerts, and debug artifacts so
agents can monitor, troubleshoot, and integrate runtime systems.

## Required Shape

An observability descriptor should include:

- `schema`: `universal.core.observability.v1`.
- `id`: stable observability surface ID.
- `kind`: `observability`.
- `logs`: log locations, formats, levels, retention, and correlation fields.
- `metrics`: metric names, units, labels, and scrape or export mechanisms.
- `health`: readiness, liveness, status, or diagnostic checks.
- `traces`: trace propagation, span naming, and exporters when available.

## Extension Points

Projects may add provider-specific dashboards, alert rules, sampling policies,
profilers, crash dumps, or debug bundles. Custom metrics should keep stable
names, units, and label meanings.

## Invariants

- Health checks are safe for automation to call.
- Metrics include units or clear dimensions.
- Logs do not require parsing undocumented prose for critical state.
- Sensitive data handling is explicit for logs and traces.

## Validation Rules

- Resolve local dashboard, alert, and debug artifact references.
- Warn when metrics omit units or label definitions.
- Warn when health checks are missing for long-running services.
- Warn when logs may contain secrets without redaction notes.

## Agent Implementation Notes

Use this contract to connect services, jobs, realtime sessions, model serving,
and deployment systems to monitoring and troubleshooting workflows.

