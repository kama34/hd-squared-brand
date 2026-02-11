# Error Learning & Memory Skill

## Overview

**Purpose**: Автоматическое обучение на ошибках через создание структурированной документации об ошибках, их причинах и решениях. Превращает каждую ошибку в институциональное знание, доступное для будущих проектов.

**Target Users**: CTO (primary)

**Capabilities**:
- Автоматическое документирование ошибок после исправления
- Категоризация ошибок (Compilation / Runtime / Deployment / Security / Performance)
- Анализ root cause и prevention strategies
- Построение knowledge base об ошибках для всей команды
- Интеграция с agent memory для persistent learning

## Required Tools

- `Write` - Create error documentation files
- `Read` - Read existing error logs, code context
- `Grep` - Search for similar errors in history
- `Bash` - Get error logs from CI/CD, test output
- `mcp__ide__getDiagnostics` - Get compiler/linter errors

## Core Workflow

### Trigger Points (CTO проактивно запускает skill)

1. **После исправления compilation error** - компилятор снова работает
2. **После исправления failed tests** - тесты зеленые
3. **После исправления deployment error** - deployment успешен
4. **После исправления security vulnerability** - vulnerability устранена
5. **После исправления performance issue** - метрики улучшены

### Process

```
1. [ERROR OCCURS] → CTO fixes error
2. [ERROR FIXED] → CTO triggers: "Документируй исправленную ошибку"
3. [SKILL ANALYZES]:
   - Error message/stack trace
   - Files changed to fix
   - Root cause analysis
   - Prevention strategy
4. [SKILL CREATES] → .claude/agent-memory/cto/errors/YYYY-MM-DD-[category]-[short-name].md
5. [SKILL UPDATES] → .claude/agent-memory/cto/error-index.md (searchable index)
```

## Error Document Template

```markdown
# Error: [Short Description]

**Date**: YYYY-MM-DD
**Startup**: [Sales AI / Project X]
**Category**: [Compilation / Runtime / Deployment / Security / Performance / Dependencies]
**Severity**: [Critical / High / Medium / Low]

## Original Error

\```
[Full error message with stack trace]
\```

**Affected Files**:
- file1.ts:123
- file2.py:45

## Context

**What was attempted**:
[Описание что пытались сделать когда произошла ошибка]

**Environment**:
- OS: Windows / Linux / macOS
- Language/Framework: Node.js 20 / Python 3.11 / React 18
- Build Tool: Vite / Webpack / Docker
- CI/CD: GitHub Actions / GitLab CI

## Root Cause

**Analysis**:
[Детальный анализ почему возникла ошибка]

**Contributing Factors**:
- Factor 1 (e.g., missing dependency)
- Factor 2 (e.g., incorrect configuration)
- Factor 3 (e.g., environment mismatch)

## Solution Applied

**Changes Made**:

1. **File: path/to/file1.ts**
\```typescript
// BEFORE (broken)
[code before]

// AFTER (fixed)
[code after]
\```

2. **File: config/vite.config.ts**
\```typescript
// Changed setting X to Y
[code change]
\```

**Commands Run**:
\```bash
npm install missing-package
npm run build
\```

**Result**: [Tests pass / Build successful / Deployment successful]

## Prevention

**How to avoid in the future**:

1. **Check X before Y** - [Specific check to perform]
2. **Add validation** - [Validation to add to CI/CD]
3. **Update documentation** - [What docs need updating]
4. **Automate check** - [How to automate prevention]

**CI/CD Integration**:
\```yaml
# Add to .github/workflows/ci.yml
- name: Prevent error [short-name]
  run: [validation command]
\```

## Related Errors

**Similar past errors**:
- [Link to 2026-01-15-deployment-docker-image-lowercase.md]
- [Link to 2025-12-20-compilation-missing-types.md]

**Patterns observed**:
- This is the 3rd time we had Docker image naming issues
- Consider creating pre-flight checklist for deployments

## Lessons Learned

**Technical Insights**:
- [Key technical learning]

**Process Improvements**:
- [What to change in workflow]

**Documentation Gaps**:
- [What was missing from docs that led to error]

## Tags

`deployment` `docker` `ci-cd` `Sales-AI` `vite` `image-naming`

---

**Created by**: CTO agent
**Skill**: error-learning
**Last Updated**: YYYY-MM-DD
```

## Usage Examples

### Example 1: Document Compilation Error

**Trigger**: TypeScript compilation error fixed

