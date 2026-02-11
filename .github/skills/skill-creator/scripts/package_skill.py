#!/usr/bin/env python3
"""
Package a skill folder into a distributable .skill zip file.
Usage: python package_skill.py <path/to/skill-folder> [output-directory]
"""
import sys
import zipfile
from pathlib import Path
from scripts.quick_validate import validate_skill


def package_skill(skill_path, output_dir=None):
    skill_path = Path(skill_path).resolve()
    if not skill_path.exists() or not skill_path.is_dir():
        print(f"❌ Error: Skill folder not found: {skill_path}")
        return None
    valid, message = validate_skill(skill_path)
    if not valid:
        print(f"❌ Validation failed: {message}")
        return None
    if output_dir:
        output_path = Path(output_dir).resolve()
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path.cwd()
    skill_filename = output_path / f"{skill_path.name}.skill"
    try:
        with zipfile.ZipFile(skill_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in skill_path.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(skill_path.parent)
                    zipf.write(file_path, arcname)
                    print(f"  Added: {arcname}")
        print(f"\n✅ Successfully packaged skill to: {skill_filename}")
        return skill_filename
    except Exception as e:
        print(f"❌ Error creating .skill file: {e}")
        return None


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python package_skill.py <path/to/skill-folder> [output-directory]')
        sys.exit(1)
    result = package_skill(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    sys.exit(0 if result else 1)
