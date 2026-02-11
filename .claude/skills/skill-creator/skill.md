# Skill Creator Skill (Meta-Skill)

## Overview
**Purpose**: Meta-skill для создания новых skills по шаблону.
**Target Users**: Skill Creator agent, CTO
**Capabilities**: Skill template generation, structure validation, documentation scaffolding

## Required Tools
`Read` (existing skills as templates), `Write`, `Edit`

## Usage
```
"Используя skill-creator skill, create new skill 'customer-success-metrics'"

→ Analyzes existing skill patterns (finance-forecasting, tech-audit, etc.)
→ Generates skill.md template with:
  - Overview (Purpose, Target Users, Capabilities)
  - Required Tools (Claude Code tools used)
  - Usage Examples (3 minimum)
  - Workflows (trigger → process → result)
  - Integration with Other Skills
  - Best Practices
  - Troubleshooting
  - Version History

→ Creates directory structure:
  .claude/skills/customer-success-metrics/
  ├── skill.md
  └── [supporting files as needed]
```

## Skill Template Structure

```markdown
# [Skill Name] Skill

## Overview
**Purpose**: [One-line description]
**Target Users**: [Primary agents]
**Capabilities**:
- [Capability 1]
- [Capability 2]

## Required Tools
- `[Tool 1]` - [Usage]
- `[Tool 2]` - [Usage]

## Usage Examples

### Example 1: [Scenario]
[Full example with Sales AI context]

## Workflow
1. [Step 1]
2. [Step 2]

## Integration with Other Skills
- **[skill-name]** - [How they integrate]

## Best Practices
### 1. [Practice Title]
❌ BAD: [Anti-pattern]
✅ GOOD: [Best practice]

## Troubleshooting
### Problem: "[Issue]"
**Solution**: [Fix]

## Version History
- **2026-02-10**: Adapted for Claude Code CLI
```
