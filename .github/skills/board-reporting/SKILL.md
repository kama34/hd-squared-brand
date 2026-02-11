# Board Reporting Skill

## Overview

**Purpose**: Предоставить CEO и Board структурированные шаблоны для квартальных отчетов, investor updates и стратегических презентаций. Обеспечивает прозрачность, фокус на key metrics и actionable insights.

**Target Users**: @CEO (primary), @Board, @CFO (contributes financial data)

**Dependencies**: Finance data from @CFO, Product metrics from @CTO, Market intelligence from @CMO

---

## Components

### 1. `board_deck_template.md`

Шаблон квартальной презентации для Board Meeting.

**Структура** (15 слайдов максимум):
1. Executive Summary (1 слайд)
2. Key Metrics Dashboard (1 слайд)
3. Progress vs OKRs (1-2 слайда)
4. Financial Update (2 слайда)
5. Product/Tech Update (1-2 слайда)
6. GTM & Growth (1-2 слайда)
7. Risks & Mitigation (1 слайд)
8. Deep Dive Topic (2-3 слайда - varies by quarter)
9. Ask from Board (1 слайд)
10. Appendix (additional data if needed)

### 2. `investor_update_template.md`

Ежемесячный email update для инвесторов.

**Формат**: Text-based email (не презентация)

**Sections**:
- TL;DR (3 bullets)
- Metrics (MRR, Churn, Runway)
- Wins этого месяца
- Challenges
- Ask (если есть)

### 3. `metrics_dashboard.md`

Стандартный набор метрик для tracking.

**Categories**:
- **Financial**: MRR, ARR, Burn Rate, Runway
- **Growth**: New Customers, Churn, CAC, LTV
- **Product**: Active Users, Feature Adoption, NPS
- **Team**: Headcount, Key Hires, Employee NPS

---

## Use Cases

### Use Case 1: Подготовка квартального Board Deck

**Scenario**: @CEO готовит Q1 2026 Board Meeting за неделю до встречи.

**Process**:

#### Шаг 1: Соберите данные от C-level

**От @CFO**:
```
Request: "Нужны финансовые данные для Board Deck Q1 2026:
- MRR, ARR, growth rates
- Burn rate, runway
- CAC, LTV, LTV/CAC ratio
- P&L summary
- Scenario analysis (если требуется fundraising)"
```

**От @CTO**:
```
Request: "Нужен продуктовый update для Board:
- Key features shipped (топ 3-5)
- Tech debt status
- Infrastructure costs
- Security incidents (если были)
- Roadmap на Q2"
```

**От @CMO**:
```
Request: "Нужен GTM update для Board:
- Lead generation (месячный рост)
- CAC по каналам
- Конкурентный landscape (новые угрозы?)
- Customer testimonials/case studies"
```

#### Шаг 2: Используйте board_deck_template.md

**Slide 1: Executive Summary**

```markdown
# Q1 2026 Board Update

**TL;DR**:
✅ Achieved 70% of OKRs (3/4 Key Results met)  
✅ MRR grew 15% QoQ ($120k → $138k)  
⚠️ Churn increased to 6% (target: <5%) — mitigation in progress  

**Focus for Q2**: Reduce churn, scale enterprise sales
```

**Slide 2: Key Metrics Dashboard**

```markdown
| Metric | Q1 2026 | Q4 2025 | Change | Status |
|--------|---------|---------|--------|--------|
| **MRR** | $138k | $120k | +15% | ✅ |
| **ARR** | $1.66M | $1.44M | +15% | ✅ |
| **Churn** | 6.0% | 4.5% | +1.5pp | 🔴 |
| **CAC** | $550 | $600 | -8% | ✅ |
| **LTV** | $2,100 | $2,400 | -12% | 🟡 |
| **LTV/CAC** | 3.8x | 4.0x | -0.2x | ✅ |
| **Runway** | 14mo | 16mo | -2mo | 🟡 |

**Commentary**: Churn spike due to product onboarding complexity (addressed in Q2 roadmap).
```

