# Pitch Audit Skill

## Overview

**Purpose**: Критический аудит pitch deck структуры и содержания для выявления логических дыр, слабых аргументов и улучшения инвестиционной привлекательности.

**Target Users**: CEO (primary), Board (review before investor meetings)

**Capabilities**:
- Slide-by-slide audit of pitch deck structure
- Investment appeal analysis
- Best practices compliance check
- Prioritized recommendations with fix examples

## Required Tools

- `Read` - Read pitch deck structure
- `Write` - Save audit report
- `WebSearch` - Research industry benchmarks and comps

## Usage Example

```markdown
"Используя pitch-audit skill, review Sales AI Series A pitch deck"

**Input**: Pitch deck structure (from pitch-questions skill or existing deck)

---

## Pitch Deck Audit Report: Sales AI Series A

**Date**: 2026-02-10
**Reviewer**: CEO + Board
**Deck Version**: v1.0 (12 slides)

---

### OVERALL ASSESSMENT: 🟡 GOOD (7.5/10)

**Strengths** ✅:
- Clear problem/solution narrative
- Strong traction ($138k MRR, 118 customers)
- Healthy unit economics (LTV/CAC 3.8x)
- Realistic market sizing (defendable SAM/SOM)

**Critical Issues** 🔴:
1. Missing: Customer testimonials / case studies
2. Missing: Competitive moat (what prevents copycats?)
3. Weak: Team slide (only 2 people, no VP Sales yet)
4. Risk: Churn spike not addressed (4% → 6% in Q1)

**Priority Fixes** (in order):

---

### ISSUE #1: No Customer Social Proof 🔴 CRITICAL

**Where**: Missing from entire deck
**Category**: Credibility / Traction
**Criticality**: HIGH

**Problem**:
Deck has numbers (118 customers, $138k MRR) but no customer voices. Investors will ask "Are customers actually happy?"

**Fixes**:
1. Add Slide 5.5 "Customer Success Stories" with 2-3 testimonials
2. Include customer logos on Traction slide (with permission)
3. Add NPS score (if >30) to metrics
4. Prepare customer references (investors can call)

**Example Improvement**:

```markdown
### Slide 5.5: Customer Success Stories

**Customer A** (E-commerce, 50 employees):
"Sales AI reduced our reporting time from 8 hours to 30 minutes per week.
ROI paid for itself in first month."
- Revenue impact: +15% from data-driven decisions

**Customer B** (SaaS, 120 employees):
"Switched from Competitor A. Sales AI insights are actionable, not just pretty charts."
- Time saved: 10 hours/week
- Churn from Competitor A: They were too complex
```

---

### ISSUE #2: Weak Competitive Moat 🔴 CRITICAL

**Where**: Slide 7 (Competition)
**Category**: Defensibility
**Criticality**: HIGH

**Problem**:
Deck shows "Faster, simpler, cheaper" but doesn't explain WHY competitors can't copy this. Investors will ask "What stops Competitor A from adding AI?"

**Fixes**:
1. Add proprietary data advantage (if exists)
2. Highlight network effects (if applicable)
3. Explain switching costs (customer lock-in)
4. Show patents/IP (if any)

**Current Slide** (weak):
```
Competition:
- Us: Setup <5min, Price $29
- Competitor A: Setup 15min, Price $39
```

**Improved Slide** (stronger):
```
Why We're Defensible:
1. Proprietary ML models trained on 118 customers' data
2. Network effects: More users → better AI insights
3. Switching costs: 30-day onboarding investment
4. First-mover advantage: 2-year head start in SMB AI analytics

Competitors CAN copy features, but NOT our data advantage
```

---

### ISSUE #3: Team Perception Risk 🟡 MEDIUM

**Where**: Slide 9 (Team)
**Category**: Execution Risk
**Criticality**: MEDIUM

**Problem**:
Only 2 co-founders shown. Investors will worry about execution capacity to scale to $10M ARR.

**Fixes**:
1. Add "Key Hires Planned" section
2. Show advisor/board members (if impressive)
3. Highlight VP Sales finalists (de-risk hiring concern)
4. Add org chart vision (next 12 months)

**Example Addition**:

```markdown
### Slide 9: Team (Enhanced)

**Current Team**:
- CEO: Ex-Salesforce (10 years), built $50M ARR product
- CTO: Ex-Google (8 years), ML/AI expertise

**Key Hires (Next 6 Months)**:
- VP Sales: 3 finalists from Salesforce, HubSpot (decision by March 31)
- Head of Customer Success: Starting April 1
- 2 Senior Engineers: Recruited via ex-Google network

