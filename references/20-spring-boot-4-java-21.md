# Spring Boot 4 and Java 21+ Conventions

## Applicability and precedence
Target **Spring Boot 4.x and Java 21 or newer**. Do not fall back to Spring Boot 3; explain incompatibilities and ask before changing the target. Inspect actual versions and local instructions first. Piotr's `claude-ai-spring-boot` conventions are the primary authority for Spring-specific choices. This policy is independently worded and does not adopt Piotr's personal Maven group ID, artifact naming, or release conventions.

## Java and code structure
- Use Java 21+ features supported by the configured toolchain. Do not raise the version without confirmation.
- **Do not introduce Lombok.** Prefer explicit Java and logger declarations. If a project already uses Lombok, do not expand its use; ask before a migration.
- Use constructor injection for required dependencies; avoid field injection.
- Prefer records for suitable immutable request/response DTOs and configuration value carriers. Do not use records for mutable JPA entities.
- Keep controllers focused on transport concerns; put business rules in application/service logic and persistence behavior in repositories or persistence components.
- **Packages:** preserve the existing repository organization. For a new project without established conventions, ask the user to choose feature/domain-first or layer-first packaging before implementing.
- Do not add interfaces solely to mirror every implementation class without a reason.

## Spring MVC and REST APIs
- Use appropriate HTTP methods and status codes. Common choices include `201 Created` for successful resource creation and `204 No Content` when success intentionally has no body.
- Validate incoming request bodies with Jakarta Bean Validation and `@Valid` where appropriate, including POST/PUT endpoints.
- Use explicit request/response DTOs when they create a stable API boundary; do not expose persistence entities as public contracts by default.
- Centralize REST exception mapping with `@RestControllerAdvice` where appropriate. Preserve useful diagnostic context internally without exposing secrets or stack traces.
- Keep error responses consistent. Spring Problem Details may be used when supported and aligned with the current contract; do not enable it if it silently changes existing API behavior.
- Consider pagination, sorting, idempotency, compatibility, and stable error semantics where relevant.
- Use `ResponseEntity` when explicit status/header control helps; it is not mandatory for every endpoint.

## Injection and configuration
- Use constructor injection for required dependencies.
- Prefer `@ConfigurationProperties` for related structured settings. Direct property injection may be appropriate for isolated values when clearer and consistent with the project.
- Keep secrets out of source control, logs, tests, and checked-in sample configuration.
- Do not change deployment defaults, virtual-thread settings, graceful shutdown, or Problem Details globally without confirming requirements and compatibility.

## Persistence and transactions
- Use Jakarta Persistence (`jakarta.persistence`), not `javax.persistence`.
- Keep persistence details out of controllers.
- Define transaction boundaries around business operations requiring atomicity. Use `@Transactional(readOnly = true)` for read service operations and `@Transactional` for writes, consistent with Piotr’s conventions; respect existing transaction boundaries, propagation, and side effects.
- Consider existing data, rollout order, backward compatibility, and rollback for migrations. Ask before destructive data operations.
- Enforce invariants at appropriate application and database layers.

## HTTP clients
- Prefer Spring `RestClient` for blocking outbound HTTP instead of the older `RestTemplate` API.
- Consider declarative `@HttpExchange` clients for stable service boundaries when they fit the actual Spring version.
- `WebClient` is not interchangeable with `RestClient`: use it when reactive/non-blocking behavior is an explicit requirement or the architecture already calls for it.
- Configure timeouts and define error, retry, and observability behavior based on integration semantics. Do not retry non-idempotent operations automatically without a safe idempotency strategy.
- Check current dependencies before adding another client library.

## Logging and operations
- Use the project's SLF4J conventions and parameterized messages; avoid `System.out.println` in application code.
- Never log credentials, tokens, secrets, or unnecessary personal data.
- Preserve exception causes, avoid swallowing errors, and avoid duplicate noisy stack traces.
- Add metrics, tracing, health checks, graceful shutdown, or resilience controls when confirmed operational needs require them; do not introduce broad infrastructure changes speculatively.

## Compatibility and verification
- Inspect build files, wrappers, toolchain declarations, modules, and CI before changes.
- Preserve dependency-management strategy and the project's Spring Boot 4.x patch line unless an approved change is needed.
- Never copy `pl.piomin.services` or source-specific artifact names into another project.
- Confirm referenced APIs exist in the actual Boot 4 version and dependencies.
- Add positive and negative tests for meaningful behavior, especially validation and error paths.


Source note: Adapted guidance from the supplied Personal ChatGPT skill pack; verify Spring-specific decisions against piomin/claude-ai-spring-boot, which remains authoritative.
