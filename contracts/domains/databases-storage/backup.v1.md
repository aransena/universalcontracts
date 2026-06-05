# Backup Contract v1

Contract ID: `universal.db.backup.v1`

## Purpose

Describe a database, object store, filesystem, or application data backup and
its restore expectations.

## Required Shape

A backup descriptor should include:

- `schema`: `universal.db.backup.v1`.
- `id`: stable backup ID.
- `kind`: `backup`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: backup tool or service.
- `subject`: database, bucket, filesystem path, dataset, or service.
- `files`: archive, manifest, checksums, logs, or restore scripts.
- `scope`: included and excluded data.
- `restore`: target requirements, steps, and compatibility.
- `retention`: expiration, rotation, and legal hold rules.

## Extension Points

Projects may add snapshot provider IDs, encryption metadata, incremental chains,
point-in-time recovery, or tenant-specific retention.

## Invariants

- Backup scope is explicit.
- Restore requirements are discoverable.
- Integrity metadata is available when data loss matters.
- Sensitive backups declare encryption or access controls.

## Validation Rules

- Resolve local backup manifests and checksum references.
- Warn when restore steps are missing.
- Warn when sensitive data lacks encryption or permission notes.

## Agent Implementation Notes

Use this contract when sharing, restoring, validating, or migrating stored data.

