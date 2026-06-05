# User Session Contract v1

Contract ID: `universal.app.user_session.v1`

## Purpose

Describe browser, mobile, API, device, or service sessions and their lifecycle,
storage, expiration, security, and observability.

## Required Shape

A user session descriptor should include:

- `schema`: `universal.app.user_session.v1`.
- `id`: stable session surface ID.
- `kind`: `user_session`.
- `subject`: user, device, service account, browser client, or authenticated
  actor.
- `state`: anonymous, pending, active, expired, revoked, locked, or custom.
- `storage`: cookie, header, token store, cache, database, device, or browser
  storage surface.
- `lifecycle`: creation, refresh, rotation, expiration, logout, revoke, and
  cleanup behavior.
- `security`: binding, replay protection, CSRF, same-site, transport, and abuse
  controls.
- `observability`: audit events, active-session views, suspicious activity, and
  diagnostics.

## Extension Points

Projects may add device trust, remember-me behavior, session sharing, admin
revocation, regional storage, or offline session behavior.

## Invariants

- Session creation and revocation paths are explicit.
- Sensitive session material is referenced, not embedded.
- Expiration and refresh behavior are visible to clients.
- Security-relevant session events are auditable.

## Validation Rules

- Resolve auth, browser storage, cache, database, and audit references.
- Warn when sessions omit expiration or revocation behavior.
- Warn when browser sessions omit CSRF or same-site notes.
- Warn when session storage lacks cleanup behavior.

## Agent Implementation Notes

Use this contract before changing cookies, JWTs, refresh tokens, API sessions,
device sessions, logout behavior, or session dashboards.
