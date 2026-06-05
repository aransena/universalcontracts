# Simulation Run Contract v1

Contract ID: `universal.sim.simulation_run.v1`

## Purpose

Describe one execution of a simulation, including scenario, parameters,
environment, outputs, metrics, and replay artifacts.

## Required Shape

A simulation run descriptor should include:

- `schema`: `universal.sim.simulation_run.v1`.
- `id`: stable simulation run ID.
- `kind`: `simulation_run`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: simulator project and version.
- `scenario`: scenario or world reference.
- `parameters`: seeds, physics, agent policies, and runtime settings.
- `lifecycle`: run state and timestamps.
- `outputs`: streams, datasets, reports, media, or artifacts.
- `metrics`: summary values, units, and pass/fail criteria.

## Extension Points

Projects may add engine-specific settings, hardware acceleration, random number
generators, recorded controls, deterministic replay, or fault injection.

## Invariants

- Scenario, parameters, and seed are explicit enough for replay attempts.
- Outputs are discoverable through manifests.
- Metrics include units and scope.
- Failed runs retain enough information for diagnosis.

## Validation Rules

- Resolve scenario, output, and report references.
- Warn when randomness is used without seed or determinism notes.
- Warn when metrics omit units.

## Agent Implementation Notes

Use this contract for replayable simulation, synthetic data generation, testing,
and analysis.

