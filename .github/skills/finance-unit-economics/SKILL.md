# Навык: Finance Unit Economics

## Обзор

Назначение: Быстрый и корректный расчёт ключевых показателей unit-economics (LTV, CAC, Churn, Payback, LTV/CAC и др.) для использования CFO и других принимающих решений.

Целевые пользователи: `@CFO` (primary), `@CEO`, `@CMO`.

Все текстовые артефакты и комментарии в скриптах — на русском языке (требование `CFO`). Код остаётся работоспособным.

## Установка

Требования: Python 3.8+, pandas, numpy

```bash
pip install pandas numpy
```

## Компоненты

- `scripts/compute_unit_economics.py` — функции для расчёта LTV, CAC, churn, payback и проверки здоровья экономики.

## Примеры использования

```python
from compute_unit_economics import calculate_ltv, calculate_cac, ltv_cac_ratio

# Пример
ltv = calculate_ltv(arpu=120, gross_margin=0.75, monthly_churn=0.04)
cac = calculate_cac(sales_marketing_spend=120_000, new_customers=200)
ratio = ltv_cac_ratio(ltv, cac)

print(f"LTV: {ltv:.2f}")
print(f"CAC: {cac:.2f}")
print(f"LTV/CAC: {ratio:.2f}x")
```

## Best Practices

- Всегда сохраняйте входные предположения и исходные данные вместе со скриптом расчёта.
- Используйте версионирование файлов расчётов (commit) перед отправкой в Board.
