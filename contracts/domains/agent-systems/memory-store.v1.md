# Memory Store Contract v1

Contract ID: `universal.agent.memory_store.v1`

## Purpose

Describe an agent memory, retrieval, or context store so agents and tools can
understand content, retention, permissions, and lookup semantics.

## Required Shape

A memory store descriptor should include:

- `schema`: `universal.agent.memory_store.v1`.
- `id`: stable memory store ID.
- `kind`: `memory_store`.
- `storage`: database, index, files, vector store, or service reference.
- `records`: record types, schemas, embeddings, and metadata fields.
- `retrieval`: query modes, ranking, filters, and freshness.
- `retention`: expiration, deletion, archival, and user-control rules.
- `permissions`: read, write, delete, and export access.

## Extension Points

Projects may add embedding models, chunking policy, privacy classifications,
tenant isolation, summarization, or compaction metadata.

## Invariants

- Stored content types and ownership are explicit.
- Retrieval semantics are clear enough for downstream use.
- Privacy and deletion expectations are documented.
- Memory updates do not silently overwrite user-owned content.

## Validation Rules

- Resolve local schema, index, and storage references.
- Warn when retention or deletion policy is missing.
- Warn when embeddings omit model or dimension information.

## Agent Implementation Notes

Use this contract when agents need persistent context, retrieval, personalization,
or auditable memory.

