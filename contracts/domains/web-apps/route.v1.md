# Web Route Contract v1

Contract ID: `universal.web.route.v1`

## Purpose

Describe one web route, page, or view entry so agents can reason about
navigation, data dependencies, permissions, cache behavior, and UI states.

## Required Shape

A route descriptor should include:

- `schema`: `universal.web.route.v1`.
- `id`: stable route ID.
- `kind`: `web_route`.
- `path`: path pattern, parameters, query parameters, and canonical URL rules.
- `rendering`: client, server, static, hybrid, or embedded rendering behavior.
- `auth`: anonymous, authenticated, role-based, or permission-gated access.
- `data`: loaders, API calls, local data, stream subscriptions, and cache keys.
- `states`: loading, empty, ready, error, unauthorized, offline, and degraded
  states.
- `actions`: navigation, mutations, form submits, uploads, downloads, or
  side-effecting commands.

## Extension Points

Projects may add framework route IDs, layout inheritance, route guards,
metadata, prefetching, analytics, experiments, or internationalized paths.

## Invariants

- Route parameters and permissions are explicit.
- Data dependencies are discoverable without reading every component.
- Error and empty states are represented when user-facing.
- Side-effecting actions are distinguishable from navigation-only actions.

## Validation Rules

- Resolve local schema, data, and screen references.
- Warn when protected routes omit auth or role information.
- Warn when side-effecting actions omit error behavior.
- Warn when dynamic parameters lack descriptions.

## Agent Implementation Notes

Use this contract when adding, refactoring, testing, or integrating a web route.

