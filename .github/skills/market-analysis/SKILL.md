# Market Analysis Skill

## Overview

**Purpose**: Обеспечить CMO и CEO систематическим подходом к анализу рынка, конкурентов, позиционирования и Go-to-Market стратегии. Использует web-search (Brave Search MCP) для continuous market intelligence.

**Target Users**: @CMO (primary), @CEO, @Board

**Dependencies**: 
- MCP Brave Search (для web research)
- Knowledge base: `.github/knowledge-base/04_Marketing/`

---

## Components

### 1. `competitor_analysis_framework.md`

Фреймворк для систематического анализа конкурентов.

**Structure**:
- Competitor Identification (Direct, Indirect, Substitute)
- SWOT Analysis (Strengths, Weaknesses, Opportunities, Threats)
- Feature Matrix (что есть у них, чего нет у нас?)
- Pricing Comparison
- Positioning Analysis (как они себя позиционируют?)
- GTM Strategy (какие каналы используют?)

### 2. `market_sizing_template.md`

TAM, SAM, SOM расчет методология.

**Formulas**:
- **TAM (Total Addressable Market)**: Весь рынок (теоретический максимум)
- **SAM (Serviceable Addressable Market)**: Сегмент который мы можем обслужить
- **SOM (Serviceable Obtainable Market)**: Реалистичная доля в первые 3-5 лет

**Methods**: Top-down, Bottom-up, Value theory

### 3. `positioning_strategy.md`

Positioning statement template и differentiation strategies.

**Format**:
```
For [target customer]
Who [statement of need/opportunity]
Our product is [product category]
That [statement of benefit]
Unlike [primary competitive alternative]
Our product [statement of primary differentiation]
```

### 4. `channel_analysis.md`

Оценка GTM каналов (SEO, Paid Ads, Content, Partnerships, etc.)

**Metrics per channel**:
- Cost per Lead (CPL)
- Conversion Rate
- CAC (Customer Acquisition Cost)
- Payback Period
- Scalability (can we 10x spend?)

---

## Use Cases

### Use Case 1: Competitive Intelligence Report (Monthly)

**Scenario**: @CMO готовит monthly competitive update для @CEO.

**Process**:

#### Шаг 1: Web Search для новых событий

**Используйте web-search tool** (Brave Search):

```
Запросы:
1. "[Competitor A] new features 2026"
2. "[Competitor B] funding announcement"
3. "[Competitor C] pricing changes"
4. "[Industry keyword] startup news"
```

**Пример находок**:
- Competitor A raised $20M Series B (TechCrunch article)
- Competitor B launched mobile app (ProductHunt)
- Competitor C acquired by Enterprise Player (Press release)

#### Шаг 2: Используйте competitor_analysis_framework.md

**Создайте отчет**:

