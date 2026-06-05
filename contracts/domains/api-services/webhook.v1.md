# Webhook Contract v1

Contract ID: `universal.api.webhook.v1`

## Purpose

Describe an outbound or inbound webhook event surface, including event schemas,
delivery guarantees, signatures, retries, and subscriptions.

## Required Shape

A webhook descriptor should include:

- `schema`: `universal.api.webhook.v1`.
- `id`: stable webhook surface ID.
- `kind`: `webhook`.
- `direction`: `incoming`, `outgoing`, or `bidirectional`.
- `events`: event names, schemas, versions, and examples.
- `delivery`: endpoint URL shape, retry policy, timeout, and ordering.
- `security`: signing, authentication, replay protection, and secret refs.
- `subscription`: registration, filtering, and lifecycle rules.

## Extension Points

Projects may add provider-specific headers, tenant routing, event filters,
dead-letter queues, or replay tools.

## Invariants

- Event schema versions are declared.
- Receivers can verify authenticity when required.
- Retry and duplicate delivery behavior is explicit.
- Unknown event types are either skippable or documented as fatal.

## Validation Rules

- Resolve local event schema references.
- Warn when signatures or replay protection are omitted for external webhooks.
- Warn when retry behavior is unspecified.

## Agent Implementation Notes

Use this contract when integrating event-driven services or connecting external
automation systems.

