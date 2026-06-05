# Web Project Contract v1

Contract ID: `universal.web.project.v1`

## Purpose

Describe a web project's stable development, build, runtime, and deployment
surface without depending on a specific framework or hosting provider.

## Required Shape

A web project descriptor should include:

- `schema`: `universal.web.project.v1`.
- `id`: stable web project ID.
- `kind`: `web_project`.
- `producer`: project name, version, and ownership.
- `contracts`: claimed contract IDs.
- `framework`: framework family, rendering mode, and routing mode when known.
- `package`: package manager, dependency manifest, and lockfile references.
- `commands`: install, build, run, test, lint, format, validate, and package.
- `configuration`: environment variables, configuration files, defaults, and
  secrets.
- `build_outputs`: generated assets, server bundles, static files, or manifests.
- `deployment_targets`: static host, server runtime, edge runtime, container,
  embedded web view, or custom target references.

## Extension Points

Projects may add framework-specific conventions, code generation, module
federation, internationalization, feature flags, or asset pipeline metadata.
These should be additive and should not hide commands, configuration, or build
outputs from generic agents.

## Invariants

- Required commands are discoverable from a clean checkout after setup.
- Generated outputs are distinguished from source files.
- Secrets are referenced, not embedded.
- Deployment assumptions are explicit enough to avoid local-only behavior.

## Validation Rules

- Resolve dependency manifest, lockfile, configuration, and output references.
- Warn when deployment targets omit runtime or environment assumptions.
- Warn when build outputs are undocumented.
- Warn when commands depend on undeclared environment variables.

## Agent Implementation Notes

Use this contract before modifying build systems, routing, runtime behavior,
environment handling, or deployment configuration in a web project.
