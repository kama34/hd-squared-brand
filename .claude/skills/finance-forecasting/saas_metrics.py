"""
SaaS Metrics Module

Calculate SaaS-specific financial metrics: LTV, CAC, Churn, Magic Number, Payback Period.

Functions:
- calculate_ltv: Lifetime Value
- calculate_cac: Customer Acquisition Cost
- calculate_payback_period: Payback period in months
- calculate_magic_number: Sales efficiency metric
- calculate_churn: Monthly churn rate
- ltv_cac_ratio: LTV/CAC ratio with health check
"""

from typing import Optional


def calculate_ltv(
    arpu: float,
    gross_margin: float,
    monthly_churn: float
) -> float:
    """
    Calculate Lifetime Value (LTV).
    
    Formula: LTV = ARPU × Gross Margin × (1 / Churn Rate)
    
    Args:
        arpu: Average Revenue Per User per month ($)
        gross_margin: Gross margin (0-1, e.g., 0.75 = 75%)
        monthly_churn: Monthly churn rate (0-1, e.g., 0.05 = 5%)
        
    Returns:
        Lifetime Value ($)
        
    Raises:
        ValueError: If churn rate is 0 (would result in infinite LTV)
        
    Examples:
        >>> calculate_ltv(arpu=100, gross_margin=0.8, monthly_churn=0.05)
        1600.0
        
        >>> calculate_ltv(arpu=150, gross_margin=0.7, monthly_churn=0.03)
        3500.0
    """
    if monthly_churn <= 0:
        raise ValueError(
            "Churn rate must be > 0. Use minimum observed churn (e.g., 0.01 for 1%)."
        )
    
    if not 0 < gross_margin <= 1:
        raise ValueError("Gross margin must be between 0 and 1")
    
    ltv = arpu * gross_margin * (1 / monthly_churn)
    return round(ltv, 2)


def calculate_cac(
    sales_marketing_spend: float,
    new_customers: int
) -> float:
    """
    Calculate Customer Acquisition Cost (CAC).
    
    Formula: CAC = Sales & Marketing Spend / New Customers
    
    Args:
        sales_marketing_spend: Total S&M spend in period ($)
        new_customers: Number of new customers acquired in period
        
    Returns:
        Customer Acquisition Cost ($)
        
    Examples:
        >>> calculate_cac(sales_marketing_spend=50_000, new_customers=100)
        500.0
        
        >>> calculate_cac(sales_marketing_spend=120_000, new_customers=200)
        600.0
    """
    if new_customers == 0:
        raise ValueError("Cannot calculate CAC with 0 new customers")
    
    cac = sales_marketing_spend / new_customers
    return round(cac, 2)


def calculate_payback_period(
    cac: float,
    arpu: float,
    gross_margin: float
) -> float:
    """
    Calculate CAC Payback Period in months.
    
    Formula: Payback Period = CAC / (ARPU × Gross Margin)
    
    Args:
        cac: Customer Acquisition Cost ($)
        arpu: Average Revenue Per User per month ($)
        gross_margin: Gross margin (0-1)
        
    Returns:
        Payback period in months
        
    Examples:
        >>> calculate_payback_period(cac=600, arpu=100, gross_margin=0.75)
        8.0
        
        >>> calculate_payback_period(cac=1200, arpu=150, gross_margin=0.8)
        10.0
    """
    if arpu * gross_margin == 0:
        raise ValueError("ARPU or gross margin cannot be 0")
    
    payback = cac / (arpu * gross_margin)
    return round(payback, 1)


def calculate_magic_number(
    new_arr_quarter: float,
    prior_quarter_sm_spend: float
) -> float:
    """
    Calculate Magic Number (sales efficiency).
    
    Formula: Magic Number = Net New ARR / Prior Quarter S&M Spend
    
    Interpretation:
    - > 1.0: Excellent sales efficiency
    - 0.75-1.0: Good
    - 0.5-0.75: Acceptable
    - < 0.5: Poor efficiency
    
    Args:
        new_arr_quarter: Net new ARR added in current quarter ($)
        prior_quarter_sm_spend: Sales & Marketing spend in prior quarter ($)
        
    Returns:
        Magic Number (ratio)
        
    Examples:
        >>> calculate_magic_number(new_arr_quarter=150_000, prior_quarter_sm_spend=100_000)
        1.5
        
        >>> calculate_magic_number(new_arr_quarter=75_000, prior_quarter_sm_spend=150_000)
        0.5
    """
    if prior_quarter_sm_spend == 0:
        raise ValueError("Prior quarter S&M spend cannot be 0")
    
    magic_number = new_arr_quarter / prior_quarter_sm_spend
    return round(magic_number, 2)


def calculate_churn(
    customers_start: int,
    customers_end: int,
    new_customers: int
) -> float:
    """
    Calculate monthly churn rate.
    
    Formula: Churn Rate = (Customers Lost / Customers at Start) × 100%
    where Customers Lost = Customers Start + New - Customers End
    
    Args:
        customers_start: Customers at start of period
        customers_end: Customers at end of period
        new_customers: New customers added during period
        
    Returns:
        Churn rate as percentage (0-100)
        
    Examples:
        >>> calculate_churn(customers_start=1000, customers_end=1020, new_customers=50)
        3.0
        
        >>> calculate_churn(customers_start=500, customers_end=520, new_customers=40)
        4.0
    """
    if customers_start == 0:
        raise ValueError("Cannot calculate churn with 0 starting customers")
    
    customers_lost = customers_start + new_customers - customers_end
    churn_rate = (customers_lost / customers_start) * 100
    
    return round(churn_rate, 2)


