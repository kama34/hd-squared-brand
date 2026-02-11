# Finance Forecasting Skill

## Overview

**Purpose**: Обеспечить CFO и других руководителей готовыми Python-скриптами для финансовых расчетов, прогнозирования и unit-экономики. Все вычисления должны быть code-based для исключения человеческих ошибок и обеспечения воспроизводимости.

**Target Users**: @CFO (primary), @CEO, @Board

**Dependencies**: Python 3.8+, pandas, numpy, matplotlib (опционально для графиков)

---

## Installation

```bash
pip install pandas numpy matplotlib
```

---

## Components

### 1. `forecast_model.py`

Python-модуль для прогнозирования Runway, Cash Flow и Burn Rate.

**Functions**:
- `calculate_runway(cash_balance, monthly_burn)` → Runway в месяцах
- `project_cashflow(starting_cash, monthly_revenue, monthly_expenses, months)` → DataFrame с прогнозом
- `scenario_analysis(base_case, best_case, worst_case)` → Comparison table

**Usage Example**:
```python
from forecast_model import calculate_runway, project_cashflow

# Runway calculation
runway = calculate_runway(cash_balance=500_000, monthly_burn=50_000)
print(f"Runway: {runway} months")  # Output: 10 months

# Cash flow projection
projection = project_cashflow(
    starting_cash=500_000,
    monthly_revenue=30_000,
    monthly_expenses=50_000,
    months=12
)
print(projection)
```

### 2. `saas_metrics.py`

Расчет SaaS-специфичных метрик: LTV, CAC, Churn, Magic Number, Payback Period.

**Functions**:
- `calculate_ltv(arpu, gross_margin, monthly_churn)` → Lifetime Value
- `calculate_cac(sales_marketing_spend, new_customers)` → Customer Acquisition Cost
- `calculate_payback_period(cac, arpu, gross_margin)` → Payback Period в месяцах
- `calculate_magic_number(new_arr_quarter, prior_quarter_sm_spend)` → Magic Number (sales efficiency)
- `calculate_churn(customers_start, customers_end, new_customers)` → Monthly Churn %
- `ltv_cac_ratio(ltv, cac)` → LTV/CAC ratio с health check

**Usage Example**:
```python
from saas_metrics import calculate_ltv, calculate_cac, ltv_cac_ratio

# LTV
ltv = calculate_ltv(arpu=100, gross_margin=0.8, monthly_churn=0.05)  # $1,600

# CAC
cac = calculate_cac(sales_marketing_spend=50_000, new_customers=100)  # $500

# LTV/CAC ratio
ratio = ltv_cac_ratio(ltv=1600, cac=500)
print(ratio)  # 3.2x ✅ Healthy (>3x target)
```

---

## Use Cases

### Use Case 1: CFO готовит еженедельный отчет по Runway

**Scenario**: @CEO спрашивает: "Сколько у нас Runway?"

**CFO Process (Code-First)**:
```python
from forecast_model import calculate_runway

# Данные из банковского аккаунта
cash_balance = 750_000

# Burn rate за последний месяц
revenue_last_month = 45_000
expenses_last_month = 95_000
burn_rate = expenses_last_month - revenue_last_month  # $50,000/month

# Расчет Runway
runway_months = calculate_runway(cash_balance, burn_rate)

print(f"💰 Cash Balance: ${cash_balance:,}")
print(f"🔥 Monthly Burn: ${burn_rate:,}")
print(f"⏱️  Runway: {runway_months:.1f} months")

if runway_months < 3:
    print("🔴 CRITICAL: Start fundraising IMMEDIATELY")
elif runway_months < 6:
    print("⚠️  WARNING: Start fundraising NOW")
else:
    print("✅ Healthy runway")
```

**Report to @CEO**:
```markdown
## Weekly Финансовый отчет

**Дата**: 2026-02-05

💰 **Cash Balance**: $750,000  
🔥 **Monthly Burn Rate**: $50,000  
⏱️  **Runway**: 15.0 months  

✅ **Статус**: Healthy runway

**Комментарий**: При текущем burn rate ($50k/месяц) мы можем работать 15 месяцев без дополнительного финансирования. Следующий раунд рекомендуется начинать в Q4 2026 (через 9 месяцев).
```

