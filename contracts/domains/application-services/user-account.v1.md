# User Account Contract v1

Contract ID: `universal.app.user_account.v1`

## Purpose

Describe user, account, organization, and tenant identity data used by an
application.

## Required Shape

A user account descriptor should include:

- `schema`: `universal.app.user_account.v1`.
- `id`: stable user account surface ID.
- `kind`: `user_account`.
- `subject`: user, account, organization, tenant, or membership model.
- `fields`: identifiers, profile fields, contact fields, status, and sensitivity.
- `lifecycle`: invited, active, suspended, deleted, merged, and restored states.
- `relationships`: memberships, roles, teams, organizations, tenants, and owners.
- `privacy`: consent, export, deletion, retention, and redaction behavior.
- `interfaces`: APIs, forms, events, admin tools, and storage mappings.

## Extension Points

Projects may add identity-provider IDs, verification states, profile media,
custom claims, tenant metadata, or account merge rules.

## Invariants

- Stable identifiers are distinct from display names and contact fields.
- Deletion and deactivation behavior are distinguishable.
- Sensitive account fields have privacy and access rules.
- Membership and tenant boundaries are explicit.

## Validation Rules

- Resolve data model, schema, API, form, and access policy references.
- Warn when user identifiers are ambiguous.
- Warn when deletion behavior omits privacy implications.
- Warn when tenant membership lacks access boundaries.

## Agent Implementation Notes

Use this contract before implementing account settings, onboarding, admin
screens, user exports, profile APIs, or tenant-aware features.
