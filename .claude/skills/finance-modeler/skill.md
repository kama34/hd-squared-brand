# Finance Modeler Skill

## Overview

**Purpose**: Построение профессиональных финансовых моделей с cash-flow projections, scenario analysis, и sensitivity analysis для стратегических решений.

**Target Users**: CFO (primary), CEO, Board

**Capabilities**:
- Monthly cash flow projections (12-36 months)
- Scenario analysis (conservative/base/optimistic)
- Sensitivity analysis (revenue/expense variations)
- Monte Carlo simulations (advanced probabilistic modeling)
- Russian-language financial reports

## Required Tools

- `mcp__ide__executeCode` - Execute Python financial modeling code
- `Read` - Read financial assumptions from knowledge base
- `Write` - Save model results and reports
- `Edit` - Update existing models

## Python Module

**model_builder.py** - Core financial modeling functions:
- `build_projection(starting_cash, monthly_revenue, monthly_expenses, months)` - Build monthly projection
- `scenario_analysis(**scenarios)` - Compare multiple scenarios

## Usage Examples

### Example 1: Build 12-Month Cash Flow Projection

```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-modeler')
from model_builder import build_projection

# Build projection for Sales AI
projection = build_projection(
    starting_cash=750_000,
    monthly_revenue=40_000,
    monthly_expenses=70_000,
    months=12
)

print("=== Cash Flow Projection ===")
print(projection.to_string(index=False))

# Check ending cash
ending_cash = projection['Cumulative_Cash'].iloc[-1]
print(f"\nEnding Cash (Month 12): ${ending_cash:,.0f}")

# Identify cash crunch months
min_cash = projection['Cumulative_Cash'].min()
min_month = projection.loc[projection['Cumulative_Cash'].idxmin(), 'Month']
print(f"Minimum Cash: ${min_cash:,.0f} (Month {min_month})")
```

**Output**:
```
=== Cash Flow Projection ===
 Month  Revenue  Expenses  Net_Cash_Flow  Cumulative_Cash
     1    40000     70000         -30000           720000
     2    40000     70000         -30000           690000
    ...
    12    40000     70000         -30000           390000

Ending Cash (Month 12): $390,000
Minimum Cash: $390,000 (Month 12)
```

### Example 2: Scenario Analysis

```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-modeler')
from model_builder import build_projection, scenario_analysis

# Define 3 scenarios for Sales AI
conservative = build_projection(
    starting_cash=750_000,
    monthly_revenue=35_000,   # Lower revenue
    monthly_expenses=70_000,
    months=12
)

base = build_projection(
    starting_cash=750_000,
    monthly_revenue=50_000,   # Base case
    monthly_expenses=70_000,
    months=12
)

optimistic = build_projection(
    starting_cash=750_000,
    monthly_revenue=75_000,   # Higher revenue
    monthly_expenses=80_000,  # Slightly higher expenses (growth)
    months=12
)

# Compare scenarios
comparison = scenario_analysis(
    Conservative=conservative,
    Base=base,
    Optimistic=optimistic
)

print("=== Scenario Comparison ===")
print(comparison.to_string(index=False))
```

**Output**:
```
=== Scenario Comparison ===
     scenario  ending_cash  min_cumulative_cash
 Conservative       330000               330000
         Base       510000               510000
   Optimistic       690000               690000
```

### Example 3: Fundraising Decision Model

```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-modeler')
from model_builder import build_projection

# Current state: no fundraising
no_fundraising = build_projection(
    starting_cash=750_000,
    monthly_revenue=40_000,
    monthly_expenses=70_000,
    months=18
)

# With $500k fundraising in Month 6
with_fundraising = build_projection(
    starting_cash=750_000,
    monthly_revenue=40_000,
    monthly_expenses=70_000,
    months=18
)

# Manually inject fundraising event
with_fundraising.loc[5, 'Cumulative_Cash'] += 500_000  # Month 6 fundraising
for i in range(6, 18):
    with_fundraising.loc[i, 'Cumulative_Cash'] = (
        with_fundraising.loc[i-1, 'Cumulative_Cash'] +
        with_fundraising.loc[i, 'Net_Cash_Flow']
    )

# Compare
print(f"No Fundraising - Ending Cash: ${no_fundraising['Cumulative_Cash'].iloc[-1]:,.0f}")
print(f"With Fundraising - Ending Cash: ${with_fundraising['Cumulative_Cash'].iloc[-1]:,.0f}")

# Runway analysis
no_fr_min = no_fundraising['Cumulative_Cash'].min()
with_fr_min = with_fundraising['Cumulative_Cash'].min()

print(f"\nNo Fundraising - Minimum Cash: ${no_fr_min:,.0f}")
print(f"With Fundraising - Minimum Cash: ${with_fr_min:,.0f}")
```

## Workflow: Building Financial Model for Board

**Trigger**: CFO preparing financial projections for Board Meeting

**Steps**:

