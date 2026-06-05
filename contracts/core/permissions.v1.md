# Permissions Contract v1

Contract ID: `universal.core.permissions.v1`

## Purpose

Describe what access a system, tool, plugin, service, or job needs before it is
run, installed, or integrated.

## Required Shape

A permissions descriptor should include:

- `schema`: `universal.core.permissions.v1`.
- `id`: stable permission surface ID.
- `kind`: `permissions`.
- `scopes`: named access scopes and their purpose.
- `resources`: filesystem paths, network hosts, APIs, devices, databases, or
  secrets.
- `operations`: read, write, execute, delete, upload, publish, subscribe, or
  administer.
- `approval`: required user, admin, or service-account approval.

## Extension Points

Projects may add host-specific permission models, delegated identity scopes,
cloud access roles, device permissions, sandbox profiles, or tenant boundaries.

## Invariants

- Required access is explicit before execution.
- Secret names or references may be stored, but secret values are not.
- Destructive operations are distinguishable from read-only operations.
- Least-privilege alternatives are documented when available.

## Validation Rules

- Check that declared resources use recognizable reference forms.
- Warn when broad access lacks a reason.
- Warn when secrets are represented as literal values.
- Warn when destructive operations omit approval expectations.

## Agent Implementation Notes

Use this contract when installing plugins, running automation, deploying
services, connecting devices, or granting API access.
