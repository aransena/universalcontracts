# Seed Data Contract v1

Contract ID: `universal.db.seed_data.v1`

## Purpose

Describe seed, fixture, demo, reference, and bootstrap data used to initialize
or test a database-backed system.

## Required Shape

A seed data descriptor should include:

- `schema`: `universal.db.seed_data.v1`.
- `id`: stable seed data set ID.
- `kind`: `seed_data`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: project, command, generator, or dataset owner.
- `target`: database schema, environment, tenant, service, or fixture scope.
- `files`: seed files, manifests, checksums, generators, or load reports.
- `records`: object counts, key ranges, fixture names, and reset behavior.
- `safety`: destructive behavior, idempotency, privacy, and environment limits.

## Extension Points

Projects may add factory definitions, anonymized production samples, synthetic
data generators, reference tables, tenancy scopes, or locale-specific fixtures.

## Invariants

- Load target and environment safety are explicit.
- Seed data is repeatable or declares why it is not.
- Production-sensitive values are anonymized or excluded.
- Reset and cleanup behavior is discoverable.

## Validation Rules

- Resolve seed files, generators, and target schema references.
- Warn when destructive load behavior is undeclared.
- Warn when fixture data lacks privacy or provenance notes.
- Warn when load order is ambiguous.

## Agent Implementation Notes

Use this contract when adding tests, demos, local development fixtures, bootstrap
commands, reference data, or migration support data.
