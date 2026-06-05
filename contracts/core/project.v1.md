# Project Contract v1

Contract ID: `universal.core.project.v1`

## Purpose

Describe the stable interface of a software repository so humans, applications,
and agents can build, run, test, package, and extend it without guessing.

## Applies To

- Libraries
- Services
- CLIs
- Apps
- Plugins
- Device or capture adapters
- Data and ML projects

## Required Shape

A project-level manifest should expose:

- `schema`: `universal.core.project.v1`.
- `id`: stable project ID.
- `kind`: `project`.
- `project`: name, description, version, and project-local metadata.
- `interfaces`: advertised contracts implemented by the project.
- `commands`: build, test, run, lint, format, package, validate.
- `entry_points`: CLI commands, services, modules, web routes, or binaries.
- `configuration`: configuration files, environment variables, and precedence.
- `artifacts`: generated outputs and where they are written.
- `ownership`: modules or directories that are public, internal, generated, or
  user-editable.

## Extension Points

Projects may add framework-specific commands, module ownership, generated code
metadata, deployment targets, or project-local profiles. Extensions should keep
command, configuration, entry point, and ownership meaning stable.

## Invariants

- A command advertised as required must work from a clean checkout after
  documented setup.
- Generated files must be marked as generated.
- User-editable files must not be overwritten by normal build or runtime
  commands unless the contract explicitly says so.
- Public interfaces must be documented by contract ID or project-local schema.

## Validation Rules

- Check that required commands are documented.
- Resolve referenced configuration, artifact, and entry point paths.
- Warn when generated or user-editable ownership is unclear.
- Warn when public interfaces lack contract or schema references.

## Agent Implementation Notes

Agents should read this contract before making broad changes. If a project
declares commands, use those commands instead of inventing new validation
steps.
