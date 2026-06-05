# Agent Trace Contract v1

Contract ID: `universal.agent.agent_trace.v1`

## Purpose

Describe an agent execution trace with steps, tool calls, decisions, errors,
artifacts, and observability signals.

## Required Shape

An agent trace descriptor should include:

- `schema`: `universal.agent.agent_trace.v1`.
- `id`: stable trace ID.
- `kind`: `agent_trace`.
- `created_at`: ISO 8601 UTC timestamp.
- `subject`: goal, task, session, or workflow reference.
- `steps`: ordered step log, events, spans, or stream reference.
- `tools`: called tools, arguments, results, and side effects.
- `artifacts`: files, patches, reports, or messages produced.
- `status`: `ok`, `partial`, `failed`, `cancelled`, or `unknown`.

## Extension Points

Projects may add model tokens, prompts, policies, hidden reasoning summaries,
latency, cost, sandbox events, or approval records.

## Invariants

- Step order and final status are machine-readable.
- External side effects are traceable.
- Failed traces keep enough error context for diagnosis.
- Redacted content is marked without breaking replay of public steps.

## Validation Rules

- Resolve local step, artifact, and tool references.
- Warn when side effects lack result or approval records.
- Warn when status is final but trace has no terminal step.

## Agent Implementation Notes

Use this contract to audit, replay, compare, or debug agent behavior.

