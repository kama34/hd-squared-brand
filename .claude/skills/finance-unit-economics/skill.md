# Finance Unit Economics Skill

## Overview

**Purpose**: Быстрый и точный расчет ключевых показателей unit-economics (LTV, CAC, Churn, Payback, LTV/CAC) для принятия решений о growth стратегии.

**Target Users**: CFO (primary), CEO, CMO

**Capabilities**:
- LTV (Lifetime Value) calculation
- CAC (Customer Acquisition Cost) calculation
- Churn rate analysis
- Payback period computation
- LTV/CAC ratio health check
- Russian-language reports

## Required Tools

- `mcp__ide__executeCode` - Execute Python calculations
- `Read` - Read customer/revenue data from knowledge base
- `Write` - Save unit economics reports

## Python Module

**compute_unit_economics.py** - Core unit economics functions (Russian comments):
- `calculate_ltv(arpu, gross_margin, monthly_churn)` - Lifetime Value
- `calculate_cac(sales_marketing_spend, new_customers)` - Customer Acquisition Cost
- `ltv_cac_ratio(ltv, cac)` - LTV/CAC ratio
- `calculate_payback_period(cac, arpu, gross_margin)` - Months to recover CAC
- `calculate_churn(customers_start, customers_end, new_customers)` - Monthly churn rate

## Usage Examples

### Example 1: Basic Unit Economics Calculation

```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-unit-economics')
from compute_unit_economics import (
    calculate_ltv,
    calculate_cac,
    ltv_cac_ratio,
    calculate_payback_period
)

# Sales AI data (Q1 2026)
arpu = 120                      # $120/month average revenue per user
gross_margin = 0.75             # 75% gross margin
monthly_churn = 0.04            # 4% monthly churn
sales_marketing_spend = 120_000 # $120k S&M spend last quarter
new_customers = 200             # 200 new customers acquired

# Calculate metrics
ltv = calculate_ltv(arpu, gross_margin, monthly_churn)
cac = calculate_cac(sales_marketing_spend, new_customers)
ratio = ltv_cac_ratio(ltv, cac)
payback = calculate_payback_period(cac, arpu, gross_margin)

# Display results
print("=== Unit Economics Analysis ===")
print(f"ARPU: ${arpu}/month")
print(f"Gross Margin: {gross_margin*100:.0f}%")
print(f"Monthly Churn: {monthly_churn*100:.1f}%")
print(f"")
print(f"LTV: ${ltv:,.2f}")
print(f"CAC: ${cac:,.2f}")
print(f"LTV/CAC Ratio: {ratio:.2f}x")
print(f"Payback Period: {payback:.1f} months")

# Health check
if ratio >= 3:
    print("✅ Excellent unit economics (LTV/CAC > 3x)")
elif ratio >= 2:
    print("🟡 Acceptable unit economics (LTV/CAC 2-3x)")
else:
    print("🔴 Poor unit economics (LTV/CAC < 2x)")
```

**Output**:
```
=== Unit Economics Analysis ===
ARPU: $120/month
Gross Margin: 75%
Monthly Churn: 4.0%

LTV: $2,250.00
CAC: $600.00
LTV/CAC Ratio: 3.75x
Payback Period: 6.7 months
✅ Excellent unit economics (LTV/CAC > 3x)
```

### Example 2: Churn Analysis

```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-unit-economics')
from compute_unit_economics import calculate_churn

# Sales AI customer data
customers_start = 115  # Customers at start of month
customers_end = 118    # Customers at end of month
new_customers = 8      # New customers acquired

# Calculate churn
churn_rate = calculate_churn(customers_start, customers_end, new_customers)

print(f"Customers Start: {customers_start}")
print(f"New Customers: {new_customers}")
print(f"Customers End: {customers_end}")
print(f"Customers Lost: {customers_start + new_customers - customers_end}")
print(f"Monthly Churn Rate: {churn_rate*100:.2f}%")

# Benchmark
if churn_rate < 0.05:
    print("✅ Churn is healthy (<5% for SMB SaaS)")
elif churn_rate < 0.08:
    print("⚠️ Churn is elevated (5-8%)")
else:
    print("🔴 Churn is critical (>8%)")
```

