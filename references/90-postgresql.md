# PostgreSQL application conventions

Inspect existing schema, ORM mappings, indexes, migrations, query style and transaction behavior. Preserve existing migration tool (Flyway, Liquibase or another); if no tool exists and a migration is needed, ask which to use. Avoid destructive migrations without a rollback/data preservation plan and approval. Use parameterized queries, explicit constraints, appropriate indexes and query plans when performance matters; avoid N+1 queries. Keep database-specific integration tests on PostgreSQL Testcontainers as described in [50-testing-integration-testcontainers.md](50-testing-integration-testcontainers.md). Never assume credentials or modify production data.

Approved as a separate general reference in Phase 2.
