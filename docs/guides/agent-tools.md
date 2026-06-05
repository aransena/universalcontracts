# Guide: Exposing Tools to Agents

## Start Here

Use:

- `universal.agent.tool_surface.v1`
- `universal.agent.agent_capability.v1`
- `universal.core.permissions.v1`
- `universal.core.command.v1`
- `universal.core.api_surface.v1`

## Add Traceability

For auditable agent behavior, add:

- `universal.agent.conversation_session.v1`
- `universal.agent.agent_trace.v1`
- `universal.core.provenance.v1`

For persistent retrieval or memory:

- `universal.agent.memory_store.v1`
- `universal.knowledge.search_index.v1`

## Agent Checklist

1. Declare tool input and output schemas.
2. Declare side effects and permissions before execution.
3. Keep error shapes machine-readable.
4. Trace tool calls, approvals, and artifacts.
5. Separate local analysis tools from tools that mutate external state.

