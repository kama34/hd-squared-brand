# Repository Auto-Cleanup Skill

## Overview

**Purpose**: Автоматическая организация файлов в правильную структуру после завершения задач. Поддерживает чистоту репозитория, предотвращает накопление misplaced files, обеспечивает соответствие архитектурным стандартам.

**Target Users**: CTO (primary)

**Capabilities**:
- Сканирование репозитория на misplaced files
- Автоматическое распределение файлов по правильным каталогам
- Обновление imports/references после перемещения
- Очистка временных файлов
- Валидация структуры согласно project conventions
- Commit изменений с понятным сообщением

## Required Tools

- `Glob` - Find files in wrong locations
- `Read` - Analyze file content to determine correct location
- `Edit` - Update imports/references after moving files
- `Bash` - Move files, run git commands
- `Grep` - Search for import statements to update

## Core Workflow

### Trigger Points (CTO проактивно запускает skill)

1. **После successful commit** - код работает, но структура может быть неправильной
2. **После создания >3 файлов** - много новых файлов могут быть в wrong places
3. **После завершения major task** - фича реализована, время организовать
4. **Перед code review** - привести repo в порядок перед review
5. **Перед PR merge** - финальная очистка перед мержем в main

### Process

```
1. [TASK COMPLETED] → CTO triggers: "Организуй структуру репозитория"
2. [SKILL SCANS]:
   - Root directory for misplaced files
   - Temp/test files that should be deleted
   - Config files in wrong locations
   - Code files not in src/
3. [SKILL CREATES PLAN]:
   - List of files to move
   - List of files to delete
   - Imports/references to update
4. [SKILL EXECUTES]:
   - Move files to correct locations
   - Update imports
   - Delete temp files
   - Commit changes
5. [SKILL REPORTS]:
   - Summary of changes
   - Updated directory structure
```

## Repository Organization Rules

### Sales AI Project Structure (Active Startup)

```
Sales AI/
├── SalesAI-Website/              # Main website codebase
│   ├── src/                      # Source code
│   │   ├── components/           # React components
│   │   ├── pages/                # Page components
│   │   ├── utils/                # Utility functions
│   │   ├── hooks/                # Custom React hooks
│   │   ├── services/             # API services
│   │   ├── types/                # TypeScript types
│   │   └── styles/               # CSS/SCSS files
│   ├── public/                   # Static assets
│   ├── tests/                    # Test files
│   └── vite.config.ts            # Build config
├── configs/                      # Project configurations
│   ├── docker/                   # Docker files
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   ├── nginx/                    # Nginx configs
│   └── ci-cd/                    # CI/CD configs
│       └── .github/workflows/
├── knowledge-base/               # Startup documentation
│   ├── 01_Strategy/
│   ├── 02_Finance/
│   ├── 03_Tech/
│   │   └── architecture_decisions/  # ADRs
│   ├── 04_Marketing/
│   └── 05_Legal/
├── scripts/                      # Automation scripts
│   ├── deploy.sh
│   └── backup.sh
└── docs/                         # Additional documentation
    └── api-docs/
```

### Misplaced File Patterns

**Pattern 1: Code files in root**

```
❌ WRONG:
Sales AI/
├── Header.tsx                   # Component in root
├── utils.js                     # Utils in root
└── api.ts                       # API service in root

✅ CORRECT:
Sales AI/SalesAI-Website/src/
├── components/Header.tsx
├── utils/utils.js
└── services/api.ts
```

**Pattern 2: Config files scattered**

```
❌ WRONG:
Sales AI/
├── Dockerfile                   # In root
├── .dockerignore               # In root
└── nginx.conf                  # In root

✅ CORRECT:
Sales AI/configs/docker/
├── Dockerfile
├── .dockerignore
└── nginx.conf
```

**Pattern 3: Temporary files not cleaned**

```
❌ WRONG (should delete):
Sales AI/
├── test.html                   # Temp test file
├── backup/                     # Old backup
├── node_modules_old/           # Old dependencies
└── .DS_Store                   # macOS metadata

✅ CORRECT:
# These should be deleted or moved to /tmp/
```

**Pattern 4: Documentation in wrong place**

```
❌ WRONG:
Sales AI/
└── architecture-diagram.md     # In root

✅ CORRECT:
Sales AI/knowledge-base/03_Tech/
└── architecture-diagram.md
```