```markdown
# Competitive Intelligence Update - February 2026

**Date**: 2026-02-05  
**Analyst**: @CMO

---

## Executive Summary

**Key Developments**:
1. 🔴 **HIGH THREAT**: Competitor A raised $20M Series B → will scale sales aggressively
2. 🟡 **MEDIUM**: Competitor B launched mobile app → addressing our differentiator
3. 🟢 **OPPORTUNITY**: Competitor C acquired → market consolidation (customers looking for alternatives)

**Recommended Actions**:
- Prioritize mobile app roadmap (competitor parity by Q4)
- Increase content marketing to capture Competitor C's displaced customers

---

## Competitor A - Series B Funding Analysis

**Source**: [TechCrunch article link]

**Details**:
- Amount: $20M Series B
- Lead Investor: [VC Firm X]
- Valuation: Estimated $100M post-money
- Use of Funds (from press release):
  - 50% Sales & Marketing (hiring 20 AEs)
  - 30% Product (AI features)
  - 20% International expansion (Europe)

**Threat Assessment**: 🔴 HIGH

**Impact on Us**:
- **Sales**: They will flood market with 20 AEs → expect pricing pressure
- **Product**: AI features may leapfrog us if we don't invest
- **Geography**: Europe expansion → safe for now (we're US-only)

**Strategic Response**:

1. **Near-term** (1-3 months):
   - Monitor their hiring (LinkedIn tracking)
   - Prepare competitive battle cards for sales team
   - Test our messaging против их new positioning

2. **Mid-term** (3-6 months):
   - Evaluate AI feature investment (request from @CTO: feasibility + cost)
   - Consider pricing adjustment if they go aggressive

3. **Long-term** (6-12 months):
   - Europe expansion feasibility study (if they succeed there)

---

## Competitor B - Mobile App Launch

**Source**: [ProductHunt link]

**Analysis**:

**Features** (from app store description):
- Offline mode ✅ (we don't have this)
- Push notifications ✅ (we don't have this)
- Barcode scanning ❌ (niche feature)

**User Reviews** (App Store, 4.1★, 200 reviews):
- Positive: "Finally, mobile version!" (most requested)
- Negative: "Slow loading", "Crashes on Android"

**Threat Level**: 🟡 MEDIUM

**Why Not High?**:
- Early version (bugs, poor reviews)
- Our web app is mobile-responsive (good enough for 80% of users)

**Action Plan**:
- Track adoption rate (how many of THEIR users download?)
- Prioritize mobile app in our Q3 roadmap IF adoption >30%
- Emphasize our stability in messaging: "Web-first, zero bugs"

---

## Competitor C - Acquisition by [Company X]

**Source**: [Press release link]

**Details**:
- Acquirer: [Enterprise Company X]
- Price: Undisclosed (estimated $50-80M based on ARR)
- Reason: Strategic acquisition (bolt-on to existing product)

**Threat Level**: 🟢 LOW (actually an OPPORTUNITY)

**Why Opportunity?**:
- Enterprise acquisitions often disrupt SMB customers (price increases, deprecated features)
- Competitor C had 500+ SMB customers → potential churn

**Proactive Actions**:

1. **Immediate** (this week):
   - Create migration guide: "Switching from [Competitor C] to [Our Product]"
   - Publish blog post: "What [Competitor C] Acquisition Means for SMBs"
   - Offer migration discount (20% off first 3 months)

2. **Outreach** (next 2 weeks):
   - LinkedIn campaign targeting Competitor C users
   - Email campaign: "Concerned about [Competitor C] changes? We're here to help"

3. **Measurement**:
   - Track signups with source = "Competitor C migration"
   - Target: Convert 5-10% of their SMB base (25-50 customers)

---

## Competitive Positioning Matrix

| Feature | Us | Competitor A | Competitor B | Competitor C |
|---------|-----|--------------|--------------|--------------|
| **Pricing** | $29/mo | $39/mo | $25/mo | $49/mo |
| **Setup Time** | <5 min | ~15 min | ~10 min | <5 min |
| **Integrations** | 15+ | 30+ ⚠️ | 8 | 20+ |
| **Mobile App** | ❌ | ✅ | ✅ | ✅ |
| **White-label** | ❌ | ❌ | ❌ | ✅ |
| **Support** | Email (24hr) | Chat (instant) ⚠️ | Email (48hr) | Phone |

**Legend**: ⚠️ = Competitor advantage

**Gaps to Address**:
1. Integrations (us: 15, Competitor A: 30) → prioritize top 10 requested
2. Mobile app → Q3 roadmap
3. Support (consider chat widget instead of email-only)

---

## Recommendations for @CEO

1. **Budget Request**: +$10k/month for content marketing to capture Competitor C customers
2. **Product Priority**: Accelerate mobile app (market moving this direction)
3. **Sales Training**: Update battle cards with Competitor A's new positioning

**Next Update**: March 5, 2026
```

#### Шаг 3: Обновите competitor_list.md в knowledge base

**Добавьте в `.github/knowledge-base/04_Marketing/competitor_list.md`**:

```markdown
## News & Updates Log

### 2026-02-05: Competitor A Series B

**Event**: Raised $20M Series B from [VC Firm X]  
**Impact**: HIGH - will scale sales aggressively  
**Action**: Monitor hiring, prepare competitive response  
**Owner**: @CMO  
**Status**: Ongoing
```

