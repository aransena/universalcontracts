# TODO

## Cleanup And Review

- Review the current working tree before committing.
- Remove accidental editor artifacts such as `contracts/core/.stream.v1.md.swp`.
- Split large documentation, contract, schema, profile, and example changes into
  reviewable commits if useful.

## Examples

- Broaden the initial profile examples into richer multi-file fixtures where the
  profile needs more than one descriptor to demonstrate real project adoption.
- Add negative fixtures for validator development.

## Profile Validators

- Add an implementation-level profile validator that can check whether a project
  satisfies a selected `universal.profile.*.v1` descriptor.
- Start with the highest-value profiles:
  - `universal.profile.database_backed_module.v1`
  - `universal.profile.service_module.v1`
  - `universal.profile.web_application.v1`
  - `universal.profile.event_producer_consumer.v1`
- Validate required fields, referenced descriptors, examples, schemas,
  conformance checks, and required integration points.

## Machine Schemas

- Add JSON Schemas for high-value portable descriptors:
  - project or module descriptors
  - service module descriptors
  - database schema, data model, query surface, access policy, and migration
  - web application descriptors
  - event surface descriptors
- Keep schemas permissive by default so project-specific fields remain additive.

## Dogfooding

- Apply UC profiles to at least one real modular app.
- Record where agents still improvise or miss integration handoff points.
- Tighten contracts or profiles where dogfooding shows repeated ambiguity.
- Note where UC is too strict and should permit more project-local extension.

## Maturity And Stability

- Define promotion criteria for moving contracts and profiles from `candidate`
  to `stable`.
- Candidate-to-stable criteria should consider:
  - representative examples
  - validator coverage
  - successful use in at least one real project
  - no unresolved naming or shape inconsistencies
  - documented migration path for breaking changes

## Agent Workflow

- Package the adoption workflow so developers can point agents at UC with
  minimal setup.
- Keep the drop-in system prompt current with profiles and catalog behavior.
- Expand the implementation brief template for profile-specific evidence.
- Add a final-response checklist for agents: selected profile, selected
  contracts, local extensions, validation run, and known conformance gaps.
