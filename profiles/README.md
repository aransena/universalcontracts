# Machine-Readable Profiles

Profiles define reusable integration patterns over Universal Contracts. They are
JSON descriptors so agents and lightweight tooling can choose a concrete
contract set without parsing prose.

Use profiles when a project wants modules built by different teams to expose the
same integration handoff points. Profiles are additive: they require fields,
examples, schemas, and validation behavior without changing base contract
meanings.

Common profile fields:

- `base_contracts`: contract IDs that make up the portable spine.
- `required_fields`: profile-specific required field groups.
- `integration_points`: named handoff surfaces between modules.
- `conformance`: checks an implementation should satisfy before claiming the
  profile.
- `agent_guidance`: short instructions for implementation agents.
