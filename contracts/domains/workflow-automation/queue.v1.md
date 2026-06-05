# Queue Contract v1

Contract ID: `universal.workflow.queue.v1`

## Purpose

Describe a work queue, topic, stream, or broker-backed task surface.

## Required Shape

A queue descriptor should include:

- `schema`: `universal.workflow.queue.v1`.
- `id`: stable queue ID.
- `kind`: `queue`.
- `transport`: broker, stream, topic, table, or local queue technology.
- `messages`: payload schemas, keys, ordering, and compatibility.
- `producers`: systems allowed to publish.
- `consumers`: systems expected to consume.
- `delivery`: retries, acknowledgements, visibility timeout, and dead letters.
- `limits`: throughput, retention, payload size, and backpressure behavior.

## Extension Points

Projects may add partitions, priorities, consumer groups, deduplication,
ordering keys, or provider-specific queue settings.

## Invariants

- Message schemas and delivery guarantees are explicit.
- Producers and consumers agree on compatibility.
- Dead-letter or failure handling is declared.
- Unknown message types are skippable or documented as fatal.

## Validation Rules

- Resolve local message schema references.
- Warn when retry or dead-letter behavior is missing.
- Warn when ordering expectations are unspecified.

## Agent Implementation Notes

Use this contract to connect workflows, services, realtime systems, and
background jobs.

