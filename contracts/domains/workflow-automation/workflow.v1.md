# Workflow Contract v1

Contract ID: `universal.workflow.workflow.v1`

## Purpose

Describe an ordered or event-driven workflow with tasks, dependencies, triggers,
inputs, outputs, and recovery behavior.

## Required Shape

A workflow descriptor should include:

- `schema`: `universal.workflow.workflow.v1`.
- `id`: stable workflow ID.
- `kind`: `workflow`.
- `producer`: project and workflow engine.
- `triggers`: schedules, events, API calls, manual starts, or dependencies.
- `tasks`: task IDs, commands, services, inputs, outputs, and dependencies.
- `state`: lifecycle, checkpoints, retries, and terminal states.
- `artifacts`: generated datasets, reports, models, or side effects.

## Extension Points

Projects may add DAG engine metadata, approvals, human tasks, branch rules,
resource pools, or tenant scopes.

## Invariants

- Task order and dependency rules are explicit.
- Inputs and outputs are discoverable at task and workflow levels.
- Retry and cancellation behavior is documented.
- Side effects are not hidden in task code.

## Validation Rules

- Check task IDs and dependency references.
- Resolve local command, schema, and artifact references.
- Warn when cycles or missing terminal states appear.

## Agent Implementation Notes

Use this contract when agents need to inspect, run, resume, or modify workflows.

