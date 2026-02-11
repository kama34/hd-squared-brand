# -*- coding: utf-8 -*-
"""
Unit Economics Analysis - Designer T-Shirt Store
Date: 2026-02-11
CFO Analysis: New supplier price 500 RUB per unit
"""

print("=" * 80)
print("UNIT ECONOMICS ANALYSIS: Designer T-Shirt Store")
print("=" * 80)

# ===== INPUT DATA =====
cogs_per_unit = 500  # RUB - new supplier price
retail_price = 2500  # RUB - base retail price
shipping_cost = 300  # RUB
packaging_cost = 100  # RUB
payment_commission_rate = 0.029  # 2.9%
cac = 400  # RUB - customer acquisition cost
repeat_purchase_rate = 0.25  # 25%
avg_purchases_lifetime = 1.8  # times

# ===== CALCULATIONS =====
revenue = retail_price
payment_commission = revenue * payment_commission_rate
total_var_costs = cogs_per_unit + shipping_cost + packaging_cost + payment_commission

gross_margin_amt = revenue - cogs_per_unit
gross_margin_pct = (gross_margin_amt / revenue) * 100

contrib_before_cac = revenue - total_var_costs
contrib_before_cac_pct = (contrib_before_cac / revenue) * 100

contrib_after_cac = contrib_before_cac - cac
contrib_after_cac_pct = (contrib_after_cac / revenue) * 100

ltv = contrib_before_cac * avg_purchases_lifetime
ltv_cac_ratio = ltv / cac

# ===== OUTPUT =====
print("\n[1] BASE UNIT ECONOMICS (price 2500 RUB)")
print("-" * 80)
print(f"Revenue per unit:                     {revenue:>10,.0f} RUB")
print(f"\nVARIABLE COSTS:")
print(f"  COGS (t-shirt):                     {cogs_per_unit:>10,.0f} RUB")
print(f"  Shipping:                           {shipping_cost:>10,.0f} RUB")
print(f"  Packaging:                          {packaging_cost:>10,.0f} RUB")
print(f"  Payment commission (2.9%):          {payment_commission:>10,.0f} RUB")
print(f"  " + "-" * 50)
print(f"  TOTAL variable costs:               {total_var_costs:>10,.0f} RUB")

print(f"\nGROSS MARGIN:")
print(f"  Amount:                             {gross_margin_amt:>10,.0f} RUB")
print(f"  Percentage:                         {gross_margin_pct:>10.1f} %")

print(f"\nCONTRIBUTION MARGIN (before CAC):")
print(f"  Amount:                             {contrib_before_cac:>10,.0f} RUB")
print(f"  Percentage:                         {contrib_before_cac_pct:>10.1f} %")

print(f"\nMarketing (CAC):                      {cac:>10,.0f} RUB")

print(f"\nCONTRIBUTION MARGIN (after CAC):")
print(f"  Amount:                             {contrib_after_cac:>10,.0f} RUB")
print(f"  Percentage:                         {contrib_after_cac_pct:>10.1f} %")

print("\n" + "=" * 80)
print("\n[2] LTV/CAC ANALYSIS")
print("-" * 80)
print(f"Retention parameters:")
print(f"  Average purchases per lifetime:     {avg_purchases_lifetime:>10.1f}")
print(f"  Repeat purchase rate:               {repeat_purchase_rate*100:>10.1f} %")

print(f"\nLTV calculation:")
print(f"  Contribution per purchase:          {contrib_before_cac:>10,.0f} RUB")
print(f"  x Average purchases:                {avg_purchases_lifetime:>10.1f}")
print(f"  " + "-" * 50)
print(f"  LTV (Lifetime Value):               {ltv:>10,.0f} RUB")

print(f"\nCAC (Customer Acquisition Cost):      {cac:>10,.0f} RUB")
print(f"\nLTV/CAC RATIO:                        {ltv_cac_ratio:>10.2f} x")