## Usage Examples

### Example 1: Cleanup After Feature Development

**Trigger**: CTO finished implementing login feature

**Current state**:
```
Sales AI/
├── LoginForm.tsx               # New component (root)
├── auth.ts                     # New service (root)
├── login-test.html             # Temp test file
├── old-login.tsx               # Backup of old code
└── SalesAI-Website/
    └── src/
        └── (existing files)
```

**User says**: "Организуй структуру репозитория"

**Process**:

1. **Scan for misplaced files**:
```bash
# Use Glob to find files in root
glob: "*.*"
path: "Sales AI/"
```

2. **Analyze each file** (Read file content to determine type):
```javascript
// LoginForm.tsx - React component → move to src/components/
// auth.ts - Service → move to src/services/
// login-test.html - Temp test → delete
// old-login.tsx - Backup → delete (already in git history)
```

3. **Create cleanup plan**:
```markdown
## Repository Cleanup Plan

**Files to move**:
- LoginForm.tsx → SalesAI-Website/src/components/LoginForm.tsx
- auth.ts → SalesAI-Website/src/services/auth.ts

**Files to delete**:
- login-test.html (temporary test file)
- old-login.tsx (backup - available in git history)

**Imports to update**:
- LoginForm.tsx: Update relative imports for new location
- Any file importing LoginForm.tsx or auth.ts
```

4. **Execute cleanup**:
```bash
# Move files
mv "Sales AI/LoginForm.tsx" "Sales AI/SalesAI-Website/src/components/"
mv "Sales AI/auth.ts" "Sales AI/SalesAI-Website/src/services/"

# Delete temp files
rm "Sales AI/login-test.html"
rm "Sales AI/old-login.tsx"
```

5. **Update imports** (Use Grep to find files importing moved files):
```bash
# Find files importing LoginForm
grep "import.*LoginForm" --output_mode files_with_matches

# Update each file
# Before: import LoginForm from '../LoginForm';
# After: import LoginForm from './components/LoginForm';
```

6. **Verify build still works**:
```bash
cd "Sales AI/SalesAI-Website"
npm run build
```

7. **Commit cleanup**:
```bash
git add -A
git commit -m "chore: organize repository structure

- Move LoginForm.tsx to src/components/
- Move auth.ts to src/services/
- Remove temporary test files
- Update imports for new file locations

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

8. **Report**:
```markdown
## Repository Cleanup Complete

**Moved**:
- LoginForm.tsx → src/components/
- auth.ts → src/services/

**Deleted**:
- login-test.html
- old-login.tsx

**Updated imports**: 2 files

**Build status**: ✅ Successful

**Commit**: abc123def
```

### Example 2: Organize Config Files

**Trigger**: CTO added Docker and nginx configs

**Current state**:
```
Sales AI/
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── .dockerignore
└── configs/
    └── (empty)
```

**User says**: "Организуй конфигурационные файлы"

**Process**:

1. **Identify config files**:
```bash
# Find Docker-related files
glob: "Dockerfile*"
glob: "docker-compose*.yml"
glob: "nginx*.conf"
```

2. **Create proper structure**:
```bash
mkdir -p "Sales AI/configs/docker"
mkdir -p "Sales AI/configs/nginx"
```

3. **Move files**:
```bash
mv "Sales AI/Dockerfile" "Sales AI/configs/docker/"
mv "Sales AI/docker-compose.yml" "Sales AI/configs/docker/"
mv "Sales AI/.dockerignore" "Sales AI/configs/docker/"
mv "Sales AI/nginx.conf" "Sales AI/configs/nginx/"
```

4. **Update CI/CD references**:
```yaml
# .github/workflows/deploy-website.yml

# Before:
context: .
file: ./Dockerfile

# After:
context: .
file: ./configs/docker/Dockerfile
```

5. **Update documentation**:
```markdown
# Sales AI/knowledge-base/03_Tech/deployment-guide.md

## Building Docker Image

\```bash
# Before:
docker build -t salesai-website .

# After:
docker build -f configs/docker/Dockerfile -t salesai-website .
\```
```

