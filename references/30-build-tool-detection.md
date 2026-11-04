# Build tool and project detection

Inspect repository root and modules before any commands. `pom.xml` indicates Maven; `build.gradle` or `build.gradle.kts` indicates Gradle. If both exist, identify the actual active build from README/CI/wrappers; ask if ambiguous. Use checked-in wrappers (`./mvnw`, `./gradlew`) when executable, otherwise installed tool if available and confirmed. Respect multi-module structure.

Maven examples: `./mvnw test`, `./mvnw verify`, `./mvnw -Dtest=ExampleTest test`.
Gradle examples: `./gradlew test`, `./gradlew build`, `./gradlew test --tests 'package.ExampleTest'`. For integration-test tasks use the repository's configured integration test goal/task, not a guessed one. Read toolchains, profiles and plugins before choosing commands. Never overwrite group IDs, versions, plugins or wrapper files just to conform to a sample. Report exact commands and results.

Sources: github/awesome-copilot, skills/java-springboot/SKILL.md; rrezartprebreza/spring-boot-skills, templates/spring-boot-4/AGENTS.md; user-approved override of Piotr's Maven-only preference.
