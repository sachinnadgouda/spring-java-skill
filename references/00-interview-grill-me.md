# Interview-First Requirements Clarification

## Mandatory gate
Run this workflow before every coding task, including small changes, bug fixes, refactors, tests, and configuration edits. Read the repository first so you do not ask questions already answered by the codebase.

**Do not edit or write implementation code until the user confirms the written requirements summary.** Reading files, inspecting build metadata, running non-mutating checks, and asking questions are allowed before confirmation. Do not run commands that change files, install dependencies, migrate databases, or alter external state before approval unless explicitly authorized.

## 1. Inspect first
1. Identify the repository root and read applicable instructions (`AGENTS.md`, `CLAUDE.md`, contribution guides, and local instructions).
2. Inspect build files, Java/Spring versions, modules, architecture, nearby code, tests, API contracts, configuration, and naming/style.
3. Search for existing implementations and shared utilities before proposing new abstractions.
4. Separate repository facts from assumptions needing user input.
5. For narrow edits, still inspect first; ask fewer questions only when the code genuinely resolves them.

## 2. Ask questions in batches
Ask all currently useful questions in one round, grouped by topic. Avoid one-question-at-a-time interviewing. Skip questions answered by code, docs, tests, or the prompt. Ask follow-up rounds only when answers reveal new material uncertainty.

Cover relevant items:
- **Goal and scope:** desired outcome, in/out of scope, feature/defect/refactor/migration.
- **Users and actors:** callers, roles, permissions, public/internal/service-to-service use.
- **Behavior:** happy path, state transitions, retries, duplicates, concurrency, partial failure.
- **Edge cases:** missing/invalid values, boundaries, not-found, conflicting updates, time zones, large inputs.
- **Data model:** entities, identifiers, relationships, invariants, ownership, retention, audit, migration/backfill.
- **API contract:** routes, methods, schemas, status codes, pagination, sorting, filtering, idempotency, versioning, compatibility, error format.
- **Errors and observability:** expected failures, retryability, exception mapping, logs, metrics, traces, alerts.
- **Security/privacy:** authentication, authorization, validation, secrets, sensitive data, tenant boundaries, rate limits, abuse.
- **Performance/scale:** volume, latency, throughput, concurrency, payload sizes, caching, consistency.
- **Integrations:** external systems, timeouts, retries, circuit breaking, client choice, failure behavior.
- **Testing:** unit, MVC slice, persistence, integration, contract, end-to-end, security, performance coverage.
- **Acceptance criteria:** observable pass/fail conditions, required commands, compatibility constraints, completion definition.
- **Delivery constraints:** deployment, feature flags, rollback, schema compatibility, runbooks, docs, deadlines where relevant.

Do not force irrelevant questions into small tasks. Ask many questions per round, but only those that could change design, behavior, risk, or acceptance criteria.

## 3. Handle uncertainty honestly
- Never invent requirements or silently choose between materially different interpretations.
- Offer a recommended default and brief trade-off where useful, then ask the user to choose.
- If the user says “I don't know,” recommend a safe, reversible option and seek confirmation when the choice materially affects behavior.
- If an answer requires a prototype or benchmark, identify that dependency instead of asking speculative questions.
- A suggestion is not approval.

## 4. Summarize and wait
Present a written summary containing:
1. Goal and non-goals.
2. Users/actors and key flow.
3. Data and API contract.
4. Validation, errors, security, performance.
5. Test plan.
6. Acceptance criteria.
7. Assumptions and unresolved decisions.
8. Expected files/components to change, where knowable.

Ask: **“Please confirm this summary before I change code.”** Stop. Do not write or modify code until explicit confirmation. If scope changes, update the summary and obtain confirmation again.

## 5. After confirmation
Implement the smallest coherent change. Follow existing project patterns and these references. Run focused tests/build, inspect the diff, and report changes, verification, failures, and uncertainty. Never claim a test passed unless it was actually run and passed.


Source note: Adapted guidance from the supplied Personal ChatGPT skill pack; verify Spring-specific decisions against piomin/claude-ai-spring-boot, which remains authoritative.
