# Learnings and controlled self-improvement

When the user corrects an agent decision, or a build/test fails for a **repeatable** reason, append a concise factual record to `learnings/learnings.md`: timestamp, task context, symptom, root cause (if verified), correction, evidence and affected rule. Do not log secrets or sensitive data. A single incident may be logged; do not claim a repeated pattern without evidence.

When the same underlying cause recurs, propose a **unified diff against the exact reference file** and explain the evidence and expected regression test. **Never apply the patch without explicit user approval.** Document the optional mode `self_improvement.auto_apply=false` (default). The user may later request `true`, but until explicitly changed and confirmed it remains false; even then, do not bypass other approval gates. Maintain a regression case for approved fixes and report outcomes.
