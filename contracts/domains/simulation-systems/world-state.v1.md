# World State Contract v1

Contract ID: `universal.sim.world_state.v1`

## Purpose

Describe a simulated or captured world state with entities, coordinates,
resources, time, and environment conditions.

## Required Shape

A world state descriptor should include:

- `schema`: `universal.sim.world_state.v1`.
- `id`: stable world state ID.
- `kind`: `world_state`.
- `timestamps`: clock, units, and fields such as `timestamp_unix_ns`,
  `timestamp_monotonic_ns`, or `timestamp_sim_ns`.
- `coordinate_frames`: frame references and transforms.
- `entities`: objects, actors, devices, assets, and their properties.
- `environment`: weather, lighting, map, terrain, or context.
- `files`: state snapshot, meshes, maps, textures, or auxiliary data.

## Extension Points

Projects may add physics engine state, uncertainty, semantic maps, occupancy,
sensor readings, or domain-specific entity properties.

## Invariants

- Coordinates and units are explicit.
- Entity IDs are stable within the state or sequence.
- Snapshot files are discoverable.
- Unknown entity properties are additive unless a profile closes shape.

## Validation Rules

- Resolve local frame, map, and asset references.
- Warn when spatial entities lack coordinate frame information.
- Warn when units are missing for physical quantities.
- Warn when timestamp fields do not follow UC timestamp naming conventions.

## Agent Implementation Notes

Use this contract for replay, synthetic data, robotics, geospatial analysis, and
simulation debugging.
