# Навык: Finance Modeler (Профессиональное финансовое моделирование)

## Обзор

Назначение: На основе unit-economics и прикладных предположений строить профессиональную финансовую модель (cash-flow projection, scenario analysis, sensitivity, простая Monte Carlo) и генерировать отчёты на русском языке для `@CFO`, `@CEO` и `@Board`.

Целевые пользователи: `@CFO` (primary), `@CEO`, `@Board`.

## Установка

```bash
pip install pandas numpy
```

## Компоненты

- `scripts/model_builder.py` — сборка финансовой модели по входным предположениям и unit-economics, сценарный анализ и вывод summary на русском.

## Примеры использования

```python
from model_builder import build_projection, scenario_analysis

# Пример построения проекции
projection = build_projection(starting_cash=500_000, monthly_revenue=50_000, monthly_expenses=80_000, months=12)
print(projection.tail())

# Пример сценарного анализа
scenarios = scenario_analysis(base=projection, conservative=..., optimistic=...)
print(scenarios)
```

## Output

Генерируется таблица с помесячным прогнозом, сводка сценариев и короткий текстовый отчёт на русском с выводом рекомендаций.
