# Pitch Questions Skill

## Overview

**Purpose**: Пошаговый сбор информации для создания структуры pitch deck через направленные вопросы по блокам (Product, Problem, Market, Business Model, Traction, Team, Financials, Ask).

**Target Users**: CEO (primary), Board (preparation)

**Capabilities**:
- Interactive Q&A session for pitch deck preparation
- Structured slide-by-slide specification generation
- USP and key metrics extraction
- Russian-language output for Sales AI context

## Required Tools

- `Read` - Read existing pitch materials
- `Write` - Save pitch deck structure
- `WebSearch` - Research industry benchmarks for comparison

## Usage Example

```markdown
"Используя pitch-questions skill, help me prepare Sales AI Series A pitch deck structure"

**Process**:

Q1: Какую проблему решает Sales AI?
A: SMB owners тратят 10 hours/week на manual data analysis и reporting

Q2: Для кого это критично? (Target audience)
A: SMB companies (10-500 employees) в SaaS, E-commerce, Services

Q3: Почему существующие решения не работают?
A: Too complex (enterprise-focused), expensive ($200+/mo), require data science skills

Q4: Каково ваше уникальное решение?
A: AI-powered analytics с plain-English insights в 5 minutes, $29/mo

Q5: Размер рынка? (TAM/SAM/SOM)
A: TAM: $3.6B (US SMB BI market), SAM: $204M (ICP), SOM: $3.1M Year 5

Q6: Какая traction сейчас?
A: MRR: $138k, 118 customers, +15% QoQ growth, LTV/CAC: 3.8x

Q7: Кто в команде?
A: 2 co-founders (ex-Salesforce, ex-Google), hiring VP Sales

Q8: Сколько денег нужно и зачем?
A: $5M Series A для sales team (50%), R&D (30%), ops (20%)

**Output**: Структура из 12 слайдов

---

## Sales AI Series A Pitch Deck Structure

### Slide 1: Problem
- **title**: "SMBs Drowning in Data"
- **key_message**: "10 hours/week wasted on manual analytics"
- **visual_guidance**: Pain point illustration, clock/time waste visual
- **data_needed**: Survey: 78% SMB owners struggle with data analysis
- **speaker_notes**: "This is a $10B problem affecting 5.8M US SMBs"

### Slide 2: Solution
- **title**: "AI Analytics in 5 Minutes"
- **key_message**: "From data chaos to actionable insights instantly"
- **visual_guidance**: Before/After comparison, product screenshot
- **data_needed**: Time saved: 10 hours → 30 minutes
- **speaker_notes**: "Unlike competitors (dashboards), we deliver decisions"

### Slide 3: Product Demo
- **title**: "See It In Action"
- **key_message**: "Ask question → Get AI insight → Take action"
- **visual_guidance**: 3-step flow diagram with screenshots
- **data_needed**: 87% of AI insights led to customer actions
- **speaker_notes**: "This is actual product, 118 customers use it daily"

### Slide 4: Market Size
- **title**: "$3.6B Market Opportunity"
- **key_message**: "Large, growing, underserved SMB segment"
- **visual_guidance**: TAM/SAM/SOM funnel
- **data_needed**: TAM: $3.6B, SAM: $204M, SOM: $3.1M (Year 5)
- **speaker_notes**: "Even 1.5% market share = $3M ARR"

### Slide 5: Business Model
- **title**: "Profitable Unit Economics"
- **key_message**: "LTV/CAC: 3.8x, Payback: 6.7 months"
- **visual_guidance**: Unit economics chart
- **data_needed**: ARPU: $120, CAC: $600, LTV: $2,250
- **speaker_notes**: "Healthy margins, capital efficient growth"

### Slide 6: Traction
- **title**: "Growing 15% QoQ"
- **key_message**: "$138k MRR, 118 customers, strong retention"
- **visual_guidance**: MRR growth chart (last 12 months)
- **data_needed**: Q4 2025: $120k → Q1 2026: $138k
- **speaker_notes**: "Consistent growth, product-market fit validated"

### Slide 7: Competition
- **title**: "Why We Win"
- **key_message**: "Faster, simpler, cheaper than alternatives"
- **visual_guidance**: Competitive matrix
- **data_needed**: Setup: <5min vs 15min, Price: $29 vs $39+
- **speaker_notes**: "30% of customers switched from competitors"

### Slide 8: Go-to-Market
- **title**: "Proven GTM Channels"
- **key_message**: "Content-first strategy, CAC declining"
- **visual_guidance**: Channel mix pie chart
- **data_needed**: Content 50%, Google Ads 30%, Referrals 20%
- **speaker_notes**: "CAC improved $650 → $600 via channel optimization"

### Slide 9: Team
- **title**: "Domain Experts"
- **key_message**: "Built by ex-Salesforce, ex-Google engineers"
- **visual_guidance**: Team photos with credentials
- **data_needed**: Combined 20 years in enterprise SaaS
- **speaker_notes**: "Hiring VP Sales (3 finalists from Salesforce, HubSpot)"

### Slide 10: Financials
- **title**: "Path to $10M ARR"
- **key_message**: "3-year projection: $1.6M - $6.1M ARR"
- **visual_guidance**: 3-scenario forecast chart
- **data_needed**: Conservative/Base/Optimistic projections
- **speaker_notes**: "Base case: $3.1M ARR Year 3 with current trajectory"

### Slide 11: The Ask
- **title**: "Raising $5M Series A"
- **key_message**: "$25M pre-money valuation (15x ARR multiple)"
- **visual_guidance**: Use of funds breakdown
- **data_needed**: 50% Sales, 30% R&D, 20% Ops
- **speaker_notes**: "Valuation justified by growth rate + unit economics"

### Slide 12: Vision
- **title**: "Democratizing Data Analytics"
- **key_message**: "Every SMB owner = data-driven decision maker"
- **visual_guidance**: Aspirational future vision
- **data_needed**: Long-term impact: 100k+ SMBs empowered
- **speaker_notes**: "Join us in transforming how SMBs use data"

---
```

## Workflow

1. **Start Q&A session**: CEO answers questions one block at a time
2. **Collect data**: Problem, Solution, Market, Model, Traction, Team, Financials, Ask
3. **Generate structure**: 12-15 slide specifications with all fields
4. **Save output**: Write to knowledge base
5. **Iterate**: Refine based on CEO feedback

## Integration with Other Skills

- **investor-qa-generator** - Uses pitch structure to generate anticipated questions
- **pitch-audit** - Reviews generated structure for weaknesses
- **board-reporting** - Similar structure for Board vs Investor decks

## Version History

- **2026-02-10**: Adapted for Claude Code CLI
- **Original**: GitHub Copilot version

## Related Files

- `.github/skills/pitch-questions/` - Original version
