# Repository Cleanup Skill - Quick Reference

## Purpose

Автоматически организовать файлы в правильную структуру после завершения задач.

## Quick Start

### 1. After Completing Task

**Trigger phrase**:
```
"Организуй структуру репозитория"
```

**Examples**:
```
"Организуй структуру репозитория"
"Очисти экспериментальные файлы"
"Организуй конфигурационные файлы"
```

### 2. Skill Scans Repository

**Looks for**:
- Files in root directory (should be in subdirectories)
- Temporary/test files (`*-test.html`, `*-old`, `*-backup`)
- Config files in wrong locations
- Code files not in `src/`
- Unused backup directories

### 3. Skill Creates Plan

**Plan includes**:
- Files to move (with destinations)
- Files to delete (temp/backup files)
- Imports to update (after moving)
- Safety checks (verify not imported)

### 4. Skill Executes Cleanup

**Actions**:
1. Move files to correct locations
2. Update import statements
3. Delete temporary files (after confirmation)
4. Verify build still works
5. Commit with descriptive message

## Repository Structure (Sales AI Example)

```
Sales AI/
├── SalesAI-Website/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── services/        # API services
│   │   ├── utils/           # Utility functions
│   │   └── types/           # TypeScript types
│   ├── public/              # Static assets
│   └── tests/               # Test files
├── configs/
│   ├── docker/              # Docker files
│   ├── nginx/               # Nginx configs
│   └── ci-cd/               # CI/CD configs
├── knowledge-base/          # Documentation
├── scripts/                 # Automation scripts
└── docs/                    # Additional docs
```

## Misplaced File Examples

### ❌ WRONG

```
Sales AI/
├── Header.tsx              # Component in root
├── Dockerfile              # Config in root
├── test.html               # Temp file
└── old-code.tsx            # Backup
```

### ✅ CORRECT

```
Sales AI/
├── SalesAI-Website/src/components/Header.tsx
├── configs/docker/Dockerfile
└── (test.html deleted)
└── (old-code.tsx deleted - in git history)
```

## Automatic Triggers (CTO Agent)

CTO agent automatically runs this skill when:
- After `git commit` with >3 new files
- User says: "create PR", "pull request" (cleanup before PR)
- After merging branch
- Every Friday (weekly maintenance)

## Safety Checks

Before deleting any file:
1. Check if imported anywhere
2. Check if referenced in configs
3. Verify available in git history
4. Ask user confirmation for non-obvious files

## Cleanup Checklist

**Before cleanup**:
- [ ] All tests passing?
- [ ] Code committed? (can revert if cleanup breaks things)
- [ ] Identified which files to move/delete?

**After cleanup**:
- [ ] Run build - still works?
- [ ] Run tests - still passing?
- [ ] Commit with descriptive message

## Example Cleanup Commit

```bash
git commit -m "chore: organize repository structure

- Move LoginForm.tsx to src/components/
- Move auth.ts to src/services/
- Remove temporary test files
- Update imports for new file locations

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

## File Type Detection

| File Type | Correct Location |
|-----------|------------------|
| React components (`.tsx`) | `src/components/` |
| TypeScript types | `src/types/` |
| API services | `src/services/` |
| Utility functions | `src/utils/` |
| React hooks (`use*.tsx`) | `src/hooks/` |
| Docker files | `configs/docker/` |
| Nginx configs | `configs/nginx/` |
| CI/CD workflows (`.yml`) | `configs/ci-cd/.github/workflows/` |
| Documentation (`.md`) | `knowledge-base/03_Tech/docs/` |
| Scripts (`.sh`, `.py`) | `scripts/` |
| Tests (`*test*`, `*spec*`) | `tests/` |
| Temp files (`*tmp*`, `*temp*`) | DELETE |
| Backup files (`*-old`, `*backup*`) | DELETE |

## Integration with Workflow

```
1. [TASK COMPLETED] → CTO triggers: "Организуй структуру"
2. [SKILL SCANS] → Finds misplaced files
3. [SKILL CREATES PLAN] → Shows to user for confirmation
4. [USER APPROVES] → Skill executes cleanup
5. [SKILL VERIFIES] → Build still works
6. [SKILL COMMITS] → Clean structure committed
```

## Benefits

- Maintain clean repository structure
- Easier code navigation
- Faster code reviews (reviewers find files easily)
- Better onboarding (new developers understand structure)
- Prevent accumulation of technical debt (temp files)
- Consistent architecture across projects

## Files

- **skill.md** - Complete documentation
- **README.md** - This quick reference

## Related Skills

- **error-learning** - Cleanup mistakes → error documentation
- **tech-audit** - Clean structure → easier audits
- **devops-cicd** - Organized configs → reliable deployments

## Troubleshooting

**Problem**: Build breaks after moving files
**Solution**: Check imports, update paths, re-run build. If broken - revert: `git reset --hard HEAD`

**Problem**: Accidentally deleted important file
**Solution**: Restore from git: `git checkout HEAD -- path/to/file`

---

**Created**: 2026-02-11
**Type**: Semi-automatic (CTO triggers proactively)
**Target User**: CTO agent
