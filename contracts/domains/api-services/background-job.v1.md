# Background Job Contract v1

Contract ID: `universal.api.background_job.v1`

## Purpose

Describe a service-owned asynchronous job, worker task, queue consumer, or
scheduled process.

## Required Shape

A background job descriptor should include:

- `schema`: `universal.api.background_job.v1`.
- `id`: stable job ID.
- `kind`: `background_job`.
- `producer`: service or worker project and version.
- `trigger`: schedule, queue, API call, event, or manual command.
- `inputs`: payload schemas, datasets, configuration references, or service
  dependencies.
- `outputs`: artifacts, side effects, events, database writes, or reports.
- `lifecycle`: queued, running, retrying, completed, failed, or cancelled states.
- `observability`: logs, metrics, health, traces, and dead-letter references.

## Extension Points

Projects may add worker pool, priority, retry backoff, idempotency key, lock,
partition, or scheduler metadata.

## Invariants

- Trigger and side effects are explicit.
- Retry and idempotency behavior is documented.
- Failed jobs preserve enough context for diagnosis.
- Outputs are discoverable even when they are not file-based.

## Validation Rules

- Resolve local payload and output schema references.
- Warn when retryable jobs omit idempotency notes.
- Warn when side effects are undeclared.

## Agent Implementation Notes

Use this contract when agents need to start, monitor, replay, or reason about
asynchronous work.