---

### Use Case 2: @CFO анализирует Unit Economics для Board Meeting

**Scenario**: @Board запрашивает: "Здоровая ли наша unit-economics?"

**CFO Process**:
```python
from saas_metrics import (
    calculate_ltv, 
    calculate_cac, 
    ltv_cac_ratio,
    calculate_payback_period
)

# Данные за последний квартал
arpu = 120  # Average Revenue Per User (monthly)
gross_margin = 0.75  # 75% gross margin
monthly_churn = 0.04  # 4% churn
sales_marketing_spend = 120_000
new_customers = 200

# Расчеты
ltv = calculate_ltv(arpu, gross_margin, monthly_churn)
cac = calculate_cac(sales_marketing_spend, new_customers)
ratio = ltv_cac_ratio(ltv, cac)
payback = calculate_payback_period(cac, arpu, gross_margin)

# Отчет
print(f"📊 Unit Economics Analysis (Q1 2026)")
print(f"")
print(f"💵 ARPU (Monthly): ${arpu}")
print(f"📈 Gross Margin: {gross_margin*100:.0f}%")
print(f"📉 Monthly Churn: {monthly_churn*100:.1f}%")
print(f"")
print(f"✨ LTV: ${ltv:,.0f}")
print(f"💸 CAC: ${cac:,.0f}")
print(f"🎯 LTV/CAC Ratio: {ratio:.1f}x")
print(f"⏱️  Payback Period: {payback:.1f} months")
print(f"")

# Health check
if ratio >= 3:
    print("✅ Health Status: EXCELLENT (LTV/CAC > 3x)")
elif ratio >= 2:
    print("🟡 Health Status: ACCEPTABLE (LTV/CAC 2-3x, improve efficiency)")
else:
    print("🔴 Health Status: CRITICAL (LTV/CAC < 2x, unit economics broken)")
```

**Output**:
```
📊 Unit Economics Analysis (Q1 2026)

💵 ARPU (Monthly): $120
📈 Gross Margin: 75%
📉 Monthly Churn: 4.0%

✨ LTV: $2,250
💸 CAC: $600
🎯 LTV/CAC Ratio: 3.8x
⏱️  Payback Period: 6.7 months

✅ Health Status: EXCELLENT (LTV/CAC > 3x)
```

**Board Slide**:
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| LTV | $2,250 | $1,500+ | ✅ Strong |
| CAC | $600 | <$1,000 | ✅ Efficient |
| LTV/CAC | 3.8x | >3x target | ✅ Excellent |
| Payback | 6.7mo | <12mo | ✅ Fast |

---

### Use Case 3: Scenario Planning для Pivot Decision

**Scenario**: @CEO рассматривает pivot и просит @CFO показать финансовые последствия.

**CFO Process**:
```python
from forecast_model import project_cashflow, scenario_analysis
import pandas as pd

# Current state
starting_cash = 800_000

# Сценарий 1: Status Quo (продолжаем текущую стратегию)
status_quo = project_cashflow(
    starting_cash=starting_cash,
    monthly_revenue=40_000,
    monthly_expenses=70_000,
    months=12
)

# Сценарий 2: Pivot (6 месяцев на переход, затем рост)
# Первые 6 месяцев: revenue падает (-30%), expenses растут (+20% на R&D)
# Следующие 6 месяцев: revenue растет (+50% от нового baseline)
pivot_revenue = [28_000] * 6 + [60_000] * 6  # -30%, затем +50%
pivot_expenses = [84_000] * 6 + [70_000] * 6  # +20%, затем норма

pivot_projection = pd.DataFrame({
    'Month': range(1, 13),
    'Revenue': pivot_revenue,
    'Expenses': pivot_expenses,
    'Net_Cash_Flow': [r - e for r, e in zip(pivot_revenue, pivot_expenses)]
})
pivot_projection['Cumulative_Cash'] = starting_cash + pivot_projection['Net_Cash_Flow'].cumsum()

# Сценарий 3: Aggressive Growth (удваиваем маркетинг)
growth = project_cashflow(
    starting_cash=starting_cash,
    monthly_revenue=40_000 * 1.15,  # +15%/month growth
    monthly_expenses=100_000,  # +$30k на маркетинг
    months=12
)

print("=== SCENARIO COMPARISON ===\n")

print("Scenario 1: Status Quo")
print(f"  Ending Cash: ${status_quo['Cumulative_Cash'].iloc[-1]:,.0f}")
print(f"  Runway: {status_quo['Cumulative_Cash'].iloc[-1] / 30_000:.1f} months\n")

print("Scenario 2: Pivot")
print(f"  Ending Cash: ${pivot_projection['Cumulative_Cash'].iloc[-1]:,.0f}")
print(f"  Risk: Revenue uncertainty during transition\n")

print("Scenario 3: Aggressive Growth")
print(f"  Ending Cash: ${growth['Cumulative_Cash'].iloc[-1]:,.0f}")
print(f"  Risk: Burns cash faster, needs fundraising\n")
```

