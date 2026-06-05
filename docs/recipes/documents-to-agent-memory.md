# Recipe: Documents to Agent Memory

## Flow

```text
document corpus -> extraction run -> search index -> memory store -> tool surface -> agent trace
```

## Contracts

- `universal.knowledge.document_corpus.v1`
- `universal.knowledge.document.v1`
- `universal.knowledge.extraction_run.v1`
- `universal.knowledge.search_index.v1`
- `universal.agent.memory_store.v1`
- `universal.agent.tool_surface.v1`
- `universal.agent.agent_trace.v1`
- `universal.core.permissions.v1`

## Interoperability Handoff

1. Corpus descriptors declare sources, licenses, privacy, and index references.
2. Extraction runs preserve parser settings, output files, quality, and errors.
3. Search indexes declare source version, fields, query modes, and limits.
4. Memory stores declare retention, retrieval, and permissions.
5. Tool surfaces and traces make agent access auditable.

## Agent Notes

Do not treat extracted text as source truth. Preserve document provenance and
make retrieval limits visible to agents.

