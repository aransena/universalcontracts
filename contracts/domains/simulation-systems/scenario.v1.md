# Scenario Contract v1

Contract ID: `universal.sim.scenario.v1`

## Purpose

Describe a simulation scenario, initial conditions, actors, assets, goals, and
constraints.

## Required Shape

A scenario descriptor should include:

- `schema`: `universal.sim.scenario.v1`.
- `id`: stable scenario ID.
- `kind`: `scenario`.
- `created_at`: ISO 8601 UTC timestamp when authored or imported.
- `producer`: scenario authoring project.
- `world`: map, environment, scene, or world-state reference.
- `actors`: agents, devices, vehicles, users, or simulated entities.
- `initial_state`: initial positions, values, resources, and conditions.
- `goals`: objectives, success criteria, constraints, or expected outcomes.
- `assets`: referenced media, models, datasets, or configuration.

## Extension Points

Projects may add domain-specific physics, behavior trees, traffic rules,
weather, sensor configuration, scripts, or validation profiles.

## Invariants

- Initial state and assets are discoverable.
- Success criteria are explicit when the scenario is used for tests.
- Coordinate frames and units are declared where spatial data appears.
- Scenario files do not depend on hidden runtime defaults.

## Validation Rules

- Resolve world, asset, and script references.
- Warn when spatial data lacks coordinate frames or units.
- Warn when test scenarios omit success criteria.

## Agent Implementation Notes

Use this contract to share, replay, compare, or generate simulation scenarios.

