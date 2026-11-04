# Google Cloud Platform (optional, only when present or requested)

Inspect current GCP service selection, project configuration, deployment manifests, IaC, identity and environment boundaries. Do not assume Cloud Run, GKE, Cloud SQL or another service. Prefer least-privilege service identities, managed secret references and explicit environment configuration. Confirm region, project, network, cost and data requirements if not evident from code. Do not deploy, change IAM, enable APIs or incur costs without explicit approval. Validate configuration and report limits of local testing.

Approved as a separate optional reference in Phase 2.
