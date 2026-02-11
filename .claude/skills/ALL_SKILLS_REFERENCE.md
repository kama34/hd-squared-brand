# Complete Skills Reference (30 Skills)

**Status**: 16/30 fully adapted (53%), 14/30 pending completion

## All Skills by Category

### 💰 Finance & Modeling (4 skills)

| # | Skill | Status | Python Modules | Purpose |
|---|-------|--------|----------------|---------|
| 1 | **finance-forecasting** | ✅ Complete | forecast_model.py, saas_metrics.py | Runway, cash flow, SaaS metrics |
| 2 | **finance-modeler** | ✅ Complete | model_builder.py | Scenario analysis, projections |
| 3 | **finance-unit-economics** | ✅ Complete | compute_unit_economics.py | LTV, CAC, churn (Russian docs) |
| 4 | **investor-qa-generator** | ✅ Complete | generate_investor_questions.py | Investor Q&A preparation |

### 🌐 Web Development (2 skills)

| # | Skill | Status | Files | Purpose |
|---|-------|--------|-------|---------|
| 5 | **frontend-development** | ✅ Complete | skill.md | HTML5, CSS3, JavaScript ES6+, React, accessibility, performance |
| 6 | **backend-development** | ✅ Complete | skill.md | Node.js/Express, Python, REST APIs, databases, auth, security |

### 🚀 DevOps & Infrastructure (1 skill)

| # | Skill | Status | Files | Purpose |
|---|-------|--------|-------|---------|
| 7 | **devops-cicd** | ✅ Complete | skill.md | Docker, CI/CD (GitHub Actions), deployment, monitoring, secrets |

### 🛡️ Technical & Security (1 skill)

| # | Skill | Status | Files | Purpose |
|---|-------|--------|-------|---------|
| 8 | **tech-audit** | ✅ Complete | audit_checklist.md, owasp_checklist.md | Code review, OWASP Top 10 |

### ⚙️ Configuration Management (3 skills)

| # | Skill | Status | Files | Purpose |
|---|-------|--------|-------|---------|
| 9 | **config-validation** | ✅ Complete | skill.md | Validate & edit sales funnel configs, variable scoping, cleanup |
| 10 | **config-parser-rules** | ✅ Complete | skill.md | Parser rules reference, syntax examples, troubleshooting |
| 11 | **config-templates** | ✅ Complete | skill.md | Ready-to-use config templates, stage scaffolding, patterns |

### 📊 Business & Strategy (3 skills)

| # | Skill | Status | Files | Purpose |
|---|-------|--------|-------|---------|
| 12 | **board-reporting** | ✅ Complete | Templates | Quarterly Board Decks, investor updates |
| 13 | **market-analysis** | ✅ Complete | Frameworks | Competitive intel, TAM/SAM/SOM |
| 14 | **mcp-advisor** | ✅ Complete | Recommendations | MCP server setup и troubleshooting |

### 🎤 Pitch & Presentation (2 skills)

| # | Skill | Status | Purpose |
|---|-------|--------|---------|
| 15 | **pitch-questions** | 🔄 Pending | Generate questions CEO might receive |
| 16 | **pitch-audit** | 🔄 Pending | Pitch deck review и improvement |

### 🌐 Landing & Site (4 skills)

| # | Skill | Status | Purpose |
|---|-------|--------|---------|
| 17 | **landing-structure** | 🔄 Pending | Landing page structure best practices |
| 18 | **site-audit** | 🔄 Pending | Accessibility, SEO, performance |
| 19 | **html-fixes** | 🔄 Pending | HTML/CSS bug fixes |
| 20 | **design-language** | 🔄 Pending | Design system consistency |

### 📢 Marketing & Brand (2 skills)

| # | Skill | Status | Purpose |
|---|-------|--------|---------|
| 21 | **marketing-alignment** | 🔄 Pending | Marketing message consistency |
| 22 | **brand-analysis** | 🔄 Pending | Brand positioning analysis |

### 💻 Development & Tools (5 skills)

| # | Skill | Status | Purpose |
|---|-------|--------|---------|
| 23 | **error-learning** | ✅ Complete | Автоматическое документирование ошибок и их решений |
| 24 | **repo-cleanup** | ✅ Complete | Автоматическая организация файлов в правильную структуру |
| 25 | **repo-analyzer** | 🔄 Pending | Repository structure analysis |
| 26 | **repo-agent-suggester** | 🔄 Pending | AI agent recommendations |
| 27 | **stitch-integration** | 🔄 Pending | Stitch Data integration |