**User says**: "Документируй исправленную ошибку с TypeScript типами"

**Process**:

1. **Read recent git diff** to see what was changed:
```bash
git diff HEAD~1 HEAD
```

2. **Capture error from build logs**:
```bash
cat build-error.log
# or
npm run build 2>&1 | tee build.log
```

3. **Analyze files changed**:
```bash
git show --stat HEAD
```

4. **Create error document**:
```markdown
# Error: Missing Type Definition for User.profile

**Date**: 2026-02-11
**Startup**: Sales AI
**Category**: Compilation
**Severity**: Medium

## Original Error

\```
src/components/UserProfile.tsx:23:15 - error TS2339: Property 'profile' does not exist on type 'User'.

23   return user.profile.name;
                ~~~~~~~~

Found 1 error in src/components/UserProfile.tsx:23
\```

**Affected Files**:
- src/components/UserProfile.tsx:23
- src/types/User.ts

## Root Cause

**Analysis**:
TypeScript interface `User` did not include `profile` property. Code assumed the property existed based on backend API response, but TypeScript types were not updated after backend schema change.

**Contributing Factors**:
- Backend added `profile` field to User model
- Frontend types not synced with backend schema
- No automated type generation from backend schema

## Solution Applied

**Changes Made**:

1. **File: src/types/User.ts**
\```typescript
// BEFORE
interface User {
  id: string;
  email: string;
  name: string;
}

// AFTER
interface User {
  id: string;
  email: string;
  name: string;
  profile: {
    name: string;
    avatar?: string;
    bio?: string;
  };
}
\```

**Result**: Compilation successful, TypeScript errors resolved.

## Prevention

**How to avoid in the future**:

1. **Sync types with backend** - Use code generation (e.g., openapi-typescript)
2. **Add CI check** - Fail build if types diverge from API schema
3. **Document schema changes** - Backend must notify frontend of schema changes

**CI/CD Integration**:
\```yaml
# .github/workflows/ci.yml
- name: Validate TypeScript types match API schema
  run: npm run validate-types
\```

## Tags

`typescript` `compilation` `types` `Sales-AI` `frontend`
```

5. **Save to agent memory**:
```bash
Write D:/Drive/Wiki/.claude/agent-memory/cto/errors/2026-02-11-compilation-missing-user-profile-type.md
```

6. **Update error index**:
```bash
# Append to error-index.md
- [2026-02-11 - Missing User.profile Type](errors/2026-02-11-compilation-missing-user-profile-type.md) - TypeScript, Compilation
```

### Example 2: Document Deployment Error

**Trigger**: Docker deployment error fixed (Sales AI real example)

**User says**: "Документируй исправленную ошибку с Docker image"

**Process**:

1. **Read deployment logs**:
```bash
# From GitHub Actions or local docker build
cat .github/workflows/deploy-website.yml
docker build -t test . 2>&1
```

2. **Identify error**:
```
ERROR: invalid reference format: repository name (SalesAI-Website) must be lowercase
```

3. **Analyze fix**:
```bash
git diff HEAD~1 .github/workflows/deploy-website.yml
```

