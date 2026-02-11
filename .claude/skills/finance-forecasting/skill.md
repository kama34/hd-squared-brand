# Finance Forecasting Skill

## Overview

**Purpose**: Финансовое прогнозирование и расчет метрик для стартапов. Code-first подход для исключения ошибок и обеспечения воспроизводимости.

**Target Users**: CFO, CEO, Board

**Capabilities**:
- Runway calculation (месяцы до исчерпания cash)
- Cash flow projections (прогнозы на 3-12+ месяцев)
- Scenario analysis (консервативный/базовый/агрессивный сценарии)
- SaaS metrics (LTV, CAC, Churn, Magic Number, Payback Period)
- Unit economics health check

## Required Tools

Claude Code tools used by this skill:
- `mcp__ide__executeCode` - Execute Python calculations
- `Read` - Read financial data from knowledge base
- `Write` - Save calculation results
- `Edit` - Update financial reports

## Dependencies

Python packages required:
```bash
pip install pandas numpy
```

## Python Modules

### forecast_model.py

Functions for financial forecasting:
- `calculate_runway(cash_balance, monthly_burn)` - Calculate runway in months
- `project_cashflow(starting_cash, monthly_revenue, monthly_expenses, months)` - Project cash flow
- `scenario_analysis(scenarios, starting_cash, months)` - Compare scenarios
- `get_runway_status(runway_months)` - Get runway health status

### saas_metrics.py

Functions for SaaS metrics:
- `calculate_ltv(arpu, gross_margin, monthly_churn)` - Lifetime Value
- `calculate_cac(sales_marketing_spend, new_customers)` - Customer Acquisition Cost
- `calculate_payback_period(cac, arpu, gross_margin)` - Payback period in months
- `calculate_magic_number(new_arr_quarter, prior_quarter_sm_spend)` - Sales efficiency
- `calculate_churn(customers_start, customers_end, new_customers)` - Monthly churn rate
- `ltv_cac_ratio(ltv, cac)` - LTV/CAC ratio with health check
- `unit_economics_health_check(...)` - Complete unit economics analysis

## Usage Examples

### Example 1: Calculate Runway

```python
# Import module from skill directory
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-forecasting')
from forecast_model import calculate_runway, get_runway_status

# Load financial data from startup knowledge base
# Replace "Sales AI" with actual startup name
cash_balance = 750_000  # From knowledge base: Sales AI/knowledge-base/02_Finance/
monthly_burn = 50_000   # expenses - revenue

# Calculate runway
runway = calculate_runway(cash_balance, monthly_burn)
status = get_runway_status(runway)

# Display results
print(f"💰 Cash Balance: ${cash_balance:,}")
print(f"🔥 Monthly Burn: ${monthly_burn:,}")
print(f"⏱️  Runway: {runway} months")
print(f"{status['emoji']} {status['message']}")
```

**Output**:
```
💰 Cash Balance: $750,000
🔥 Monthly Burn: $50,000
⏱️  Runway: 15.0 months
✅ Healthy runway
```

### Example 2: Unit Economics Analysis

```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-forecasting')
from saas_metrics import unit_economics_health_check

# Load data from startup knowledge base
health = unit_economics_health_check(
    arpu=120,                      # Monthly revenue per customer
    gross_margin=0.75,             # 75% gross margin
    monthly_churn=0.04,            # 4% monthly churn
    sales_marketing_spend=120_000, # Last quarter S&M spend
    new_customers=200              # New customers acquired
)

# Display results
metrics = health['metrics']
print(f"📊 Unit Economics Analysis")
print(f"")
print(f"💵 ARPU: ${metrics['arpu']}")
print(f"📈 Gross Margin: {metrics['gross_margin']*100:.0f}%")
print(f"📉 Monthly Churn: {metrics['monthly_churn_pct']:.1f}%")
print(f"")
print(f"✨ LTV: ${metrics['ltv']:,.0f}")
print(f"💸 CAC: ${metrics['cac']:,.0f}")
print(f"🎯 LTV/CAC Ratio: {metrics['ltv_cac_ratio']:.1f}x")
print(f"⏱️  Payback Period: {metrics['payback_months']:.1f} months")
print(f"")

# Health status
ltv_cac_status = health['status']['ltv_cac']
payback_status = health['status']['payback']
overall_status = health['status']['overall']

print(f"{overall_status['emoji']} Overall Status: {overall_status['status'].upper()}")
print(f"{ltv_cac_status['emoji']} {ltv_cac_status['message']}")
print(f"{payback_status['emoji']} {payback_status['message']}")
```