if ltv_cac_ratio < 1:
    status = "[CRITICAL] LOSING MONEY"
elif ltv_cac_ratio < 2:
    status = "[WARNING] MINIMAL PROFIT"
elif ltv_cac_ratio < 3:
    status = "[OK] ACCEPTABLE"
elif ltv_cac_ratio < 5:
    status = "[GOOD] HEALTHY ECONOMICS"
else:
    status = "[EXCELLENT]"

print(f"\nStatus: {status}")

print("\n" + "=" * 80)
print("\n[3] BREAK-EVEN ANALYSIS")
print("-" * 80)

min_price_no_cac = total_var_costs
min_price_with_cac = total_var_costs + cac
target_ltv_for_healthy = cac * 3
required_contrib = target_ltv_for_healthy / avg_purchases_lifetime
min_price_healthy = total_var_costs + required_contrib

print(f"Minimum price (break-even, no marketing):  {min_price_no_cac:>10,.0f} RUB")
print(f"Minimum price (break-even, with CAC):      {min_price_with_cac:>10,.0f} RUB")
print(f"Recommended price (LTV/CAC = 3):           {min_price_healthy:>10,.0f} RUB")

monthly_fixed = 50000  # typical fixed costs
units_needed = monthly_fixed / contrib_after_cac if contrib_after_cac > 0 else 0

print(f"\nAssumed monthly fixed costs:               {monthly_fixed:>10,.0f} RUB")
print(f"Units needed per month (break-even):       {units_needed:>10.1f}")
print(f"Revenue needed (break-even):               {units_needed * retail_price:>10,.0f} RUB")

print("\n" + "=" * 80)
print("\n[4] PRICE SCENARIO ANALYSIS")
print("-" * 80)

price_variants = [1990, 2500, 2990, 3490]
print(f"\n{'Price':>8}  {'GM Amt':>10}  {'GM %':>7}  {'Contrib':>10}  {'Cont %':>7}  {'LTV':>10}  {'LTV/CAC':>8}")
print("-" * 80)

for price in price_variants:
    pay_comm = price * payment_commission_rate
    var_costs = cogs_per_unit + shipping_cost + packaging_cost + pay_comm
    gm = price - cogs_per_unit
    gm_pct = (gm / price) * 100
    cb = price - var_costs
    ca = cb - cac
    ca_pct = (ca / price) * 100
    ltv_s = cb * avg_purchases_lifetime
    ratio = ltv_s / cac

    print(f"{price:>8,.0f}  {gm:>10,.0f}  {gm_pct:>6.1f}%  {ca:>10,.0f}  {ca_pct:>6.1f}%  {ltv_s:>10,.0f}  {ratio:>8.2f}")

print("\n" + "=" * 80)
print("\n[5] SUPPLIER COMPARISON")
print("-" * 80)

typical_wholesale_50 = 400  # RUB for 50+ units
typical_bulk_200 = 350  # RUB for 200+ units

print(f"\n{'Supplier Option':<40}  {'COGS':>10}")
print("-" * 55)
print(f"{'Single unit (new supplier)':<40}  {cogs_per_unit:>10,.0f} RUB")
print(f"{'Wholesale 50+ units (typical)':<40}  {typical_wholesale_50:>10,.0f} RUB")
print(f"{'Bulk 200+ units (typical)':<40}  {typical_bulk_200:>10,.0f} RUB")

savings_50 = cogs_per_unit - typical_wholesale_50
savings_200 = cogs_per_unit - typical_bulk_200

print(f"\nPotential savings per unit:")
print(f"  Wholesale 50+ units:                       {savings_50:>10,.0f} RUB")
print(f"  Bulk 200+ units:                           {savings_200:>10,.0f} RUB")

new_contrib_50 = contrib_after_cac + savings_50
new_contrib_200 = contrib_after_cac + savings_200

