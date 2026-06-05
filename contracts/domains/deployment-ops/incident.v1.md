# Incident Contract v1

Contract ID: `universal.ops.incident.v1`

## Purpose

Describe an operational incident, investigation, remediation, and follow-up
actions in a machine-readable way.

## Required Shape

An incident descriptor should include:

- `schema`: `universal.ops.incident.v1`.
- `id`: stable incident ID.
- `kind`: `incident`.
- `created_at`: ISO 8601 UTC timestamp.
- `status`: open, mitigated, resolved, closed, or unknown.
- `severity`: project-defined severity or impact level.
- `subjects`: affected services, deployments, datasets, users, or environments.
- `timeline`: events, detections, mitigations, and resolution references.
- `evidence`: logs, metrics, traces, screenshots, reports, or tickets.
- `actions`: remediation, follow-up, owners, and due dates.

## Extension Points

Projects may add paging metadata, customer impact, root-cause categories,
postmortems, approvals, or compliance reporting.

## Invariants

- Affected subjects are explicit.
- Timeline events preserve ordering.
- Evidence is linked rather than only described in prose.
- Follow-up work is distinguishable from immediate mitigation.

## Validation Rules

- Resolve local evidence and timeline references.
- Warn when resolved incidents omit mitigation or cause notes.
- Warn when high severity incidents omit affected subjects.

## Agent Implementation Notes

Use this contract for incident review, operational learning, and connecting
observability data to remediation.

