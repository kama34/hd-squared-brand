# Investor QA Generator Skill

## Overview

**Purpose**: Генерация жестких, глубоких вопросов инвесторов по структуре pitch презентации для подготовки к Q&A сессии. Включает анализ скрытых мотивов каждого вопроса.

**Target Users**: CEO (primary), CFO, Board

**Capabilities**:
- Generate 10-15 tough investor questions by category (Market, Product, Finance, Team)
- Reveal hidden motives behind each question
- Identify "killer question" (hardest to answer)
- Suggest additional slides/data for answers
- Prepare CEO for due diligence

## Required Tools

- `Read` - Read pitch deck structure from knowledge base
- `Write` - Save Q&A preparation document
- `WebSearch` - Research common investor concerns in industry

## Usage Examples

### Example 1: Generate Questions from Pitch Deck

```markdown
**Input**: Sales AI pitch deck structure

**Process**:

1. Read pitch deck:
   ```
   Read: Sales AI/knowledge-base/01_Strategy/pitch_deck_series_a.md

   Structure:
   1. Problem - SMBs waste 10 hours/week on manual reporting
   2. Solution - AI-powered analytics in 5 minutes
   3. Market Size - TAM: $3.6B, SAM: $204M, SOM: $3.1M (Year 5)
   4. Product Demo - Screenshots, key features
   5. Traction - MRR: $138k, 118 customers, +15% QoQ growth
   6. Business Model - $29-$99/month pricing, LTV/CAC: 3.8x
   7. Competition - Positioning vs 3 competitors
   8. Go-to-Market - Content (50%), Google Ads (30%), Referrals (20%)
   9. Team - 2 co-founders (ex-Salesforce, ex-Google)
   10. Financials - 3-year projection ($1.6M-$6.1M ARR scenarios)
   11. The Ask - $5M Series A at $25M pre-money
   12. Use of Funds - 50% Sales, 30% R&D, 20% Ops
   ```

2. Generate questions:

---

## Investor Q&A Preparation (Sales AI Series A)

**Date**: 2026-02-10
**Generated for**: CEO pitch presentation

---

### КАТЕГОРИЯ: РЫНОК (Market)

**Q1**: "Ваш TAM $3.6B основан на отчете Gartner. Но Gartner включает enterprise сегмент, который вы не таргетируете. Как вы объясните, что SAM $204M реалистичен?"

**Скрытый мотив**: Проверить, понимаете ли вы свой рынок глубоко или используете inflated numbers для привлечения внимания.

**Как подготовиться**:
- Подготовьте детальную методологию TAM→SAM→SOM
- Покажите bottom-up расчет SAM (количество компаний × ARPU)
- Добавьте слайд в Appendix с breakdown по индустриям
- Сравните с comparable company market share (Competitor D: 2% за 6 лет)

**Дополнительные данные**:
- US Census data: 5.8M SMBs (10-500 employees)
- % data-driven companies: 40% (source: SMB survey)
- ICP conversion rate: 15% addressable → 348k companies

---

**Q2**: "3 конкурента уже на рынке. Почему клиент должен выбрать вас, а не более established player?"

**Скрытый мотив**: Проверить, есть ли у вас defensible moat или вы просто "me-too" продукт.

**Как подготовиться**:
- Четко артикулируйте differentiation (AI insights vs dashboards)
- Покажите customer testimonials (цитаты: "We switched from Competitor A because...")
- Добавьте slide: Feature Comparison Matrix (highlight 2-3 unique features)
- Proof point: 30% of new customers = switchers from competitors

**Killer slide**:
```
Title: "Why Customers Choose Us Over Competitors"

Key Points:
1. Setup Time: <5min (vs 15min for Competitor A)
2. AI Insights: Actionable recommendations (competitors = passive dashboards)
3. Pricing: $29/mo (vs $39 for Competitor A, $49 for Competitor C)

