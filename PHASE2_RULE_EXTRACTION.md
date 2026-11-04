# Phase 2 — Rule extraction and conflict review

Status: **Phase 2 decisions recorded; awaiting explicit "go" for Phase 3. No Phase 3 work started.**

## Source rules (focused extraction)

The table records prescriptive statements from the selected source files; links are paths inside the unmodified `vendor/` snapshots. Some long files are summarized by their principal normative bullets rather than reproduced verbatim.

| Source | Topic | Rule (paraphrased) | Source file |
|---|---|---|---|
| Karpathy | Behavior | State your assumptions explicitly. If uncertain, ask. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | If multiple interpretations exist, present them - don't pick silently. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | If a simpler approach exists, say so. Push back when warranted. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | If something is unclear, stop. Name what's confusing. Ask. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | No features beyond what was asked. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | No abstractions for single-use code. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | No "flexibility" or "configurability" that wasn't requested. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | No error handling for impossible scenarios. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | If you write 200 lines and it could be 50, rewrite it. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | Don't "improve" adjacent code, comments, or formatting. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | Don't refactor things that aren't broken. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | Match existing style, even if you'd do it differently. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | If you notice unrelated dead code, mention it - don't delete it. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | Remove imports/variables/functions that YOUR changes made unused. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | Don't remove pre-existing dead code unless asked. | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | "Add validation" → "Write tests for invalid inputs, then make them pass" | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | "Fix the bug" → "Write a test that reproduces it, then make it pass" | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Karpathy | Behavior | "Refactor X" → "Ensure tests pass before and after" | `vendor/andrej-karpathy-skills/CLAUDE.md` |
| Piotr | Engineering / testing | **No Lombok** — write explicit constructors, getters, setters; use `LoggerFactory.getLogger()` for loggers | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **Constructor injection** — no `@Autowired` on fields | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **RestClient** over RestTemplate/WebClient for blocking HTTP calls | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **RestTestClient** with `@AutoConfigureRestTestClient` for integration tests | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **Testcontainers** with `@ServiceConnection` (not `@DynamicPropertySource`) | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **Jakarta Persistence** (not `javax.persistence`) | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **Java records** for DTOs (request/response objects) | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **Maven** for dependency management | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **Group ID**: `pl.piomin.services` | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **Artifact name** = parent directory name | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **Semantic versioning** — bump PATCH on each new version | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **Docker Compose** for local dependencies | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **CI pipeline** — generate CI/CD config; detect existing CI setup (`.github/workflows/`, `.circleci/`, `.gitlab-ci.yml`) and match it, or default to a sensible choice | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | **Tests** — always write both positive and negative test cases | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | Update `README.md` on each new version | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | Use latest Spring Boot 4.x and Java 21+ | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | `@Transactional(readOnly = true)` at service class level, `@Transactional` on mutating methods | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | `@Valid @RequestBody` on all POST/PUT endpoints | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | `@RestControllerAdvice` for global exception handling | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | Return `ResponseEntity` with proper status codes (201 Created, 204 No Content) | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | `@ConfigurationProperties` for type-safe config (no raw `@Value` for groups) | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | `@HttpExchange` interfaces for declarative HTTP clients | `vendor/claude-ai-spring-boot/skills/conventions/SKILL.md` |
| Piotr | Engineering / testing | Constructor injection (no field injection) | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | `@Valid` on all request bodies | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | `@Transactional` for multi-step writes | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | `@Transactional(readOnly = true)` for reads | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Type-safe config with `@ConfigurationProperties` | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Global exception handling with `@RestControllerAdvice` | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Externalize secrets (use env vars, not properties files) | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Field injection (`@Autowired` on fields) | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Skip input validation on endpoints | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Mix blocking and reactive code | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Store secrets in application.properties | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Use deprecated Spring Boot 2.x/3.x patterns | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Hardcode URLs, credentials, environment values | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Controller → Service → Repository | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Controller handles HTTP, validation | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Service handles business logic, transactions | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Repository handles data persistence | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Domain models independent of frameworks | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Use case driven design | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Dependency inversion (interfaces) | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | Clear boundaries between layers | `vendor/claude-ai-spring-boot/skills/spring-boot/SKILL.md` |
| Piotr | Engineering / testing | "write tests" / "add test coverage" / "test this" | `vendor/claude-ai-spring-boot/skills/testing-patterns/SKILL.md` |
| Piotr | Engineering / testing | Test failures or debugging test issues | `vendor/claude-ai-spring-boot/skills/testing-patterns/SKILL.md` |
| Piotr | Engineering / testing | Choosing between unit, slice, and integration tests | `vendor/claude-ai-spring-boot/skills/testing-patterns/SKILL.md` |
| Piotr | Engineering / testing | Building new Spring Boot 4.x applications (default to modern features) | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | Modernizing/refactoring existing Java code | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | User asks about records, sealed classes, pattern matching, virtual threads | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | JPA entities (Hibernate needs mutable objects, no-arg constructor) | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | Classes that need inheritance | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | Objects with mutable state | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | Runs each HTTP request on a virtual thread (Tomcat) | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | Makes `@Async` methods use virtual threads | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | Allows blocking I/O (JDBC, RestClient) to scale like reactive code | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | `synchronized` blocks holding across blocking calls (use `ReentrantLock` instead) | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | Thread-local heavy frameworks (check compatibility first) | `vendor/claude-ai-spring-boot/skills/java-modern/SKILL.md` |
| Piotr | Engineering / testing | User mentions "N+1 problem" / "too many queries" | `vendor/claude-ai-spring-boot/skills/jpa-patterns/SKILL.md` |
| Piotr | Engineering / testing | LazyInitializationException errors | `vendor/claude-ai-spring-boot/skills/jpa-patterns/SKILL.md` |
| Piotr | Engineering / testing | Questions about fetch strategies (EAGER vs LAZY) | `vendor/claude-ai-spring-boot/skills/jpa-patterns/SKILL.md` |
| Piotr | Engineering / testing | Transaction management issues | `vendor/claude-ai-spring-boot/skills/jpa-patterns/SKILL.md` |
| Piotr | Engineering / testing | Entity relationship design | `vendor/claude-ai-spring-boot/skills/jpa-patterns/SKILL.md` |
| Piotr | Engineering / testing | Query optimization | `vendor/claude-ai-spring-boot/skills/jpa-patterns/SKILL.md` |
| Siva | Engineering / testing | When developing Spring Boot applications using Spring MVC, Spring Data JPA, Spring Modulith, Spring Security | `vendor/sivalabs-agent-skills/skills/spring-boot/SKILL.md` |
| Siva | Engineering / testing | To create recommended Spring Boot package structure | `vendor/sivalabs-agent-skills/skills/spring-boot/SKILL.md` |
| Siva | Engineering / testing | To implement REST APIs, entities/repositories, service layer, modular monoliths | `vendor/sivalabs-agent-skills/skills/spring-boot/SKILL.md` |
| Siva | Engineering / testing | To use Thymeleaf view templates for building web applications | `vendor/sivalabs-agent-skills/skills/spring-boot/SKILL.md` |
| Siva | Engineering / testing | To write tests for REST APIs and Web applications | `vendor/sivalabs-agent-skills/skills/spring-boot/SKILL.md` |
| Siva | Engineering / testing | To write ArchUnit tests for testing architecture | `vendor/sivalabs-agent-skills/skills/spring-boot/SKILL.md` |
| Siva | Engineering / testing | To configure the recommended plugins and configurations to improve code quality, and testing while using Maven. | `vendor/sivalabs-agent-skills/skills/spring-boot/SKILL.md` |
| Siva | Engineering / testing | To use Spring Boot's Docker Compose support for local development | `vendor/sivalabs-agent-skills/skills/spring-boot/SKILL.md` |
| Siva | Engineering / testing | To create Taskfile for easier execution of common tasks while working with a Spring Boot application | `vendor/sivalabs-agent-skills/skills/spring-boot/SKILL.md` |
| Siva | Engineering / testing | **Assert behaviour, not implementation.** Verify *what* the code produces, not *how* it | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-unit-mocking.md` |
| Siva | Engineering / testing | **Use `verify()` sparingly** — mainly to prove a side effect happened (a charge was | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-unit-mocking.md` |
| Siva | Engineering / testing | A **pure unit test** (Mockito, no framework) can have ~100% coverage and still pass | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | A **whole-application smoke test** catches wiring/startup failures (a bad bean | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | A **sliced Spring test** boots the real framework around the components under test, so it | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | **~95% — sliced Spring tests.** `@SpringBootTest(classes = { … })` paired with a | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | **At least one smoke test**, plus at least one **request-level** end-to-end test. | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | **Some unit tests** for complex framework-free business logic — fine, just rarely | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | Consolidate common mocks into an `abstract BaseIntegrationTest`; don't sprinkle | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | Put shared config in `application-test.properties` + `@ActiveProfiles("test")`. | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | Avoid `@DirtiesContext` — it discards the cached context (10 uses ≈ 50–150s wasted); fix | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | Monitor with `<logger name="org.springframework.test.context.cache" level="DEBUG"/>`. | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | **Skip mock-based tests in native runs** with JUnit's `@DisabledInNativeImage` on the | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | **For a native-safe bean replacement, prefer `@TestBean`** (a static factory method | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Siva | Engineering / testing | This is another reason to lean on **real-component / Testcontainers** tests — the | `vendor/sivalabs-agent-skills/skills/spring-boot/references/testing-strategy.md` |
| Decebal | Engineering / testing | User says "create controller" / "add service" / "Spring Boot help" | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | Reviewing Spring Boot code | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | Setting up new Spring Boot project structure | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | Interface + Impl for testability | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | `@Transactional(readOnly = true)` at class level | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | `@Transactional` for write methods | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | Throw domain exceptions, not generic ones | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | Use mappers (MapStruct) for entity ↔ DTO conversion | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | Use derived queries when possible | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | `Optional` for single results | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | `existsBy` instead of `findBy` for existence checks | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | Avoid native queries unless necessary | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | Use `@EntityGraph` for fetch optimization | `vendor/claude-code-java/skills/spring-boot-patterns/SKILL.md` |
| Decebal | Engineering / testing | Writing new test classes | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | Reviewing/improving existing tests | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | User asks to "add tests" / "improve test coverage" | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | Code review mentions missing tests | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | One test at a time | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | Verify compilation after each | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | Run tests to validate | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | Refactor if needed | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | **Aim for**: 80%+ line coverage on core logic | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | **Focus on**: Business logic, complex algorithms, edge cases | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | **Skip**: Trivial getters/setters, POJOs, generated code | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | **Test**: Happy paths + error conditions + boundary cases | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | Complex business logic | `vendor/claude-code-java/skills/test-quality/SKILL.md` |
| Decebal | Engineering / testing | User asks "review this API" / "check REST endpoints" | `vendor/claude-code-java/skills/api-contract-review/SKILL.md` |
| Decebal | Engineering / testing | Before releasing API changes | `vendor/claude-code-java/skills/api-contract-review/SKILL.md` |
| Decebal | Engineering / testing | Reviewing PR with controller changes | `vendor/claude-code-java/skills/api-contract-review/SKILL.md` |
| Decebal | Engineering / testing | Checking backward compatibility | `vendor/claude-code-java/skills/api-contract-review/SKILL.md` |
| Decebal | Engineering / testing | Add optional field to request | `vendor/claude-code-java/skills/api-contract-review/SKILL.md` |
| Decebal | Engineering / testing | Add field to response | `vendor/claude-code-java/skills/api-contract-review/SKILL.md` |
| Decebal | Engineering / testing | Add new endpoint | `vendor/claude-code-java/skills/api-contract-review/SKILL.md` |
| Decebal | Engineering / testing | Add new optional query parameter | `vendor/claude-code-java/skills/api-contract-review/SKILL.md` |
| Rrezart | Engineering / testing | Spring Boot 4.x, Spring Framework 7, Java 21 | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Maven wrapper: `./mvnw` | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Jakarta EE 11, Jackson 3, and Boot 4 modular starters | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Use dedicated technology test starters rather than the classic test starter | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Build: `./mvnw verify` | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Unit tests: `./mvnw test` | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Single test: `./mvnw -Dtest=ClassName test` | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Native tests: use the configured native profile; do not invent one | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Inspect neighboring code and the dependency tree before choosing an API or starter. | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Keep controllers as adapters and transactions in application services. | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Use DTOs; do not expose Hibernate entities as external contracts. | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Use `tools.jackson` APIs for Jackson customization. | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Rrezart | Engineering / testing | Use `@MockitoBean`/`@MockitoSpyBean` and explicit test auto-configuration. | `vendor/spring-boot-skills/templates/spring-boot-4/AGENTS.md` |
| Jeffallan | Engineering / testing | Use field injection (`@Autowired` on fields) | `vendor/claude-skills/skills/spring-boot-engineer/SKILL.md` |
| Jeffallan | Engineering / testing | Skip input validation on API endpoints | `vendor/claude-skills/skills/spring-boot-engineer/SKILL.md` |
| Jeffallan | Engineering / testing | Use `@Component` when `@Service`/`@Repository`/`@Controller` applies | `vendor/claude-skills/skills/spring-boot-engineer/SKILL.md` |
| Jeffallan | Engineering / testing | Mix blocking and reactive code (e.g., calling `.block()` inside a WebFlux chain) | `vendor/claude-skills/skills/spring-boot-engineer/SKILL.md` |
| Jeffallan | Engineering / testing | Store secrets or credentials in `application.properties`/`application.yml` | `vendor/claude-skills/skills/spring-boot-engineer/SKILL.md` |
| Jeffallan | Engineering / testing | Hardcode URLs, credentials, or environment-specific values | `vendor/claude-skills/skills/spring-boot-engineer/SKILL.md` |
| Jeffallan | Engineering / testing | Use deprecated Spring Boot 2.x patterns (e.g., `WebSecurityConfigurerAdapter`) | `vendor/claude-skills/skills/spring-boot-engineer/SKILL.md` |
| Jeffallan | Engineering / testing | Write tests following AAA pattern (Arrange, Act, Assert) | `vendor/claude-skills/skills/spring-boot-engineer/references/testing.md` |
| Jeffallan | Engineering / testing | Use descriptive test names with @DisplayName | `vendor/claude-skills/skills/spring-boot-engineer/references/testing.md` |
| Jeffallan | Engineering / testing | Mock external dependencies, use real DB with Testcontainers | `vendor/claude-skills/skills/spring-boot-engineer/references/testing.md` |
| Jeffallan | Engineering / testing | Achieve 85%+ code coverage | `vendor/claude-skills/skills/spring-boot-engineer/references/testing.md` |
| Jeffallan | Engineering / testing | Test happy path and edge cases | `vendor/claude-skills/skills/spring-boot-engineer/references/testing.md` |
| Jeffallan | Engineering / testing | Use @Transactional for test data cleanup | `vendor/claude-skills/skills/spring-boot-engineer/references/testing.md` |
| Jeffallan | Engineering / testing | Separate unit tests from integration tests | `vendor/claude-skills/skills/spring-boot-engineer/references/testing.md` |
| Jeffallan | Engineering / testing | Use parameterized tests for multiple scenarios | `vendor/claude-skills/skills/spring-boot-engineer/references/testing.md` |
| Jeffallan | Engineering / testing | Test security rules and validation | `vendor/claude-skills/skills/spring-boot-engineer/references/testing.md` |
| Jeffallan | Engineering / testing | Keep tests fast and independent | `vendor/claude-skills/skills/spring-boot-engineer/references/testing.md` |
| Awesome Copilot | Engineering / testing | **Build Tool:** Use Maven (`pom.xml`) or Gradle (`build.gradle`) for dependency management. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **Starters:** Use Spring Boot starters (e.g., `spring-boot-starter-web`, `spring-boot-starter-data-jpa`) to simplify dependency management. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **Package Structure:** Organize code by feature/domain (e.g., `com.example.app.order`, `com.example.app.user`) rather than by layer (e.g., `com.example.app.controller`, `com.example.app.service`). | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **Constructor Injection:** Always use constructor-based injection for required dependencies. This makes components easier to test and dependencies explicit. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **Immutability:** Declare dependency fields as `private final`. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **Component Stereotypes:** Use `@Component`, `@Service`, `@Repository`, and `@Controller`/`@RestController` annotations appropriately to define beans. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **Externalized Configuration:** Use `application.yml` (or `application.properties`) for configuration. YAML is often preferred for its readability and hierarchical structure. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **Type-Safe Properties:** Use `@ConfigurationProperties` to bind configuration to strongly-typed Java objects. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **Profiles:** Use Spring Profiles (`application-dev.yml`, `application-prod.yml`) to manage environment-specific configurations. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **Secrets Management:** Do not hardcode secrets. Use environment variables, or a dedicated secret management tool like HashiCorp Vault or AWS Secrets Manager. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **RESTful APIs:** Design clear and consistent RESTful endpoints. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **DTOs (Data Transfer Objects):** Use DTOs to expose and consume data in the API layer. Do not expose JPA entities directly to the client. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Awesome Copilot | Engineering / testing | **Validation:** Use Java Bean Validation (JSR 380) with annotations (`@Valid`, `@NotNull`, `@Size`) on DTOs to validate request payloads. | `vendor/awesome-copilot/skills/java-springboot/SKILL.md` |
| Matt Pocock | Interview | **Anything, anywhere.** Use `grill-me`. It needs no repo and writes no files, and the subject doesn't have to be code. | `vendor/skills/docs/productivity/grill-me.md` |
| Matt Pocock | Interview | You disagree with something. A session with no pushback from you is a session you didn't need. | `vendor/skills/docs/productivity/grill-me.md` |
| Matt Pocock | Interview | Questions arrive in a few rounds, not one at a time for a long time, and later rounds clearly build on what you said earlier. | `vendor/skills/docs/productivity/grill-me.md` |
| Matt Pocock | Interview | You end up somewhere you didn't expect, because a question showed you a decision you had been making without noticing. | `vendor/skills/docs/productivity/grill-me.md` |
| Matt Pocock | Interview | At the end you could defend each choice to someone who wasn't there. | `vendor/skills/docs/productivity/grill-me.md` |
| Matt Pocock | Interview | A round arrives as a numbered list, each question with its recommendation on a separate `➡️` line, and you can answer the whole round by number. | `vendor/skills/docs/productivity/grilling.md` |
| Matt Pocock | Interview | Nothing in a round needs another question in the same round answered first. | `vendor/skills/docs/productivity/grilling.md` |
| Matt Pocock | Interview | Later rounds ask things the first round could not have asked. | `vendor/skills/docs/productivity/grilling.md` |
| Matt Pocock | Interview | It goes and looks facts up (reading files, dispatching a sub-agent) rather than asking you something it could have found out. | `vendor/skills/docs/productivity/grilling.md` |
| Matt Pocock | Interview | Research running in the background does not stall the round; only the questions that depend on it wait. | `vendor/skills/docs/productivity/grilling.md` |
| Matt Pocock | Interview | It stops at the end and asks you to confirm the understanding is shared, instead of starting work. | `vendor/skills/docs/productivity/grilling.md` |
| Matt Pocock | Interview | Question count stays high while round count stays low. | `vendor/skills/docs/productivity/grilling.md` |

## Conflict decisions already determined by authority

| Topic | Competing guidance | Resolution |
|---|---|---|
| Lombok | Piotr prohibits; Jeffallan example permits Lombok | **No Lombok** (Piotr) |
| Dependency injection | Constructor injection widely agreed; Piotr explicitly prohibits field injection | **Constructor injection** (Piotr) |
| Blocking REST client | Piotr selects `RestClient`; others mention alternatives | **RestClient** for blocking requests (Piotr) |
| HTTP integration test client | Piotr selects `RestTestClient`; other sources use MockMvc or other clients | **RestTestClient** for relevant Boot 4 integration tests (Piotr) |
| Testcontainers configuration | Piotr selects `@ServiceConnection` rather than `@DynamicPropertySource` | **@ServiceConnection** where supported (Piotr) |
| Build tool | Piotr prescribes Maven; user explicitly requires existing repo detection | **User requirement overrides**: Maven or Gradle as detected |
| Group ID | Piotr prescribes `pl.piomin.services`; user explicitly prohibits copying it | **User requirement overrides**: preserve project group ID |
| Spring version | Jeffallan examples use Boot 3; user targets Boot 4 only | **Boot 4 / Java 21+ only** |

## Finalized user decisions (2026-10-26)

| Topic | Confirmed decision | Implementation consequence for Phase 3 |
|---|---|---|
| Terraform reference | **Include** | Add a separate Terraform reference file; do not assume a provider or deployment architecture beyond inspected project context. |
| GCP reference | **Include** | Add a separate Google Cloud Platform reference file; do not presume a specific GCP service. |
| General PostgreSQL reference | **Include** | Add a separate PostgreSQL development reference in addition to the mandatory PostgreSQL/Testcontainers integration-testing reference. |
| Package organization | **Follow existing repository structure** | Inspect the project first; preserve its feature-first or layer-first organization, rather than imposing a new one. For a new project with no established structure, ask before choosing. |
| Database migrations | **Use existing migration tool** | Detect the project's migration tooling and follow it; if none is present and a migration is required, ask before selecting a tool. |
| Testing scope | **Risk-based** | Select unit, slice, and integration tests according to change risk; retain positive and negative cases and PostgreSQL Testcontainers when applicable. |

### Approval gate

These six choices resolve the outstanding Phase 2 questions. Phase 3 remains **not started** until the user explicitly replies **go**.

## Constraints carried forward

- Interview always first, inspect code before asking, batch many questions, summarize and await confirmation before code.
- Record repeatable corrections/failures in learnings; propose exact diffs on recurrence; never auto-apply.
- This report is a review artifact, not the final merged skill.
- Source archive provenance is based on uploaded snapshots; Git commits remain unverified.