**Output**:
```
Customers Start: 115
New Customers: 8
Customers End: 118
Customers Lost: 5
Monthly Churn Rate: 4.35%
✅ Churn is healthy (<5% for SMB SaaS)
```

### Example 3: CAC by Channel Analysis

```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-unit-economics')
from compute_unit_economics import calculate_cac

# Sales AI marketing channels (Q1 2026)
channels = {
    'Content Marketing': {'spend': 30_000, 'customers': 80},
    'Google Ads': {'spend': 50_000, 'customers': 70},
    'LinkedIn Ads': {'spend': 25_000, 'customers': 30},
    'Referrals': {'spend': 5_000, 'customers': 20}  # Low spend (just incentives)
}

print("=== CAC by Channel ===\n")
results = []
for channel, data in channels.items():
    cac = calculate_cac(data['spend'], data['customers'])
    results.append({
        'Channel': channel,
        'CAC': cac,
        'Customers': data['customers'],
        'Spend': data['spend']
    })

# Sort by CAC (best to worst)
results.sort(key=lambda x: x['CAC'])

for r in results:
    print(f"{r['Channel']:20s} - CAC: ${r['CAC']:6.2f} ({r['Customers']} customers, ${r['Spend']:,} spend)")

# Recommendation
best_channel = results[0]
print(f"\n✅ Best Channel: {best_channel['Channel']} (CAC: ${best_channel['CAC']:.2f})")
print(f"Recommendation: Increase budget allocation to {best_channel['Channel']}")
```

**Output**:
```
=== CAC by Channel ===

Referrals             - CAC: $250.00 (20 customers, $5,000 spend)
Content Marketing     - CAC: $375.00 (80 customers, $30,000 spend)
Google Ads            - CAC: $714.29 (70 customers, $50,000 spend)
LinkedIn Ads          - CAC: $833.33 (30 customers, $25,000 spend)

✅ Best Channel: Referrals (CAC: $250.00)
Recommendation: Increase budget allocation to Referrals
```

## Workflow: Quarterly Unit Economics Review

**Trigger**: End of quarter (Q1, Q2, Q3, Q4)

**Steps**:

1. **Collect data** from knowledge base:
   ```
   Read: [Startup]/knowledge-base/02_Finance/revenue_data_q1_2026.json
   Read: [Startup]/knowledge-base/04_Marketing/marketing_spend_q1_2026.csv
   ```

2. **Calculate metrics**:
   ```python
   # Execute via mcp__ide__executeCode
   ltv = calculate_ltv(arpu, gross_margin, monthly_churn)
   cac = calculate_cac(total_sm_spend, total_new_customers)
   ratio = ltv_cac_ratio(ltv, cac)
   payback = calculate_payback_period(cac, arpu, gross_margin)
   ```

3. **Generate Russian report**:
   ```markdown
   ## Анализ Unit-Economics (Q1 2026)

   ### Основные Метрики
   - ARPU: $120/месяц
   - Gross Margin: 75%
   - Monthly Churn: 4.0%

   ### Результаты
   - **LTV**: $2,250
   - **CAC**: $600
   - **LTV/CAC**: 3.75x ✅ Отлично
   - **Payback**: 6.7 месяцев ✅ Быстро

   ### Динамика (QoQ)
   | Метрика | Q4 2025 | Q1 2026 | Изменение |
   |---------|---------|---------|-----------|
   | LTV | $2,400 | $2,250 | -6.3% ⚠️ |
   | CAC | $650 | $600 | -7.7% ✅ |
   | Ratio | 3.7x | 3.75x | +1.4% ✅ |

   ### Выводы
   - ✅ LTV/CAC ratio остается здоровым (>3x)
   - ⚠️ LTV снизился из-за роста churn (3.5% → 4.0%)
   - ✅ CAC улучшился благодаря более эффективным каналам

   ### Рекомендации
   1. Приоритет: Снизить churn до <3.5% (улучшить onboarding)
   2. Продолжить оптимизацию CAC (фокус на Referrals)
   3. Целевой LTV/CAC для Q2: 4.0x
   ```

