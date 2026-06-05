# Database Schema Contract v1

Contract ID: `universal.db.database_schema.v1`

## Purpose

Describe database structure, ownership, migrations, relationships, and access
expectations in a portable way.

## Required Shape

A database schema descriptor should include:

- `schema`: `universal.db.database_schema.v1`.
- `id`: stable schema ID.
- `kind`: `database_schema`.
- `engine`: database type and version family.
- `objects`: tables, collections, indexes, views, functions, or buckets.
- `fields`: column or property names, types, constraints, and units.
- `relationships`: keys, references, joins, or ownership links.
- `migrations`: migration set or current version reference.

## Extension Points

Projects may add ORM models, warehouse metadata, partitioning, retention,
row-level security, tenancy, or provider-specific index options.

## Invariants

- Public data objects and fields are discoverable.
- Schema version and migration path are explicit.
- Sensitive fields and access restrictions are marked.
- Generated or internal objects are distinguished from public ones.

## Validation Rules

- Resolve local schema, migration, and model references.
- Warn when public fields omit types or descriptions.
- Warn when sensitive objects omit access notes.

## Agent Implementation Notes

Use this contract before writing queries, migrations, data exports, or pipeline
integrations.

