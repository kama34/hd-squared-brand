"""
Financial Forecasting Module

Forecasts Runway, Cash Flow, and Burn Rate for startup financial planning.

Functions:
- calculate_runway: Calculate months of runway
- project_cashflow: Project cash flow over time
- scenario_analysis: Compare multiple scenarios
"""

import pandas as pd
from typing import Optional, Union


def calculate_runway(
    cash_balance: float,
    monthly_burn: float
) -> float:
    """
    Calculate runway in months.
    
    Args:
        cash_balance: Current cash in bank ($)
        monthly_burn: Monthly burn rate (expenses - revenue) ($)
        
    Returns:
        Runway in months (float). Returns inf if profitable (burn <= 0).
        
    Examples:
        >>> calculate_runway(500_000, 50_000)
        10.0
        
        >>> calculate_runway(750_000, -10_000)  # Profitable
        inf
    """
    if monthly_burn <= 0:
        return float('inf')  # Profitable or breakeven = infinite runway
        
    runway = cash_balance / monthly_burn
    return round(runway, 1)


def project_cashflow(
    starting_cash: float,
    monthly_revenue: Union[float, list],
    monthly_expenses: Union[float, list],
    months: int
) -> pd.DataFrame:
    """
    Project cash flow over time.
    
    Args:
        starting_cash: Starting cash balance ($)
        monthly_revenue: Monthly revenue ($) - can be constant or list
        monthly_expenses: Monthly expenses ($) - can be constant or list
        months: Number of months to project
        
    Returns:
        DataFrame with columns: Month, Revenue, Expenses, Net_Cash_Flow, Cumulative_Cash
        
    Examples:
        >>> projection = project_cashflow(
        ...     starting_cash=500_000,
        ...     monthly_revenue=30_000,
        ...     monthly_expenses=50_000,
        ...     months=12
        ... )
        >>> projection.head(3)
           Month  Revenue  Expenses  Net_Cash_Flow  Cumulative_Cash
        0      1    30000     50000         -20000           480000
        1      2    30000     50000         -20000           460000
        2      3    30000     50000         -20000           440000
    """
    # Convert constants to lists
    if isinstance(monthly_revenue, (int, float)):
        revenue_list = [monthly_revenue] * months
    else:
        revenue_list = monthly_revenue
        
    if isinstance(monthly_expenses, (int, float)):
        expenses_list = [monthly_expenses] * months
    else:
        expenses_list = monthly_expenses
        
    # Validate lengths
    if len(revenue_list) != months or len(expenses_list) != months:
        raise ValueError(f"Revenue and expenses lists must have {months} elements")
    
    # Build projection
    data = []
    cumulative_cash = starting_cash
    
    for month in range(1, months + 1):
        revenue = revenue_list[month - 1]
        expenses = expenses_list[month - 1]
        net_cash_flow = revenue - expenses
        cumulative_cash += net_cash_flow
        
        data.append({
            'Month': month,
            'Revenue': revenue,
            'Expenses': expenses,
            'Net_Cash_Flow': net_cash_flow,
            'Cumulative_Cash': cumulative_cash
        })
    
    return pd.DataFrame(data)


def scenario_analysis(
    scenarios: dict,
    starting_cash: float,
    months: int = 12
) -> pd.DataFrame:
    """
    Compare multiple cash flow scenarios.
    
    Args:
        scenarios: Dict with scenario names as keys and (revenue, expenses) tuples as values
        starting_cash: Starting cash balance ($)
        months: Number of months to project
        
    Returns:
        DataFrame comparing ending cash across scenarios
        
    Examples:
        >>> scenarios = {
        ...     'Conservative': (30_000, 50_000),
        ...     'Base': (40_000, 55_000),
        ...     'Aggressive': (60_000, 80_000)
        ... }
        >>> comparison = scenario_analysis(scenarios, starting_cash=500_000, months=12)
        >>> comparison
                  Scenario  Ending_Cash  Total_Burn  Runway_Months
        0  Conservative      260000     -240000           13.0
        1          Base      320000     -180000           17.8
        2    Aggressive      260000     -240000           10.8
    """
    results = []
    
    for scenario_name, (revenue, expenses) in scenarios.items():
        projection = project_cashflow(starting_cash, revenue, expenses, months)
        ending_cash = projection['Cumulative_Cash'].iloc[-1]
        total_burn = projection['Net_Cash_Flow'].sum()
        
        # Calculate future runway from ending position
        final_burn = expenses - revenue
        runway = calculate_runway(ending_cash, final_burn) if final_burn > 0 else float('inf')
        
        results.append({
            'Scenario': scenario_name,
            'Ending_Cash': int(ending_cash),
            'Total_Burn': int(total_burn),
            'Runway_Months': runway
        })
    
    return pd.DataFrame(results)


def get_runway_status(runway_months: float) -> dict:
    """
    Get runway health status and recommendations.
    
    Args:
        runway_months: Runway in months
        
    Returns:
        Dict with status, emoji, message
        
    Examples:
        >>> get_runway_status(15)
        {'status': 'healthy', 'emoji': '✅', 'message': 'Healthy runway'}
        
        >>> get_runway_status(4)
        {'status': 'warning', 'emoji': '⚠️', 'message': 'WARNING: Start fundraising NOW'}
    """
    if runway_months == float('inf'):
        return {
            'status': 'profitable',
            'emoji': '🟢',
            'message': 'Profitable - no fundraising needed'
        }
    elif runway_months < 3:
        return {
            'status': 'critical',
            'emoji': '🔴',
            'message': 'CRITICAL: Start fundraising IMMEDIATELY'
        }
    elif runway_months < 6:
        return {
            'status': 'warning',
            'emoji': '⚠️',
            'message': 'WARNING: Start fundraising NOW'
        }
    else:
        return {
            'status': 'healthy',
            'emoji': '✅',
            'message': 'Healthy runway'
        }


if __name__ == "__main__":
    # Example usage
    print("=== Runway Calculation ===")
    cash = 750_000
    burn = 50_000
    runway = calculate_runway(cash, burn)
    status = get_runway_status(runway)
    
    print(f"💰 Cash Balance: ${cash:,}")
    print(f"🔥 Monthly Burn: ${burn:,}")
    print(f"⏱️  Runway: {runway} months")
    print(f"{status['emoji']} {status['message']}\n")
    
    print("=== Cash Flow Projection ===")
    projection = project_cashflow(
        starting_cash=500_000,
        monthly_revenue=30_000,
        monthly_expenses=50_000,
        months=6
    )
    print(projection)
    print()
    
    print("=== Scenario Analysis ===")
    scenarios = {
        'Status Quo': (40_000, 70_000),
        'Growth': (60_000, 100_000),
        'Conservative': (40_000, 55_000)
    }
    comparison = scenario_analysis(scenarios, starting_cash=800_000, months=12)
    print(comparison)
