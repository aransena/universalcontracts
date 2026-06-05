# Service Surface Contract v1

Contract ID: `universal.api.service_surface.v1`

## Purpose

Describe a service's externally usable surface, including APIs, jobs, webhooks,
configuration, auth, observability, and lifecycle.

## Required Shape

A service surface descriptor should include:

- `schema`: `universal.api.service_surface.v1`.
- `id`: stable service ID.
- `kind`: `service_surface`.
- `producer`: service project and version.
- `contracts`: claimed contract IDs.
- `apis`: API surface, endpoint, query API, remote procedure call, or message
  schema references.
- `auth`: authentication and permission requirements.
- `runtime`: environment, deployment, and service dependency references.
- `observability`: health, logs, metrics, traces, and alert references.

## Extension Points

Projects may add framework routing metadata, service mesh details, tenant
models, feature flags, or cloud-specific deployment fields.

## Invariants

- Consumers can discover how to call or monitor the service.
- Auth and rate limits are explicit.
- Runtime dependencies are not hidden in application code.
- Breaking surface changes are versioned or declared through a profile.

## Validation Rules

- Resolve local API, configuration, runtime, and observability references.
- Warn when endpoints are exposed without auth or limit notes.
- Warn when health checks are absent for long-running services.

## Agent Implementation Notes

Use this contract as the service-level map before integrating or modifying an
API-backed system.