6. **Commit**:
```bash
git commit -m "chore: organize config files into dedicated directories

- Move Docker files to configs/docker/
- Move nginx config to configs/nginx/
- Update CI/CD workflow paths
- Update deployment documentation

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

### Example 3: Cleanup After Multiple Experiments

**Trigger**: CTO tried multiple approaches, left test files

**Current state**:
```
Sales AI/SalesAI-Website/
├── src/
│   ├── test-api-v1.ts          # Old test
│   ├── test-api-v2.ts          # Old test
│   ├── api-final.ts            # Actual implementation
│   ├── components/
│   │   ├── Button-old.tsx      # Backup
│   │   ├── Button-new.tsx      # Backup
│   │   └── Button.tsx          # Final version
└── dist_backup/                # Old build output
```

**User says**: "Очисти экспериментальные файлы"

**Process**:

1. **Identify test/backup files**:
```bash
# Pattern: test-*, *-old, *-new, *-backup, *_backup
grep "test-|old|new|backup" --output_mode files_with_matches
```

2. **Verify files are not imported**:
```bash
# Check if any file imports test-api-v1.ts
grep "test-api-v1" --output_mode files_with_matches
# Result: No matches (safe to delete)
```

3. **Create cleanup plan**:
```markdown
## Cleanup Experimental Files

**Safe to delete** (not imported, superseded):
- src/test-api-v1.ts (old experiment)
- src/test-api-v2.ts (old experiment)
- src/components/Button-old.tsx (superseded by Button.tsx)
- src/components/Button-new.tsx (superseded by Button.tsx)
- dist_backup/ (old build output)

**Keep**:
- src/api-final.ts (rename to api.ts for clarity)
- src/components/Button.tsx (current implementation)
```

4. **Execute**:
```bash
# Delete old files
rm "Sales AI/SalesAI-Website/src/test-api-v1.ts"
rm "Sales AI/SalesAI-Website/src/test-api-v2.ts"
rm "Sales AI/SalesAI-Website/src/components/Button-old.tsx"
rm "Sales AI/SalesAI-Website/src/components/Button-new.tsx"
rm -rf "Sales AI/SalesAI-Website/dist_backup"

# Rename final version
mv "Sales AI/SalesAI-Website/src/api-final.ts" "Sales AI/SalesAI-Website/src/api.ts"
```

5. **Update imports if renamed**:
```bash
# Find files importing api-final.ts
grep "api-final" --output_mode files_with_matches

# Update to import api.ts
# (Use Edit tool)
```

6. **Commit**:
```bash
git commit -m "chore: remove experimental and backup files

- Remove old test files (test-api-v1, test-api-v2)
- Remove superseded component versions (Button-old, Button-new)
- Remove old build output (dist_backup)
- Rename api-final.ts to api.ts

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

## Integration with CTO Workflow

### CTO Agent Prompts to Trigger Skill

**Add to `.github/agents/cto.agent.md`** (в секцию "Операционные процедуры"):

```markdown
### После завершения задачи (Feature/Fix)

**После того как задача выполнена и код работает:**

1. **Проверить build и tests** - убедиться что все green
2. **Запустить repo-cleanup skill**:
   - Фраза: "Организуй структуру репозитория"
   - Или автоматически если создано >3 новых файла
3. **Skill проверит**:
   - Файлы в неправильных местах (root, wrong directories)
   - Временные/тестовые файлы для удаления
   - Backup файлы (доступны в git history)
   - Неиспользуемые конфиги
4. **Skill создаст план** - показать пользователю для подтверждения
5. **После одобрения** - выполнить cleanup и commit
6. **Проверить что build не сломался** после перемещения файлов
```

### Automatic Triggers (Context-Based)

CTO agent должен **сам определять** когда запускать skill:

**Trigger patterns**:
- After `git commit` with >3 files changed
- After implementing feature (user says "done", "complete", "finish")
- Before creating PR (user says "create PR", "pull request")
- After merging branch (cleanup merged code)
- Weekly maintenance (every Friday cleanup)

