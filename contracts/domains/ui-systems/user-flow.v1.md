# UI User Flow Contract v1

Contract ID: `universal.ui.user_flow.v1`

## Purpose

Describe a multi-step user workflow across screens, forms, services, and
artifacts.

## Required Shape

A user flow descriptor should include:

- `schema`: `universal.ui.user_flow.v1`.
- `id`: stable flow ID.
- `kind`: `ui_user_flow`.
- `actors`: user roles, agents, services, or devices involved.
- `entry_points`: routes, screens, links, commands, or external triggers.
- `steps`: ordered or branched actions, validations, screens, and decisions.
- `data`: inputs, outputs, drafts, persisted state, and side effects.
- `exits`: completion, cancellation, timeout, failure, and recovery paths.
- `permissions`: auth, roles, approvals, and destructive action constraints.
- `artifacts`: records, uploads, downloads, notifications, or reports produced.

## Extension Points

Projects may add analytics, experiments, onboarding variants, localization,
human approval steps, or platform-specific path differences.

## Invariants

- Entry and exit conditions are explicit.
- Failure and cancellation paths are not hidden.
- Side effects are declared at the step where they occur.
- Roles and permissions are visible before automation executes the flow.

## Validation Rules

- Resolve route, screen, form, artifact, and permission references.
- Warn when flows omit recovery from expected failures.
- Warn when side effects lack status or error mapping.
- Warn when required user roles are not declared.

## Agent Implementation Notes

Use this contract to preserve end-to-end UX behavior while changing individual
screens, components, APIs, or storage.

