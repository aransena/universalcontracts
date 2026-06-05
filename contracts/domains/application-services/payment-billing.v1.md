# Payment Billing Contract v1

Contract ID: `universal.app.payment_billing.v1`

## Purpose

Describe payment, subscription, invoice, entitlement, refund, and billing-event
surfaces without binding to a specific payment provider.

## Required Shape

A payment billing descriptor should include:

- `schema`: `universal.app.payment_billing.v1`.
- `id`: stable payment billing surface ID.
- `kind`: `payment_billing`.
- `subjects`: accounts, customers, organizations, subscriptions, orders,
  invoices, or entitlements.
- `flows`: checkout, invoice, renewal, cancellation, refund, dispute, and tax
  flows.
- `records`: local payment records, provider IDs, event IDs, status, and
  reconciliation fields.
- `permissions`: payer, admin, support, service-account, and approval behavior.
- `security`: secret references, webhook signing, idempotency, audit, and
  compliance controls.
- `integration`: provider APIs, webhooks, queues, jobs, reports, and exports.

## Extension Points

Projects may add pricing catalogs, coupons, metering, tax regions, trials,
usage-based billing, revenue reports, or entitlement sync.

## Invariants

- Payment provider state and local state reconciliation are explicit.
- Webhook and retry handling are idempotent.
- Sensitive payment data is referenced, not stored in descriptors.
- Billing status changes are auditable.

## Validation Rules

- Resolve auth, webhook, transaction, job, schema, and audit references.
- Warn when payment events omit idempotency or reconciliation behavior.
- Warn when secret references or webhook signing are missing.
- Warn when entitlements lack source-of-truth semantics.

## Agent Implementation Notes

Use this contract before implementing checkout, subscriptions, invoices,
refunds, provider webhooks, entitlements, or billing admin surfaces.
