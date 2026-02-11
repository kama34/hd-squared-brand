#!/usr/bin/env python3
import argparse
import json
import os
import sys


def build_obj(args):
    out = {
        "displayName": args.name,
        "description": args.description or "",
        "scope": args.scope if isinstance(args.scope, list) else [s.strip() for s in args.scope.split(',') if s.strip()],
        "prompt": args.prompt,
    }
    if args.placeholders:
        try:
            ph = json.loads(args.placeholders)
        except Exception as e:
            print("Invalid placeholders JSON:\n", e, file=sys.stderr)
            sys.exit(2)
        out["placeholders"] = ph
    return out


def main():
    p = argparse.ArgumentParser(description="Create a Copilot-style prompt template JSON file")
    p.add_argument("--name", required=True, help="Display name for the prompt template")
    p.add_argument("--description", default="", help="Short description")
    p.add_argument("--prompt", required=True, help="The prompt text (can contain placeholders)")
    p.add_argument("--scope", default="*", help="Comma-separated list of scopes/languages (e.g. javascript,typescript)")
    p.add_argument("--placeholders", help='JSON string describing placeholders (e.g. "{\"goal\":{\"description\":\"...\"}}")')
    p.add_argument("--output-dir", default=os.path.join(os.path.dirname(__file__), '..', 'templates'), help="Output directory for templates")
    args = p.parse_args()

    outdir = os.path.abspath(args.output_dir)
    os.makedirs(outdir, exist_ok=True)

    safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in args.name).strip().replace(' ', '_')
    filename = f"{safe_name}.prompt.json"
    path = os.path.join(outdir, filename)

    obj = build_obj(args)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

    print(f"Wrote prompt template: {path}")


if __name__ == '__main__':
    main()
