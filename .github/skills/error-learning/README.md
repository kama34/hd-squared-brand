# Error Learning Skill - Quick Reference

## Purpose

Превратить каждую ошибку в институциональное знание через автоматическое документирование.

## Quick Start

### 1. After Fixing Error

**Trigger phrase**:
```
"Документируй исправленную ошибку [category]: [short-description]"
```

**Examples**:
```
"Документируй исправленную ошибку Deployment: Docker image lowercase"
"Документируй исправленную ошибку Compilation: Missing TypeScript types"
"Документируй исправленную ошибку Runtime: Null reference in formatList"
```

### 2. Skill Creates Error Document

**Location**: `.claude/agent-memory/cto/errors/YYYY-MM-DD-[category]-[name].md`

**Structure**:
- Original error message & stack trace
- Root cause analysis
- Solution applied (code changes)
- Prevention strategy (how to avoid)
- Tags for searchability

### 3. Skill Updates Index

**File**: `.claude/agent-memory/cto/error-index.md`

Searchable index by:
- Category (Compilation, Runtime, Deployment, Security, Performance, Dependencies)
- Tags (`docker`, `typescript`, `ci-cd`, etc.)
- Startup name (`Sales AI`, etc.)
- Date

## Categories

- **Compilation** - TypeScript errors, build failures
- **Runtime** - Crashes, exceptions, null references
- **Deployment** - Docker, CI/CD, infrastructure
- **Security** - Vulnerabilities, OWASP issues
- **Performance** - Slow queries, high latency
- **Dependencies** - npm/pip package issues

## Automatic Triggers (CTO Agent)

CTO agent automatically runs this skill when:
- Commit message contains: `fix:`, `bug:`, `error:`, `resolve:`
- After successful build following failed build
- After deployment success following deployment failure
- User says: "fixed", "solved", "resolved error"

## Integration with Workflow

```
1. [ERROR OCCURS] → CTO fixes error
2. [ERROR FIXED] → CTO triggers: "Документируй исправленную ошибку"
3. [SKILL CREATES] → Error document in agent memory
4. [SKILL UPDATES] → Error index for searchability
5. [CTO COMMITS] → Both fix and error doc together
```

## Example Error Document

See: `.claude/agent-memory/cto/errors/EXAMPLE-2026-02-10-deployment-docker-image-lowercase.md`

## Benefits

- Build institutional knowledge across projects
- Prevent error recurrence through documented prevention steps
- Faster debugging (check if we've seen this before)
- Track error patterns (which categories are most common)
- Onboard new team members faster (learn from past mistakes)

## Files

- **skill.md** - Complete documentation
- **README.md** - This quick reference
- **Error documents** - In `.claude/agent-memory/cto/errors/`
- **Error index** - In `.claude/agent-memory/cto/error-index.md`

## Related Skills

- **tech-audit** - Uses error patterns for security audits
- **devops-cicd** - Uses deployment errors for prevention
- **repo-cleanup** - Cleanup mistakes → error docs

## Metrics

Track in `.claude/agent-memory/cto/error-metrics.md`:
- Total errors documented
- Errors by category
- Recurrence rate
- Prevention effectiveness
- Most common patterns

---

**Created**: 2026-02-11
**Type**: Semi-automatic (CTO triggers proactively)
**Target User**: CTO agent
