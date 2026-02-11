#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit Economics Analysis: HD Squared (Дизайнерский Магазин)
Анализ с новым поставщиком футболок по 500 RUB/шт
"""

import json
from datetime import datetime

# ===== РЕАЛЬНЫЕ ДАННЫЕ ИЗ ФАЙЛОВ =====
print('=' * 60)
print('АНАЛИЗ UNIT ECONOMICS: ДИЗАЙНЕРСКИЙ МАГАЗИН')
print('Проект: HD Squared (Футболки с вышивкой)')
print('=' * 60)
print()

# Текущие сценарии из файлов
current_cogs = 3200  # RUB (факт)
target_cogs_opt = 1630  # RUB (целевой опт)

# НОВЫЙ сценарий: поставщик нашелся с 500 RUB/шт
new_blank_cost = 500  # RUB
embroidery_cost = 1000  # RUB (из файла, текущая)
embroidery_cost_target = 600  # RUB (целевая при объемах)
packaging = 150  # RUB (текущая)
packaging_target = 100  # RUB (целевая)
logistics = 50  # RUB (текущая)
logistics_target = 30  # RUB (целевая)

# Новый COGS с поставщиком 500 RUB
new_cogs_mvp = new_blank_cost + embroidery_cost + packaging + logistics
new_cogs_scale = new_blank_cost + embroidery_cost_target + packaging_target + logistics_target

# Розничные цены из файлов
prices = [5500, 6900, 8900]

# Налоги
usn_rate = 0.07  # УСН 6% + 1%
acquiring_rate = 0.03  # Эквайринг

# CAC из файлов
cac_optimistic = 800
cac_target = 1500
cac_expensive = 2500

# LTV параметры (из маркетинговой стратегии)
repeat_rate = 0.25  # 25% repeat purchase (премиум сегмент)

print('1. СУЩЕСТВУЮЩИЕ СЦЕНАРИИ (из файлов)')
print('-' * 60)
print(f'Текущий COGS (факт):       {current_cogs:,} RUB'.replace(',', ' '))
print(f'Целевой COGS (опт):        {target_cogs_opt:,} RUB'.replace(',', ' '))
print()

print('2. НОВЫЙ СЦЕНАРИЙ: Поставщик 500 RUB/шт')
print('-' * 60)
print(f'Бланк (новый):             {new_blank_cost} RUB')
print(f'Вышивка (текущая):         {embroidery_cost} RUB')
print(f'Упаковка (текущая):        {packaging} RUB')
print(f'Логистика (текущая):       {logistics} RUB')
print(f'ИТОГО COGS (MVP):          {new_cogs_mvp:,} RUB'.replace(',', ' '))
print()
print(f'При масштабировании:')
print(f'  - Вышивка (опт):         {embroidery_cost_target} RUB')
print(f'  - Упаковка (опт):        {packaging_target} RUB')
print(f'  - Логистика (опт):       {logistics_target} RUB')
print(f'ИТОГО COGS (Scale):        {new_cogs_scale:,} RUB'.replace(',', ' '))
print()


def calculate_unit_economics(price, cogs, cac, repeat_rate=0.25):
    """
    Расчет полной юнит-экономики
    """
    acquiring = price * acquiring_rate
    tax = price * usn_rate
    gross_profit = price - cogs
    gross_margin = (gross_profit / price) * 100
    cm = gross_profit - acquiring - tax
    cm_margin = (cm / price) * 100
    net_profit = cm - cac
    ltv = cm * (1 + repeat_rate)
    ltv_cac = ltv / cac if cac > 0 else 0
    payback = cac / cm if cm > 0 else float('inf')

    return {
        'price': price,
        'cogs': cogs,
        'gross_profit': gross_profit,
        'gross_margin': gross_margin,
        'acquiring': acquiring,
        'tax': tax,
        'cm': cm,
        'cm_margin': cm_margin,
        'cac': cac,
        'net_profit': net_profit,
        'ltv': ltv,
        'ltv_cac': ltv_cac,
        'payback_months': payback
    }


print('=' * 60)
print('3. СРАВНЕНИЕ: БЫЛО -> СТАЛО')
print('=' * 60)
print()

recommended_price = 6900

print(f'Анализ при рекомендованной цене: {recommended_price:,} RUB'.replace(',', ' '))
print()

scenarios = [
    ('БЫЛО (Текущий факт)', current_cogs, cac_target),
    ('БЫЛО (Целевой опт)', target_cogs_opt, cac_target),
    ('СТАЛО (Новый COGS MVP)', new_cogs_mvp, cac_target),
    ('СТАЛО (Новый COGS Scale)', new_cogs_scale, cac_target)
]

results = []
for name, cogs, cac in scenarios:
    result = calculate_unit_economics(recommended_price, cogs, cac, repeat_rate)
    result['scenario'] = name
    results.append(result)

    print(f'{name}:')
    print(f'  COGS:               {cogs:,} RUB'.replace(',', ' '))
    print(f'  Gross Margin:       {result["gross_margin"]:.1f}%')
    print(f'  CM:                 {result["cm"]:.0f} RUB')
    print(f'  CM Margin:          {result["cm_margin"]:.1f}%')
    print(f'  CAC:                {cac:,} RUB'.replace(',', ' '))
    print(f'  Net Profit:         {result["net_profit"]:.0f} RUB')
    print(f'  LTV:                {result["ltv"]:.0f} RUB')
    print(f'  LTV/CAC:            {result["ltv_cac"]:.2f}x')
    print(f'  Payback:            {result["payback_months"]:.1f} months')
    print()

print('=' * 60)
print('4. ДЕТАЛЬНЫЙ АНАЛИЗ: Новый COGS по всем ценам')
print('=' * 60)
print()

for price in prices:
    print(f'Цена: {price:,} RUB'.replace(',', ' '))
    print('-' * 60)

    for cac_name, cac in [('Оптимистичный', cac_optimistic),
                           ('Целевой', cac_target),
                           ('Дорогой', cac_expensive)]:
        result = calculate_unit_economics(price, new_cogs_mvp, cac, repeat_rate)

        status = 'OK' if result['ltv_cac'] >= 3 else ('WARNING' if result['ltv_cac'] >= 2 else 'BAD')
        profit_status = 'OK' if result['net_profit'] > 0 else 'LOSS'

        print(f'  CAC {cac_name} ({cac} RUB): '
              f'Net Profit = {result["net_profit"]:.0f} RUB [{profit_status}], '
              f'LTV/CAC = {result["ltv_cac"]:.2f}x [{status}]')

    print()

print('=' * 60)
print('5. BREAK-EVEN ANALYSIS')
print('=' * 60)
print()

fixed_costs_monthly = 50000

for price in prices:
    result = calculate_unit_economics(price, new_cogs_mvp, cac_target, repeat_rate)
    breakeven_units = fixed_costs_monthly / result['cm'] if result['cm'] > 0 else float('inf')

    print(f'Цена {price:,} RUB: Break-even = {breakeven_units:.1f} футболок/месяц'.replace(',', ' '))

print()
print('(Предполагаемые фикс. расходы: 50 000 RUB/месяц)')
print()

# Сохраним результаты в JSON
output_data = {
    'analysis_date': datetime.now().isoformat(),
    'project': 'HD Squared',
    'new_supplier': {
        'blank_cost': new_blank_cost,
        'cogs_mvp': new_cogs_mvp,
        'cogs_scale': new_cogs_scale
    },
    'comparison': [
        {
            'scenario': r['scenario'],
            'cogs': r['cogs'],
            'price': r['price'],
            'gross_margin': round(r['gross_margin'], 1),
            'cm': round(r['cm'], 0),
            'ltv': round(r['ltv'], 0),
            'ltv_cac': round(r['ltv_cac'], 2),
            'payback_months': round(r['payback_months'], 1)
        }
        for r in results
    ]
}

output_file = r'D:\Drive\Дизайнерский магазин\unit_economics_new_supplier.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f'Результаты сохранены: {output_file}')
