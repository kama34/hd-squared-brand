# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Russian startup studio workspace that manages multiple startups using an AI-powered C-level team and knowledge base system. All work is conducted in Russian language.

## Critical Concepts

### Multi-Startup Context

**BEFORE any action**, identify which startup is being discussed:
1. Look for explicit startup name mentions
2. Check file paths (e.g., `<Startup Name>/knowledge-base/`)
3. Ask the user if unclear

### Directory Structure

```
Root/
├── .github/
│   ├── agents/              # AI C-level team definitions (CEO, CFO, CMO, CTO, Board, etc.)
│   ├── skills/              # 22 reusable skills for agents
│   └── knowledge-base/      # TEMPLATES (not real startup data)
├── .claude/
│   ├── agents/              # Claude Code-adapted agent definitions
│   └── skills/              # Claude Code-adapted skills
├── <Startup Name>/          # Individual startup directories (e.g., "Sales AI")
│   └── knowledge-base/      # REAL startup data (strategy, finance, tech, marketing, legal)
└── Футболки/                # Product content (t-shirts design business)
```

### Templates vs Real Data

| Location | Type | Usage |
|----------|------|-------|
| `.github/knowledge-base/` | **TEMPLATES** | Reference when creating new startups |
| `<Startup Name>/knowledge-base/` | **REAL DATA** | Use for analysis and decisions |

**Never** use template data for actual startup analysis or decisions.

## Working with AI Agents

### Available Agents (`.github/agents/`)

- **CEO** (`ceo.agent.md`) - Strategy, vision, decision-making, OKR planning, board reporting
- **CFO** (`cfo.agent.md`) - Financial modeling, unit economics, runway tracking, budget
- **CMO** (`cmo.agent.md`) - Marketing strategy, competitor analysis, user personas, GTM
- **CTO** (`cto.agent.md`) - Technical architecture, security, code review, tech stack
- **Board** (`board.agent.md`) - Strategic oversight, major decisions (pivot, funding, M&A)
- **Specialized**: copywriter, ui-designer, site-audit, landing-structure, content-editor, skill-builder, agent-builder

### Agent Workflows

**Sprint Planning**:
1. @CMO identifies critical features for customer retention
2. @CTO estimates effort and technical risks
3. @CFO verifies budget constraints
4. @CEO synthesizes and creates prioritized task list

**Strategic Decisions** (Pivot, major features, hiring):
1. @CEO initiates discussion
2. C-level agents provide domain reports
3. @Board approves/rejects/requests revision

**Financial Analysis**:
- @CFO MUST use Python for all calculations (see Skills section)
- Results formatted as Markdown tables
- WARNING if Runway < 6 months

### 🔴 CRITICAL: Agent File Placement Rules

**ALL agents MUST save files in the correct knowledge-base structure.**

