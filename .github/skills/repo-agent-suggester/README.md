Repo Agent Suggester
=====================

Usage:

- Analyze repository and show suggested agents:

```bash
python .github/skills/repo-agent-suggester/skill.py analyze --repo .
```

- Create a suggested agent by name:

```bash
python .github/skills/repo-agent-suggester/skill.py create --repo . --name ci-helper
```

- Improve an agent file with a note:

```bash
python .github/skills/repo-agent-suggester/skill.py improve --file .github/agents/ci-helper.agent.md --note "Add auto-labeling for docs"
```

Files:
- `SKILL.md` - skill metadata
- `skill.py` - analyzer and generator script
