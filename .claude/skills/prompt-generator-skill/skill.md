# Prompt Generator Skill

## Overview
**Purpose**: Generate optimized prompts for Claude Code for common tasks.
**Target Users**: All agents (CEO, CFO, CTO, CMO)
**Capabilities**: Prompt templates for skills, task-specific prompt generation

## Required Tools
`Read`, `Write`

## Usage
```
"Используя prompt-generator-skill, generate prompt для CFO financial analysis task"

→ Output:
"Действуй как CFO агент согласно .github/agents/cfo.agent.md:

ЗАДАЧА: [Sales AI] Используя finance-forecasting skill, проведи следующий анализ:
1. Calculate runway при текущем burn rate
2. Generate 3 scenarios (conservative/base/optimistic)
3. Recommend fundraising timeline

ОБЯЗАТЕЛЬНО используй Python код из finance-forecasting skill.
Сохрани результаты в Sales AI/knowledge-base/02_Finance/analysis_2026_02_10.md"
```
