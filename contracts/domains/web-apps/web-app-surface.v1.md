# Web App Surface Contract v1

Contract ID: `universal.web.app_surface.v1`

## Purpose

Describe the stable surface of a web application so agents can navigate,
integrate, test, and extend it without relying on incidental implementation
details.

## Applies To

- Browser applications
- Server-rendered web apps
- Admin consoles
- Dashboards
- SaaS products
- Internal tools

## Required Shape

A web app surface descriptor should include:

- `schema`: `universal.web.app_surface.v1`.
- `id`: stable app or surface ID.
- `kind`: `web_app`.
- `producer`: project and version.
- `contracts`: claimed contract IDs.
- `routes`: route IDs, paths, parameters, ownership, and access requirements.
- `entry_points`: primary URLs, build outputs, or app mounts.
- `state`: browser storage, URL state, server state, and cache assumptions.
- `auth`: authentication flows, roles, and permission boundaries.
- `commands`: build, run, test, lint, and validate commands when available.

## Recommended Fields

- `api_dependencies`: backend APIs, schemas, and transports.
- `design_system`: token, component, icon, and layout conventions.
- `storage`: localStorage, sessionStorage, IndexedDB, cookies, and persistence.
- `observability`: logs, analytics, error reporting, and performance metrics.
- `fixtures`: seeded users, mock data, and deterministic test states.

## Extension Points

Projects may add framework-specific routing, component maps, feature flags,
state machines, accessibility profiles, or visual regression metadata. Generic
agents should still be able to discover routes, auth requirements, and commands.

## Invariants

- Public routes and required permissions are documented.
- Build and run commands are stable from a clean checkout after setup.
- User-editable content and generated assets are distinguished.
- Test fixtures do not silently depend on production credentials.

## Validation Rules

- Check that advertised commands exist or are documented as unavailable.
- Resolve local schema, fixture, and build output references.
- Warn when protected routes omit auth or role information.
- Warn when browser storage is used without documenting key ownership.

## Agent Implementation Notes

Use this contract as a practical map before modifying a web app. Preserve local
design and state conventions instead of inventing new ones.