4. **Create error document**:
```markdown
# Error: Docker Image Name Must Be Lowercase

**Date**: 2026-02-10
**Startup**: Sales AI
**Category**: Deployment
**Severity**: High (blocks deployment)

## Original Error

\```
ERROR [internal] load metadata for docker.io/library/SalesAI-Website:latest
> [internal] load metadata for docker.io/library/SalesAI-Website:latest:
ERROR: invalid reference format: repository name (SalesAI-Website) must be lowercase
\```

**Affected Files**:
- .github/workflows/deploy-website.yml:45

## Context

**What was attempted**:
Setting up CI/CD pipeline for Sales AI website deployment. Used startup name "SalesAI-Website" directly as Docker image name.

**Environment**:
- Docker 24.0
- GitHub Actions
- nginx base image

## Root Cause

**Analysis**:
Docker enforces strict naming conventions: image names must be lowercase. Used project directory name "SalesAI-Website" (with capitals) directly as image name without transformation.

**Contributing Factors**:
- Docker naming convention not checked before setup
- No validation in CI/CD pipeline for image names
- Project directory uses PascalCase naming

## Solution Applied

**Changes Made**:

1. **File: .github/workflows/deploy-website.yml**
\```yaml
# BEFORE
image: SalesAI-Website

# AFTER
image: salesai-website  # Lowercase
\```

Alternative solution using shell transformation:
\```yaml
image: $(echo "SalesAI-Website" | tr '[:upper:]' '[:lower:]')
\```

**Result**: Docker build successful, image tagged correctly.

## Prevention

**How to avoid in the future**:

1. **Always lowercase Docker images** - Add to CTO checklist
2. **Validate in CI** - Add pre-flight check:
   \```bash
   if [[ "$IMAGE_NAME" =~ [A-Z] ]]; then
     echo "ERROR: Docker image name must be lowercase"
     exit 1
   fi
   \```
3. **Use linter** - hadolint checks Dockerfile best practices
4. **Document in devops-cicd skill** - Add to Docker best practices

**CI/CD Integration**:
\```yaml
- name: Validate Docker image name
  run: |
    if [[ "${{ env.IMAGE_NAME }}" =~ [A-Z] ]]; then
      echo "ERROR: Docker image must be lowercase"
      exit 1
    fi
\```

## Related Errors

**Similar past errors**:
- None (first Docker deployment for this startup)

**Patterns observed**:
- Need Docker deployment checklist for new projects
- Consider creating starter template with validated configs

## Lessons Learned

**Technical Insights**:
- Docker image naming: lowercase, alphanumeric + dash/underscore/dot only
- GitHub Actions doesn't validate image names before build

**Process Improvements**:
- Add pre-deployment validation step to CI/CD
- Create reusable GitHub Actions workflow with built-in checks

**Documentation Gaps**:
- devops-cicd skill should include Docker naming rules
- Need deployment checklist in CTO agent memory

## Tags

`docker` `deployment` `ci-cd` `github-actions` `Sales-AI` `naming-convention`
```

5. **Save and index**

### Example 3: Document Runtime Error

**Trigger**: JavaScript runtime error in production fixed

**User says**: "Документируй исправленную runtime ошибку с null reference"

**Process**:

1. **Read error logs from production**:
```bash
# From server logs or error monitoring (Sentry, LogRocket)
grep "TypeError" production.log
```

2. **Error**:
```
TypeError: Cannot read property 'length' of null
  at formatList (app.js:234:15)
```

3. **Create error document**:
```markdown
# Error: Null Reference in formatList Function

**Date**: 2026-02-11
**Startup**: Sales AI
**Category**: Runtime
**Severity**: High (crashes user session)

## Original Error

\```
TypeError: Cannot read property 'length' of null
  at formatList (app.js:234:15)
  at UserDashboard (app.js:456:10)
  at renderComponent (framework.js:123:5)
\```

**Affected Files**:
- src/utils/formatList.js:234
- src/components/UserDashboard.tsx:456

## Root Cause

**Analysis**:
Function `formatList()` expected array but received `null` when user had no data. Code did not handle null/undefined case.

**Contributing Factors**:
- API returns `null` for empty lists (should return `[]`)
- Frontend did not validate input before processing
- No TypeScript type guards to prevent null

## Solution Applied

**Changes Made**:

1. **File: src/utils/formatList.js**
\```javascript
// BEFORE
function formatList(items) {
  return items.length > 0 ? items.join(', ') : 'None';
}

// AFTER
function formatList(items) {
  if (!items || !Array.isArray(items)) {
    return 'None';
  }
  return items.length > 0 ? items.join(', ') : 'None';
}
\```

2. **Backend fix: Ensure API returns empty array**
\```python
# api/users.py
def get_user_items(user_id):
    items = db.query(...)
    return items or []  # Never return None
\```

**Result**: Error no longer occurs, graceful degradation when no data.

## Prevention

**How to avoid in the future**:

1. **Always validate inputs** - Check null/undefined before operations
2. **TypeScript strict mode** - Enable `strictNullChecks` in tsconfig.json
3. **Backend contract** - API should return `[]` not `null` for empty lists
4. **Add tests** - Test edge cases (null, undefined, empty array)

**Test case to add**:
\```javascript
describe('formatList', () => {
  it('handles null input', () => {
    expect(formatList(null)).toBe('None');
  });

  it('handles undefined input', () => {
    expect(formatList(undefined)).toBe('None');
  });

  it('handles empty array', () => {
    expect(formatList([])).toBe('None');
  });
});
\```

## Tags

`javascript` `runtime` `null-reference` `Sales-AI` `error-handling`
```

## Integration with CTO Workflow

### CTO Agent Prompts to Trigger Skill

**Add to `.github/agents/cto.agent.md`** (в секцию "Операционные процедуры"):