**CTO internal prompt** (добавить в agent.md):
```markdown
### Проактивная очистка репозитория

**Когда запускать repo-cleanup skill автоматически:**

1. **После major commit**:
   - If `git status` shows >3 new files in wrong locations
   - If files in root directory (except allowed: README.md, package.json, etc.)
   - If temp files detected (*.tmp, *-old, *-backup, *-test)

2. **Перед PR**:
   - User says "create PR", "pull request"
   - Cleanup ensures repo is organized before review

3. **После эксперимента**:
   - Multiple versions of same file detected (file-v1, file-v2, file-final)
   - Old backup directories (dist_backup, node_modules_old)

4. **Weekly maintenance** (каждую пятницу):
   - Scan entire repo for misplaced files
   - Clean temp files
   - Organize configs

**Workflow**:
1. Detect trigger condition
2. Run: "Используя repo-cleanup skill, scan repository structure"
3. Generate cleanup plan
4. Ask user confirmation: "Найдены файлы в неправильных местах. Переместить?"
5. If confirmed → Execute cleanup → Commit
6. Verify build still works
```

## Allowed Files in Root Directory

**Sales AI root** (these are OK to keep in root):

```
Sales AI/
├── README.md                   # Project overview (OK)
├── .gitignore                  # Git config (OK)
├── .env.example                # Environment template (OK)
├── LICENSE                     # License file (OK)
├── package.json                # If monorepo (OK)
└── .editorconfig               # Editor settings (OK)
```

**Everything else should be in subdirectories**.

## File Type Detection Rules

### How to determine correct location for a file:

```python
def get_correct_location(file_path, file_content):
    """Determine correct location based on file type and content"""

    # 1. React/Vue components → src/components/
    if file_content.includes('export default function') or file_content.includes('export const'):
        if file_content.includes('return (') and file_content.includes('JSX'):
            return 'SalesAI-Website/src/components/'

    # 2. TypeScript types → src/types/
    if file_content.includes('export interface') or file_content.includes('export type'):
        return 'SalesAI-Website/src/types/'

    # 3. API services → src/services/
    if file_content.includes('fetch(') or file_content.includes('axios'):
        return 'SalesAI-Website/src/services/'

    # 4. Utility functions → src/utils/
    if file_content.includes('export function') and not is_component(file_content):
        return 'SalesAI-Website/src/utils/'

    # 5. React hooks → src/hooks/
    if file_path.startswith('use') and file_content.includes('useState'):
        return 'SalesAI-Website/src/hooks/'

    # 6. Docker configs → configs/docker/
    if file_path.includes('Dockerfile') or file_path.includes('docker-compose'):
        return 'configs/docker/'

    # 7. Nginx configs → configs/nginx/
    if file_path.endswith('.conf') and file_content.includes('server {'):
        return 'configs/nginx/'

    # 8. CI/CD workflows → configs/ci-cd/.github/workflows/
    if file_path.endswith('.yml') and file_content.includes('on:'):
        return 'configs/ci-cd/.github/workflows/'

    # 9. Documentation → knowledge-base/03_Tech/
    if file_path.endswith('.md') and not file_path == 'README.md':
        return 'knowledge-base/03_Tech/docs/'

    # 10. Scripts → scripts/
    if file_path.endswith('.sh') or file_path.endswith('.py'):
        return 'scripts/'

    # 11. Tests → tests/
    if file_path.includes('test') or file_path.includes('spec'):
        return 'SalesAI-Website/tests/'

    # 12. Temp files → DELETE
    if file_path.includes('temp') or file_path.includes('tmp'):
        return 'DELETE'

    # 13. Backup files → DELETE
    if file_path.includes('backup') or file_path.includes('-old'):
        return 'DELETE'

    # Default: ask user
    return 'ASK_USER'
```

## Cleanup Safety Checks

**Before deleting any file, verify**:

1. **Not imported anywhere**:
```bash
grep -r "import.*filename" SalesAI-Website/src/
# If no matches → safe to delete
```

2. **Not referenced in configs**:
```bash
grep -r "filename" package.json tsconfig.json vite.config.ts
# If no matches → safe to delete
```

3. **Available in git history**:
```bash
git log --all --full-history -- filename
# If exists in git → safe to delete (recoverable)
```

4. **User confirmation for non-obvious files**:
```
Found: experimental-feature.ts
Not imported, not in git history.
Delete? [y/N]:
```

## Integration with Other Skills

### error-learning
- After cleanup, if build breaks → Document as error
- Cleanup mistakes become learning material

### tech-audit
- Clean structure → Easier security audits
- Organized configs → Better security review

### devops-cicd
- Clean config files → Easier CI/CD maintenance
- Proper structure → Reliable deployments

