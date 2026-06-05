# Data Access Policy Contract v1

Contract ID: `universal.db.data_access_policy.v1`

## Purpose

Describe database and storage access rules, including subjects, permissions,
tenant isolation, sensitive fields, retention, and audit expectations.

## Required Shape

A data access policy descriptor should include:

- `schema`: `universal.db.data_access_policy.v1`.
- `id`: stable access policy ID.
- `kind`: `data_access_policy`.
- `subject`: database, schema, table, collection, bucket, query surface, or
  service boundary.
- `permissions`: roles, scopes, operations, approvals, and denial behavior.
- `fields`: sensitive, restricted, derived, redacted, or public fields.
- `tenancy`: tenant key, isolation model, sharing rules, and break-glass access.
- `privacy`: retention, deletion, export, consent, and lawful-use constraints.
- `observability`: audit logs, access traces, alerts, and review reports.

## Extension Points

Projects may add policy engine references, row-level security rules, masking
functions, consent providers, legal holds, or data residency constraints.

## Invariants

- Sensitive fields have explicit access and redaction behavior.
- Tenant isolation rules are discoverable before queries are written.
- Administrative exceptions are auditable.
- Policy changes are reviewable and tied to affected data surfaces.

## Validation Rules

- Resolve referenced schema, query surface, and audit log descriptors.
- Warn when sensitive fields omit permissions or retention behavior.
- Warn when tenant-scoped data lacks an isolation rule.
- Warn when privileged access lacks observability.

## Agent Implementation Notes

Use this contract when adding data access code, authorization checks, exports,
admin tools, analytics, or cross-tenant features.
