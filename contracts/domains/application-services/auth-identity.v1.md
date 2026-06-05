# Auth Identity Contract v1

Contract ID: `universal.app.auth_identity.v1`

## Purpose

Describe authentication identity surfaces, credential flows, token handling,
session binding, recovery, and identity-provider integration.

## Required Shape

An auth identity descriptor should include:

- `schema`: `universal.app.auth_identity.v1`.
- `id`: stable auth identity surface ID.
- `kind`: `auth_identity`.
- `providers`: local, external, federated, passwordless, device, or service
  identity providers.
- `credentials`: password, token, key, passkey, certificate, or delegated
  credential references.
- `flows`: sign-in, sign-up, recovery, verification, refresh, logout, and revoke
  flows.
- `sessions`: session stores, token lifetime, binding, rotation, and invalidation.
- `security`: rate limits, replay protection, MFA, lockout, and audit behavior.
- `interfaces`: APIs, routes, forms, callbacks, jobs, and events.

## Extension Points

Projects may add identity-provider metadata, risk scoring, account linking,
device trust, impersonation, invitation flows, or migration rules.

## Invariants

- Credentials and tokens are never stored as literal values in descriptors.
- Session invalidation and credential recovery behavior are discoverable.
- Security-sensitive flows have audit and abuse controls.
- Auth identities map to user or service-account surfaces.

## Validation Rules

- Resolve user account, session, API, route, form, and audit references.
- Warn when token lifetime or revocation behavior is missing.
- Warn when recovery flows omit abuse controls.
- Warn when provider callbacks omit error and replay behavior.

## Agent Implementation Notes

Use this contract before adding login, signup, token refresh, password reset,
SSO, service-account auth, or identity-provider callbacks.
