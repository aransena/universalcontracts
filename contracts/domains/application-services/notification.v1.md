# Notification Contract v1

Contract ID: `universal.app.notification.v1`

## Purpose

Describe application notifications across email, SMS, push, in-app, webhook, or
chat channels.

## Required Shape

A notification descriptor should include:

- `schema`: `universal.app.notification.v1`.
- `id`: stable notification surface ID.
- `kind`: `notification`.
- `producer`: service, workflow, job, user action, or integration that emits the
  notification.
- `channels`: email, SMS, push, in-app, webhook, chat, or custom channel.
- `messages`: templates, variables, localization, priority, and schema version.
- `recipients`: users, accounts, roles, teams, devices, or external endpoints.
- `preferences`: opt-in, opt-out, quiet hours, frequency, and suppression rules.
- `delivery`: provider, retry, dedupe, bounce, failure, and audit behavior.

## Extension Points

Projects may add provider IDs, campaign metadata, personalization, experiments,
compliance categories, or channel-specific rendering constraints.

## Invariants

- Notification triggers and recipients are explicit.
- User preferences and suppression rules are respected.
- Failures are observable or intentionally ignored.
- Sensitive content has privacy and retention behavior.

## Validation Rules

- Resolve template, workflow, user account, preference, and audit references.
- Warn when notifications omit opt-out or preference behavior.
- Warn when retries can duplicate user-visible messages.
- Warn when sensitive content lacks privacy notes.

## Agent Implementation Notes

Use this contract before adding emails, push notifications, in-app alerts,
system messages, webhooks, or communication preferences.
