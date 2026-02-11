#!/usr/bin/env python3
"""Stub: generate a slide structure from collected answers."""
import json

def example_structure():
    return [
        {"title": "Cover", "message": "One-line value prop and ask"},
        {"title": "Problem", "message": "Who has the problem and how big it is"},
    ]

if __name__ == '__main__':
    print(json.dumps(example_structure(), ensure_ascii=False, indent=2))
