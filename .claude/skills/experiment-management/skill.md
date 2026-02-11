# Experiment Management Skill

## Overview
**Purpose**: A/B test tracking, hypothesis management, statistical significance calculation.
**Target Users**: CMO (primary), CTO (implementation)
**Capabilities**: Experiment tracking, statistical analysis, winner determination

## Required Tools
`Read`, `mcp__ide__executeCode` (Python stats), `Write`

## Usage Example
```python
"Используя experiment-management skill, analyze A/B test results для Sales AI landing page"

import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/experiment-management')
from ab_test_analysis import calculate_significance

# Variant A (control): "Start Free Trial"
variant_a = {'visitors': 1000, 'conversions': 150}

# Variant B (test): "Get My Free Trial"
variant_b = {'visitors': 1000, 'conversions': 175}

result = calculate_significance(variant_a, variant_b)
print(f"Winner: {result['winner']}")
print(f"Confidence: {result['confidence']:.1f}%")
print(f"Uplift: {result['uplift']:.1f}%")
```
