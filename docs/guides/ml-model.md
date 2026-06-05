# Guide: Training, Evaluating, or Serving an ML Model

## Start Here

For training:

- `universal.ml.training_run.v1`
- `universal.ml.model_artifact.v1`
- `universal.data.dataset.v1`
- `universal.core.lifecycle.v1`
- `universal.core.provenance.v1`

For evaluation:

- `universal.ml.evaluation_report.v1`
- `universal.core.test_run.v1`

For serving:

- `universal.ml.inference_service.v1`
- `universal.core.api_surface.v1`
- `universal.ops.deployment.v1`
- `universal.ops.service_health.v1`

## Add Related Contracts

If the model uses document retrieval:

- `universal.knowledge.search_index.v1`
- `universal.agent.memory_store.v1`

If the model is deployed to edge devices:

- `universal.edge.edge_deployment.v1`
- `universal.edge.sbc_service.v1`

## Agent Checklist

1. Trace datasets, parameters, seeds, model artifacts, and metrics.
2. Preserve input and output descriptions for downstream callers.
3. Link evaluation reports to the evaluated subject and datasets.
4. Keep serving schemas, auth, limits, and health visible.
5. Use project-local profiles for model-family-specific details.

