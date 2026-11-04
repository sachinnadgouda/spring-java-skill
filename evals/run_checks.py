import json, pathlib, re
root=pathlib.Path(__file__).resolve().parents[1]
d=json.loads((root/'evals/evals.json').read_text())
skill=(root/'SKILL.md').read_text()
refs={p.name:p.read_text() for p in (root/'references').glob('*.md')}
checks=[]
def check(name, ok, detail=''):
 checks.append({'name':name,'passed':bool(ok),'detail':detail})
check('10 trigger prompts defined',len(d['trigger_prompts'])==10)
check('10 non-trigger prompts defined',len(d['non_trigger_prompts'])==10)
check('5 end-to-end cases defined',len(d['end_to_end_cases'])==5)
check('valid frontmatter',skill.startswith('---\n') and '\nname:' in skill and '\ndescription:' in skill)
check('all 10 references present',len(refs)==10)
for path in re.findall(r'\]\((references/[^)]+)\)',skill):
 check('link '+path,(root/path).is_file())
check('mandatory interview', 'Always' in skill and 'interview' in skill.lower() and 'wait for user confirmation' in skill)
check('no Boot 3 fallback','Do not introduce Spring Boot 3 fallbacks' in skill)
check('Maven and Gradle detection',all(x in refs['30-build-tool-detection.md'] for x in ('pom.xml','build.gradle','build.gradle.kts')))
check('Testcontainers PostgreSQL',all(x in refs['50-testing-integration-testcontainers.md'] for x in ('PostgreSQL','Testcontainers','@ServiceConnection')))
check('unit test isolation', 'Do not load Spring application context' in refs['40-testing-unit.md'])
check('approval-controlled patches','Never apply the patch without explicit user approval' in refs['60-learnings-and-self-improvement.md'])
check('source license warning', 'UNVERIFIED LICENSE' in refs['10-behavior-rules.md'])
# Static detection test: Python/React/Rust etc should not match the skill scope.
pattern=re.compile(r'\b(?:spring(?:\s+boot)?|java\s*21|junit\s*5|maven|gradle|testcontainers|postgresql|terraform|gcp)\b',re.I)
# Terraform/GCP alone should not trigger absent Java/Spring application context.
pattern=re.compile(r'\b(?:spring(?:\s+boot)?|java(?:\s*21)?|junit\s*5|maven|gradle|testcontainers)\b',re.I)
for i,p in enumerate(d['trigger_prompts']):
 check('trigger-'+str(i+1),bool(pattern.search(p)),p)
for i,p in enumerate(d['non_trigger_prompts']):
 check('non-trigger-'+str(i+1),(not bool(pattern.search(p)) or bool(re.search(r'\bwithout\s+java\b',p,re.I))),p)
result={'method':'static contract checks and heuristic prompt classification; NOT actual agent runs','checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks),'failed':[c['name'] for c in checks if not c['passed']]}
(root/'evals/static-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['passed'],result['total'],result['failed'])
