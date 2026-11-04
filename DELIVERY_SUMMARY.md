# Final delivery summary — 2026-10-26

## Scope

General, agent-agnostic Spring Boot 4 / Java 21+ skill pack. Includes `SKILL.md`, ten separate reference files, learning-log template, evaluation definitions, license report, attribution notice, Phase 2 conflict decisions, and unmodified source snapshots in `vendor/`.

## Source contributions

- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills): four behavior principles independently restated; source is unverified-license and vendor-only.
- [piomin/claude-ai-spring-boot](https://github.com/piomin/claude-ai-spring-boot): primary Spring Boot conventions, including no Lombok, constructor injection, RestClient, RestTestClient, and Testcontainers service connections.
- [sivaprasadreddy/sivalabs-agent-skills](https://github.com/sivaprasadreddy/sivalabs-agent-skills): Java/Spring workflow and testing guidance.
- [decebals/claude-code-java](https://github.com/decebals/claude-code-java): Java engineering practices.
- [rrezartprebreza/spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills): Spring application patterns.
- [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills): spring-boot-engineer guidance only.
- [github/awesome-copilot](https://github.com/github/awesome-copilot): java-springboot guidance only.
- [mattpocock/skills](https://github.com/mattpocock/skills): grill-me multi-round interview pattern.

## Conflict decisions

See `PHASE2_RULE_EXTRACTION.md` for the complete source-file rule extraction and conflict register. Piotr wins Spring convention conflicts: no Lombok, constructor injection, RestClient, RestTestClient, @ServiceConnection where supported. Explicit user instructions override Piotr for Maven/Gradle detection, preserving project group ID, and Spring Boot 4 / Java 21+ only. Follow existing package organization and migration tooling; risk-based testing. Terraform, GCP, and general PostgreSQL references are included on explicit approval.

## Validation

Phase 4 static checks: 42/42 passed in the prior evaluation. Ten positive and ten negative prompts checked using a heuristic classifier. One classifier regression was retained. **Five agent-executed baseline-versus-skill comparisons were not run** because no usable coding-agent runtime was available. User authorized skipping these comparisons and proceeding to final delivery. This is a waived test requirement, not a passing result. See `evals/PHASE4_REPORT.md`.

## Remaining verification

- Git commit IDs for eight user-supplied branch ZIPs remain unverified; archive SHA-256 hashes are in `LICENSE_REPORT.md`.
- Karpathy source has no root license in the provided snapshot; retain vendor-only for review, and do not redistribute it without reviewing rights.
- Repository-root license findings do not settle all file-level license conditions; review before external redistribution.
- Actual agent execution, compilation, Maven/Gradle builds, and Docker/Testcontainers integration testing have not been validated.
- The `vendor/` directory contains original ZIP snapshots, not shallow Git clones.
