# Coordinate Frame Contract v1

Contract ID: `universal.geo.coordinate_frame.v1`

## Purpose

Describe a spatial reference frame, coordinate system, transform, or map
projection used by geospatial, robotics, simulation, or capture systems.

## Required Shape

A coordinate frame descriptor should include:

- `schema`: `universal.geo.coordinate_frame.v1`.
- `id`: stable frame ID.
- `kind`: `coordinate_frame`.
- `frame_type`: geographic, projected, local, body, sensor, map, or custom.
- `definition`: EPSG, WKT, PROJ, transform matrix, origin, axes, or units.
- `parent`: parent frame and transform when applicable.
- `validity`: region, time range, datum, or calibration reference.

## Extension Points

Projects may add covariance, dynamic transforms, geoid models, sensor extrinsics,
robot kinematics, or simulator-specific coordinate systems.

## Invariants

- Units and axis conventions are explicit.
- Parent transforms are declared when coordinates cross frames.
- Custom frames have enough definition for downstream transformation.
- Dynamic frames declare timestamp requirements.

## Validation Rules

- Resolve parent frame and calibration references.
- Warn when axes or units are missing.
- Warn when custom frames lack origin or transform definition.

## Agent Implementation Notes

Use this contract anywhere spatial data needs to be merged, visualized, replayed,
or analyzed.

