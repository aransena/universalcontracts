# Configuration Contract v1

Contract ID: `universal.core.config.v1`

## Purpose

Describe configuration sources, precedence, defaults, validation, and secret
references so agents can run or integrate a system without guessing how settings
are resolved.

## Required Shape

A configuration descriptor should include:

- `schema`: `universal.core.config.v1`.
- `id`: stable configuration surface ID.
- `kind`: `configuration`.
- `sources`: files, environment variables, flags, remote stores, or defaults.
- `precedence`: ordered resolution rules.
- `fields`: known settings, types, defaults, units, and required status.
- `secrets`: secret references, required scopes, and redaction expectations.

## Extension Points

Projects may add framework-specific loaders, typed settings classes, tenant
overrides, feature flags, or remote configuration metadata. Custom settings
should stay declared in `fields` or a referenced local schema.

## Invariants

- Required settings are discoverable before runtime.
- Secret values are not stored in producer-owned manifests.
- Precedence is explicit when multiple sources can define the same setting.
- Defaults do not hide security or data-loss behavior.

## Validation Rules

- Resolve local configuration file references.
- Check that required settings have a source or default.
- Warn when secrets are represented as literal values.
- Warn when precedence is missing for multiple sources.

## Agent Implementation Notes

Use this contract before running commands, services, tests, plugins, or jobs that
depend on environment-specific settings.