def ltv_cac_ratio(ltv: float, cac: float) -> dict:
    """
    Calculate LTV/CAC ratio with health assessment.
    
    Benchmarks:
    - > 3x: Excellent (healthy unit economics)
    - 2-3x: Acceptable (room for improvement)
    - < 2x: Poor (unit economics broken)
    
    Args:
        ltv: Lifetime Value ($)
        cac: Customer Acquisition Cost ($)
        
    Returns:
        Dict with ratio, status, and message
        
    Examples:
        >>> result = ltv_cac_ratio(ltv=1600, cac=500)
        >>> result['ratio']
        3.2
        >>> result['status']
        'excellent'
        
        >>> result = ltv_cac_ratio(ltv=900, cac=600)
        >>> result['status']
        'poor'
    """
    if cac == 0:
        raise ValueError("CAC cannot be 0")
    
    ratio = ltv / cac
    
    if ratio >= 3:
        status = 'excellent'
        emoji = '✅'
        message = f'EXCELLENT (LTV/CAC = {ratio:.1f}x > 3x target)'
    elif ratio >= 2:
        status = 'acceptable'
        emoji = '🟡'
        message = f'ACCEPTABLE (LTV/CAC = {ratio:.1f}x, aim for >3x)'
    else:
        status = 'poor'
        emoji = '🔴'
        message = f'CRITICAL (LTV/CAC = {ratio:.1f}x < 2x, unit economics broken)'
    
    return {
        'ratio': round(ratio, 2),
        'status': status,
        'emoji': emoji,
        'message': message
    }


def unit_economics_health_check(
    arpu: float,
    gross_margin: float,
    monthly_churn: float,
    sales_marketing_spend: float,
    new_customers: int
) -> dict:
    """
    Complete unit economics health check.
    
    Args:
        arpu: Average Revenue Per User per month ($)
        gross_margin: Gross margin (0-1)
        monthly_churn: Monthly churn rate (0-1)
        sales_marketing_spend: S&M spend in period ($)
        new_customers: New customers acquired in period
        
    Returns:
        Dict with all metrics and overall health status
        
    Example:
        >>> health = unit_economics_health_check(
        ...     arpu=120,
        ...     gross_margin=0.75,
        ...     monthly_churn=0.04,
        ...     sales_marketing_spend=120_000,
        ...     new_customers=200
        ... )
        >>> health['overall_status']
        'excellent'
    """
    ltv = calculate_ltv(arpu, gross_margin, monthly_churn)
    cac = calculate_cac(sales_marketing_spend, new_customers)
    ratio_result = ltv_cac_ratio(ltv, cac)
    payback = calculate_payback_period(cac, arpu, gross_margin)
    
    # Payback health check
    if payback <= 12:
        payback_status = 'excellent'
        payback_emoji = '✅'
    elif payback <= 18:
        payback_status = 'acceptable'
        payback_emoji = '🟡'
    else:
        payback_status = 'poor'
        payback_emoji = '🔴'
    
    # Overall health
    if ratio_result['status'] == 'excellent' and payback_status in ['excellent', 'acceptable']:
        overall_status = 'excellent'
        overall_emoji = '✅'
    elif ratio_result['status'] == 'poor' or payback_status == 'poor':
        overall_status = 'poor'
        overall_emoji = '🔴'
    else:
        overall_status = 'acceptable'
        overall_emoji = '🟡'
    
    return {
        'metrics': {
            'ltv': ltv,
            'cac': cac,
            'ltv_cac_ratio': ratio_result['ratio'],
            'payback_months': payback,
            'arpu': arpu,
            'gross_margin': gross_margin,
            'monthly_churn_pct': monthly_churn * 100
        },
        'status': {
            'ltv_cac': {
                'status': ratio_result['status'],
                'emoji': ratio_result['emoji'],
                'message': ratio_result['message']
            },
            'payback': {
                'status': payback_status,
                'emoji': payback_emoji,
                'message': f'Payback: {payback} months (target: <12mo)'
            },
            'overall': {
                'status': overall_status,
                'emoji': overall_emoji
            }
        }
    }


if __name__ == "__main__":
    # Example usage
    print("=== SaaS Metrics Calculation ===\n")
    
    # Input data
    arpu = 120
    gross_margin = 0.75
    monthly_churn = 0.04
    sm_spend = 120_000
    new_customers = 200
    
    # Individual calculations
    print("Individual Metrics:")
    ltv = calculate_ltv(arpu, gross_margin, monthly_churn)
    print(f"✨ LTV: ${ltv:,.0f}")
    
    cac = calculate_cac(sm_spend, new_customers)
    print(f"💸 CAC: ${cac:,.0f}")
    
    ratio_result = ltv_cac_ratio(ltv, cac)
    print(f"{ratio_result['emoji']} LTV/CAC: {ratio_result['ratio']}x - {ratio_result['message']}")
    
    payback = calculate_payback_period(cac, arpu, gross_margin)
    print(f"⏱️  Payback Period: {payback} months")
    
    print("\n" + "="*50 + "\n")
    
    # Full health check
    print("Complete Unit Economics Health Check:")
    health = unit_economics_health_check(
        arpu=arpu,
        gross_margin=gross_margin,
        monthly_churn=monthly_churn,
        sales_marketing_spend=sm_spend,
        new_customers=new_customers
    )
    
    print(f"\n{health['status']['overall']['emoji']} Overall Status: {health['status']['overall']['status'].upper()}")
    print(f"\n{health['status']['ltv_cac']['emoji']} {health['status']['ltv_cac']['message']}")
    print(f"{health['status']['payback']['emoji']} {health['status']['payback']['message']}")
