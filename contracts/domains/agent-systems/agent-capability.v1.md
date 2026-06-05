# Agent Capability Contract v1

Contract ID: `universal.agent.capability.v1`

## Purpose

Describe what an agent can do, what tools and data it may use, and what safety
or approval boundaries apply.

## Required Shape

An agent capability descriptor should include:

- `schema`: `universal.agent.capability.v1`.
- `id`: stable capability ID.
- `kind`: `agent_capability`.
- `agent`: agent, model, runtime, or service reference.
- `goals`: supported task classes and limits.
- `tools`: callable tool or API surface references.
- `permissions`: required scopes, resources, and approvals.
- `inputs`: accepted prompts, files, context, or event sources.
- `outputs`: generated artifacts, actions, messages, or reports.

## Extension Points

Projects may add model-specific settings, planning modes, memory policy,
delegation rules, sandbox profiles, or evaluation scores.

## Invariants

- Capabilities do not imply permission unless permissions are declared.
- Destructive or external actions are distinguishable from local analysis.
- Tool and data dependencies are explicit.
- Human approval requirements are discoverable.

## Validation Rules

- Resolve tool, permission, and runtime references.
- Warn when broad capabilities omit constraints.
- Warn when external actions omit approval or audit notes.

## Agent Implementation Notes

Use this contract to advertise agent behavior without hiding operational or
safety boundaries.