---

### Use Case 2: Market Sizing для Fundraising

**Scenario**: @CEO запрашивает у @CMO: "Нужен TAM/SAM/SOM анализ для Series A deck."

**Process**:

#### Шаг 1: Используйте market_sizing_template.md

**TAM (Total Addressable Market)** - Top-Down Approach:

```markdown
### TAM Calculation (Top-Down)

**Industry**: Business Intelligence & Analytics Software

**Data Sources** (web-search):
- Gartner: "BI software market size 2026" → $30B globally
- IDC: "Analytics tools market forecast" → $40B globally (broader category)

**Assumption**: We focus on SMB segment (10-500 employees), which is 30% of total BI market.

**TAM = $30B × 30% = $9B**

**Geographic Focus**: US market = 40% of global → **TAM (US) = $3.6B**
```

**SAM (Serviceable Addressable Market)** - Bottom-Up Approach:

```markdown
### SAM Calculation (Bottom-Up)

**Our ICP (Ideal Customer Profile)**:
- SMB companies (10-500 employees)
- Industries: SaaS, E-commerce, Professional Services
- Must have: Data-driven decision making need
- Budget: $500-$5,000/year for analytics tools

**Market Size**:
- US SMBs (10-500 employees): 5.8M companies (US Census Bureau)
- % in target industries (SaaS, E-commerce, Services): ~15% = 870k companies
- % data-driven (need analytics): ~40% = 348k companies

**Our Pricing**: Average $49/mo × 12 = $588/year

**SAM = 348,000 companies × $588 = $204M**
```

**SOM (Serviceable Obtainable Market)** - Realistic 5-Year Target:

```markdown
### SOM Calculation (5-Year Projection)

**Assumptions**:
- Year 1: Capture 0.1% of SAM (early traction)
- Year 2: 0.3% (product-market fit)
- Year 3: 0.6% (scaling GTM)
- Year 4: 1.0%
- Year 5: 1.5% (market leader in niche)

**SOM (Year 5)**:
- Target: 1.5% of SAM = 1.5% × 348k companies = **5,220 customers**
- Revenue: 5,220 × $588/year = **$3.1M ARR**

**Conservative/Base/Aggressive Scenarios**:

| Scenario | Year 5 Market Share | Customers | ARR |
|----------|---------------------|-----------|-----|
| Conservative | 0.8% | 2,784 | $1.6M |
| **Base** | **1.5%** | **5,220** | **$3.1M** |
| Aggressive | 3.0% | 10,440 | $6.1M |
```

#### Шаг 2: Визуализация для Investor Deck

```markdown
### Market Opportunity Slide (PowerPoint)

[Funnel graphic]:

TAM (Total Addressable Market)
$3.6B - US BI Software Market (SMB segment)
│
▼
SAM (Serviceable Addressable Market)
$204M - Our Target ICP (348k companies)
│
▼
SOM (Serviceable Obtainable Market)
$3.1M - Realistic 5-Year Target (5.2k customers)

**Key Message**: "Even capturing 1.5% of our addressable market = $3M ARR"
```

#### Шаг 3: Defend Your Numbers

**Investors будут challenge assumptions. Prepare rebuttals**:

**Question**: "Why only 1.5% market share in 5 years? Too conservative?"

**Answer**:
> "1.5% is conservative because:
> 1. Market is fragmented (50+ competitors)
> 2. We're focusing on quality (high NPS) not just growth
> 3. Comparable companies (Competitor D) achieved 2% in 6 years
> 4. If we hit 3% (aggressive case) → $6M ARR"

**Question**: "What if TAM is smaller? Gartner estimates vary."

**Answer**:
> "Even if TAM is 50% smaller ($1.8B instead of $3.6B), our SAM drops to $100M, and SOM to $1.5M ARR in Year 5 — still a venture-backable business."

---

### Use Case 3: Positioning Strategy для нового продукта

**Scenario**: @CTO launches новую фичу "AI-powered insights". @CMO должен создать positioning.

**Process**:

#### Шаг 1: Используйте positioning_strategy.md template

