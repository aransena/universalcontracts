# Tool Surface Contract v1

Contract ID: `universal.agent.tool_surface.v1`

## Purpose

Describe tools callable by agents, including inputs, outputs, side effects,
permissions, and error behavior.

## Required Shape

A tool surface descriptor should include:

- `schema`: `universal.agent.tool_surface.v1`.
- `id`: stable tool surface ID.
- `kind`: `tool_surface`.
- `tools`: tool names, descriptions, input schemas, and output schemas.
- `side_effects`: filesystem, network, database, user-visible, or destructive
  behavior.
- `permissions`: required scopes and approvals.
- `errors`: recoverable errors, retry behavior, and fatal conditions.
- `runtime`: endpoint, command, plugin, or service reference.

## Extension Points

Projects may add agent-tool protocol, API specification, function-call, plugin,
or host-specific metadata. Portable fields should still identify how an agent
can call the tool safely.

## Invariants

- Inputs and outputs are schema-backed or explicitly described.
- Side effects are declared before execution.
- Permission requirements are visible at tool level.
- Errors can be handled programmatically where possible.

## Validation Rules

- Resolve local input and output schema references.
- Warn when side-effecting tools omit permissions.
- Warn when structured outputs are undocumented.

## Agent Implementation Notes

Use this contract when exposing project automation, APIs, plugins, or local
commands to agents.
