# Migration Contract v1

Contract ID: `universal.db.migration.v1`

## Purpose

Describe a database or storage migration, including ordering, reversibility,
preconditions, side effects, and validation.

## Required Shape

A migration descriptor should include:

- `schema`: `universal.db.migration.v1`.
- `id`: stable migration ID.
- `kind`: `migration`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: project and migration tool.
- `from_version`: source schema or storage version.
- `to_version`: target schema or storage version.
- `files`: migration scripts, rollback scripts, checks, or reports.
- `effects`: created, changed, removed, or backfilled objects.
- `safety`: transaction, lock, backup, and rollback expectations.

## Extension Points

Projects may add ORM metadata, online migration phases, shard or tenant scope,
feature flag gates, or cloud-provider operations.

## Invariants

- Ordering is stable.
- Destructive effects are explicit.
- Rollback or irreversibility is documented.
- Validation checks are linked when available.

## Validation Rules

- Resolve local migration and rollback files.
- Warn when destructive migrations omit backup or rollback notes.
- Warn when version ordering is ambiguous.

## Agent Implementation Notes

Use this contract before applying, reviewing, packaging, or troubleshooting
schema and storage migrations.

