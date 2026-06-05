# Index Plan Contract v1

Contract ID: `universal.db.index_plan.v1`

## Purpose

Describe database, search, vector, cache, or object metadata indexes that
support query performance and access patterns.

## Required Shape

An index plan descriptor should include:

- `schema`: `universal.db.index_plan.v1`.
- `id`: stable index plan ID.
- `kind`: `index_plan`.
- `subject`: database schema, table, collection, search surface, query surface,
  or workload.
- `indexes`: index names, fields, order, uniqueness, filter, and storage class.
- `queries`: supported query patterns, sort orders, pagination, and joins.
- `performance`: expected cardinality, selectivity, cost, latency, and limits.
- `lifecycle`: creation, backfill, validation, deprecation, and removal plan.
- `observability`: slow query signals, explain reports, metrics, and alerts.

## Extension Points

Projects may add provider-specific index options, vector dimensions, text
analyzers, partial indexes, covering indexes, or online build metadata.

## Invariants

- Every index is tied to a query pattern or workload.
- Expensive indexes declare write and storage tradeoffs.
- Backfill and removal behavior are explicit for production data.
- Query performance claims are measurable or scoped.

## Validation Rules

- Resolve query surface, schema, and observability references.
- Warn when indexes lack supported query patterns.
- Warn when production index changes omit lifecycle or backfill notes.
- Warn when performance expectations lack measurable signals.

## Agent Implementation Notes

Use this contract when adding filters, search, dashboards, reports, repository
methods, or migrations that affect query performance.
