# Audit Log Contract v1

Contract ID: `universal.app.audit_log.v1`

## Purpose

Describe audit events, access logs, administrative actions, security events,
retention, review, and export behavior.

## Required Shape

An audit log descriptor should include:

- `schema`: `universal.app.audit_log.v1`.
- `id`: stable audit log surface ID.
- `kind`: `audit_log`.
- `subjects`: users, service accounts, tenants, resources, records, jobs, or
  integrations being audited.
- `events`: event names, actors, resources, outcomes, reasons, and schemas.
- `timestamps`: event, receipt, commit, and export timestamp semantics.
- `storage`: database, log stream, object store, analytics system, or archive.
- `retention`: retention window, deletion behavior, legal hold, and export rules.
- `access`: reviewer roles, redaction, privacy, and tamper-evidence behavior.

## Extension Points

Projects may add compliance categories, correlation IDs, SIEM exports, review
workflows, integrity signatures, or incident links.

## Invariants

- Security-relevant and privileged actions are auditable.
- Audit logs cannot silently expose sensitive data to unauthorized reviewers.
- Retention and deletion behavior are explicit.
- Event schemas preserve enough context for investigation.

## Validation Rules

- Resolve auth, access control, storage, incident, and export references.
- Warn when privileged actions omit audit events.
- Warn when audit storage lacks retention or access behavior.
- Warn when event fields cannot identify actor, subject, and outcome.

## Agent Implementation Notes

Use this contract before implementing admin tools, auth changes, data exports,
security events, billing changes, or compliance reports.