### 🧪 Management & Meta (3 skills)

| # | Skill | Status | Purpose |
|---|-------|--------|---------|
| 28 | **experiment-management** | 🔄 Pending | A/B test tracking |
| 29 | **prompt-generator-skill** | 🔄 Pending | Prompt engineering |
| 30 | **skill-creator** | 🔄 Pending | Create new skills |

## Quick Usage Guide

### Finance Skills

```python
# finance-forecasting: Quick calculations
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-forecasting')
from forecast_model import calculate_runway
runway = calculate_runway(750_000, 50_000)  # 15.0 months

# finance-modeler: Scenario analysis
from model_builder import build_projection, scenario_analysis
projection = build_projection(750_000, 40_000, 70_000, 12)

# finance-unit-economics: Russian docs
from compute_unit_economics import calculate_ltv, ltv_cac_ratio
ltv = calculate_ltv(arpu=120, gross_margin=0.75, monthly_churn=0.04)

# investor-qa-generator: Q&A prep
"Используя investor-qa-generator skill, generate questions для Sales AI Series A pitch"
```

### Web Development Skills

```bash
# frontend-development: Build or edit websites (HTML/CSS/JS/React)
"Действуй как CTO, используя frontend-development skill:
ЗАДАЧА: [Sales AI] Создай responsive landing page с accessibility"

# backend-development: APIs, databases, authentication
"Действуй как CTO, используя backend-development skill:
ЗАДАЧА: [Sales AI] Создай REST API для dashboard metrics с JWT auth"

# devops-cicd: Docker, CI/CD, deployment automation
"Действуй как CTO, используя devops-cicd skill:
ЗАДАЧА: [Sales AI] Настрой CI/CD: main → production deploy, другие ветки → staging"

# Example: Full-stack + DevOps
"Действуй как CTO, используя frontend-development, backend-development, devops-cicd skills:
ЗАДАЧА: [Sales AI] Создай full-stack app с автоматическим deployment через GitHub Actions"
```

### Technical Skills

```bash
# tech-audit: Code review + security
"Используя tech-audit skill, проведи OWASP audit Sales AI/site/code4.html"

# error-learning: Document errors after fixing (semi-automatic)
"Документируй исправленную ошибку Deployment: Docker image lowercase"
# Триггер: Автоматически после commit с "fix:", "bug:", "error:"
# Создает: .claude/agent-memory/cto/errors/2026-02-11-deployment-docker-lowercase.md

# repo-cleanup: Organize repository structure (semi-automatic)
"Организуй структуру репозитория"
# Триггер: Автоматически после commit с >3 файлами, перед PR, каждую пятницу
# Действия: Move misplaced files, delete temp files, update imports, commit

# mcp-advisor: MCP setup
"Используя mcp-advisor skill, recommend MCP servers для Sales AI project"
```

### Configuration Management Skills

```bash
# config-validation: Validate sales funnel config files
"Используя config-validation skill, validate Sales AI/configs/bildanov/bildanov_config.json"

# Example: Add variable to stage
"Используя config-validation skill, add variable 'greeting_message' to Welcome stage in bildanov_config.json"

# config-parser-rules: Reference for parser rules
"Check config-parser-rules skill for examples of nested variable errors"

# config-templates: Scaffolding new configs
"Используя config-templates skill, create new sales funnel config for Dental Clinic"

# Example: Add stage from template
"Используя config-templates skill, add Warming stage to existing config"
```

### Business Skills

```markdown
# board-reporting: Board Deck
"Используя board-reporting skill, create Q1 2026 Board Deck для Sales AI"

# market-analysis: Competitive intel
"Используя market-analysis skill, analyze Competitor A's recent funding"
```

## Tool Mapping (GitHub Copilot → Claude Code)

| Original | Claude Code | Skills Using It |
|----------|-------------|-----------------|
| `@workspace` search | `Grep`, `Glob` | tech-audit, repo-analyzer |
| Python REPL | `mcp__ide__executeCode` | All finance skills |
| File operations | `Read`, `Write`, `Edit` | All skills |
| Terminal | `Bash` | tech-audit, site-audit |
| Web search | `WebSearch`, `WebFetch` | market-analysis, mcp-advisor |
| Linter | `mcp__ide__getDiagnostics` | tech-audit, html-fixes |

## Priority for Completion

