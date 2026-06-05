# Browser Storage Contract v1

Contract ID: `universal.web.browser_storage.v1`

## Purpose

Describe browser-managed storage such as key-value stores, cookies, local
databases, caches, and persisted session state.

## Required Shape

A browser storage descriptor should include:

- `schema`: `universal.web.browser_storage.v1`.
- `id`: stable storage surface ID.
- `kind`: `browser_storage`.
- `stores`: storage mechanisms, namespaces, keys, object stores, or cache names.
- `fields`: stored values, schemas, defaults, units, and ownership.
- `lifecycle`: creation, migration, expiration, clearing, and reset behavior.
- `privacy`: sensitivity, consent, retention, and export or deletion behavior.
- `compatibility`: versioning, backward compatibility, and fallback behavior.

## Extension Points

Projects may add encryption, offline sync, conflict resolution, quota handling,
feature flags, or tenant-specific namespaces.

## Invariants

- Key ownership is explicit.
- User-owned and generated state are distinguishable.
- Migrations are declared when persisted shape changes.
- Sensitive values are not stored without privacy and deletion notes.

## Validation Rules

- Resolve local schema and migration references.
- Warn when persistent stores omit retention or reset behavior.
- Warn when sensitive values lack privacy notes.
- Warn when cache invalidation is undocumented.

## Agent Implementation Notes

Use this contract before changing local persistence, session behavior, offline
state, or browser-side migrations.

