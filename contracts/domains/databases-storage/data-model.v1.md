# Data Model Contract v1

Contract ID: `universal.db.data_model.v1`

## Purpose

Describe application-level data models, repositories, ORM entities, aggregate
roots, validation rules, and their mapping to storage objects.

## Required Shape

A data model descriptor should include:

- `schema`: `universal.db.data_model.v1`.
- `id`: stable data model ID.
- `kind`: `data_model`.
- `subject`: module, bounded context, package, service, or repository surface.
- `models`: entities, value objects, documents, records, aggregates, or views.
- `fields`: field names, types, validation, defaults, units, and sensitivity.
- `storage`: database schema, table, collection, bucket, index, or query mapping.
- `lifecycle`: create, update, delete, archive, restore, and migration behavior.
- `interfaces`: repository methods, API DTOs, events, forms, or serializers.

## Extension Points

Projects may add ORM annotations, generated code, domain events, validation
libraries, serializer options, fixtures, or backward compatibility aliases.

## Invariants

- Public model fields map to storage or declared derived values.
- Validation is consistent across UI, API, and storage boundaries.
- Sensitive fields carry access and serialization expectations.
- Renames and deletions have migration or compatibility notes.

## Validation Rules

- Resolve referenced schema, query surface, API, form, and event descriptors.
- Warn when fields lack storage mapping or derivation notes.
- Warn when sensitive fields lack access or serialization behavior.
- Warn when public model changes omit migration implications.

## Agent Implementation Notes

Use this contract before editing domain models, repository methods, serializers,
forms, API DTOs, migrations, or fixtures.
