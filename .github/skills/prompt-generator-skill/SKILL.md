---
name: prompt-generator-skill
description: Generate VS Code Copilot-style prompt files for Copilot/customization-like prompt templates. Use when a user needs a reusable prompt file template for code assistance or automation.
---
# Prompt Generator Skill

This skill provides a small script to generate prompt files compatible with VS Code Copilot-style prompt files. Use the bundled script when you want to create a prompt template quickly and consistently.

## Usage

- Run the generator script in `scripts/` to create a prompt file in `templates/`.
- The generated files are JSON prompt templates with fields: `displayName`, `description`, `scope`, `prompt`, and optional `placeholders`.

## Bundled resources

- `scripts/create_prompt.py` — CLI script to generate prompt templates.
- `templates/example.prompt.json` — example prompt template.
