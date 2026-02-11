Repo Instructions Analyzer
=================================

Небольшая утилита и начальная реализация скилла для помощи в создании `*.instructions.md`.

Запуск:

PowerShell:

```powershell
python .github/skills/repo-analyzer/skill.py --root . --list
python .github/skills/repo-analyzer/skill.py --root . --create --files ci.instructions.md docker.instructions.md
```

Copilot-style templates:

Для генерации файлов, содержащих секции в стиле VS Code Copilot Custom Instructions, добавьте флаг `--copilot`.

Примеры:

```powershell
python .github/skills/repo-analyzer/skill.py --root . --list
python .github/skills/repo-analyzer/skill.py --root . --create --files ci.instructions.md --copilot
```

Описание:
- `--list` — показать рекомендации для текущего репозитория
- `--create --files <names>` — создать шаблонные инструкции
- `--copilot` — включить разделы "What would you like the assistant to know..." и "How would you like the assistant to respond..."
