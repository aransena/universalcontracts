# Profiles

Profiles let projects and domains customize Universal Contracts without
fragmenting the portable spine.

## Profile Layers

Universal Contracts use three layers:

1. Base contract: reusable portable meaning, for example
   `universal.core.stream.v1`.
2. Domain profile: a reusable narrowing or extension for a domain, for example a
   capture stream profile or UI component profile.
3. Project-local profile: application-specific requirements owned by one
   project or organization.

## Profile Descriptor Shape

A profile descriptor should include:

- `schema`: `universal.profile.v1`.
- `id`: stable profile ID.
- `kind`: `profile`.
- `title`: human-readable profile title.
- `base_contracts`: contract IDs this profile extends or narrows.
- `domain_packs`: domain packs the profile composes.
- `maturity`: `draft`, `candidate`, `stable`, or `deprecated`.
- `required_fields`: additional fields required by the profile.
- `allowed_values`: narrowed enum-like values.
- `schemas`: local or shared schema references.
- `examples`: example descriptor or fixture references.
- `compatibility`: compatible versions, migration notes, and replacements.
- `integration_points`: named handoff points, required contracts, and whether
  the point is required.
- `conformance`: minimum level, supported levels, and checks.
- `agent_guidance`: short instructions for implementation agents.

Machine-readable UC profiles live in `profiles/*.v1.json` and are included in
`contracts/catalog.json`.

## Profile Rules

- Profiles may add fields.
- Profiles may narrow allowed values.
- Profiles may require additional files or schemas.
- Profiles may define stricter validation.
- Profiles must not change base field meanings.
- Unknown profile fields remain extension data unless the profile explicitly
  closes shape.

## Catalog Representation

Catalog entries list profile relationships through:

- `composes_core`
- `related_domain_packs`
- `example_paths`
- `profiles`

Profiles are not a replacement for contracts. They select and narrow a contract
set for a recurring integration pattern, such as a database-backed module, web
application, service module, event producer/consumer, UI component package, CLI
tool, data exchange surface, ML serving module, edge telemetry module,
integration connector, or file processing pipeline.

## Agent Workflow

1. Select the smallest profile that matches the module being built.
2. Load each `base_contracts` entry and preserve its required shape and
   invariants.
3. Apply `required_fields` and `allowed_values` from the profile.
4. Keep project-specific fields additive and declared through local schemas.
5. Report the selected profile, selected contracts, project-specific
   customizations, and conformance checks performed.
