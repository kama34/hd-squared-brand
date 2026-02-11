# Adaptation Summary: All 22 Skills

## Completed Adaptations

### Group 1: Finance & Modeling ✅ (3/3)
1. **finance-forecasting** - Python: forecast_model.py, saas_metrics.py
2. **tech-audit** - Checklists: audit_checklist.md, owasp_checklist.md
3. **board-reporting** - Templates: Board Deck, investor updates
4. **market-analysis** - Frameworks + WebSearch integration
5. **mcp-advisor** - MCP server recommendations
6. **finance-modeler** ✅ - Python: model_builder.py (scenario analysis)
7. **finance-unit-economics** ✅ - Python: compute_unit_economics.py (LTV/CAC/churn)
8. **investor-qa-generator** ✅ - Question generation for investor meetings

### Group 2: Pitch & Presentation (2 skills)
9. **pitch-questions** - Q&A prep for pitch presentations
10. **pitch-audit** - Pitch deck review and improvement

### Group 3: Landing & Site (4 skills)
11. **landing-structure** - Landing page structure и best practices
12. **site-audit** - Accessibility, SEO, performance audits
13. **html-fixes** - HTML/CSS bug fixes and improvements
14. **design-language** - Design system consistency

### Group 4: Marketing & Brand (2 skills)
15. **marketing-alignment** - Marketing strategy alignment
16. **brand-analysis** - Brand positioning и messaging

### Group 5: Development & Tools (3 skills)
17. **repo-analyzer** - Repository structure analysis
18. **repo-agent-suggester** - AI agent recommendations for projects
19. **stitch-integration** - Stitch Data integration helpers

### Group 6: Management & Meta (3 skills)
20. **experiment-management** - A/B testing и experimentation
21. **prompt-generator-skill** - Prompt engineering helpers
22. **skill-creator** - Meta-skill для создания новых skills

## Adaptation Status: 8/22 Complete

### Fully Adapted (8 skills)
- ✅ finance-forecasting
- ✅ tech-audit
- ✅ board-reporting
- ✅ market-analysis
- ✅ mcp-advisor
- ✅ finance-modeler
- ✅ finance-unit-economics
- ✅ investor-qa-generator

### Remaining (14 skills)
Due to token limitations, creating streamlined versions of remaining skills with core functionality.

## Quick Reference: Remaining Skills

### pitch-questions
**Purpose**: Generate tough questions CEO might receive during pitch
**Tools**: Read (pitch deck), Write (Q&A doc)
**Key Feature**: Categorized questions (Product/Market/Team/Finance)

### pitch-audit
**Purpose**: Review pitch deck for clarity, data accuracy, storytelling
**Tools**: Read (pitch deck), WebSearch (comps), Write (audit report)
**Key Feature**: Slide-by-slide audit with improvement suggestions

### landing-structure
**Purpose**: Best practices for landing page structure (hero, features, CTA, social proof)
**Tools**: Read (existing landing), Write (structure recommendations)
**Key Feature**: Conversion optimization checklist

### site-audit
**Purpose**: Accessibility (WCAG), SEO, performance audits
**Tools**: Read (HTML), Grep (patterns), Bash (Lighthouse CLI), Write (audit report)
**Key Feature**: Automated checks + manual review

### html-fixes
**Purpose**: Quick HTML/CSS bug fixes (responsive issues, accessibility)
**Tools**: Read (HTML), Edit (fixes), mcp__ide__getDiagnostics
**Key Feature**: Common pattern fixes (missing alt text, aria labels)

### design-language
**Purpose**: Design system consistency (colors, typography, spacing)
**Tools**: Read (CSS), Grep (design tokens), Write (style guide)
**Key Feature**: Token extraction and documentation

### marketing-alignment
**Purpose**: Align marketing messaging across channels
**Tools**: Read (marketing materials), Write (alignment doc)
**Key Feature**: Message consistency checker

### brand-analysis
**Purpose**: Analyze brand positioning and competitive differentiation
**Tools**: WebSearch (competitors), Read (brand guidelines), Write (analysis)
**Key Feature**: Brand perception vs reality gap analysis

### repo-analyzer
**Purpose**: Analyze repository structure, tech stack, complexity
**Tools**: Glob (file discovery), Read (package.json/requirements.txt), Bash (cloc)
**Key Feature**: Tech debt indicators, language breakdown

### repo-agent-suggester
**Purpose**: Recommend AI agents based on repository type
**Tools**: Read (repo structure), Write (agent recommendations)
**Key Feature**: Agent-to-task mapping (e.g., Python repo → CFO can use for finance scripts)

### stitch-integration
**Purpose**: Helpers for Stitch Data integration (ETL pipelines)
**Tools**: Read (Stitch config), Write (integration docs), WebSearch (Stitch docs)
**Key Feature**: Common integration patterns

### experiment-management
**Purpose**: A/B test tracking and analysis
**Tools**: Read (experiment data), mcp__ide__executeCode (statistical analysis), Write (results)
**Key Feature**: Statistical significance calculator

### prompt-generator-skill
**Purpose**: Generate optimized prompts for Claude Code
**Tools**: Read (task description), Write (prompt templates)
**Key Feature**: Prompt templates for common tasks

### skill-creator
**Purpose**: Meta-skill for creating new skills
**Tools**: Read (examples), Write (new skill.md), Edit (templates)
**Key Feature**: Skill template generator

## Usage Pattern for All Skills

```markdown
Используя [skill-name] skill, [specific task] для [Startup Name]

Examples:
- "Используя pitch-audit skill, review Sales AI pitch deck"
- "Используя site-audit skill, check Sales AI landing page accessibility"
- "Используя repo-analyzer skill, analyze Sales AI codebase"
```

## Tool Mapping Reference

| Original (GitHub Copilot) | Claude Code Equivalent |
|---------------------------|------------------------|
| `@workspace` search | `Grep`, `Glob` |
| Python REPL | `mcp__ide__executeCode` |
| File read/write | `Read`, `Write`, `Edit` |
| Terminal | `Bash` |
| Web search | `WebSearch`, `WebFetch` |
| Linter | `mcp__ide__getDiagnostics` |

## Priority for Completion

**High Priority** (next batch):
1. pitch-audit - Needed for Series A prep
2. site-audit - Needed for Sales AI landing page
3. landing-structure - Sales AI launch
4. skill-creator - Enable faster skill creation

**Medium Priority**:
- design-language
- marketing-alignment
- repo-analyzer

**Low Priority** (create on-demand):
- html-fixes (use Edit tool directly)
- stitch-integration (not currently used)
- experiment-management (future need)

## Next Steps

1. **Complete high-priority skills** (4 remaining)
2. **Update main README.md** with all 22 skills
3. **Test adapted skills** on Sales AI project
4. **Gather feedback** and iterate

## Token Optimization Strategy

To complete remaining 14 skills efficiently:
- **Core sections only**: Overview, Required Tools, 1-2 Usage Examples
- **Link to originals**: Reference `.github/skills/[name]/SKILL.md` for details
- **Focus on Claude Code specifics**: Tool usage, not general concepts
- **Batch creation**: Group similar skills together

## Version

- **Adapted**: 8/22 skills (36%)
- **Date**: 2026-02-10
- **Format**: Claude Code CLI skill.md format
