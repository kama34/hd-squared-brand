#!/usr/bin/env python3
"""
Skill initializer - creates a new skill folder with template files.
Usage:
    python init_skill.py <skill-name> --path <output-directory>
"""
import sys
from pathlib import Path

SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Complete and informative explanation of what the skill does and when to use it.]
---

# {skill_title}

## Overview

[TODO]

"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""Example helper script for {skill_name}"""

def main():
    print("This is an example script for {skill_name}")

if __name__ == '__main__':
    main()
'''

EXAMPLE_REFERENCE = """# Reference for {skill_title}

This is a placeholder reference document.
"""

EXAMPLE_ASSET = """Example asset placeholder"""


def title_case_skill_name(skill_name):
    return " ".join(word.capitalize() for word in skill_name.split('-'))


def init_skill(skill_name, path):
    skill_dir = Path(path).resolve() / skill_name
    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    # Create SKILL.md
    skill_title = title_case_skill_name(skill_name)
    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(SKILL_TEMPLATE.format(skill_name=skill_name, skill_title=skill_title))
        print("✅ Created SKILL.md")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    # Create resource directories
    try:
        scripts_dir = skill_dir / 'scripts'
        scripts_dir.mkdir(exist_ok=True)
        (scripts_dir / 'example.py').write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
        print("✅ Created scripts/example.py")

        references_dir = skill_dir / 'references'
        references_dir.mkdir(exist_ok=True)
        (references_dir / 'reference.md').write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title))
        print("✅ Created references/reference.md")

        assets_dir = skill_dir / 'assets'
        assets_dir.mkdir(exist_ok=True)
        (assets_dir / 'example_asset.txt').write_text(EXAMPLE_ASSET)
        print("✅ Created assets/example_asset.txt")
    except Exception as e:
        print(f"❌ Error creating resource directories: {e}")
        return None

    print(f"\n✅ Skill '{skill_name}' initialized successfully at {skill_dir}")
    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_skill.py <skill-name> --path <path>")
        sys.exit(1)
    skill_name = sys.argv[1]
    path = sys.argv[3]
    init_skill(skill_name, path)

if __name__ == '__main__':
    main()
