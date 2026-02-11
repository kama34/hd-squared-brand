#!/usr/bin/env python3
"""Interactive helper to show steps to connect an MCP.

This script does NOT perform network operations. It prints recommended steps and checks.
"""
import argparse
import json
from pathlib import Path


MCP_GUIDE = {
    'mcp-code-search': {
        'name': 'Code Search / Indexer MCP',
        'steps': [
            'Install indexer service or choose hosted MCP',
            'Point indexer at repository root and run initial index',
            'Configure incremental updates (webhook or CI step)',
            'Test queries locally against the index',
        ],
    },
    'mcp-dep-scanner': {
        'name': 'Dependency Scanner MCP',
        'steps': [
            'Provide access to package manifests (package.json, requirements.txt, pyproject.toml)',
            'Run dependency scan and collect SBOM',
            'Configure periodic scans in CI',
        ],
    },
    'mcp-docker-inspector': {
        'name': 'Docker Inspector MCP',
        'steps': [
            'Locate Dockerfile(s) and build artifacts',
            'Scan built images or Dockerfile layers for vulnerabilities',
            'Expose image metadata to MCP for context retrieval',
        ],
    },
    'mcp-ci-listener': {
        'name': 'CI/CD Events MCP',
        'steps': [
            'Choose CI provider integration (GitHub Actions, GitLab, Jenkins)',
            'Create a service user/token with minimal permissions',
            'Configure webhook/event forwarding to MCP endpoint',
            'Map pipeline metadata fields to MCP context schema',
        ],
    },
}


def list_mcps():
    for k, v in MCP_GUIDE.items():
        print(f"{k}: {v['name']}")


def show_steps(mcp_id):
    m = MCP_GUIDE.get(mcp_id)
    if not m:
        print('Unknown MCP id. Available:')
        list_mcps()
        return
    print(f"Steps to connect {mcp_id} — {m['name']}:\n")
    for i, s in enumerate(m['steps'], 1):
        print(f"{i}. {s}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--mcp', help='MCP id to get connection steps for')
    args = p.parse_args()
    if not args.mcp:
        print('Available MCPs:')
        list_mcps()
        return
    show_steps(args.mcp)


if __name__ == '__main__':
    main()