```markdown
### После исправления ошибки

**Каждый раз после исправления ошибки (compilation, runtime, deployment, security):**

1. **Проверить что ошибка действительно исправлена**:
   - Компиляция успешна / Тесты зеленые / Deployment работает
2. **Запустить error-learning skill**:
   - Фраза: "Документируй исправленную ошибку"
   - Или автоматически при commit message содержит "fix:", "bug:", "error:"
3. **Skill создаст документ** в `.claude/agent-memory/cto/errors/`
4. **Review документ** - убедиться что root cause корректен
5. **Commit error doc** вместе с fix:
   ```bash
   git add .claude/agent-memory/cto/errors/
   git commit -m "docs: document [error-type] error and solution"
   ```
```

### Automatic Triggers (Context-Based)

CTO agent должен **сам определять** когда запускать skill по контексту:

**Trigger patterns**:
- User says: "fix", "исправь", "resolve", "fixed bug"
- Commit message contains: "fix:", "bug:", "error:", "resolve:"
- After successful build following failed build
- After deployment success following deployment failure

**CTO internal prompt** (добавить в agent.md):
```markdown
### Проактивное документирование ошибок

**Когда видишь что ошибка исправлена:**

1. **Определить категорию**:
   - Compilation (TypeScript errors, build failures)
   - Runtime (crashes, exceptions)
   - Deployment (Docker, CI/CD, infrastructure)
   - Security (vulnerabilities, OWASP)
   - Performance (slow queries, high latency)
   - Dependencies (npm/pip package issues)

2. **Собрать контекст**:
   - Git diff (что изменилось для fix)
   - Error logs (оригинальная ошибка)
   - Build/test output (подтверждение что fixed)

3. **Запустить error-learning skill**:
   - "Используя error-learning skill, документируй ошибку [category]: [short-description]"

4. **Результат**:
   - Создан файл в `.claude/agent-memory/cto/errors/YYYY-MM-DD-[category]-[name].md`
   - Обновлен error-index.md
   - Знание сохранено для будущих проектов
```

## Error Index Structure

**File**: `.claude/agent-memory/cto/error-index.md`

```markdown
# CTO Error Learning Index

Searchable index of all documented errors. Updated automatically by error-learning skill.

## Categories

- [Compilation](#compilation) (5 errors)
- [Runtime](#runtime) (3 errors)
- [Deployment](#deployment) (7 errors)
- [Security](#security) (2 errors)
- [Performance](#performance) (1 error)
- [Dependencies](#dependencies) (4 errors)

---

## Compilation

| Date | Error | Tags | Severity |
|------|-------|------|----------|
| 2026-02-11 | [Missing User.profile Type](errors/2026-02-11-compilation-missing-user-profile-type.md) | typescript, types | Medium |
| 2026-02-05 | [Circular Dependency in Modules](errors/2026-02-05-compilation-circular-dependency.md) | javascript, imports | High |

## Deployment

| Date | Error | Tags | Severity |
|------|-------|------|----------|
| 2026-02-10 | [Docker Image Name Must Be Lowercase](errors/2026-02-10-deployment-docker-image-lowercase.md) | docker, ci-cd | High |
| 2026-02-09 | [Vite Build Output Directory Mismatch](errors/2026-02-09-deployment-vite-dist-mismatch.md) | vite, docker | High |
| 2026-02-08 | [Missing package-lock.json in Docker](errors/2026-02-08-deployment-package-lock-missing.md) | npm, docker | Medium |

## Runtime

| Date | Error | Tags | Severity |
|------|-------|------|----------|
| 2026-02-11 | [Null Reference in formatList](errors/2026-02-11-runtime-null-reference-formatlist.md) | javascript, null | High |

---

**Total Errors Documented**: 22
**Last Updated**: 2026-02-11
**Most Common Category**: Deployment (7 errors)
**Most Common Tags**: docker (5), typescript (4), ci-cd (4)
```

## Integration with Other Skills

### tech-audit
- tech-audit finds security vulnerability → error-learning documents fix
- Error logs inform future security audits (patterns of vulnerabilities)

### devops-cicd
- Deployment errors → Improve CI/CD workflows
- Document common deployment issues in devops-cicd skill

### frontend-development / backend-development
- Runtime/compilation errors → Update best practices in respective skills
- TypeScript type errors → Improve type safety guidelines

### board-reporting
- Error metrics for Board (number of critical errors, MTTR)
- Downtime incidents → Board post-mortems from error logs

