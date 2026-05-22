# Schemas

JSON Schemas are provided for contracts where machine validation is useful.

Core schemas:

- `manifest.v1.schema.json`
- `lifecycle.v1.schema.json`
- `stream.v1.schema.json`
- `artifact.v1.schema.json`

Domain schemas:

- `recording-bundle.v1.schema.json`
- `payload-index-row.v1.schema.json`

Schemas intentionally allow additional properties unless the contract needs a
closed shape. This lets projects add domain-specific metadata while preserving
the universal interface.

