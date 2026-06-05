# Change Stream Contract v1

Contract ID: `universal.db.change_stream.v1`

## Purpose

Describe database change capture, outbox events, audit streams, CDC feeds, or
materialized update streams emitted from storage changes.

## Required Shape

A change stream descriptor should include:

- `schema`: `universal.db.change_stream.v1`.
- `id`: stable change stream ID.
- `kind`: `change_stream`.
- `source`: database, schema, table, collection, outbox, bucket, or service.
- `transport`: log, queue, topic, webhook, file, stream, or polling surface.
- `messages`: event shape, operation types, keys, ordering, and schema version.
- `timestamps`: commit, publish, delivery, and processing timestamp semantics.
- `delivery`: at-least-once, at-most-once, exactly-once, retry, and dead-letter
  behavior.
- `consumers`: known consumers, ownership, compatibility, and replay needs.

## Extension Points

Projects may add connector IDs, snapshot markers, offset storage, partitioning,
redaction, schema registry references, or consumer-specific transforms.

## Invariants

- Message ordering and dedupe semantics are explicit.
- Consumers can replay or know why replay is unavailable.
- Sensitive fields are redacted or covered by access policy.
- Schema changes are coordinated with consumer compatibility.

## Validation Rules

- Resolve source schema, transport, consumer, and policy references.
- Warn when event messages omit keys or versioning.
- Warn when replayable streams omit offset or checkpoint semantics.
- Warn when sensitive data can leave storage without policy references.

## Agent Implementation Notes

Use this contract when implementing outbox patterns, CDC connectors, event
publishers, search indexing, analytics sync, or integration events.
