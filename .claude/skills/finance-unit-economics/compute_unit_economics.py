#!/usr/bin/env python3
"""Модуль расчёта unit-economics.

Все функции и docstrings на русском языке по требованию CFO.
Код возвращает числовые значения; для репортов используйте эти функции как building blocks.
"""
from typing import Optional

def calculate_ltv(arpu: float, gross_margin: float, monthly_churn: float) -> float:
    """Рассчитать LTV по формуле: ARPU * gross_margin * (1 / monthly_churn).

    arpu: средняя выручка с клиента в месяц
    gross_margin: доля валовой прибыли (0..1)
    monthly_churn: месячный отток (0..1)
    """
    if monthly_churn <= 0:
        raise ValueError("monthly_churn не может быть 0 или отрицательным. Используйте малую положительную величину.")
    return arpu * gross_margin * (1.0 / monthly_churn)


def calculate_cac(sales_marketing_spend: float, new_customers: int) -> float:
    """Рассчитать CAC: затраты на продажи и маркетинг / число новых клиентов."""
    if new_customers <= 0:
        raise ValueError("new_customers должен быть > 0")
    return float(sales_marketing_spend) / float(new_customers)


def ltv_cac_ratio(ltv: float, cac: float) -> float:
    """Возвращает отношение LTV/CAC."""
    if cac == 0:
        return float('inf')
    return ltv / cac


def calculate_payback_period(cac: float, arpu: float, gross_margin: float) -> float:
    """Сколько месяцев требуется, чтобы окупить CAC: CAC / (ARPU * gross_margin)"""
    monthly_contribution = arpu * gross_margin
    if monthly_contribution <= 0:
        raise ValueError("ARPU * gross_margin должно быть > 0")
    return cac / monthly_contribution


def calculate_churn(customers_start: int, customers_end: int, new_customers: int) -> float:
    """Простой расчет месячного churn: (customers_start - (customers_end - new_customers)) / customers_start"""
    if customers_start <= 0:
        raise ValueError("customers_start должен быть > 0")
    lost = customers_start - (customers_end - new_customers)
    return max(0.0, float(lost) / float(customers_start))


if __name__ == '__main__':
    # Пример использования из командной строки
    print('Пример: calculate LTV')
    print('LTV:', calculate_ltv(120, 0.75, 0.04))