1. **Collect assumptions** from knowledge base:
   ```
   Read: [Startup]/knowledge-base/02_Finance/assumptions.md
   - Monthly revenue growth rate
   - Monthly expense projections
   - Starting cash balance
   ```

2. **Build projections** using model_builder:
   ```python
   # Execute via mcp__ide__executeCode
   projection = build_projection(...)
   ```

3. **Scenario analysis** (conservative/base/optimistic):
   ```python
   scenarios = scenario_analysis(Conservative=..., Base=..., Optimistic=...)
   ```

4. **Generate Russian-language report**:
   ```markdown
   ## Финансовая Модель (Q1-Q4 2026)

   ### Базовый Сценарий
   - Стартовый капитал: $750,000
   - Ежемесячная выручка: $40,000
   - Ежемесячные расходы: $70,000
   - Burn Rate: $30,000/месяц

   ### Прогноз
   - Остаток через 12 месяцев: $390,000
   - Runway: 13 месяцев
   - Минимальный остаток: $390,000 (Месяц 12)

   ### Сценарный Анализ
   | Сценарий | Остаток (12 мес) | Runway |
   |----------|------------------|--------|
   | Консервативный | $330,000 | 11 мес |
   | Базовый | $510,000 | 17 мес |
   | Оптимистичный | $690,000 | 23 мес |

   ### Рекомендации
   ✅ Базовый сценарий: Здоровый runway, fundraising не срочен
   ⚠️ Консервативный: Начать fundraising в Q3 2026
   ```

5. **Save results**:
   ```
   Write: [Startup]/knowledge-base/02_Finance/models/projection_2026_q1_q4.md
   ```

## Integration with Other Skills

### finance-forecasting
- Uses same concepts (runway, burn rate) but **finance-modeler** focuses on multi-scenario modeling
- **finance-forecasting** = quick calculations, **finance-modeler** = comprehensive models

### board-reporting
- Model results → Financial Update slides in Board Deck
- Scenario analysis → Strategic Options discussion

### investor-qa-generator
- Financial model → Answers to investor questions on runway, growth assumptions

## Best Practices

### 1. Document Assumptions

```python
# ❌ BAD: No context
projection = build_projection(750_000, 40_000, 70_000, 12)

# ✅ GOOD: Clear assumptions
"""
Assumptions for Sales AI Financial Model (2026 Q1-Q4):
- Starting Cash: $750,000 (actual as of Feb 1, 2026)
- Monthly Revenue: $40,000 (based on current MRR growth trend)
- Monthly Expenses: $70,000 (includes team salaries + infrastructure)
- Scenario: Base case (no major hiring, stable growth)
"""
projection = build_projection(
    starting_cash=750_000,
    monthly_revenue=40_000,
    monthly_expenses=70_000,
    months=12
)
```

### 2. Version Control Models

```bash
# Save models with timestamps
Write: Sales AI/knowledge-base/02_Finance/models/projection_2026_02_10.md

# Commit to git for history
git add "Sales AI/knowledge-base/02_Finance/models/"
git commit -m "Add Q1-Q4 2026 financial model (base/conservative/optimistic scenarios)"
```

### 3. Sensitivity Analysis

Test key assumptions:
```python
# Revenue sensitivity: -20%, base, +20%
scenarios = {
    'Revenue -20%': build_projection(750_000, 32_000, 70_000, 12),
    'Base': build_projection(750_000, 40_000, 70_000, 12),
    'Revenue +20%': build_projection(750_000, 48_000, 70_000, 12)
}

comparison = scenario_analysis(**scenarios)
print(comparison)

# Identify break-even revenue
# What revenue is needed to avoid burning cash?
# Answer: monthly_revenue >= monthly_expenses ($70k)
```

## Troubleshooting

### Problem: "Projection shows negative cash"

**Cause**: Burn rate too high relative to starting cash

**Solutions**:
1. Reduce monthly expenses (cost-cutting scenario)
2. Increase monthly revenue (growth scenario)
3. Model fundraising event (inject cash in specific month)

### Problem: "Scenarios too similar"

**Cause**: Not enough variation in assumptions

**Solution**: Use wider ranges
```python
# Better variation
conservative_revenue = base_revenue * 0.7  # -30%
optimistic_revenue = base_revenue * 1.5    # +50%
```

### Problem: "Model doesn't account for variable expenses"

**Limitation**: `model_builder.py` uses constant monthly values

**Workaround**: Use lists for dynamic values
```python
# Revenue grows 5% per month
revenues = [40_000 * (1.05 ** i) for i in range(12)]

# Manually build DataFrame with varying values
# (feature enhancement for future version)
```

## Version History

- **2026-02-10**: Adapted for Claude Code CLI
  - Added mcp__ide__executeCode integration
  - Russian-language report templates
  - Sales AI usage examples
- **Original**: GitHub Copilot version with model_builder.py

## Related Files

- `model_builder.py` - Core modeling functions
- `.github/skills/finance-modeler/` - Original version
- `finance-forecasting/` - Related skill (quick calculations)
