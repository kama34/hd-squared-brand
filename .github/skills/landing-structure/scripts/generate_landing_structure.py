#!/usr/bin/env python3
"""Примерный CLI-генератор структуры лендинга.

Выводит markdown со стандартными секциями лендинга. Этот скрипт — пример, который можно
подключить в CI или запустить локально, чтобы быстро получить каркас для копирайтера.
"""
import argparse
import json
from textwrap import dedent


TEMPLATE = """
# {product}

## Hero
- Заголовок: {hero_title}
- Подзаголовок: {hero_sub}
- Ключевое преимущество: {value_prop}
- CTA: {primary_cta}

## Problem / Pain
- Кого это касается: {audience}
- Краткое описание боли: 

## Solution
- Как решаем: {solution_short}

## Benefits
- 1. {benefit_1}
- 2. {benefit_2}
- 3. {benefit_3}

## Features
- Фича A: краткий тезис
- Фича B: краткий тезис

## Social proof
- Отзыв / кейс: пример
- Логотипы клиентов

## Pricing / Offer
- Оффер: {offer}

## FAQ
- Q1: 
- Q2: 

## Final CTA
- Повтор CTA: {primary_cta}

"""


def generate(data: dict) -> str:
    hero_title = data.get('hero_title') or f"{data.get('product')} — коротко о пользе"
    hero_sub = data.get('hero_sub') or data.get('product')
    value_prop = data.get('value_prop') or 'Экономия времени и увеличение лидов'
    solution_short = data.get('solution_short') or 'Автоматизация воронки через AI'
    return TEMPLATE.format(
        product=data.get('product', 'Продукт'),
        hero_title=hero_title,
        hero_sub=hero_sub,
        value_prop=value_prop,
        primary_cta=data.get('primary_cta', 'Запросить демо'),
        audience=data.get('audience', 'ЦА'),
        solution_short=solution_short,
        benefit_1=data.get('benefit_1', 'Увеличение конверсии'),
        benefit_2=data.get('benefit_2', 'Снижение CPL'),
        benefit_3=data.get('benefit_3', 'Автоматизация рутины'),
        offer=data.get('offer', '14 дней бесплатно'),
    )


def main():
    parser = argparse.ArgumentParser(description='Generate landing structure (sample)')
    parser.add_argument('--product', help='Краткое название/описание продукта')
    parser.add_argument('--audience', help='Целевая аудитория')
    parser.add_argument('--goal', help='Цель лендинга')
    parser.add_argument('--primary_cta', help='Текст основного CTA')
    parser.add_argument('--offer', help='Коммерческое предложение')
    parser.add_argument('--tone', help='Тон коммуникации')
    parser.add_argument('--out', help='Файл для записи (если не задано — stdout)')
    parser.add_argument('--json', help='JSON-файл с полями для шаблона')
    args = parser.parse_args()

    data = {}
    if args.json:
        with open(args.json, 'r', encoding='utf-8') as f:
            data = json.load(f)

    # CLI args override JSON
    for k in ('product', 'audience', 'goal', 'primary_cta', 'offer', 'tone'):
        v = getattr(args, k)
        if v:
            data[k] = v

    md = generate(data)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f'Wrote landing skeleton to {args.out}')
    else:
        print(md)


if __name__ == '__main__':
    main()
