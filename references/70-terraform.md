# Terraform (optional, only when present or requested)

Inspect `.tf`, `.tfvars`, providers, modules, state backend, workspace and CI before proposing changes. Preserve provider versions, naming, layout and existing deployment approach. Never assume a cloud provider from Terraform alone. Avoid secrets in source, plans or logs. Use `terraform fmt -check`, `terraform validate` and plan when safely configured; never apply or destroy infrastructure without explicit confirmation and normal permissions. Ask about ambiguous environment and state ownership. Keep changes limited to confirmed scope.

Approved as a separate optional reference in Phase 2; principles adapted from the source corpus where applicable, without claiming a particular source mandates this architecture.