**Rule #1: Identify Startup Context**
BEFORE saving any file, agents MUST:
1. Identify which startup the work is for (from file paths in user's request)
2. If unclear → ASK the user: "Для какого стартапа этот документ/анализ?"
3. NEVER assume or guess the startup

**Rule #2: Use Correct Directory Structure**
Each agent has a designated directory in `<Startup Name>/knowledge-base/`:

| Agent | Target Directory | File Types |
|-------|-----------------|------------|
| **CFO** | `02_Finance/` | Financial models, unit economics, Python scripts, reports |
| **CEO** | `01_Strategy/` | OKRs, decisions, vision docs, board materials |
| **CMO** | `04_Marketing/` | User personas, competitor analysis, campaigns, brand book |
| **CTO** | `03_Tech/` | Architecture decisions, security policies, tech stack |
| **Legal** | `05_Legal/` | Contracts, compliance, privacy policies |

**Rule #3: Forbidden Locations**
❌ NEVER save startup-specific files to:
- `.github/knowledge-base/` (these are TEMPLATES only)
- Root directory (`D:\Drive\Дизайнерский магазин\`)
- Current working directory (unless it's already the correct location)
- Another startup's directory

**Rule #4: Create Structure If Missing**
If `<Startup Name>/knowledge-base/<XX_Domain>/` doesn't exist:
- Create the directory structure before saving
- Use full absolute paths in Write tool

**Examples**:
- ✅ `Футболки/Язык и рогатка/Бизнес часть/02_Finance/unit_economics_2026-02-11.md`
- ✅ `Sales AI/knowledge-base/04_Marketing/competitor_analysis.md`
- ❌ `unit_economics_calc.py` (where is the startup context?)
- ❌ `.github/knowledge-base/02_Finance/real_data.csv` (templates only!)

**Enforcement**: This is a BLOCKING requirement. Files saved to wrong locations will confuse multi-startup operations and corrupt the knowledge base.

## Skills System

Located in `.github/skills/` (originals) and `.claude/skills/` (Claude Code adaptations)

### Finance & Modeling
- `finance-forecasting` - Revenue/cost projections, runway calculation
- `finance-modeler` - Scenario analysis, sensitivity modeling
- `finance-unit-economics` - LTV/CAC/churn calculations

### Pitch & Fundraising
- `pitch-questions` - Generate pitch deck structure and slides
- `pitch-audit` - Score and improve pitch decks (iterate until score ~9/10)
- `investor-qa-generator` - Generate Q&A for investor meetings
- `board-reporting` - Structure board meeting materials

### Site & Marketing
- `landing-structure` - Landing page best practices
- `site-audit` - Accessibility, SEO, performance checks
- `html-fixes` - HTML/CSS bug fixes
- `design-language` - Design system consistency
- `marketing-alignment` - Cross-channel messaging alignment
- `brand-analysis` - Brand positioning analysis
- `market-analysis` - Competitive landscape research

### Development
- `tech-audit` - Security (OWASP Top 10), code quality checks
- `repo-analyzer` - Repository structure analysis
- `repo-agent-suggester` - Recommend AI agents for projects
- `backend-development` - Backend development assistance
- `frontend-development` - Frontend development assistance
- `devops-cicd` - DevOps and CI/CD workflows

### Management & Meta
- `experiment-management` - HADI framework, A/B testing, hypothesis tracking
- `skill-creator` - Create new skills
- `prompt-generator-skill` - Prompt engineering helpers

### Usage Pattern
```
"Используя <skill-name> skill, <task> для <Startup Name>"
```

Example: `"Используя finance-modeler skill, create 3-year projection for Sales AI"`

## Knowledge Base Structure

Each startup should have: `<Startup Name>/knowledge-base/`

### 01_Strategy/
- `vision_mission.md` - Company vision, mission, values
- `okr_YYYY_QX.md` - Quarterly Objectives and Key Results (≥70% = success)
- `pitch_deck_structure.md` - Investor pitch materials
- `decisions/` - Architecture Decision Records (ADRs)

### 02_Finance/
- `financial_model_template.csv` - Revenue, costs, runway projections
- `budget_allocation.md` - Quarterly budget breakdown
- `unit_economics_rules.md` - LTV/CAC ratios, payback period, churn targets

### 03_Tech/
- `stack_definition.md` - Tech stack (languages, frameworks, infrastructure)
- `security_policies.md` - Security standards, compliance
- `architecture_decisions/` - Major technical decisions (immutable ADRs)

### 04_Marketing/
- `brand_book.md` - Brand guidelines, tone of voice
- `user_personas.md` - ICP (Ideal Customer Profile), user segments
- `competitor_list.md` - Competitive landscape, positioning

### 05_Legal/
- `term_sheet_template.md` - Investment terms (requires legal counsel review)
- `privacy_policy_draft.md` - Data handling policies (GDPR, CCPA)

### Experiments/
- HADI format: Hypothesis → Action → Data → Insight
- Use `hypothesis_template.md` for new experiments
- Track in `experiments/` directory

## Maintenance Schedule

### Weekly (Fridays)
- @CFO: Update financial model, check runway
- @CMO: Competitor analysis (web search for new players)
- @CTO: Security audit critical changes
- @CEO: Review OKR progress

### Monthly (End of month)
- @CFO: Budget vs actual, unit economics analysis
- @CMO: Full competitor update, user persona refinement
- @CTO: Full tech audit (security + code quality)
- @CEO: Monthly board update

### Quarterly (Last week of Q)
- All agents: Create next quarter's planning documents
- @CEO: New OKR creation (with input from CTO/CFO/CMO)
- @Board: Approve OKRs and budget for Q+1

### Trigger Events
- **Pivot**: Update vision_mission, user_personas, competitor_list, brand_book
- **Fundraising**: Update pitch_deck, financial_model, term_sheet
- **Product-Market Fit**: Update OKRs (shift to growth), increase marketing budget
- **Significant Growth** (MRR +100%): Recalculate unit economics, plan infrastructure scaling

## Common Workflows

### Creating a New Startup
1. Create directory: `<Startup Name>/`
2. Copy templates from `.github/knowledge-base/` to `<Startup Name>/knowledge-base/`
3. Customize templates with real startup data
4. Update `.github/copilot-instructions.md` with startup name

### Pitch Deck Iteration (CEO)
1. Use `pitch-questions` skill to generate initial deck
2. Use `pitch-audit` skill → get score
3. Improve deck based on audit feedback
4. Repeat audit until score ≥ 9/10
5. Use `investor-qa-generator` skill for Q&A prep
6. Create supplemental slides with `pitch-questions`

### Financial Modeling (CFO)
1. Use `finance-forecasting` skill for projections
2. Python calculations via `mcp__ide__executeCode`
3. Save results to `02_Finance/` directory
4. Alert @CEO if Runway < 6 months

### Competitor Research (CMO)
1. Use `WebSearch` tool with Brave Search
2. Update `competitor_list.md` monthly
3. Use `market-analysis` skill for deep dive
4. Track Product Hunt, TechCrunch, Hacker News

### Security Audit (CTO)
1. Use `tech-audit` skill monthly
2. Check against OWASP Top 10 (`owasp_checklist.md`)
3. Update `security_policies.md` with findings
4. Create tasks for high/critical issues

## HADI Experiment Framework

CEO requires all major hypotheses follow this format:

**Hypothesis**: Expected change in key metric, target segment, time horizon
**Action**: Specific steps, owner, resources, start/stop criteria
**Data**: Data sources, measurement method, observation period
**Insight**: Results, recommendations (scale/iterate/stop)

Use `experiment-management` skill to track experiments.

## Security & Permissions

### Agent Access Levels
- **CEO/Board/CFO/CMO**: Read-only access to code (`Read`, `WebSearch`, `WebFetch`)
- **CTO**: Full code access (`Read`, `Write`, `Edit`, `Bash`)
- **CFO**: Python execution (`mcp__ide__executeCode`) for financial calculations

### Critical Operations (Require Human Approval)
- Commits to main branch
- Infrastructure changes
- Expenses >$1000
- Destructive actions (force push, data deletion)
- External API calls with confidential data

### Data Protection
- **NEVER** hardcode API keys, passwords, tokens
- **NEVER** send financial data to external APIs without explicit permission
- Use environment variables (`${env:VAR_NAME}`) for secrets
- **NEVER** read financial data of other startups without permission

## Communication Style

- **Language**: All text and documents in Russian
- **Tone**: Business-focused, direct, action-oriented
- **Structure**: Use headings, lists, tables
- **Evidence-based**: Cite sources (knowledge base files, documentation)
- **Actionable**: Include next steps and recommendations
- **Transparent**: Report bad news immediately, with mitigation plans

## Success Metrics

### Business (CEO)
- Revenue Growth: MRR increasing month-over-month
- Product-Market Fit: NPS >40, Churn <5%
- Runway: Always >6 months
- Team Velocity: ±20% of roadmap

### Finance (CFO)
- LTV/CAC ratio >3:1
- Payback period <12 months
- Churn rate <5% monthly (SaaS)

### Marketing (CMO)
- CAC trending down
- Conversion rate improving
- Competitive positioning clear

### Technology (CTO)
- Security: No high/critical vulnerabilities
- Performance: P95 latency within SLAs
- Quality: Code coverage >80%

## Key Mental Models

- **Pareto Principle**: 80% results from 20% effort - focus on high-impact work
- **Type 1 vs Type 2 Decisions**: Irreversible (slow, careful) vs Reversible (fast, experimental)
- **Opportunity Cost**: What we DON'T do if we do this?
- **Runway First**: Always maintain >6 months runway before starting fundraising

## Version

**Created**: 2026-02-11
**Language**: Russian (user-facing), English (this file)
**Format**: Claude Code CLI
**Startup Studio**: Multi-tenant design
