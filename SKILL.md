---
name: spring-java-skill
description: Use for any Java 21+ or Spring Boot 4 repository task, including features, bugs, APIs, tests, refactors, persistence, build tooling, Terraform or GCP infrastructure associated with the Java/Spring application. Inspect the repository, conduct a mandatory multi-question interview, and wait for explicit implementation approval before changing code.
---

# Spring Java engineering skill

1. **Always** inspect the available repository and relevant files first, even for a small task. Identify Spring/Java versions, build tool, existing conventions and test setup. If no repository is accessible, ask for it; do not invent facts.
2. **Always** conduct the multi-round interview in [00-interview-grill-me.md](references/00-interview-grill-me.md). Skip questions the code answers; ask many independent questions per round. Produce a written scope/acceptance summary and **wait for user confirmation before writing code**.
3. Apply [10-behavior-rules.md](references/10-behavior-rules.md) and [20-spring-boot-4-java-21.md](references/20-spring-boot-4-java-21.md). Piotr's Spring conventions take precedence over other sourced conventions, except explicit user requirements. When non-Piotr sources conflict and no choice is approved, ask rather than assume.
4. Detect and use the project's build tool per [30-build-tool-detection.md](references/30-build-tool-detection.md). Select tests by risk: [40-testing-unit.md](references/40-testing-unit.md), [50-testing-integration-testcontainers.md](references/50-testing-integration-testcontainers.md).
5. When relevant, consult [70-terraform.md](references/70-terraform.md), [80-gcp.md](references/80-gcp.md), and [90-postgresql.md](references/90-postgresql.md); do not presume these technologies are in use.
6. Record repeatable corrections/failures and propose (never silently apply) improvements under [60-learnings-and-self-improvement.md](references/60-learnings-and-self-improvement.md).

Do not introduce Spring Boot 3 fallbacks. Do not copy another project's group ID. Verify builds/tests and report what ran versus what could not run.

Before approval, do not install dependencies, change files, migrate databases, or perform other mutating actions. See the interview reference. For a new project, ask before selecting package organization.