**Recommendation to @CEO**:
```markdown
## Financial Scenario Analysis: Pivot Decision

| Scenario | Ending Cash (12mo) | Risk | Recommendation |
|----------|-------------------|------|----------------|
| **Status Quo** | $440,000 | Low | ✅ Safe but slow growth |
| **Pivot** | $128,000 | High | ⚠️ Risky, needs validation first |
| **Aggressive Growth** | -$80,000 | Critical | 🔴 Requires Series A ASAP |

**CFO Recommendation**: 
- Avoid full pivot without validation (ending cash too low)
- Consider hybrid: Test pivot in parallel with current product (costs +$10k/mo)
- If pivot validated → execute
- Otherwise → Status Quo + optimize unit economics
```

---

## Files Structure

```
.github/skills/finance-forecasting/
├── SKILL.md                    # This file (overview + use cases)
├── forecast_model.py           # Runway, cash flow, projections
├── saas_metrics.py             # LTV, CAC, Churn, etc.
└── examples/
    ├── runway_report.py        # Example: weekly runway report
    ├── unit_economics.py       # Example: unit economics analysis
    └── scenario_planning.py    # Example: pivot scenario modeling
```

---

## Best Practices

### 1. Always Use Code for Calculations

**NEVER** calculate in your head or use approximations.

**Bad** ❌:
> "LTV примерно $1,500, так что LTV/CAC где-то 3x"

**Good** ✅:
```python
ltv = calculate_ltv(arpu=100, gross_margin=0.8, monthly_churn=0.05)
cac = calculate_cac(50_000, 100)
ratio = ltv / cac  # Exact: 3.2x
```

### 2. Document Assumptions

Всегда явно указывайте предположения в комментариях:

```python
# Assumptions:
# - ARPU stable at $120/month (based on last 3 months avg)
# - Churn: 4% (Q1 2026 actual)
# - Gross Margin: 75% (server costs 20%, payment processing 5%)
ltv = calculate_ltv(arpu=120, gross_margin=0.75, monthly_churn=0.04)
```

### 3. Version Control Financial Models

Сохраняйте исторические версии расчетов:

```python
# saved to: .github/knowledge-base/02_Finance/calculations/runway_2026_02_05.py
```

---

## Integration with Agents

### @CFO
- **Primary user** — использует этот навык для ВСЕХ финансовых расчетов
- **Requirement**: Code-First rule = ОБЯЗАТЕЛЬНО использовать этот навык

### @CEO
- Запрашивает у @CFO отчеты, генерируемые этим навыком
- Не выполняет код напрямую (делегирует @CFO)

### @Board
- Получает результаты через @CFO (Board Decks, Scenario analyses)

---

## Troubleshooting

**Problem**: "Division by zero" в calculate_ltv

**Cause**: Churn rate = 0 (невозможно — LTV = ∞)

**Solution**: 
```python
if monthly_churn == 0:
    raise ValueError("Churn rate cannot be 0. Use minimum observed churn (e.g., 0.01).")
```

**Problem**: Negative Runway

**Cause**: Cash Flow положительный (revenue > expenses)

**Solution**:
```python
if burn_rate <= 0:
    return float('inf')  # Infinite runway (profitable)
```

---

## Changelog

- **2026-02-05**: Initial version (forecast_model.py, saas_metrics.py)
- **TBD**: Add plotting functions (matplotlib visualizations)
- **TBD**: Add Monte Carlo simulation for uncertainty modeling
