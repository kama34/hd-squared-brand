#!/usr/bin/env python3
"""Простой конструктор финансовой модели.

Этот скрипт демонстрационный — строит помесячную проекцию cashflow и простую сценарную таблицу.
Все комментарии и сообщения — на русском языке по требованию CFO.
"""
import pandas as pd
from typing import Dict


def build_projection(starting_cash: float, monthly_revenue: float, monthly_expenses: float, months: int = 12) -> pd.DataFrame:
    """Построить DataFrame с колонками: Month, Revenue, Expenses, Net_Cash_Flow, Cumulative_Cash"""
    rows = []
    cum_cash = starting_cash
    for m in range(1, months + 1):
        net = monthly_revenue - monthly_expenses
        cum_cash += net
        rows.append({'Month': m, 'Revenue': monthly_revenue, 'Expenses': monthly_expenses, 'Net_Cash_Flow': net, 'Cumulative_Cash': cum_cash})
    df = pd.DataFrame(rows)
    return df


def scenario_analysis(**scenarios: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Принять несколько проекций (DataFrame) и вернуть таблицу сравнения ending cash и min cumulative cash"""
    result = []
    for name, df in scenarios.items():
        ending = float(df['Cumulative_Cash'].iloc[-1])
        min_cum = float(df['Cumulative_Cash'].min())
        result.append({'scenario': name, 'ending_cash': ending, 'min_cumulative_cash': min_cum})
    return pd.DataFrame(result)


if __name__ == '__main__':
    print('Демо модели: building base projection')
    df = build_projection(500_000, 50_000, 80_000, months=12)
    print(df.tail())
