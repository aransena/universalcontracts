# Trajectory Contract v1

Contract ID: `universal.geo.trajectory.v1`

## Purpose

Describe ordered spatial positions, poses, routes, or tracks over time.

## Required Shape

A trajectory descriptor should include:

- `schema`: `universal.geo.trajectory.v1`.
- `id`: stable trajectory ID.
- `kind`: `trajectory`.
- `subject`: device, actor, vehicle, asset, user, or simulated entity.
- `coordinate_frame`: coordinate frame reference.
- `timestamps`: clock, units, and ordering semantics.
- `records`: path to JSONL, CSV, GeoJSON, Parquet, stream, or index.
- `fields`: position, orientation, velocity, uncertainty, and custom fields.
- `stats`: record count, duration, distance, gaps, and quality when available.

## Extension Points

Projects may add map matching, sensor fusion, covariance, route segments,
geofences, elevation, or privacy redaction metadata.

## Invariants

- Record order and timestamp semantics are explicit.
- Coordinate frame and units are declared.
- Gaps, smoothing, or redaction are marked when they affect analysis.
- Custom fields are additive unless a profile closes shape.

## Validation Rules

- Resolve coordinate frame and record references.
- Warn when spatial records omit timestamps.
- Warn when coordinates lack frame or units.

## Agent Implementation Notes

Use this contract for movement analysis, robotics, maps, capture replay,
simulation, and visualization.