## Best Practices

### 1. Document Immediately After Fix

**❌ BAD** - Wait days/weeks to document:
> "I'll document this later when I have time"

**✅ GOOD** - Document while context fresh:
> "Fix committed, now run error-learning skill to capture learnings"

**Why**: Context fades quickly. Document while you remember root cause.

### 2. Include Specific Code Changes

**❌ BAD** - Vague description:
> "Fixed the bug by changing the config"

**✅ GOOD** - Exact code changes:
> \```yaml
> # BEFORE
> image: SalesAI-Website
>
> # AFTER
> image: salesai-website
> \```

**Why**: Specific changes help future developers understand exact fix.

### 3. Analyze Root Cause, Not Just Symptoms

**❌ BAD** - Symptom-level:
> "Error was: image name invalid. Fixed by changing name."

**✅ GOOD** - Root cause:
> "Docker enforces lowercase image names. Our project uses PascalCase directory names. Need naming convention transformation in CI/CD."

**Why**: Root cause analysis prevents recurrence.

### 4. Add Prevention Steps

**❌ BAD** - No prevention:
> "Fixed the error. Done."

**✅ GOOD** - Prevention strategy:
> "To prevent: Add CI validation for image names, update devops checklist, document in skill."

**Why**: Prevention reduces future errors.

### 5. Tag Errors for Searchability

**✅ GOOD** - Comprehensive tags:
> Tags: `docker` `deployment` `ci-cd` `github-actions` `Sales-AI` `naming-convention`

**Why**: Easy to find similar past errors.

## Metrics & Tracking

### Error Learning Metrics (for CTO)

Track in `.claude/agent-memory/cto/error-metrics.md`:

```markdown
# Error Learning Metrics

**Period**: 2026 Q1

## Error Volume

- Total errors documented: 22
- By category:
  - Deployment: 7 (32%)
  - Compilation: 5 (23%)
  - Dependencies: 4 (18%)
  - Runtime: 3 (14%)
  - Security: 2 (9%)
  - Performance: 1 (4%)

## Time to Document

- Average: 15 minutes per error
- Fastest: 5 minutes (simple compilation error)
- Slowest: 45 minutes (complex deployment issue)

## Recurrence Rate

- Errors repeated: 3 / 22 (14%)
- Most repeated: Docker-related (3 times)
- **Action**: Create Docker pre-flight checklist

## Prevention Effectiveness

- Errors prevented by past documentation: 8
- CI/CD checks added from error docs: 5
- Skills updated from learnings: 3 (devops-cicd, frontend-development, tech-audit)

## Top Error Patterns

1. **Docker deployment** (7 errors) → Need better Docker skill
2. **TypeScript types** (4 errors) → Need automated type generation
3. **CI/CD config** (4 errors) → Need config validation

**Recommendation**: Focus on Docker and TypeScript in next sprint.
```

## Troubleshooting

### Problem: "Too time-consuming to document every error"

**Solution**:
- Focus on **non-trivial errors** (took >30 min to fix)
- Skip typos and obvious mistakes
- Document patterns, not individual instances
- Use templates to speed up (this skill provides templates)

### Problem: "Don't remember details days later"

**Solution**:
- Document **immediately** after fix (while in flow)
- Use git history to reconstruct: `git log`, `git diff`
- Read error logs saved during debugging
- Ask team members if collaborative fix

### Problem: "Error documents cluttering agent memory"

**Solution**:
- Archive old errors (>6 months) to `archive/` subdirectory
- Keep error-index.md updated (easy search)
- Tag errors properly for filtering
- Review quarterly: Are error patterns addressed?

## Version History

- **2026-02-11**: Created error-learning skill for CTO
  - Semi-automatic workflow (CTO triggers after fix)
  - Structured error documentation template
  - Integration with agent memory
  - Error index for searchability
  - Metrics tracking for continuous improvement

## Related Files

- `.claude/agent-memory/cto/errors/` - Error documentation directory
- `.claude/agent-memory/cto/error-index.md` - Searchable error index
- `.claude/agent-memory/cto/error-metrics.md` - Error learning metrics
- `.github/agents/cto.agent.md` - CTO agent configuration (add triggers here)

---

**Next Steps After Creating This Skill**:

1. Update `.github/agents/cto.agent.md` with error-learning triggers
2. Create initial `error-index.md` in agent memory
3. Document first error using this skill (test workflow)
4. Add to `.claude/skills/ALL_SKILLS_REFERENCE.md`
