# Query Surface Contract v1

Contract ID: `universal.db.query_surface.v1`

## Purpose

Describe the supported query surface for a database-backed module, including
named queries, parameters, result shapes, authorization, limits, and performance
expectations.

## Required Shape

A query surface descriptor should include:

- `schema`: `universal.db.query_surface.v1`.
- `id`: stable query surface ID.
- `kind`: `query_surface`.
- `subject`: database schema, repository, service, or module being queried.
- `queries`: named reads, writes, aggregations, reports, or search operations.
- `parameters`: accepted filters, pagination, sorting, limits, and defaults.
- `results`: result shapes, nullable fields, ordering, and error behavior.
- `permissions`: required roles, scopes, row filters, and tenant boundaries.
- `performance`: expected indexes, cardinality, timeout, and cost assumptions.

## Extension Points

Projects may add query builders, prepared statement IDs, ORM scopes, explain
plans, cache keys, warehouse partitions, or provider-specific query options.

## Invariants

- Public queries have stable names or entry points.
- Parameters and result shapes are explicit enough for callers to integrate.
- Authorization assumptions are visible at the query boundary.
- Expensive or unbounded queries declare limits or review expectations.

## Validation Rules

- Resolve referenced schema, model, and policy descriptors.
- Warn when public queries omit result shape or permission notes.
- Warn when unbounded queries omit pagination, limits, or timeout behavior.
- Warn when performance assumptions reference missing indexes.

## Agent Implementation Notes

Use this contract before adding repository methods, database endpoints, reports,
exports, dashboards, or data-driven UI screens.
