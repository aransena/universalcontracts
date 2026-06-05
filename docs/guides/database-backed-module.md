# Guide: Building or Reviewing a Database-Backed Module

## Start With A Profile

Use `universal.profile.database_backed_module.v1` when a module owns persistent
application data or repository behavior.

## Core Database Contracts

Use these first:

- `universal.db.database_schema.v1`
- `universal.db.data_model.v1`
- `universal.db.query_surface.v1`
- `universal.db.data_access_policy.v1`
- `universal.db.transaction_boundary.v1`
- `universal.db.migration.v1`

## Add When Needed

- `universal.db.seed_data.v1`
- `universal.db.backup.v1`
- `universal.db.replication.v1`
- `universal.db.change_stream.v1`
- `universal.db.index_plan.v1`
- `universal.db.object_store_layout.v1`

## Agent Checklist

1. Map application models to storage objects.
2. Declare public queries, parameters, result shapes, limits, and permissions.
3. Describe transaction boundaries, idempotency, retries, and failure behavior.
4. Tie schema changes to migrations and seed data changes when applicable.
5. Preserve data access policy for sensitive fields and tenant boundaries.
6. Add index, cache, replication, or change-stream descriptors when integration
   depends on freshness or performance semantics.
