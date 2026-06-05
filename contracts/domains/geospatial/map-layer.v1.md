# Map Layer Contract v1

Contract ID: `universal.geo.map_layer.v1`

## Purpose

Describe a geospatial layer such as vector features, raster imagery, point
clouds, grids, semantic maps, or overlays.

## Required Shape

A map layer descriptor should include:

- `schema`: `universal.geo.map_layer.v1`.
- `id`: stable layer ID.
- `kind`: `map_layer`.
- `layer_type`: vector, raster, point_cloud, grid, semantic, annotation, or
  custom.
- `coordinate_frame`: CRS, projection, or local frame reference.
- `files`: data, style, metadata, index, preview, or checksum roles.
- `bounds`: spatial extent, resolution, zoom, scale, or coverage.
- `fields`: feature attributes, units, classes, and schemas.
- `sources`: upstream map, sensor, dataset, or generation reference.

## Extension Points

Projects may add tile pyramids, styling, symbology, topology, semantic classes,
privacy masks, or provider-specific metadata.

## Invariants

- Coordinate frame and bounds are declared.
- Data and style files are distinguishable.
- Feature fields are documented for analysis.
- Source and license status are explicit for sharing.

## Validation Rules

- Resolve local file, frame, and source references.
- Warn when bounds or coordinate frame are missing.
- Warn when shareable layers omit license or source notes.

## Agent Implementation Notes

Use this contract for maps, dashboards, robotics worlds, GIS exports, and
spatial analysis.