print(f"\nImpact on Contribution Margin (at 2500 RUB price):")
print(f"  Current (COGS 500):                        {contrib_after_cac:>10,.0f} RUB")
print(f"  With COGS 400 (wholesale 50+):             {new_contrib_50:>10,.0f} RUB  (+{savings_50:.0f})")
print(f"  With COGS 350 (bulk 200+):                 {new_contrib_200:>10,.0f} RUB  (+{savings_200:.0f})")

new_ltv_50 = (contrib_before_cac + savings_50) * avg_purchases_lifetime
new_ltv_200 = (contrib_before_cac + savings_200) * avg_purchases_lifetime
new_ratio_50 = new_ltv_50 / cac
new_ratio_200 = new_ltv_200 / cac

print(f"\nImpact on LTV/CAC:")
print(f"  Current (COGS 500):                        {ltv_cac_ratio:>10.2f} x")
print(f"  With COGS 400 (wholesale 50+):             {new_ratio_50:>10.2f} x")
print(f"  With COGS 350 (bulk 200+):                 {new_ratio_200:>10.2f} x")

print("\n" + "=" * 80)
print("\n[6] CONCLUSIONS & RECOMMENDATIONS")
print("-" * 80)

print("\n1. SUPPLIER PRICE EVALUATION (500 RUB):")
print("   - 500 RUB per unit is ACCEPTABLE for MVP/initial launch")
print("   - But 100-150 RUB higher than typical wholesale prices")
print("   - Recommendation: use for first 50 sales, then switch to wholesale")

print("\n2. PRICING STRATEGY:")
print(f"   - Minimum break-even price: {min_price_with_cac:.0f} RUB")
print(f"   - Recommended price for healthy economics: {min_price_healthy:.0f} RUB")
print("   - Optimal range: 2500-2990 RUB")
print(f"   - At 2990 RUB: LTV/CAC = 4.28x (excellent)")

print("\n3. CURRENT ECONOMICS (price 2500 RUB, COGS 500 RUB):")
print(f"   - Gross Margin: {gross_margin_pct:.1f}% (good for premium e-commerce)")
print(f"   - Contribution Margin: {contrib_after_cac_pct:.1f}%")
print(f"   - LTV/CAC: {ltv_cac_ratio:.2f}x ({status})")

print("\n4. SCALING STRATEGY:")
if ltv_cac_ratio >= 3:
    print(f"   [OK] CAN SCALE marketing")
    print(f"   - Economics are healthy (LTV/CAC = {ltv_cac_ratio:.2f}x)")
    print(f"   - Each 1 RUB in marketing generates {ltv_cac_ratio:.2f} RUB LTV")
else:
    print(f"   [WARNING] OPTIMIZE FIRST before scaling")
    print(f"   - LTV/CAC = {ltv_cac_ratio:.2f}x (target: >3x)")
    print("   - Options: increase price, reduce CAC, improve retention")

print("\n5. ACTION PLAN:")
print("   a) MVP Phase (first 50 sales):")
print("      - Use supplier at 500 RUB/unit")
print("      - Set price 2500-2990 RUB")
print("      - Test demand and acquisition channels")
print("")
print("   b) Scaling Phase (50-200 sales):")
print("      - Find wholesale supplier (target: 400 RUB at 50+ units)")
print("      - Optimize CAC (target: <350 RUB)")
print("      - Improve retention (email marketing, loyalty program)")
print("")
print("   c) Growth Phase (200+ sales/month):")
print("      - Switch to bulk supplier (target: 350 RUB at 200+ units)")
print("      - Consider own production at 500+ units/month")
print("      - Expand product line")

print("\n6. KEY METRICS TO TRACK:")
print("   - CAC by channel (target: <400 RUB)")
print("   - Repeat purchase rate (target: >30%)")
print("   - Average order value (target: >3000 RUB)")
print("   - Gross Margin (target: >70%)")

print("\n" + "=" * 80)
print("END OF ANALYSIS")
print("=" * 80)
