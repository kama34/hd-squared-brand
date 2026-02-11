#!/usr/bin/env python3
"""
Quick validation script for a skill's SKILL.md frontmatter.
Usage: python quick_validate.py <skill_directory>
"""
import sys
import re
import yaml
from pathlib import Path

ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata'}


def validate_skill(skill_path):
    skill_path = Path(skill_path)
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, 'SKILL.md not found'
    content = skill_md.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False, 'No YAML frontmatter found'
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, 'Invalid frontmatter format'
    frontmatter_text = match.group(1)
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, 'Frontmatter must be a YAML dictionary'
    except Exception as e:
        return False, f'Invalid YAML in frontmatter: {e}'

    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, f"Unexpected key(s) in frontmatter: {', '.join(sorted(unexpected_keys))}"
    if 'name' not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    name = str(frontmatter.get('name','')).strip()
    if name and not re.match(r'^[a-z0-9-]+$', name):
        return False, "Name should be hyphen-case (lowercase letters, digits, and hyphens only)"
    if len(name) > 64:
        return False, 'Name is too long (max 64 characters)'
    description = str(frontmatter.get('description','')).strip()
    if '<' in description or '>' in description:
        return False, 'Description cannot contain angle brackets (< or >)'
    if len(description) > 1024:
        return False, 'Description too long (max 1024 characters)'

    return True, 'Skill is valid!'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python quick_validate.py <skill_directory>')
        sys.exit(1)
    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