### frontend-development / backend-development
- Organized src/ → Faster development
- Clear structure → Easier onboarding

## Best Practices

### 1. Run Cleanup Regularly

**❌ BAD** - Never cleanup, accumulate mess:
> Repo has 50+ files in root, unused backups everywhere

**✅ GOOD** - Cleanup after every major task:
> After feature complete → Run repo-cleanup → Commit organized structure

**Why**: Small frequent cleanups easier than massive occasional cleanup.

### 2. Ask Before Deleting Non-Obvious Files

**❌ BAD** - Auto-delete without confirmation:
> Deleted important config file CTO was working on

**✅ GOOD** - Confirm deletions:
> "Found backup-config.yml (not imported). Delete? [y/N]"

**Why**: Prevents accidental deletion of work-in-progress.

### 3. Update Imports After Moving Files

**❌ BAD** - Move files, forget to update imports:
> Build breaks because imports still point to old locations

**✅ GOOD** - Move + update imports + verify build:
> Move → Update all imports → Run build → Commit

**Why**: Ensures code still works after reorganization.

### 4. Commit Cleanup Separately from Features

**❌ BAD** - Mix feature code with cleanup:
> Commit: "Add login feature and reorganize 20 files"

**✅ GOOD** - Separate commits:
> Commit 1: "feat: add login feature"
> Commit 2: "chore: organize repository structure"

**Why**: Easier code review, clearer git history.

### 5. Preserve Git History When Moving

**❌ BAD** - Delete old file, create new file:
> Git sees as delete + add (loses history)

**✅ GOOD** - Use `git mv`:
```bash
git mv old/path/file.ts new/path/file.ts
```

**Why**: Preserves file history across moves.

## Cleanup Checklist

**Before running cleanup**:
- [ ] All tests passing?
- [ ] Code committed? (so you can revert if cleanup breaks things)
- [ ] Identified which files to move/delete?
- [ ] Checked imports for files to move?

**During cleanup**:
- [ ] Move files to correct locations
- [ ] Update imports/references
- [ ] Delete temp/backup files (after confirmation)
- [ ] Update documentation if needed

**After cleanup**:
- [ ] Run build - still works?
- [ ] Run tests - still passing?
- [ ] Commit cleanup with descriptive message
- [ ] Verify repo structure matches conventions

## Troubleshooting

### Problem: "Build breaks after moving files"

**Solution**:
1. Check build error - which import failed?
2. Use Grep to find all imports of moved file:
   ```bash
   grep "import.*MovedFile" --output_mode files_with_matches
   ```
3. Update each import to new path
4. Re-run build
5. If still broken - revert: `git reset --hard HEAD`

### Problem: "Accidentally deleted important file"

**Solution**:
1. Check if in git:
   ```bash
   git log --all -- path/to/file
   ```
2. Restore from git:
   ```bash
   git checkout HEAD -- path/to/file
   ```
3. If not in git - check backups or ask user

### Problem: "Too many files to organize manually"

**Solution**:
1. Use automatic file type detection (see rules above)
2. Process files in batches (10 files at a time)
3. Ask user confirmation for each batch
4. Commit incrementally (don't wait to organize everything)

### Problem: "Circular imports after reorganization"

**Solution**:
1. Identify circular dependency:
   ```bash
   npm run build
   # Error: Circular dependency: A imports B, B imports A
   ```
2. Extract shared code to separate file
3. Both A and B import shared file
4. Run build again

## Version History

- **2026-02-11**: Created repo-cleanup skill for CTO
  - Semi-automatic workflow (CTO triggers after tasks)
  - File type detection rules
  - Safe deletion checks
  - Import update automation
  - Integration with CTO workflow

## Related Files

- `.github/agents/cto.agent.md` - CTO agent configuration (add triggers here)
- `.claude/skills/tech-audit/` - Code review skill (benefits from clean structure)
- `.claude/skills/error-learning/` - Error documentation (cleanup mistakes → learnings)

---

**Next Steps After Creating This Skill**:

1. Update `.github/agents/cto.agent.md` with repo-cleanup triggers
2. Test skill on Sales AI repo (current misplaced files)
3. Add to `.claude/skills/ALL_SKILLS_REFERENCE.md`
4. Create cleanup checklist in CTO agent memory
