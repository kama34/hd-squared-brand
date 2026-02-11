#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Небольшая утилита для анализа репозитория и генерации шаблонов `*.instructions.md`.

Примеры:
  python skill.py --root . --list
  python skill.py --root . --create --files ci.instructions.md docker.instructions.md
"""
import os
import argparse
from pathlib import Path

SUGGESTIONS = [
    {
        "name": "ci.instructions.md",
        "triggers": [".github/workflows", "azure-pipelines.yml", "circleci", ".gitlab-ci.yml"],
        "title": "CI / Continuous Integration",
        "description": "Как запускается CI, какие проверки, как добавлять новые шаги.",
        "copilot_about": "Этот проект использует CI для автоматической проверки PR, включая линтинг, тесты и сборку артефактов.",
        "copilot_response": "Делай ответы компактными, предоставляй команды и примеры шагов для CI, отмечай потенциальные риски."
    },
    {
        "name": "docker.instructions.md",
        "triggers": ["Dockerfile"],
        "title": "Docker / контейнеризация",
        "description": "Как собирать и запускать контейнеры, теги, оптимизация образов.",
        "copilot_about": "Репозиторий содержит Dockerfile для образа сервиса, цель — воспроизводимая сборка и легкие образы.",
        "copilot_response": "Отвечай с примерами команд Docker, советами по оптимизации слоев и best-practices для безопасности."
    },
    {
        "name": "packaging.instructions.md",
        "triggers": ["setup.py", "pyproject.toml", "package.json"],
        "title": "Packaging / публикация",
        "description": "Как собирать и публиковать пакеты / артефакты.",
        "copilot_about": "Проект публикуется как пакет (PyPI/npm), нужна инструкция по сборке и публикации.",
        "copilot_response": "Давать шаги для сборки артефактов, проверки и безопасной публикации с примерами команд."
    },
    {
        "name": "contributing.instructions.md",
        "triggers": ["CONTRIBUTING.md"],
        "title": "Contributing",
        "description": "Правила для контрибьюторов, код-стайл, PR-шаблоны.",
        "copilot_about": "Репозиторий открыт для контрибуций, есть ожидания по стилю кода и процессу ревью.",
        "copilot_response": "Форматируй рекомендации по шагам (форк → ветка → PR), приводя чек-лист для PR."
    },
    {
        "name": "docs.instructions.md",
        "triggers": ["docs", "mkdocs.yml", "docs/"],
        "title": "Документация",
        "description": "Как работать с документацией, как добавлять страницы и собирать сайт.",
        "copilot_about": "Документация поддерживается в `docs/` и собирается с помощью MkDocs.",
        "copilot_response": "Предлагай структуру страниц, шаблоны для документации и команды сборки."
    },
    {
        "name": "release.instructions.md",
        "triggers": ["CHANGELOG.md", "RELEASE.md"],
        "title": "Релизы",
        "description": "Процедура релизов, формирование релизных заметок, семантическое версионирование.",
        "copilot_about": "Релизы делаются вручную/автоматически; важно поддерживать CHANGELOG и теги.",
        "copilot_response": "Давай шаги для подготовки релиза, генерации заметок и тегирования."
    }
]


def find_existing_instructions(root: Path):
    existing = set()
    for path in root.rglob("*.instructions.md"):
        existing.add(path.name)
    return existing


def analyze(root: Path):
    found = set()
    for s in SUGGESTIONS:
        for trig in s["triggers"]:
            # check as path or filename
            if (root / trig).exists():
                found.add(s["name"])
                break
            # search for pattern in tree
            for p in root.rglob(trig):
                if p.exists():
                    found.add(s["name"])
                    break
    return found


def create_template(path: Path, title: str, description: str):
    content = f"""# {title}

Описание: {description}

## Цель

Коротко — зачем нужна эта инструкция.

## Содержание

- Шаги для начинающих
- Часто встречающиеся проблемы
- Примеры команд

## Примеры

```bash
# команды сборки / проверки
```
"""
    path.write_text(content, encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description="Repo instructions analyzer and generator")
    p.add_argument("--root", default='.', help="Корень репозитория")
    p.add_argument("--list", action='store_true', help="Показать рекомендации")
    p.add_argument("--create", action='store_true', help="Создать выбранные шаблоны")
    p.add_argument("--files", nargs="*", help="Какие файлы создать (имена из рекомендаций)")
    p.add_argument("--copilot", action='store_true', help="Включить секции в стиле Copilot Custom Instructions")
    args = p.parse_args()

    root = Path(args.root).resolve()
    existing = find_existing_instructions(root)
    recommendations = analyze(root)

    # Filter out that already existing
    to_create = sorted(recommendations - existing)

    if args.list or (not args.create and not args.files):
        print("Рекомендуемые инструкции (найдено триггеров):")
        for name in to_create:
            s = next(x for x in SUGGESTIONS if x['name'] == name)
            print(f"- {name}: {s['title']} — {s['description']}")
        if existing:
            print('\nНайдены уже существующие *.instructions.md:')
            for e in sorted(existing):
                print(f"- {e}")
        return

    # create mode
    files = args.files or to_create
    if not files:
        print("Нет файлов для создания.")
        return

    for fname in files:
        s = next((x for x in SUGGESTIONS if x['name'] == fname), None)
        target = root / fname
        if s is None:
            # allow custom name
            if target.exists():
                print(f"Уже существует: {fname}")
                continue
            target.write_text(f"# {fname}\n\n_Шаблонная инструкция._\n", encoding='utf-8')
            print(f"Создан {target}")
            continue

        if target.exists():
            print(f"Пропущено (уже есть): {fname}")
            continue
        # create with optional Copilot-style prompts
        if args.copilot:
            copilot_block = (
                "## Custom instructions for AI assistants\n\n"
                "**What would you like the assistant to know about your project to provide better responses?**\n"
                f"{s.get('copilot_about', '')}\n\n"
                "**How would you like the assistant to respond?**\n"
                f"{s.get('copilot_response', '')}\n\n"
            )
            # write combined content
            create_template(target, s['title'], s['description'])
            # prepend copilot_block to file
            original = target.read_text(encoding='utf-8')
            target.write_text(copilot_block + original, encoding='utf-8')
        else:
            create_template(target, s['title'], s['description'])
        print(f"Создан {target}")


if __name__ == '__main__':
    main()