**Slide 3: Progress vs OKRs (Q1 2026)**

```markdown
### Objective 1: Achieve Product-Market Fit in SMB Segment

**KR1**: NPS > 40  
- **Result**: NPS = 38 ❌ (missed by 2 points)  
- **Why**: Onboarding friction → action: new tutorial video launched Apr 1

**KR2**: Churn < 5%  
- **Result**: Churn = 6% ❌ (missed)  
- **Why**: Complex setup for non-technical users  
- **Mitigation**: White-glove onboarding pilot for new customers

**KR3**: 100 paying customers  
- **Result**: 115 customers ✅ (+15%)  

**KR4**: $150k MRR  
- **Result**: $138k MRR 🟡 (92% of target)  
- **Why**: Slower expansion revenue than expected

**Overall OKR Score**: 50% (2/4 KRs met) → Needs improvement
```

**Slide 4-5: Financial Update** (data from @CFO)

```markdown
### Q1 2026 Financial Summary

**Revenue**:
- MRR: $138k (+15% QoQ)
- New Business: $45k (new customers)
- Expansion: $12k (upsells)
- Churn: -$19k (lost customers - up from -$13k in Q4)

**Expenses**:
- Total Burn: $95k/month
- Breakdown:
  - R&D (salaries + infra): $50k (53%)
  - Sales & Marketing: $30k (32%)
  - G&A: $15k (16%)

**Cash Position**:
- Starting Cash (Jan 1): $1.52M
- Ending Cash (Mar 31): $1.39M
- Runway: 14 months (at current burn)

**🟡 Recommendation**: Start fundraising in Q3 (Series A, target $3-5M)
```

**Slide 6: Deep Dive - Churn Analysis**

```markdown
### Deep Dive: Why Churn Increased (4.5% → 6%)

**Root Cause Analysis** (CFO + CTO collaboration):

1. **Onboarding Complexity** (40% of churned users)
   - Users couldn't complete setup in <30 min
   - Missing integrations (Slack, Jira) → frustration

2. **Performance Issues** (30%)
   - Dashboard load time >5sec for large datasets
   - Mobile app crashes (Android)

3. **Pricing Misalignment** (20%)
   - SMB customers hitting limits on base tier → forced upgrade too early

4. **Competition** (10%)
   - 2 customers switched to Competitor X (cheaper, simpler)

**Mitigation Plan** (Q2 Roadmap):
- [ ] Ship interactive onboarding tutorial (Week 1)
- [ ] Add Slack/Jira integrations (Week 4)
- [ ] Performance optimization sprint (Weeks 2-3)
- [ ] Pricing tier adjustment (add mid-tier at $49/mo)

**Expected Impact**: Churn → 4% by end of Q2
```

**Slide 7: Ask from Board**

```markdown
### Ask from Board

1. **Strategic Guidance**: Should we prioritize SMB (current) or test Enterprise? (30-min discussion)
2. **Network Request**: Intro to 2-3 Series A investors for Q3 fundraising prep
3. **Hiring**: Recommendation for VP Sales (when to hire? now vs Q3?)

**Decision Needed Today**:
- Approve $50k budget for sales hiring agency (find VP Sales)
```

#### Шаг 3: Отправьте Board Deck за 1 неделю до встречи

**Email к Board**:

```
Subject: Q1 2026 Board Meeting - Pre-Read Materials

Hi Board,

Attached is the Q1 2026 Board Deck for our meeting on April 10th.

**TL;DR**:
- ✅ Revenue growth continues (+15% QoQ)
- 🔴 Churn spiked to 6% (detailed RCA on slide 6)
- 💡 Requesting guidance on SMB vs Enterprise strategy

**Meeting Agenda** (2 hours):
- Business Review (30 min)
- Deep Dive: Churn Mitigation (30 min)
- Strategic Discussion: SMB vs Enterprise (30 min)
- Q&A (30 min)

Please review the deck before the meeting. Happy to answer questions async.

Best,
[CEO Name]
```

