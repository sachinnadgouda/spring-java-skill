# Unit and risk-based testing

Use JUnit Jupiter (JUnit 5) and Mockito for pure unit tests. **Do not load Spring application context** for pure units. Instantiate the subject directly, mock collaborators at boundaries, assert observable behavior rather than private implementation. Cover success, failure, boundary and validation cases relevant to risk; prefer parameterized tests for repeated cases. For a bug, first add a regression test that fails for the reported defect. Avoid arbitrary coverage percentage mandates: choose unit, slice or integration scope by actual risk, while including positive and negative cases. Preserve project naming/test conventions; avoid flakiness, shared state and unnecessary sleeps. Verify tests with the detected build tool.

Sources: piomin/claude-ai-spring-boot testing patterns; decebals/claude-code-java test-quality; Jeffallan/claude-skills spring-boot-engineer testing; user-approved risk-based scope.
