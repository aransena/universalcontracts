# Schedule Contract v1

Contract ID: `universal.workflow.schedule.v1`

## Purpose

Describe recurring or delayed execution rules in a timezone-aware, automation
friendly form.

## Required Shape

A schedule descriptor should include:

- `schema`: `universal.workflow.schedule.v1`.
- `id`: stable schedule ID.
- `kind`: `schedule`.
- `target`: workflow, job, command, endpoint, or task reference.
- `rule`: cron, interval, event window, or calendar rule.
- `timezone`: IANA timezone for wall-clock schedules.
- `windows`: allowed, blocked, or maintenance windows.
- `catchup`: missed-run and backfill behavior.
- `state`: active, paused, disabled, or draft.

## Extension Points

Projects may add scheduler-specific IDs, holiday calendars, SLAs, priorities,
tenant scopes, or approval requirements.

## Invariants

- Timezone is explicit for wall-clock rules.
- Missed-run behavior is clear.
- Paused or disabled schedules do not look active.
- Target side effects are discoverable through the target contract.

## Validation Rules

- Resolve target references.
- Warn when wall-clock schedules omit timezone.
- Warn when catchup behavior is unspecified.

## Agent Implementation Notes

Use this contract when coordinating jobs, reports, pipelines, webhooks, and
maintenance automation.
