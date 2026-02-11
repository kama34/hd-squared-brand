---
name: experiment-management
display_name: "Experiment Management"
version: 0.1
maintainers:
  - name: dev-team
    contact: ops@example.com
description: Навык для создания, трекинга и отчётности по гипотезам/экспериментам (HADI). Позволяет агентам создавать новые гипотезы, регистрировать результаты и получать сводку по активным экспериментам.
triggers:
  - "create_hypothesis"
  - "update_hypothesis"
  - "list_hypotheses"
  - "summarize_experiment"

usage:
  - Create hypothesis: `experiment-management.create_hypothesis(title, owner, segment, content_path)`
  - Update results: `experiment-management.update_hypothesis(hypothesis_path, results)`
  - List active: `experiment-management.list_hypotheses(status=running)`
  - Summarize: `experiment-management.summarize_experiment(hypothesis_path)`

files:
  - scripts/manage_hypotheses.py: helper script to scaffold and update hypothesis markdown files
  - references/: guidance and examples

notes: Use this skill from agents when creating or validating experiments; it writes artifacts to `.github/knowledge-base/experiments/` and can produce a short summary for Board/CEO.
---
