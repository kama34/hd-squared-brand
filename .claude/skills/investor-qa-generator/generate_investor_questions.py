#!/usr/bin/env python3
"""Stub: generate investor-style questions from a presentation structure."""
import json

def questions_stub(structure):
    qs = []
    qs.append({"theme":"Finance","question":"Какова ваша LTV/CAC?","motive":"Проверка unit-economics"})
    return qs

if __name__ == '__main__':
    sample = [{"title":"Cover","message":"..."},{"title":"Market","message":"..."}]
    print(json.dumps(questions_stub(sample), ensure_ascii=False, indent=2))