---

### Use Case 2: Monthly Investor Update (Email)

**Scenario**: @CEO отправляет monthly email investors в начале месяца.

**Process**:

1. **Используйте investor_update_template.md**

2. **Шаблон Email**:

```
Subject: [Company Name] - February 2026 Update

Hi [Investor Name],

Here's the monthly update for February 2026.

---

**TL;DR**:
✅ MRR crossed $140k (+16% QoQ)
✅ Shipped 2 major features (Slack integration, mobile app v2)
⚠️ Churn still elevated at 5.8% (down from 6%, but not at target yet)

---

**📊 Metrics**:

| Metric | Feb 2026 | Jan 2026 | Change |
|--------|----------|----------|--------|
| MRR | $142k | $138k | +2.9% |
| Customers | 118 | 115 | +3 |
| Churn | 5.8% | 6.0% | -0.2pp |
| CAC | $520 | $550 | -5.5% |
| Runway | 13mo | 14mo | -1mo |

---

**🎉 Wins This Month**:

1. **Slack Integration Shipped** (Feb 5)
   - Most requested feature (40% of users asked for it)
   - Early adoption: 30% of users connected within first week

2. **Mobile App V2 Launched** (Feb 20)
   - Fixed crash issues (Android)
   - Performance improved: load time -40%
   - App Store rating: 3.8 → 4.2 stars

3. **First Enterprise Deal Closed** ($2k MRR)
   - 50-seat contract with [Company X]
   - Validates potential for upmarket move

---

**🚧 Challenges**:

1. **Churn Still Above Target** (target: <5%)
   - Progress: 6.0% → 5.8%, but slow
   - New onboarding tutorial deployed (Feb 28) — too early to see impact

2. **Hiring Delays**
   - VP Sales search ongoing (3 candidates in final round)
   - Decision expected by March 15

---

**🙏 Ask**:

If you know strong VP Sales candidates (B2B SaaS, SMB focus, $1-5M ARR stage), I'd appreciate intros. Job description: [link]

---

**📅 Next Update**: March 5, 2026

Feel free to reply with questions or schedule a call.

Best,
[CEO Name]
```

---

### Use Case 3: Preparing for Fundraising (Series A Deck)

**Scenario**: @CEO готовит Series A pitch deck для investors.

**Process**:

#### Используйте pitch_deck_structure.md из knowledge base + board_deck_template.md

**Ключевые отличия от Board Deck**:

| Board Deck | Investor Deck |
|------------|---------------|
| Focus: Operations & risks | Focus: Vision & opportunity |
| Audience знает компанию | Audience видит впервые |
| Честность о problems | Highlight strengths (но не врите) |
| 15 слайдов | 12 слайдов (shorter attention span) |

**Series A Deck Structure**:

1. **Problem** (1 слайд)
   - "SMBs waste 10 hours/week on manual reporting"
2. **Solution** (1 слайд)
   - "Automated analytics dashboard in 5 minutes"
3. **Market Size** (1 слайд)
   - TAM: $10B, SAM: $2B, SOM: $200M (first 3 years)
4. **Product Demo** (2 слайда)
   - Screenshots + key differentiators
5. **Traction** (1 слайд)
   - MRR growth chart, customer logos
6. **Business Model** (1 слайд)
   - Pricing tiers, unit economics (LTV/CAC = 3.8x)
7. **Competition** (1 слайд)
   - Positioning matrix (vs Competitor A, B, C)
8. **Go-to-Market** (1 слайд)
   - Channels: Content (50%), Google Ads (30%), Referrals (20%)
9. **Team** (1 слайд)
   - Co-founders + key hires (CTO, CFO credentials)
10. **Financials** (1 слайд)
    - 3-year projection (conservative, base, aggressive)
11. **The Ask** (1 слайд)
    - "Raising $5M Series A at $25M pre-money valuation"
12. **Use of Funds** (1 слайд)
    - 50% Sales & Marketing, 30% R&D, 20% Operations

