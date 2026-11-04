# Merge changelog and review

## Sources
- Structural base: supplied `spring-java-skill-final.zip`.
- Interview and expanded Spring guidance: supplied `spring-java-skill-phase5-final-audit.zip`, edited to preserve approved authority and package decisions.

## Changes
- Replaced `references/00-interview-grill-me.md` with the more comprehensive interview and pre-approval safety procedure.
- Replaced `references/20-spring-boot-4-java-21.md` with the expanded Spring guidance, overriding its new-project feature-first default to require a user decision, and retaining Piotr's read/write transaction convention.
- Added explicit pre-approval no-mutation and new-project package-choice requirements to `SKILL.md`.
- Preserved the other eight references, eval scripts/results, vendor files, license report and NOTICE from the base.

## Limitations
- No live coding-agent comparisons were run; earlier static checks do not prove agent behavior.
- Exact source Git commits remain unverified; the Karpathy source license is unverified.
- No license is newly asserted for the merged pack. Confirm redistribution terms and copyright ownership before publication, especially if distributing vendor snapshots.
- The two enhanced references have not been validated against every upstream Spring source rule at line level; unresolved discrepancies require user review, not silent precedence changes.
