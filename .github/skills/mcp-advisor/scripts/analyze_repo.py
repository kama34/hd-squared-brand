#!/usr/bin/env python3
"""Analyze a repository and recommend MCPs (Model Context Protocol connectors).

Usage:
    python analyze_repo.py --path /path/to/repo [--output out.json]
"""
import argparse
import json
import os
from pathlib import Path


EXT_LANG_MAP = {
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.java': 'java',
    '.go': 'go',
    '.rs': 'rust',
    '.cs': 'csharp',
    '.cpp': 'cpp',
}


def find_files(root: Path):
    for p in root.rglob('*'):
        if p.is_file():
            yield p


def detect_languages(root: Path):
    counts = {}
    for f in find_files(root):
        ext = f.suffix.lower()
        lang = EXT_LANG_MAP.get(ext)
        if lang:
            counts[lang] = counts.get(lang, 0) + 1
    return counts


def detect_package_files(root: Path):
    files = []
    candidates = ['package.json', 'pyproject.toml', 'requirements.txt', 'Pipfile', 'go.mod', 'Cargo.toml', 'pom.xml']
    for name in candidates:
        for p in root.rglob(name):
            files.append(str(p.relative_to(root)))
    return files


def detect_infra(root: Path):
    infra = []
    for p in root.rglob('*'):
        if p.is_file():
            name = p.name.lower()
            if name == 'dockerfile' or name.endswith('dockerfile'):
                infra.append(str(p.relative_to(root)))
            if name in ('docker-compose.yml', 'docker-compose.yaml'):
                infra.append(str(p.relative_to(root)))
            if p.suffix in ('.yml', '.yaml'):
                try:
                    text = p.read_text(encoding='utf-8')
                except Exception:
                    text = ''
                if 'kind: deployment' in text.lower() or 'apiVersion:' in text:
                    infra.append(str(p.relative_to(root)))
    return list(set(infra))


def detect_ci(root: Path):
    ci = []
    for p in root.rglob('.github/workflows/*.yml'):
        ci.append(str(p.relative_to(root)))
    for name in ('Jenkinsfile', '.gitlab-ci.yml', '.circleci/config.yml'):
        for p in root.rglob(name):
            ci.append(str(p.relative_to(root)))
    return ci


def recommend_mcps(summary):
    recs = []
    languages = summary.get('languages', {})
    package_files = summary.get('package_files', [])
    infra = summary.get('infra', [])
    ci = summary.get('ci', [])

    # Always useful
    recs.append({
        'id': 'mcp-repo-history',
        'name': 'Repository history / blame MCP',
        'reason': 'Always useful to attach commit/author context to model queries',
        'confidence': 0.6,
    })

    # Code search
    if sum(languages.values()) > 0:
        recs.append({
            'id': 'mcp-code-search',
            'name': 'Code Search / Indexer MCP',
            'reason': f"Repository contains languages: {', '.join(languages.keys())}",
            'confidence': 0.9,
        })

    # Dependency scanning
    if package_files:
        recs.append({
            'id': 'mcp-dep-scanner',
            'name': 'Dependency Scanner MCP',
            'reason': f"Found package files: {', '.join(package_files)}",
            'confidence': 0.9,
        })

    # Container / infra
    if any('docker' in p.lower() or 'dockerfile' in p.lower() for p in infra):
        recs.append({
            'id': 'mcp-docker-inspector',
            'name': 'Docker/Container Inspector MCP',
            'reason': 'Repository contains Dockerfile/docker-compose',
            'confidence': 0.85,
        })

    if any('k8s' in p.lower() or 'kind: deployment' in ' '.join(infra).lower() for p in infra):
        recs.append({
            'id': 'mcp-k8s-inspector',
            'name': 'Kubernetes Inspector MCP',
            'reason': 'Repository contains Kubernetes manifests',
            'confidence': 0.8,
        })

    # CI / pipeline events
    if ci:
        recs.append({
            'id': 'mcp-ci-listener',
            'name': 'CI/CD Events MCP',
            'reason': 'Repository defines CI pipelines; CI events help attach runtime context',
            'confidence': 0.8,
        })

    # Security / secrets scanner
    if 'python' in languages or 'javascript' in languages:
        recs.append({
            'id': 'mcp-secrets-scanner',
            'name': 'Secrets & SCA MCP',
            'reason': 'Useful to scan for leaked secrets and SCA alerts in common languages',
            'confidence': 0.6,
        })

    return recs


def analyze(path: str):
    root = Path(path).resolve()
    languages = detect_languages(root)
    package_files = detect_package_files(root)
    infra = detect_infra(root)
    ci = detect_ci(root)

    summary = {
        'path': str(root),
        'languages': languages,
        'package_files': package_files,
        'infra': infra,
        'ci': ci,
    }

    summary['recommendations'] = recommend_mcps(summary)
    return summary


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--path', default='.', help='Path to repository root')
    p.add_argument('--output', help='Write JSON output to file')
    args = p.parse_args()

    summary = analyze(args.path)
    text = json.dumps(summary, indent=2, ensure_ascii=False)
    print(text)
    if args.output:
        Path(args.output).write_text(text, encoding='utf-8')


if __name__ == '__main__':
    main()
