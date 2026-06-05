# Tile Set Contract v1

Contract ID: `universal.geo.tile_set.v1`

## Purpose

Describe a tiled map, image, elevation, point cloud, or vector dataset for
efficient visualization and delivery.

## Required Shape

A tile set descriptor should include:

- `schema`: `universal.geo.tile_set.v1`.
- `id`: stable tile set ID.
- `kind`: `tile_set`.
- `tile_type`: raster, vector, elevation, point_cloud, imagery, or custom.
- `coordinate_frame`: CRS, projection, or tiling scheme reference.
- `layout`: zoom levels, tile matrix, x/y/z pattern, bounds, and resolution.
- `files`: tile root, manifest, metadata, style, preview, or checksums.
- `sources`: map layers, imagery, datasets, or rendering jobs.

## Extension Points

Projects may add MBTiles, PMTiles, cloud optimized GeoTIFF, CDN, cache,
compression, style, or attribution metadata.

## Invariants

- Tile addressing and coordinate frame are explicit.
- Bounds and zoom or resolution coverage are declared.
- Source and attribution are preserved.
- Missing tiles and sparse coverage are documented when expected.

## Validation Rules

- Resolve local tile root, manifest, and source references.
- Warn when tile layout is ambiguous.
- Warn when shareable tiles omit attribution or license notes.

## Agent Implementation Notes

Use this contract for map delivery, preview generation, offline packages, and
geospatial visualization.

