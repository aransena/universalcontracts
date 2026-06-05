# Schemas

JSON Schemas are provided for contracts where machine validation is useful.

Core schemas:

- `catalog.v1.schema.json`
- `maturity.v1.schema.json`
- `profile.v1.schema.json`
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

Not every first-pass contract has a schema. Add schemas once a contract's
portable spine is stable enough for machine validation. Domain-specific
precision should usually live in project-local schemas or declared profiles
before being promoted into Universal Contracts.
