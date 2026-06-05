# Transaction Boundary Contract v1

Contract ID: `universal.db.transaction_boundary.v1`

## Purpose

Describe transactional units of work, consistency assumptions, idempotency,
locking, retries, and side effects for database-backed operations.

## Required Shape

A transaction boundary descriptor should include:

- `schema`: `universal.db.transaction_boundary.v1`.
- `id`: stable transaction boundary ID.
- `kind`: `transaction_boundary`.
- `subject`: command, endpoint, job, workflow step, repository method, or domain
  operation.
- `inputs`: data objects, commands, events, files, or request fields consumed.
- `writes`: created, updated, deleted, locked, emitted, or externalized effects.
- `consistency`: isolation level, ordering, uniqueness, and concurrency rules.
- `idempotency`: keys, dedupe windows, retry behavior, and replay safety.
- `failure`: rollback, compensation, partial write, and manual recovery behavior.

## Extension Points

Projects may add saga steps, outbox patterns, advisory locks, distributed
transaction metadata, optimistic concurrency tokens, or dead-letter behavior.

## Invariants

- Write boundaries are explicit before callers rely on side effects.
- Retry behavior does not duplicate durable effects.
- External side effects are coordinated with database writes.
- Partial failures preserve enough state for recovery.

## Validation Rules

- Resolve referenced endpoint, command, job, schema, and queue descriptors.
- Warn when writes are declared without failure behavior.
- Warn when retryable operations omit idempotency.
- Warn when external side effects occur inside unclear transaction boundaries.

## Agent Implementation Notes

Use this contract before implementing checkout flows, account changes, imports,
webhooks, background jobs, workflows, or multi-table updates.