**Output**:
```
📊 Unit Economics Analysis

💵 ARPU: $120
📈 Gross Margin: 75%
📉 Monthly Churn: 4.0%

✨ LTV: $2,250
💸 CAC: $600
🎯 LTV/CAC Ratio: 3.8x
⏱️  Payback Period: 6.7 months

✅ Overall Status: EXCELLENT
✅ EXCELLENT (LTV/CAC = 3.8x > 3x target)
✅ Payback: 6.7 months (target: <12mo)
```

### Example 3: Scenario Analysis

```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-forecasting')
from forecast_model import scenario_analysis

# Define scenarios
scenarios = {
    'Status Quo': (40_000, 70_000),      # (monthly_revenue, monthly_expenses)
    'Growth': (60_000, 100_000),         # Aggressive growth
    'Conservative': (40_000, 55_000)     # Cost cutting
}

# Run analysis
comparison = scenario_analysis(
    scenarios=scenarios,
    starting_cash=800_000,
    months=12
)

print("=== Scenario Comparison (12 months) ===")
print(comparison)
```

**Output**:
```
=== Scenario Comparison (12 months) ===
      Scenario  Ending_Cash  Total_Burn  Runway_Months
0   Status Quo       440000     -360000           12.3
1       Growth       320000     -480000            6.7
2  Conservative       620000     -180000           41.3
```

## Workflow: CFO Financial Report

**Trigger**: CEO requests financial update or weekly/monthly report

**Steps**:

1. **Read financial data** from startup knowledge base:
```python
# Use Read tool to access:
# - [Startup Name]/knowledge-base/02_Finance/financial_model_results_with_founders.json
# - [Startup Name]/knowledge-base/02_Finance/unit_economics_results.json
# - [Startup Name]/knowledge-base/02_Finance/runway_results.json
```

2. **Execute calculations** using Python modules:
```python
# Use mcp__ide__executeCode tool to run:
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-forecasting')
from forecast_model import calculate_runway, get_runway_status
from saas_metrics import unit_economics_health_check

# ... calculations ...
```

3. **Generate report** in Markdown:
```markdown
## Weekly Financial Report

**Date**: 2026-02-10

### Cash Position
💰 **Cash Balance**: $750,000
🔥 **Monthly Burn Rate**: $50,000
⏱️  **Runway**: 15.0 months
✅ **Status**: Healthy runway

### Unit Economics (Q1 2026)
✨ **LTV**: $2,250
💸 **CAC**: $600
🎯 **LTV/CAC**: 3.8x ✅
⏱️  **Payback**: 6.7 months ✅

### Recommendations
- Continue current burn rate
- Consider hiring 2 engineers in Q2
- Start fundraising conversations in Q4 2026
```

4. **Save results** to knowledge base:
```python
# Use Write tool to save to:
# [Startup Name]/knowledge-base/02_Finance/reports/weekly_report_2026_02_10.md
```

## Critical Rules

### CFO Code-First Rule

**MANDATORY**: CFO must ALWAYS use Python code for calculations. Never calculate "in your head" or use approximations.

**Bad** ❌:
> "LTV примерно $2,000, так что LTV/CAC где-то 3x"