```markdown
# Positioning Statement: AI-Powered Insights

**For** [SMB business owners and managers]  
**Who** [spend hours analyzing data but struggle to find actionable insights]  
**Our product is** [an AI-powered analytics assistant]  
**That** [automatically identifies trends and recommends actions in plain English]  
**Unlike** [traditional dashboards that only show charts]  
**Our product** [tells you WHAT to do, not just WHAT happened]

---

## Key Messages (Hierarchy)

### Primary Message (Headline):
"Stop staring at dashboards. Start taking action."

### Supporting Messages:
1. **AI finds insights for you** → "No PhD in data science required"
2. **Plain English recommendations** → "Your data, explained like a conversation"
3. **Actionable, not just informative** → "We tell you what to do next"

### Proof Points:
- "Users save 5+ hours/week on manual analysis" (customer survey)
- "87% of AI-generated insights led to business actions" (internal data)
- "Built by former data analysts who felt the pain"

---

## Differentiation vs Competitors

| Competitor | Their Positioning | Our Counter-Positioning |
|------------|-------------------|-------------------------|
| **Competitor A** | "Enterprise-grade BI for SMBs" | "You're not an enterprise. Why pay enterprise prices for complexity you don't need?" |
| **Competitor B** | "Beautiful dashboards" | "Pretty charts don't pay bills. We deliver decisions, not decorations." |
| **Competitor C** | "Self-service analytics" | "Self-service = do it yourself. We do it FOR you with AI." |

---

## Target Channels for Messaging

### Website (Above the Fold):
**Headline**: "Your AI Data Analyst. $49/month."  
**Subheadline**: "Stop digging through spreadsheets. Get plain-English insights in seconds."  
**CTA**: "Try Free for 14 Days"

### LinkedIn Ads:
**Hook**: "Spending 10 hours/week in Excel?"  
**Body**: "Our AI reads your data and tells you what to do — in plain English. Join 500+ SMBs saving time."  
**CTA**: "Get Free Insights Report"

### Blog Content:
**SEO Keywords**: "ai data analytics for small business", "automated business insights", "data analysis without coding"

### Sales Script (Opening):
"Most analytics tools show you charts. We tell you what those charts mean and what action to take next. Like having a data analyst on your team for $49/month instead of $80k/year."

---

## Competitive Battle Card

**When Compared to Competitor A**:

| Objection | Response |
|-----------|----------|
| "Competitor A has more integrations" | "True, but 90% of SMBs only use 5 integrations. We have those covered. Plus, more integrations = more complexity." |
| "They have mobile app" | "Coming in Q3. But ask: do you NEED mobile analytics? Most decisions happen at a desk." |
| "Their support is faster" | "We prioritize quality over speed. 24hr response, but always from someone who understands your data, not a chatbot." |

---

## Launch Plan

**Phase 1: Existing Customers** (Week 1)
- Email announcement: "New: Your AI Data Analyst is Here"
- In-app notification
- Tutorial video

**Phase 2: Website Update** (Week 2)
- Homepage refresh with new positioning
- Landing page: `/ai-insights`
- SEO optimization

**Phase 3: Paid Acquisition** (Week 3-4)
- LinkedIn Ads ($5k budget)
- Google Ads ("ai business analytics")
- ProductHunt launch

**Phase 4: PR & Content** (Ongoing)
- Blog post: "How AI is Democratizing Data Analytics for SMBs"
- Guest post on SaaS publications
- Podcast tour (target: B2B SaaS shows)

---

## Success Metrics

**Awareness**:
- 10k impressions on LinkedIn Ads (Week 1-4)
- 500 organic visits to `/ai-insights` page (Month 1)

**Adoption**:
- 30% of existing customers enable AI feature (Month 1)
- 50 new signups attributed to AI messaging (Month 1)

**Retention**:
- Users with AI enabled have 20% lower churn (Month 3)
```

---

## Files Structure

