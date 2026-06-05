# Access Control Contract v1

Contract ID: `universal.app.access_control.v1`

## Purpose

Describe authorization rules, roles, permissions, policies, resource ownership,
and enforcement points for application features.

## Required Shape

An access control descriptor should include:

- `schema`: `universal.app.access_control.v1`.
- `id`: stable access control surface ID.
- `kind`: `access_control`.
- `subjects`: users, service accounts, roles, groups, organizations, or tenants.
- `resources`: routes, APIs, records, files, actions, jobs, tools, or admin
  surfaces.
- `permissions`: operations, scopes, grants, denials, approvals, and inheritance.
- `policies`: ownership, tenant isolation, row filters, feature gates, and
  exceptions.
- `enforcement`: UI, API, job, database, storage, and tool enforcement points.
- `observability`: audit logs, access decisions, alerts, and review reports.

## Extension Points

Projects may add policy engines, ABAC attributes, delegation, temporary grants,
approval workflows, or break-glass access.

## Invariants

- Authorization is enforced on server-side or trusted boundaries.
- UI-only restrictions do not count as security controls.
- Privileged exceptions are auditable.
- Resource ownership and tenant boundaries are explicit.

## Validation Rules

- Resolve auth, API, route, data access policy, and audit log references.
- Warn when resources lack enforcement points.
- Warn when admin permissions omit audit behavior.
- Warn when tenant-scoped resources lack isolation policy.

## Agent Implementation Notes

Use this contract before adding roles, admin surfaces, protected routes,
multi-tenant features, record ownership, or approval flows.
