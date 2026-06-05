# Object Store Layout Contract v1

Contract ID: `universal.db.object_store_layout.v1`

## Purpose

Describe buckets, prefixes, object naming, metadata, retention, and access rules
for object-store-backed systems.

## Required Shape

An object store layout descriptor should include:

- `schema`: `universal.db.object_store_layout.v1`.
- `id`: stable layout ID.
- `kind`: `object_store_layout`.
- `stores`: buckets, containers, regions, or namespaces.
- `prefixes`: path patterns, ownership, and expected object roles.
- `objects`: formats, schemas, compression, and lifecycle expectations.
- `access`: read, write, list, delete, and sharing permissions.
- `retention`: versioning, expiration, immutability, and cleanup rules.

## Extension Points

Projects may add provider-specific storage classes, replication, encryption,
CDN rules, signed URLs, or event notifications.

## Invariants

- Producers and consumers can agree on object roles from prefixes.
- Generated and user-owned objects are distinguished.
- Retention and deletion behavior are explicit.
- Access requirements do not depend only on cloud console settings.

## Validation Rules

- Check local examples and manifest references when available.
- Warn when writable prefixes omit ownership or cleanup rules.
- Warn when object formats are undocumented.

## Agent Implementation Notes

Use this contract for data lakes, media stores, backups, upload surfaces, and
pipeline handoffs.

