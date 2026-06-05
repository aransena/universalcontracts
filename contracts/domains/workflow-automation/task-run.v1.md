# Task Run Contract v1

Contract ID: `universal.workflow.task_run.v1`

## Purpose

Describe one execution of a workflow task, command, job, or human approval step.

## Required Shape

A task run descriptor should include:

- `schema`: `universal.workflow.task_run.v1`.
- `id`: stable task run ID.
- `kind`: `task_run`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: workflow engine or runner.
- `task`: task definition reference.
- `lifecycle`: queued, running, completed, failed, skipped, or cancelled state.
- `inputs`: resolved inputs, parameters, and environment references.
- `outputs`: artifacts, logs, metrics, events, or side effects.

## Extension Points

Projects may add retry attempt, worker, queue, approval, cost, resource usage,
or scheduler metadata.

## Invariants

- The task definition and resolved inputs are traceable.
- Failed tasks keep diagnostic output.
- Skipped tasks explain skip reason.
- Output references are explicit for downstream tasks.

## Validation Rules

- Resolve local task, input, output, and log references.
- Warn when failed tasks omit diagnostics.
- Warn when output claims do not match produced files.

## Agent Implementation Notes

Use this contract for workflow debugging, replay, provenance, and conformance
reports.