**Delivery Tips from CEO**:
- Practice pitch 10+ times before investor meetings
- Anticipate questions (Board can help role-play)
- Bring appendix with detailed metrics (but don't present unless asked)

---

## Files Structure

```
.github/skills/board-reporting/
├── SKILL.md                      # This file
├── board_deck_template.md        # Quarterly Board Meeting slides template
├── investor_update_template.md   # Monthly email update template
├── metrics_dashboard.md          # Standard metrics definitions
└── fundraising_deck_structure.md # Series A pitch deck template
```

---

## Best Practices

### 1. Executive Summary = Самый важный слайд

**Board не будет читать весь deck до встречи** (реальность).

TL;DR на первом слайде должен содержать:
- Top 3 wins
- Top 2 concerns
- Required decision/ask

Если Board прочитает только 1 слайд → они должны понять всё из Executive Summary.

### 2. Визуализация > Таблицы

**Bad** ❌:
```
MRR Jan: $120k
MRR Feb: $135k
MRR Mar: $142k
```

**Good** ✅:
```
[Graph showing upward MRR trend with annotations for key events]
"MRR grew 18% in Q1 (Slack integration drove 40% of new signups)"
```

### 3. Честность о проблемах (но с планом решения)

**Bad** ❌:
> "Churn немного вырос" (скрывает масштаб)

**Good** ✅:
> "Churn вырос с 4.5% до 6% (+33%). Root cause: onboarding сложность. Mitigation: новый tutorial + white-glove onboarding. Expected fix by end Q2."

Board ценит:
- Transparency (честность)
- Data-driven analysis (почему?)
- Action plan (что делаем?)

### 4. Asks должны быть конкретными

**Bad** ❌:
> "Нужна помощь с hiring"

**Good** ✅:
> "Нужны intros к 3 VP Sales candidates с experience в B2B SaaS, $1-5M ARR stage. Hiring timeline: decision к концу March."

---

## Integration with Agents

### @CEO
- **Primary user** — готовит все Board/Investor updates
- Uses данные от @CFO, @CTO, @CMO
- Synthesizes в cohesive narrative

### @CFO
- Предоставляет financial slides (P&L, cash flow, unit economics)
- Runs scenario analysis для fundraising decisions

### @CTO
- Предоставляет product/tech slides (roadmap, technical risks, infrastructure costs)

### @CMO
- Предоставляет GTM slides (CAC by channel, competitive positioning)

### @Board
- **Primary audience** — получает Board Decks
- Reviews pre-meeting materials
- Provides feedback и strategic guidance

---

## Metrics Definitions (Reference)

### Financial Metrics

**MRR (Monthly Recurring Revenue)**:
```
Sum of all monthly subscription revenue
```

**ARR (Annual Recurring Revenue)**:
```
ARR = MRR × 12
```

**Burn Rate**:
```
Monthly Expenses - Monthly Revenue
```

**Runway**:
```
Cash Balance / Monthly Burn Rate
```

### Growth Metrics

**CAC (Customer Acquisition Cost)**:
```
Total Sales & Marketing Spend / New Customers
```

**LTV (Lifetime Value)**:
```
ARPU × Gross Margin × (1 / Monthly Churn Rate)
```

**LTV/CAC Ratio**:
```
LTV / CAC
Benchmark: >3x is healthy
```

### Product Metrics

**NPS (Net Promoter Score)**:
```
% Promoters (9-10) - % Detractors (0-6)
Benchmark: >40 is excellent, 30-40 good, <30 needs improvement
```

**Churn Rate**:
```
(Customers Lost / Customers at Start) × 100%
Benchmark: SaaS SMB <5%, Enterprise <2%
```

---

## Changelog

- **2026-02-05**: Initial version (board_deck_template, investor_update_template, metrics_dashboard)
- **TBD**: Add data visualization guidelines (chart types, color schemes)
- **TBD**: Add crisis communication templates (PR incidents, security breaches)