Customer Quote:
"We tried Competitor A for 3 months but couldn't get actionable insights.
Sales AI told us exactly what to do." - [Customer Name], CEO, [Company]
```

---

### КАТЕГОРИЯ: ПРОДУКТ (Product)

**Q3**: "Вы показываете screenshots, но не live demo. Продукт готов или это vaporware?"

**Скрытый мотив**: Проверить product maturity. Ищут red flags (неготовый продукт, beta version).

**Как подготовиться**:
- Предложите live demo (не скрывайте продукт)
- Подготовьте demo environment с real data
- Добавьте metrics: 118 paying customers, NPS: 38, uptime: 99.5%
- Video demo в Appendix (если live demo невозможен на pitch)

**Данные для убедительности**:
- Product launched: [Date]
- Current version: v2.3
- Feature releases: 12 major features in last 6 months
- Customer retention: 95% (после onboarding)

---

**Q4**: "AI-powered insights — это просто hype или реальная технология? Какие ML models используете?"

**Скрытый мотив**: Проверить tech depth. Многие стартапы claim "AI" без real ML.

**Как подготовиться** (для CEO):
- Brief от CTO: Какие ML models используются (GPT-4 API, custom LSTM для forecasting, etc.)
- Explain в простых терминах: "We use GPT-4 for natural language insights + proprietary forecasting models"
- Не нужен deep dive, но избегайте buzzwords без substance
- Proof: "87% of AI insights led to customer actions" (metric)

**Tech credibility**:
- CTO bio: Ex-Google AI team, 10 years ML experience
- Patents/publications: [If any]
- Tech stack: Modern (Python, PyTorch, cloud-native)

---

### КАТЕГОРИЯ: ФИНАНСЫ (Financials)

**Q5**: "LTV/CAC 3.8x выглядит отлично, но ваш churn 4%. Для SMB это нормально, но как вы планируете его снизить? Иначе LTV упадет."

**Скрытый мотив**: Проверить, понимаете ли вы drivers of unit economics и есть ли план улучшения.

**Как подготовиться**:
- Acknowledge проблему (churn spike в Q1: 4.5% → 6% → 4% сейчас)
- Root cause analysis: Onboarding complexity (уже solved)
- Mitigation plan: New tutorial (deployed Feb 28), белое-glove onboarding
- Target: Churn <3% к концу Q2 → LTV increases to $3,000
- Recalculate unit economics с улучшенным churn

**Улучшенная модель**:
```
Current: Churn 4% → LTV $2,250
Target:  Churn 3% → LTV $3,000
Impact:  LTV/CAC: 3.8x → 5.0x (excellent)
```

---

**Q6**: "Вы просите $25M pre-money при $1.66M ARR. Это 15x revenue multiple. Почему мы должны платить такую premium оценку?"

**Скрытый мотив**: Проверить, оправдана ли ваша valuation или вы просто greedy.

**Как подготовиться**:
- Benchmark с comparable companies (show 3-5 comps)
- Обоснуйте premium: Рост (+15% QoQ), Unit economics (LTV/CAC 3.8x), Market opportunity
- Покажите traction trajectory: "$1.66M → $3.1M ARR projected in 12 months"
- Будьте готовы negotiate: "We're open to discussion, but $25M reflects our growth + market position"

**Comps table**:
| Company | ARR | Valuation | Multiple | Notes |
|---------|-----|-----------|----------|-------|
| Competitor D | $5M | $60M | 12x | Similar stage |
| Competitor E | $3M | $45M | 15x | Slower growth |
| **Sales AI** | **$1.66M** | **$25M** | **15x** | **Faster growth** |

---

### КАТЕГОРИЯ: КОМАНДА (Team)

**Q7**: "2 co-founders, но нет VP Sales. Как вы планируете scale to $10M ARR без experienced sales leader?"

**Скрытый мотив**: Проверить, есть ли у вас hiring plan и понимаете ли key gaps в команде.

**Как подготовиться**:
- Acknowledge gap: "We're actively recruiting VP Sales (3 candidates in final round)"
- Timeline: Hire by end of March
- Plan B: CEO handles sales до найма (worked so far: 118 customers)
- Use of funds: $500k allocated for sales team hiring (VP Sales + 2 AEs)

**Hiring roadmap slide**:
```
Title: "Key Hires (Next 6 Months)"

Q1 2026:
- VP Sales (finalist candidates from Salesforce, HubSpot)
- Senior Backend Engineer (scaling infra)

Q2 2026:
- 2 Account Executives (under VP Sales)
- Customer Success Manager

Budget: $500k from Series A
```

---

**Q8**: "Оба founders technical (ex-Salesforce, ex-Google). Кто отвечает за business/sales?"

**Скрытый мотив**: Проверить business acumen. Tech founders часто weak на sales/marketing.

**Как подготовиться**:
- Highlight CEO business experience (если есть)
- Покажите traction: "118 customers acquired by CEO-led sales (no formal sales team yet)"
- Explain: "We'll hire VP Sales to professionalize, but proven we can sell"
- Advisors: Do you have business-side advisors? (If yes, mention)

**Proof of business skills**:
- CAC optimization: $650 → $600 (improved channel mix)
- Pricing strategy: 3 tiers ($29/$49/$99) based on customer interviews
- GTM strategy: Content-first (50% of leads) - efficient

---

### 🔴 KILLER QUESTION

**"Если ваш churn остается 4% и вы не можете его снизить, ваш LTV падает до $2,250, что делает unit economics borderline (LTV/CAC 3.75x вместо целевого 5x). Что вы будете делать?"**

**Почему это killer**:
- Затрагивает core assumption (churn)
- Показывает, что investor глубоко проанализировал вашу модель
- Требует concrete plan, не vague promises

**Как ответить**:

1. **Acknowledge**: "Вы правы, churn — наш #1 risk. Мы это понимаем."

2. **Root Cause** (уже known): "Churn spike был из-за onboarding complexity. We fixed это."

3. **Evidence**: "New tutorial deployed Feb 28. Early data: 30% of new users completed setup (vs 20% before)."

4. **Mitigation Plan**:
   - White-glove onboarding для new customers (first 30 days)
   - Customer Success hire в Q2
   - Quarterly NPS surveys → identify churn risks early

5. **Downside Protection**: "Даже если churn остается 4%, LTV/CAC 3.75x все еще healthy (>3x benchmark). Но мы target 3% для margin of safety."

6. **Upside**: "Если churn drops to 3%, LTV/CAC becomes 5x — exceptional unit economics."

**Дополнительный слайд**:
```
Title: "Churn Mitigation Plan"