4. **Save report**:
   ```
   Write: [Startup]/knowledge-base/02_Finance/unit_economics_q1_2026.md
   ```

5. **Present to Board** (integrate with board-reporting skill)

## Integration with Other Skills

### finance-forecasting
- CAC data → Used in runway calculations
- Churn rate → Affects revenue projections

### board-reporting
- Unit economics metrics → Key Metrics Dashboard in Board Deck
- LTV/CAC trends → Financial Health slide

### market-analysis
- CAC by channel → GTM strategy decisions (CMO)
- Payback period → Budget allocation

## Best Practices

### 1. Use Realistic Churn Rates

```python
# ❌ BAD: Overly optimistic
monthly_churn = 0.01  # 1% - unrealistic for early-stage SaaS

# ✅ GOOD: Industry benchmarks
monthly_churn = 0.04  # 4% - realistic for SMB SaaS
monthly_churn = 0.02  # 2% - realistic for Enterprise SaaS
```

### 2. Account for Gross Margin Correctly

```python
# Gross Margin = (Revenue - COGS) / Revenue
# COGS includes: hosting, payment processing, customer support (direct costs)
# Exclude: sales, marketing, R&D (operating expenses)

# Example for Sales AI:
# Revenue: $120/month
# COGS: $30/month (hosting $20 + payment fees $10)
# Gross Margin = ($120 - $30) / $120 = 0.75 (75%)

gross_margin = 0.75  # Realistic for SaaS
```

### 3. Track CAC by Cohort

```python
# Track CAC for each customer acquisition cohort
cohorts = {
    '2026-01': {'spend': 40_000, 'customers': 70, 'cac': 571},
    '2026-02': {'spend': 38_000, 'customers': 65, 'cac': 585},
    '2026-03': {'spend': 42_000, 'customers': 75, 'cac': 560}
}

# Identify trends
# Is CAC improving or worsening?
```

## Troubleshooting

### Problem: "LTV calculation returns error (churn = 0)"

**Cause**: No customer churn observed yet (too early-stage)

**Solution**: Use minimum realistic churn
```python
# Use industry benchmark if no data
monthly_churn = 0.03  # 3% - conservative estimate
```

### Problem: "LTV/CAC ratio looks too good to be true"

**Causes**:
1. Churn rate too low (overly optimistic)
2. Gross margin too high (excluding some costs)
3. CAC too low (not including all S&M expenses)

**Solution**: Audit assumptions
```python
# Check:
# 1. Is churn rate realistic? (Compare to industry benchmarks)
# 2. Are all COGS included in gross margin?
# 3. Are all S&M expenses (salaries + ads + tools) in CAC?
```

### Problem: "Payback period longer than investor expectations"

**Benchmark**: Investors want payback < 12 months

**Solutions**:
1. Reduce CAC (optimize channels, referrals)
2. Increase ARPU (pricing optimization, upsells)
3. Improve gross margin (reduce COGS)

```python
# Example: What ARPU needed for 12-month payback?
target_payback = 12  # months
current_cac = 600
gross_margin = 0.75

required_arpu = current_cac / (target_payback * gross_margin)
print(f"Required ARPU for 12-month payback: ${required_arpu:.2f}/month")
# Output: Required ARPU: $66.67/month
# Current ARPU: $120/month ✅ Already meeting target
```

## Version History

- **2026-02-10**: Adapted for Claude Code CLI
  - Added mcp__ide__executeCode integration
  - CAC by channel analysis examples
  - Russian-language report templates
- **Original**: GitHub Copilot version with compute_unit_economics.py

## Related Files

- `compute_unit_economics.py` - Core calculation functions
- `.github/skills/finance-unit-economics/` - Original version
- `finance-forecasting/saas_metrics.py` - Alternative (English version)