```
.github/skills/market-analysis/
├── SKILL.md                           # This file
├── competitor_analysis_framework.md   # SWOT, feature matrix, pricing
├── market_sizing_template.md          # TAM/SAM/SOM methodology
├── positioning_strategy.md            # Positioning statement template
└── channel_analysis.md                # GTM channel ROI framework
```

---

## Best Practices

### 1. Continuous Monitoring > One-Time Analysis

**Set up alerts** (Google Alerts, Feedly, LinkedIn следование):
- Competitor names
- Industry keywords ("SMB analytics news")
- Funding announcements ("[competitor] raised")

**Frequency**:
- Daily: Quick scan (10 min)
- Weekly: Deep dive on 1-2 competitors (1 hour)
- Monthly: Comprehensive report for @CEO
- Quarterly: Strategic repositioning review

### 2. Data-Driven, не Anecdotal

**Bad** ❌:
> "I think customers prefer our UX"

**Good** ✅:
> "87% of users rated our UX 4-5 stars (vs Competitor A: 67% based on G2 reviews)"

**Sources для data**:
- G2, Capterra (user reviews)
- SimilarWeb (traffic estimates)
- LinkedIn (employee count trends)
- Crunchbase (funding history)

### 3. Positioning = Trade-Offs

**You can't be everything to everyone.**

**Good positioning**:
- "We're the simplest analytics tool for non-technical SMB owners" → embraces "simple" (not "powerful")

**Bad positioning**:
- "We're simple AND powerful AND cheap AND feature-rich" → nobody believes you

**Exercise**: "We're willing to sacrifice [X] to be the best at [Y]"
- Example: "We sacrifice advanced SQL customization to be the easiest no-code solution"

---

## Integration with Agents

### @CMO
- **Primary user** — owns market analysis and competitive intelligence
- Uses web-search extensively for real-time data
- Updates knowledge base (`04_Marketing/competitor_list.md`)

### @CEO
- **Receives insights** from @CMO
- Uses for strategic decisions (pivot, fundraising, partnerships)
- Incorporates into Board decks

### @Board
- Получает competitive updates на Board Meetings
- Provides network intelligence (e.g., "I heard Competitor X is struggling")

### @CTO
- Получает feature gap analysis от @CMO
- Prioritizes roadmap based on competitive pressure

---

## Web-Search Best Practices

### Effective Query Patterns

**Competitor Intelligence**:
```
✅ "Competitor A new features 2026"
✅ "Competitor B funding announcement"
✅ "Competitor C pricing page" site:competitor.com
❌ "competitor news" (too vague)
```

**Market Sizing**:
```
✅ "SMB analytics market size Gartner"
✅ "business intelligence software TAM forecast"
❌ "market size" (too broad)
```

**Trend Analysis**:
```
✅ "B2B SaaS trends 2026 Forrester"
✅ "AI adoption SMB survey"
❌ "what's trending" (not specific)
```

### Source Credibility

**Trustworthy**:
- Gartner, Forrester, IDC (research firms)
- TechCrunch, VentureBeat (tech news)
- Official company blogs/press releases
- Government data (US Census, Bureau of Labor Statistics)

**Be Skeptical**:
- Unverified blogs
- Competitor marketing claims (verify independently)
- Outdated data (>2 years old)

---

## Troubleshooting

**Problem**: "Web-search не находит нужную информацию о конкуренте"

**Solution**:
- Try alternative queries (company name variations)
- Check LinkedIn (employee count, recent hires → growth signal)
- Use site-specific search (`site:competitor.com pricing`)
- Reach out to @CEO/@Board (may have insider knowledge)

**Problem**: "TAM/SAM/SOM numbers сильно отличаются от разных источников"

**Solution**:
- Use multiple sources, take average or range
- Explain assumptions в investor deck: "TAM estimated $3-5B depending on methodology"
- Focus on SAM/SOM (more defendable numbers) instead of TAM

---

## Changelog

- **2026-02-05**: Initial version (competitor_analysis_framework, market_sizing_template, positioning_strategy)
- **TBD**: Add JTBD (Jobs-to-be-Done) framework for customer research
- **TBD**: Add pricing strategy framework (value-based vs cost-plus vs competitive)
