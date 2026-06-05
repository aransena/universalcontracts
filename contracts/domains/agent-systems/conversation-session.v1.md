# Conversation Session Contract v1

Contract ID: `universal.agent.conversation_session.v1`

## Purpose

Describe a conversation or interaction session with messages, participants,
tools, context, artifacts, and lifecycle.

## Required Shape

A conversation session descriptor should include:

- `schema`: `universal.agent.conversation_session.v1`.
- `id`: stable session ID.
- `kind`: `conversation_session`.
- `created_at`: ISO 8601 UTC timestamp.
- `participants`: user, agent, service, and tool identities.
- `messages`: message log, stream, or transcript reference.
- `tools`: tool calls, approvals, and results.
- `context`: files, memory, prompts, policies, or system references.
- `artifacts`: outputs produced during the session.
- `lifecycle`: active, paused, closed, cancelled, or failed state.

## Extension Points

Projects may add UI events, token accounting, model settings, redactions,
attachments, or moderation metadata.

## Invariants

- Message order is preserved.
- Tool calls and user-visible side effects are traceable.
- Context sources are explicit enough for review.
- Sensitive or redacted content is marked.

## Validation Rules

- Resolve local message, artifact, and context references.
- Warn when tool side effects lack approval records.
- Warn when transcripts omit participant identities.

## Agent Implementation Notes

Use this contract for chat exports, agent audit logs, replay, debugging, and
handoffs between systems.

