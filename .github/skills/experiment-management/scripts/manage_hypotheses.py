#!/usr/bin/env python3
"""Simple helper to create and update HADI hypothesis markdown files.

Usage:
  python manage_hypotheses.py create "Title" --owner "Name" --segment "persona"
  python manage_hypotheses.py update path/to/hypothesis.md --status complete --insight "..."
"""
import argparse
import os
import datetime


BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '..', '..', '..')
KB_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'knowledge-base'))
EXPERIMENTS_DIR = os.path.join(os.path.dirname(KB_DIR), 'knowledge-base', 'experiments')


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def slugify(s):
    return ''.join(c if c.isalnum() else '-' for c in s).lower()


def create_hypothesis(title, owner, segment):
    ensure_dir(EXPERIMENTS_DIR)
    date = datetime.date.today().isoformat()
    filename = f"{date}-{slugify(title)}.md"
    path = os.path.join(EXPERIMENTS_DIR, filename)
    if os.path.exists(path):
        print('Hypothesis already exists:', path)
        return path
    content = f"""---
title: \"{title}\"
author: {owner}
date_created: {date}
status: draft
owner: {owner}
segment: {segment}
---

## 1) Hypothesis (Гипотеза)

- Формулировка: 
- Временной горизонт: 

## 2) Action (Действие)

- План: 
- Ресурсы: 
- Start date / End date: 
- Rollout strategy / Safety: 

## 3) Data (Данные)

- Primary metrics: 
- Secondary metrics: 
- Data sources: 
- Measurement plan: 

## 4) Insight (Выводы)

- Result summary: 
- Decision: 
- Next steps: 

"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Created hypothesis:', path)
    return path


def update_hypothesis(path, status=None, insight=None):
    if not os.path.exists(path):
        print('Not found:', path)
        return
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()
    if status:
        txt = txt.replace('status: draft', f'status: {status}')
        txt = txt.replace('status: running', f'status: {status}')
    if insight:
        txt += f"\n\n### Update {datetime.date.today().isoformat()}\n{insight}\n"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(txt)
    print('Updated hypothesis:', path)


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='cmd')
    p1 = sub.add_parser('create')
    p1.add_argument('title')
    p1.add_argument('--owner', default='unknown')
    p1.add_argument('--segment', default='all')
    p2 = sub.add_parser('update')
    p2.add_argument('path')
    p2.add_argument('--status')
    p2.add_argument('--insight')

    args = parser.parse_args()
    if args.cmd == 'create':
        create_hypothesis(args.title, args.owner, args.segment)
    elif args.cmd == 'update':
        update_hypothesis(args.path, status=args.status, insight=args.insight)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