**Advisors**:
- [Advisor A]: Former VP Sales, Competitor D (went IPO)
- [Advisor B]: VC Partner, [Firm X] (SMB SaaS expertise)

**Budget**: $500k from Series A allocated for team scaling
```

---

### ISSUE #4: Churn Risk Not Addressed 🟡 MEDIUM

**Where**: Slide 6 (Traction) & Slide 10 (Financials)
**Category**: Unit Economics Risk
**Criticality**: MEDIUM

**Problem**:
Churn spiked 4.5% → 6% in Q1 2026. This is mentioned in data but not explained. Investors WILL ask about it.

**Fixes**:
1. Add 1-2 bullet points explaining churn spike (onboarding complexity)
2. Show mitigation plan (new tutorial, deployed Feb 28)
3. Include forward-looking target (churn → 3% by Q2 end)
4. Prepare backup slide with detailed churn analysis

**Add to Slide 6**:

```markdown
Traction Metrics:
- MRR: $138k (+15% QoQ) ✅
- Customers: 118 ✅
- Churn: 4% ⚠️ (spiked to 6% in Q1, now declining)

**Churn Mitigation**:
- Root cause: Onboarding complexity (identified Jan 2026)
- Fix deployed: Interactive tutorial (Feb 28)
- Early results: 30% onboarding completion (vs 20% before)
- Target: Churn <3% by Q2 end
```

---

### ISSUE #5: Market Sizing Methodology Vague 🟢 LOW

**Where**: Slide 4 (Market Size)
**Category**: Credibility
**Criticality**: LOW (but prepare defense)

**Problem**:
TAM $3.6B stated but not sourced. Investors will ask "Where did this number come from?"

**Fixes**:
1. Add footnote with source (Gartner report, year)
2. Prepare Appendix slide with detailed calculation
3. Show bottom-up validation (# companies × ARPU)

**Example Footnote**:
```
TAM: $3.6B
Source: Gartner "Business Intelligence Software Market" (2026)
Calculation: $30B global BI market × 30% SMB segment × 40% US market
```

---

### ISSUE #6: Use of Funds Generic 🟢 LOW

**Where**: Slide 11 (The Ask)
**Category**: Clarity
**Criticality**: LOW

**Problem**:
"50% Sales, 30% R&D, 20% Ops" is too vague. What specifically will you build/hire?

**Fixes**:
1. Break down each category with specifics
2. Link to hiring roadmap
3. Show expected impact (e.g., "20 AEs → $5M ARR")

**Improved Version**:

```markdown
Use of $5M:

**Sales & Marketing ($2.5M - 50%)**:
- VP Sales + 10 AEs ($1.5M salary)
- Marketing budget ($800k: ads, content, events)
- Sales tools ($200k: CRM, automation)
→ Expected impact: $5M → $10M ARR in 18 months

**R&D ($1.5M - 30%)**:
- 5 engineers ($1M salary)
- Infrastructure ($300k: cloud, tools)
- AI/ML development ($200k: models, data)
→ Expected impact: 10 major features, mobile app

**Operations ($1M - 20%)**:
- Customer Success team ($500k)
- Finance/HR ($300k)
- Legal/compliance ($200k)
→ Expected impact: Support 500+ customers
```

---

## SUMMARY & ACTION ITEMS

### Must Fix (Before Investor Meetings):
1. ✅ Add customer testimonials slide
2. ✅ Strengthen competitive moat explanation
3. ✅ Address churn spike with mitigation plan
4. ✅ Expand team slide with hiring roadmap

### Should Fix (Improves Quality):
5. Add market sizing methodology footnote
6. Detail use of funds breakdown

### Nice to Have (Appendix):
7. Detailed financial model
8. Customer case studies (full)
9. Competitive feature matrix

### Readiness Score: 7.5/10 → 9/10 (after fixes)

**Timeline**: 2-3 days to implement critical fixes, ready for investor meetings by Feb 15

---
```

## Workflow

1. **Input pitch deck structure** (text format, not PPTX)
2. **Analyze each slide** against best practices
3. **Categorize issues** (Critical/Medium/Low)
4. **Generate fixes** with examples
5. **Provide readiness score** and timeline

## Integration with Other Skills

- **pitch-questions** - Audit uses structure generated by pitch-questions
- **investor-qa-generator** - Audit identifies slides that will trigger tough questions
- **market-analysis** - Validates market sizing claims

## Version History

- **2026-02-10**: Adapted for Claude Code CLI
- **Original**: GitHub Copilot version