Problem: Churn spiked to 6% in Q1 (now 4%)

Root Cause:
- Onboarding complexity (45% of churned users)
- Performance issues (30%)

Actions Taken:
✅ New interactive tutorial (deployed Feb 28)
✅ Performance optimization (-40% load time)
✅ Slack integration (most requested feature)

Expected Impact:
- Churn: 4% → 3% by end Q2
- LTV: $2,250 → $3,000
- LTV/CAC: 3.75x → 5.0x

Monitoring:
- Weekly NPS tracking
- Monthly cohort retention analysis
- Customer Success hire (Q2)
```

---

### РЕКОМЕНДАЦИИ ПО ПОДГОТОВКЕ

**Mandatory slides to add to Appendix**:
1. TAM/SAM/SOM detailed methodology
2. Feature comparison matrix vs competitors
3. Customer testimonials / case studies
4. Churn mitigation plan (detailed)
5. Hiring roadmap (next 6-12 months)
6. Valuation comps table

**Practice answers to**:
- Killer question (churn risk)
- Valuation justification
- Competitive differentiation
- Tech depth (AI/ML models)

**Bring to meeting**:
- Live demo ready (or video backup)
- Detailed financial model (for deep dive)
- Customer references (investors can call)
- Cap table (if requested)

---
```

3. **Save preparation document**:
   ```
   Write: Sales AI/knowledge-base/01_Strategy/investor_qa_prep_series_a.md
   ```

4. **CEO rehearses answers** with Board/advisors

## Workflow: Preparing for Investor Meeting

**Timeline**: 1 week before investor pitch

**Steps**:

1. **Input pitch deck structure** to skill
2. **Generate 10-15 questions** categorized by topic
3. **Identify killer question** (hardest to answer)
4. **Prepare additional slides** for Appendix
5. **Rehearse answers** with Board (role-play)
6. **Update pitch deck** based on anticipated questions

## Integration with Other Skills

### board-reporting
- Uses Board Deck structure as input
- Prepares CEO for Board Q&A sessions

### finance-forecasting
- Financial questions reference unit economics calculations
- Scenario analysis for "what if" questions

### market-analysis
- Competitive questions based on competitor intelligence
- Market sizing questions validate TAM/SAM/SOM

### pitch-audit
- Pitch audit identifies weak slides → QA generator focuses there
- Combined workflow: Audit pitch → Generate questions → Strengthen weak areas

## Best Practices

### 1. Realistic Questions

```
❌ BAD (softball): "What's your growth rate?"
✅ GOOD (challenging): "Your growth is 15% QoQ, but Competitor A grew 30% QoQ. Why are you slower?"
```

### 2. Reveal Hidden Motives

Every question should include:
- The surface question
- The hidden motive (what investor really checks)
- How to prepare (data/slides needed)

### 3. Identify Weakest Points

Focus questions on:
- Slides with vague data ("TBD", "Estimated")
- Claims without proof ("AI-powered" without tech details)
- Financial assumptions (churn, growth rate, valuation)

## Troubleshooting

### Problem: "Generated questions too easy"

**Solution**: Make questions more specific and data-driven
```
Generic: "How do you compete?"
Specific: "Competitor A has 30 integrations, you have 15. Won't enterprise customers choose them?"
```

### Problem: "Don't know how to answer killer question"

**Solution**:
1. Flag to Board/advisors for guidance
2. Prepare honest answer (acknowledge risk + mitigation plan)
3. Add data/slides to support answer
4. If truly unanswerable → reconsider pitch strategy

### Problem: "Too many questions (overwhelming)"

**Solution**: Prioritize by likelihood
- Must prepare: 5 highest-probability questions
- Should prepare: 5 medium-probability questions
- Nice to have: 5 edge-case questions

## Version History

- **2026-02-10**: Adapted for Claude Code CLI
  - Added Read/Write integration
  - Sales AI example Q&A
  - Russian-language formatting
- **Original**: GitHub Copilot version with generate_investor_questions.py

## Related Files

- `generate_investor_questions.py` - Question generation script
- `.github/skills/investor-qa-generator/` - Original version
- `pitch-audit/` - Related skill (pitch deck review)
