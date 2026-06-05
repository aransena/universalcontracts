# Plugin Package Contract v1

Contract ID: `universal.plugin.package.v1`

## Purpose

Describe an installable plugin package, its extension points, permissions,
runtime requirements, and exported capabilities.

## Applies To

- Editor plugins
- Agent plugins
- CLI plugins
- Application extensions
- Integration packages
- Tool bundles

## Required Shape

A plugin package descriptor should include:

- `schema`: `universal.plugin.package.v1`.
- `id`: stable plugin ID.
- `kind`: `plugin`.
- `created_at`: ISO 8601 UTC timestamp when packaged.
- `producer`: project, version, and packaging command.
- `contracts`: claimed contract IDs.
- `entry_points`: commands, modules, tools, UI surfaces, hooks, or services.
- `permissions`: filesystem, network, secrets, app scopes, or user approvals.
- `configuration`: configuration files, environment variables, defaults, and
  precedence.
- `artifacts`: packaged files, generated bundles, or installation outputs.

## Recommended Fields

- `compatibility`: host app versions, OS, runtimes, and protocol versions.
- `lifecycle`: install, activate, deactivate, update, and uninstall behavior.
- `commands`: test, build, package, validate, and release commands.
- `security`: sandboxing, trust boundaries, and data handling notes.
- `examples`: minimal host configuration and fixture usage.

## Extension Points

Hosts may add platform-specific manifest fields. These should be mirrored or
referenced from portable fields so generic agents can still identify what the
plugin exports and what permissions it needs.

## Invariants

- Entry points and permissions are explicit before installation.
- Generated package outputs are distinguished from source files.
- User configuration is not overwritten by activation or update.
- Host-specific metadata does not hide universal capability information.

## Validation Rules

- Resolve local entry point and artifact paths.
- Check that requested permissions are declared and scoped.
- Warn when install or activation mutates user files without lifecycle notes.
- Warn when compatibility information is missing.

## Agent Implementation Notes

Use this contract before installing, modifying, packaging, or reviewing plugins.
Keep host-specific behavior declared, not implicit.
