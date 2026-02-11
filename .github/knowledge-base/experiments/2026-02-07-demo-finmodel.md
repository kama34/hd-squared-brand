---
title: "Demo: Financial model validation"
author: CFO
date_created: 2026-02-07
status: complete
owner: CFO
segment: Company-wide
---

## 1) Hypothesis (Гипотеза)
- Формулировка: При сохранении текущих показателей MRR=50k и OPEX=80k мы ожидаем сохранить положительный операционный статус в течение ≥12 месяцев и конечный баланс > 100k.
- Временной горизонт: 12 месяцев

## 2) Action (Действие)
- План: Построить проекцию cashflow на 12 месяцев, проверить runway, выполнить sensitivity analysis.
- Ресурсы: `finance-modeler` skill, исходные данные от accounting и sales.
- Start date / End date: 2026-02-07 / 2026-02-07 (demo)

## 3) Data (Данные)
- Primary metrics: Net Cash Flow, Cumulative Cash, Runway
- Data sources: demo assumptions (Starting Cash: 500000, Revenue: 50000, Expenses: 80000)
- Measurement plan: одномоментная проекция, затем scenario analysis

## 4) Insight (Выводы)
- Result summary: Конечный баланс через 12 мес = 140,000; текущий runway = 16.7 мес; runway после 12 мес = 4.7 мес.
- Decision: iterate — требуется сценарный анализ и план по увеличению выручки или сокращению burn.
- Next steps: CFO проведёт scenario analysis и добавит conservative/optimistic файлы в `.github/knowledge-base/02_Finance/`.
