# Cache Policy Contract v1

Contract ID: `universal.app.cache_policy.v1`

## Purpose

Describe application caching behavior across browser, CDN, API, database,
in-memory, distributed, and derived-data caches.

## Required Shape

A cache policy descriptor should include:

- `schema`: `universal.app.cache_policy.v1`.
- `id`: stable cache policy ID.
- `kind`: `cache_policy`.
- `subject`: route, endpoint, query, object, computation, media asset, or
  integration being cached.
- `storage`: browser, CDN, memory, key-value store, database, file, or object
  store cache.
- `keys`: key format, tenant scope, locale, auth scope, version, and invalidation
  inputs.
- `freshness`: ttl, stale behavior, revalidation, refresh, and consistency
  expectations.
- `invalidation`: events, writes, schedules, manual purge, and rollback behavior.
- `observability`: hit rate, age, evictions, stampede protection, and debug
  signals.

## Extension Points

Projects may add provider cache controls, surrogate keys, cache warming,
negative caching, request coalescing, or offline-first behavior.

## Invariants

- Cache keys include all fields that affect returned data.
- Stale data behavior is explicit.
- Sensitive data is not cached outside its permission boundary.
- Invalidation behavior is discoverable for writes.

## Validation Rules

- Resolve route, endpoint, query, storage, and change stream references.
- Warn when cached protected data lacks auth or tenant keying.
- Warn when mutable data omits invalidation behavior.
- Warn when cache freshness conflicts with source-of-truth semantics.

## Agent Implementation Notes

Use this contract before adding caching, memoization, CDN behavior, browser
caching, query caching, or derived read models.
