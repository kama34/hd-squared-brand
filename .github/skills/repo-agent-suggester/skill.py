#!/usr/bin/env python3
"""Repo Agent Suggester

Scans a repository and suggests agents to place in .github/agents.
Can create simple agent files and append improvements.

This script is intentionally dependency-free (stdlib only).
"""

from pathlib import Path
import argparse
import json
import textwrap
import re


def scan_repo(root: Path):
    root = Path(root)
    info = {
        "has_package_json": False,
        "has_pyproject": False,
        "has_requirements": False,
        "has_dockerfile": False,
        "has_workflows": False,
        "has_tests": False,
        "has_readme": False,
        "languages": set(),
    }

    for p in root.rglob("*"):
        if p.is_file():
            name = p.name.lower()
            if name == "package.json":
                info["has_package_json"] = True
                info["languages"].add("javascript")
            if name in ("pyproject.toml",):
                info["has_pyproject"] = True
                info["languages"].add("python")
            if name in ("requirements.txt", "requirements-dev.txt"):
                info["has_requirements"] = True
                info["languages"].add("python")
            if name == "dockerfile":
                info["has_dockerfile"] = True
            if "/.github/workflows/" in str(p).replace("\\", "/"):
                info["has_workflows"] = True
            if re.search(r"test|pytest|_test\.(js|ts|py)$", name):
                info["has_tests"] = True
            if name.startswith("readme"):
                info["has_readme"] = True

    info["languages"] = sorted(info["languages"])
    return info


def propose_agents(info):
    proposals = []

    # CI helper
    if not info.get("has_workflows"):
        proposals.append({
            "id": "ci-helper",
            "title": "CI helper",
            "description": "Create basic CI workflows (build, test, lint) and PR checks.",
            "tasks": [
                "Add .github/workflows/ci.yml with build/test steps",
                "Run linters and tests on PRs",
            ],
        })

    # Test runner
    if info.get("has_tests"):
        proposals.append({
            "id": "test-runner",
            "title": "Test runner",
            "description": "Run and report tests, collect coverage, and comment results on PRs.",
            "tasks": ["Execute test suite", "Upload coverage report"],
        })

    # Dependency updater
    proposals.append({
        "id": "dependency-updater",
        "title": "Dependency updater",
        "description": "Scan and open PRs for dependency updates (npm, pip).",
        "tasks": ["Run dependency checks", "Open upgrade PRs with changelogs"],
    })

    # Docker / build
    if info.get("has_dockerfile"):
        proposals.append({
            "id": "docker-builder",
            "title": "Docker builder",
            "description": "Build, scan and publish Docker images on release.",
            "tasks": ["Build image", "Run a security scan", "Publish to registry"],
        })

    # Security scanner
    proposals.append({
        "id": "security-scanner",
        "title": "Security scanner",
        "description": "Run static dependency/security scanning and report findings.",
        "tasks": ["Run SAST/OSS scans", "Open issues for critical findings"],
    })

    # Release manager
    proposals.append({
        "id": "release-manager",
        "title": "Release manager",
        "description": "Manage changelogs, tag releases, and publish artifacts.",
        "tasks": ["Compile changelog", "Create semantic-release PRs/tags"],
    })

    # Docs keeper
    if info.get("has_readme"):
        proposals.append({
            "id": "doc-maintainer",
            "title": "Doc maintainer",
            "description": "Run checks for docs, build docs site, and open doc PRs for missing docs.",
            "tasks": ["Check README and docs links", "Build docs site"],
        })

    return proposals


def sanitize_filename(name: str):
    return re.sub(r"[^a-z0-9_-]", "-", name.lower())


AGENT_TEMPLATE = """---
id: {id}
title: {title}
description: {description}
---

# {title}

Description:

{description}

Tasks:

{tasks_md}

Improvements:

- (none yet)
"""


def create_agent_file(agent: dict, agents_dir: Path):
    agents_dir = Path(agents_dir)
    agents_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{sanitize_filename(agent['id'])}.agent.md"
    path = agents_dir / filename
    tasks_md = "\n".join([f"- {t}" for t in agent.get("tasks", [])])
    content = AGENT_TEMPLATE.format(
        id=agent.get("id", ""),
        title=agent.get("title", ""),
        description=agent.get("description", ""),
        tasks_md=tasks_md,
    )
    path.write_text(content, encoding="utf-8")
    return path


def improve_agent_file(path: Path, note: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    text = p.read_text(encoding="utf-8")
    new = text + "\n- " + note + "\n"
    p.write_text(new, encoding="utf-8")
    return p


def main():
    parser = argparse.ArgumentParser(prog="repo-agent-suggester")
    sub = parser.add_subparsers(dest="cmd")

    a_scan = sub.add_parser("analyze")
    a_scan.add_argument("--repo", default='.')
    a_scan.add_argument("--out", help="write proposals JSON to file")

    a_create = sub.add_parser("create")
    a_create.add_argument("--repo", default='.')
    a_create.add_argument("--name", required=True, help="agent id or proposal id to create")
    a_create.add_argument("--agents-dir", default=".github/agents")

    a_createall = sub.add_parser("create-all")
    a_createall.add_argument("--repo", default='.')
    a_createall.add_argument("--agents-dir", default=".github/agents")

    a_improve = sub.add_parser("improve")
    a_improve.add_argument("--file", required=True)
    a_improve.add_argument("--note", required=True)

    args = parser.parse_args()

    if args.cmd == "analyze":
        info = scan_repo(Path(args.repo))
        proposals = propose_agents(info)
        out = {"repo": str(Path(args.repo)), "info": info, "proposals": proposals}
        print(json.dumps(out, indent=2, ensure_ascii=False))
        if getattr(args, "out", None):
            Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
        return

    if args.cmd == "create":
        proposals = propose_agents(scan_repo(Path(args.repo)))
        found = None
        for p in proposals:
            if p["id"] == args.name or p["title"].lower() == args.name.lower():
                found = p
                break
        if not found:
            print("Agent name not found among proposals. Creating minimal agent.")
            found = {"id": args.name, "title": args.name, "description": "User-created agent", "tasks": []}
        path = create_agent_file(found, Path(args.agents_dir))
        print(f"Created agent file: {path}")
        return

    if args.cmd == "create-all":
        proposals = propose_agents(scan_repo(Path(args.repo)))
        created = []
        for p in proposals:
            created.append(str(create_agent_file(p, Path(args.agents_dir))))
        print("Created:")
        print("\n".join(created))
        return

    if args.cmd == "improve":
        p = improve_agent_file(Path(args.file), args.note)
        print(f"Updated {p}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
