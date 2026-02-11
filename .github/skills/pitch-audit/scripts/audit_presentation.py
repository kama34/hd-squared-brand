#!/usr/bin/env python3
"""Stub: convert a slide-structure text into an audit report skeleton."""
import json

def audit_stub(structure):
    # structure: list of {title, message}
    problems = []
    for s in structure:
        problems.append({
            "category": "LOGIC",
            "title": f"Check {s.get('title')}",
            "criticality": "Medium",
            "where": s.get('title'),
            "why": "Placeholder reasoning",
            "fix": ["Add concrete metric", "Tighten claim"],
        })
    return problems

if __name__ == '__main__':
    # example run
    sample = [{"title": "Cover", "message": "..."}, {"title": "Problem", "message": "..."}]
    print(json.dumps(audit_stub(sample), ensure_ascii=False, indent=2))
