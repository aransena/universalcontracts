# Feature Flag Contract v1

Contract ID: `universal.app.feature_flag.v1`

## Purpose

Describe feature flags, experiments, rollout rules, configuration gates, kill
switches, and compatibility behavior.

## Required Shape

A feature flag descriptor should include:

- `schema`: `universal.app.feature_flag.v1`.
- `id`: stable feature flag surface ID.
- `kind`: `feature_flag`.
- `flags`: flag keys, descriptions, owners, default values, and maturity.
- `targets`: users, tenants, environments, devices, regions, or cohorts.
- `rules`: rollout, percentage, allowlist, denylist, dependency, and fallback
  behavior.
- `lifecycle`: proposed, active, ramping, permanent, deprecated, removed, or
  custom states.
- `observability`: exposure logs, metrics, experiments, alerts, and debug views.
- `cleanup`: removal criteria, stale flag policy, and migration notes.

## Extension Points

Projects may add provider metadata, experiment analysis, dependency graphs,
remote configuration, emergency overrides, or release links.

## Invariants

- Defaults and fallback behavior are explicit.
- Flag effects are discoverable at implementation boundaries.
- Emergency rollback or kill-switch behavior is documented when relevant.
- Stale flags have owners and cleanup expectations.

## Validation Rules

- Resolve release, configuration, route, service, metric, and experiment
  references.
- Warn when flags lack owner or default behavior.
- Warn when rollout rules omit fallback behavior.
- Warn when permanent flags should be converted to normal configuration.

## Agent Implementation Notes

Use this contract before gating UI, APIs, jobs, migrations, edge behavior,
experiments, or staged releases.
