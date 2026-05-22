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

## Required Project Manifest Fields

A project-level manifest should expose:

- `schema`: contract schema ID.
- `project.name`: stable project name.
- `project.description`: short purpose statement.
- `project.version`: implementation version when applicable.
- `interfaces`: advertised contracts implemented by the project.
- `commands`: build, test, run, lint, format, package, validate.
- `entry_points`: CLI commands, services, modules, web routes, or binaries.
- `config`: configuration files, environment variables, and precedence.
- `artifacts`: generated outputs and where they are written.
- `ownership`: modules or directories that are public, internal, generated, or
  user-editable.

## Invariants

- A command advertised as required must work from a clean checkout after
  documented setup.
- Generated files must be marked as generated.
- User-editable files must not be overwritten by normal build or runtime
  commands unless the contract explicitly says so.
- Public interfaces must be documented by contract ID or project-local schema.

## Agent Notes

Agents should read this contract before making broad changes. If a project
declares commands, use those commands instead of inventing new validation
steps.