### High Priority (Week 1)
1. **pitch-audit** - Needed for Sales AI Series A prep
2. **site-audit** - Sales AI landing page launch
3. **landing-structure** - Landing page optimization
4. **skill-creator** - Enable faster skill creation

### Medium Priority (Week 2-3)
5. design-language - Sales AI branding
6. marketing-alignment - Multi-channel consistency
7. repo-analyzer - Technical debt assessment

### Low Priority (On-demand)
8-14. Remaining skills as needed

## Integration Map

```
finance-forecasting ─┬─→ board-reporting (financial slides)
                     └─→ investor-qa-generator (answer data questions)

finance-modeler ─────→ board-reporting (scenario analysis)

tech-audit ──────────→ board-reporting (security status)

market-analysis ─────┬─→ board-reporting (competitive landscape)
                     └─→ pitch-audit (market sizing validation)

mcp-advisor ─────────→ market-analysis (brave-search MCP setup)
```

## Files by Skill

### Fully Adapted (14 skills)

```
.claude/skills/
├── finance-forecasting/
│   ├── skill.md
│   ├── forecast_model.py
│   └── saas_metrics.py
├── finance-modeler/
│   ├── skill.md
│   └── model_builder.py
├── finance-unit-economics/
│   ├── skill.md
│   └── compute_unit_economics.py
├── investor-qa-generator/
│   ├── skill.md
│   └── generate_investor_questions.py
├── frontend-development/
│   └── skill.md
├── backend-development/
│   └── skill.md
├── devops-cicd/
│   └── skill.md
├── tech-audit/
│   ├── skill.md
│   ├── audit_checklist.md
│   └── owasp_checklist.md
├── config-validation/
│   └── skill.md
├── config-parser-rules/
│   └── skill.md
├── config-templates/
│   └── skill.md
├── board-reporting/
│   └── skill.md
├── market-analysis/
│   └── skill.md
└── mcp-advisor/
    └── skill.md
```

### Pending (14 skills)

Directories created, awaiting full adaptation:
- pitch-questions/
- pitch-audit/
- landing-structure/
- site-audit/
- html-fixes/
- design-language/
- marketing-alignment/
- brand-analysis/
- repo-analyzer/
- repo-agent-suggester/
- stitch-integration/
- experiment-management/
- prompt-generator-skill/
- skill-creator/

### Recently Added (2 skills) 🆕

```
.claude/skills/
├── error-learning/
│   └── skill.md
└── repo-cleanup/
    └── skill.md
```

**error-learning**: Автоматическое обучение на ошибках через создание документации об ошибках, их причинах и решениях
**repo-cleanup**: Автоматическая организация файлов в правильную структуру после завершения задач

## Agent to Skill Mapping

| Agent | Primary Skills | Secondary Skills |
|-------|----------------|------------------|
| **@CFO** | finance-forecasting, finance-modeler, finance-unit-economics | board-reporting (financial slides) |
| **@CEO** | board-reporting, investor-qa-generator | pitch-audit, market-analysis |
| **@CTO** | tech-audit, frontend-development, backend-development, devops-cicd, error-learning, repo-cleanup, mcp-advisor | html-fixes, site-audit, repo-analyzer |
| **@CMO** | market-analysis, brand-analysis | marketing-alignment, landing-structure |
| **@Board** | board-reporting, investor-qa-generator | finance-modeler (scenarios) |
| **@config-editor** | config-validation, config-parser-rules, config-templates | (specialized agent for sales funnel configs) |

## Next Steps

1. ✅ Finance & Modeling group complete (4/4)
2. ✅ Web Development group complete (2/2)
3. ✅ DevOps & Infrastructure group complete (1/1)
4. ✅ Configuration Management group complete (3/3) 🆕
5. ⏳ Pitch & Presentation group (0/2)
6. ⏳ Landing & Site group (0/4)
7. ⏳ Marketing & Brand group (0/2)
8. ⏳ Development & Tools group (0/3)
9. ⏳ Management & Meta group (0/3)
10. 📝 Update main README.md with complete list
11. 🧪 Test all adapted skills on Sales AI project

## Documentation

- **Main README**: `.claude/skills/README.md`
- **This file**: `.claude/skills/ALL_SKILLS_REFERENCE.md`
- **Adaptation summary**: `.claude/skills/ADAPTATION_SUMMARY.md`
- **Memory**: `.claude/agent-memory/skill-creator/MEMORY.md`
- **Originals**: `.github/skills/[skill-name]/SKILL.md`

**Last updated**: 2026-02-11