**Good** ✅:
```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-forecasting')
from saas_metrics import calculate_ltv, calculate_cac, ltv_cac_ratio

ltv = calculate_ltv(arpu=120, gross_margin=0.75, monthly_churn=0.04)
cac = calculate_cac(120_000, 200)
ratio = ltv_cac_ratio(ltv, cac)
print(f"LTV: ${ltv:,.0f}, CAC: ${cac:,.0f}, Ratio: {ratio['ratio']}x")
```

### Document Assumptions

Always document assumptions in code comments:

```python
# Assumptions:
# - ARPU stable at $120/month (based on last 3 months average)
# - Churn: 4% (Q1 2026 actual from CRM data)
# - Gross Margin: 75% (server costs 20%, payment processing 5%)
ltv = calculate_ltv(arpu=120, gross_margin=0.75, monthly_churn=0.04)
```

### Startup Isolation

Always specify which startup's data you're analyzing:

```python
# Correct: Specify startup name
startup_name = "Sales AI"
finance_path = f"{startup_name}/knowledge-base/02_Finance/"

# Read data from correct startup
# ... load data from finance_path ...
```

## Benchmarks & Interpretation

### Runway Status

| Runway | Status | Action |
|--------|--------|--------|
| < 3 months | 🔴 CRITICAL | Start fundraising IMMEDIATELY |
| 3-6 months | ⚠️ WARNING | Start fundraising NOW |
| 6+ months | ✅ Healthy | Continue monitoring |
| Profitable | 🟢 Excellent | No fundraising needed |

### LTV/CAC Ratio

| Ratio | Status | Interpretation |
|-------|--------|----------------|
| > 3x | ✅ Excellent | Healthy unit economics |
| 2-3x | 🟡 Acceptable | Room for improvement |
| < 2x | 🔴 Poor | Unit economics broken |

### Payback Period

| Period | Status | Interpretation |
|--------|--------|----------------|
| < 12 months | ✅ Excellent | Fast payback |
| 12-18 months | 🟡 Acceptable | Moderate payback |
| > 18 months | 🔴 Poor | Too slow payback |

### Magic Number (Sales Efficiency)

| Magic Number | Status | Interpretation |
|--------------|--------|----------------|
| > 1.0 | ✅ Excellent | Highly efficient sales |
| 0.75-1.0 | 🟡 Good | Good efficiency |
| 0.5-0.75 | 🟢 Acceptable | Acceptable |
| < 0.5 | 🔴 Poor | Inefficient sales |

## Integration with Other Skills

### board-reporting
Financial data from this skill feeds into Board Decks:
- Runway calculations → Cash Position slide
- Unit economics → Metrics Dashboard
- Scenario analysis → Strategic Options

### market-analysis
CAC data by channel informs GTM strategy decisions.

### tech-audit
Burn rate analysis helps CTO prioritize infrastructure cost optimization.

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'pandas'"

**Solution**:
```bash
pip install pandas numpy
```

### Problem: "ZeroDivisionError in calculate_ltv"

**Cause**: Churn rate = 0 (invalid - would result in infinite LTV)

**Solution**: Use minimum observed churn (e.g., 0.01 for 1%)

### Problem: "Runway calculation returns infinity"

**Cause**: Monthly burn ≤ 0 (company is profitable or break-even)

**Interpretation**: Infinite runway means no fundraising urgency

## Version History

- **2026-02-10**: Adapted for Claude Code CLI from GitHub Copilot skill
  - Added mcp__ide__executeCode integration
  - Updated import paths for Claude Code environment
  - Added explicit startup isolation guidelines
- **2026-02-05**: Original GitHub Copilot version
  - forecast_model.py, saas_metrics.py modules
  - SKILL.md documentation

## Related Files

- `forecast_model.py` - Runway, cash flow, scenario analysis
- `saas_metrics.py` - LTV, CAC, churn, magic number calculations
- `.github/skills/finance-forecasting/` - Original GitHub Copilot version
