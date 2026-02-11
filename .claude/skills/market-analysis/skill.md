# Market Analysis Skill

## Overview

**Purpose**: Систематический подход к анализу рынка, конкурентов, позиционирования и Go-to-Market стратегии. Использует WebSearch для continuous market intelligence.

**Target Users**: CMO (primary), CEO, Board

**Capabilities**:
- Competitive intelligence (SWOT, feature matrix, pricing)
- Market sizing (TAM/SAM/SOM)
- Positioning strategy
- GTM channel analysis
- Real-time competitor monitoring

## Required Tools

Claude Code tools used by this skill:
- `WebSearch` - Research competitors, market trends, industry reports
- `WebFetch` - Fetch competitor websites, pricing pages
- `Read` - Read knowledge base (competitor lists, market data)
- `Write` - Save research findings to knowledge base
- `Edit` - Update competitor intelligence reports

## Core Frameworks

### 1. Competitor Analysis Framework

**Structure**:
- Competitor Identification (Direct, Indirect, Substitute)
- SWOT Analysis
- Feature Matrix (what they have that we don't)
- Pricing Comparison
- Positioning Analysis
- GTM Strategy (channels they use)

### 2. Market Sizing Methodology

**TAM/SAM/SOM**:
- **TAM** (Total Addressable Market): Entire market (theoretical maximum)
- **SAM** (Serviceable Addressable Market): Segment we can serve
- **SOM** (Serviceable Obtainable Market): Realistic share in 3-5 years

**Methods**: Top-down, Bottom-up, Value theory

### 3. Positioning Strategy Template

```
For [target customer]
Who [statement of need]
Our product is [product category]
That [statement of benefit]
Unlike [competitive alternative]
Our product [primary differentiation]
```

## Usage Examples

### Example 1: Monthly Competitive Intelligence Report

```markdown
**Trigger**: CMO prepares monthly update for CEO

**Process**:

1. **Web Search for competitor news**:
   ```
   Query: "Competitor A new features 2026"
   Query: "Competitor B funding announcement"
   Query: "Competitor C pricing changes"
   Query: "[Industry] startup news 2026"
   ```

2. **Findings Example**:
   - Competitor A raised $20M Series B (TechCrunch)
   - Competitor B launched mobile app (ProductHunt)
   - Competitor C acquired by Enterprise Player

3. **Generate Report**:

---

# Competitive Intelligence Update - February 2026

**Date**: 2026-02-10
**Analyst**: @CMO

## Executive Summary

**Key Developments**:
1. 🔴 **HIGH THREAT**: Competitor A raised $20M → will scale sales
2. 🟡 **MEDIUM**: Competitor B mobile app → addresses our differentiator
3. 🟢 **OPPORTUNITY**: Competitor C acquired → customers seeking alternatives

**Recommended Actions**:
- Prioritize mobile app roadmap (parity by Q4)
- Content marketing to capture Competitor C's displaced customers

---

## Competitor A - Series B Funding

**Source**: [TechCrunch link]

**Details**:
- Amount: $20M Series B
- Lead: [VC Firm X]
- Valuation: ~$100M post-money
- Use of Funds:
  - 50% Sales (hiring 20 AEs)
  - 30% Product (AI features)
  - 20% Europe expansion

**Threat Level**: 🔴 HIGH

**Impact on Us**:
- **Sales**: 20 new AEs → expect pricing pressure
- **Product**: AI features may leapfrog us
- **Geography**: Europe expansion (we're US-only → safe for now)

**Strategic Response**:
1. **Near-term** (1-3 months):
   - Monitor hiring (LinkedIn tracking)
   - Prepare competitive battle cards
   - Test messaging against their positioning

2. **Mid-term** (3-6 months):
   - Evaluate AI feature investment (ask CTO: feasibility + cost)
   - Consider pricing adjustment if they go aggressive

---

## Competitor B - Mobile App Launch

**Source**: [ProductHunt link]

**Features** (from app store):
- Offline mode ✅ (we lack this)
- Push notifications ✅ (we lack this)
- Barcode scanning ❌ (niche)

**User Reviews** (4.1★, 200 reviews):
- Positive: "Finally mobile!" (most requested)
- Negative: "Slow loading", "Android crashes"

**Threat Level**: 🟡 MEDIUM

**Why Not High?**:
- Early version (bugs, poor reviews)
- Our web app is mobile-responsive (80% use case)

**Action Plan**:
- Track adoption (% of their users downloading)
- Prioritize mobile in Q3 IF adoption >30%
- Messaging: "Web-first, zero bugs"

---

## Competitive Positioning Matrix

| Feature | Us | Competitor A | B | C |
|---------|-----|--------------|---|---|
| **Pricing** | $29 | $39 | $25 | $49 |
| **Setup** | <5min | ~15min | ~10min | <5min |
| **Integrations** | 15+ | 30+⚠️ | 8 | 20+ |
| **Mobile App** | ❌ | ✅ | ✅ | ✅ |
| **Support** | Email | Chat⚠️ | Email | Phone |

**Gaps to Address**:
1. Integrations (us: 15, A: 30) → add top 10 requested
2. Mobile app → Q3 roadmap
3. Support (consider chat widget)

---

## Recommendations for CEO

1. **Budget**: +$10k/month content marketing (capture C's customers)
2. **Product**: Accelerate mobile app
3. **Sales**: Update battle cards with A's positioning

**Next Update**: March 10, 2026

---
```

4. **Save to knowledge base**:
   ```
   Write to: [Startup]/knowledge-base/04_Marketing/competitive_intel_2026_02.md
   Edit: [Startup]/knowledge-base/04_Marketing/competitor_list.md
   ```

### Example 2: Market Sizing for Fundraising

```markdown
**Trigger**: CEO requests TAM/SAM/SOM for Series A deck

**Process**:

1. **Research market data with WebSearch**:
   ```
   Query: "business intelligence software market size 2026 Gartner"
   Query: "analytics tools market forecast IDC"
   Query: "SMB analytics market report"
   ```

2. **Calculate TAM (Top-Down)**:

---

### TAM Calculation

**Industry**: Business Intelligence & Analytics Software

**Data Sources** (from WebSearch):
- Gartner: "BI software market 2026" → $30B globally
- IDC: "Analytics tools forecast" → $40B globally (broader)

**Assumption**: SMB segment (10-500 employees) = 30% of total BI market

**TAM = $30B × 30% = $9B**

**Geographic Focus**: US = 40% of global → **TAM (US) = $3.6B**

---

3. **Calculate SAM (Bottom-Up)**:

---

### SAM Calculation

**Our ICP** (Ideal Customer Profile):
- SMB companies (10-500 employees)
- Industries: SaaS, E-commerce, Services
- Need data-driven decisions
- Budget: $500-$5k/year for analytics

**Market Size**:
- US SMBs (10-500 employees): 5.8M (US Census)
- % in target industries: ~15% = 870k
- % data-driven (need analytics): ~40% = 348k companies

**Our Pricing**: $49/mo × 12 = $588/year

**SAM = 348,000 × $588 = $204M**

---

4. **Calculate SOM (5-Year Projection)**:

---

### SOM Calculation

**Assumptions**:
- Year 1: 0.1% of SAM (early traction)
- Year 2: 0.3% (product-market fit)
- Year 3: 0.6% (scaling GTM)
- Year 4: 1.0%
- Year 5: 1.5% (market leader in niche)

**SOM (Year 5)**:
- Target: 1.5% of SAM = 5,220 customers
- Revenue: 5,220 × $588 = **$3.1M ARR**

**Scenarios**:

| Scenario | Year 5 Share | Customers | ARR |
|----------|--------------|-----------|-----|
| Conservative | 0.8% | 2,784 | $1.6M |
| **Base** | **1.5%** | **5,220** | **$3.1M** |
| Aggressive | 3.0% | 10,440 | $6.1M |

---

5. **Defend Your Numbers** (prep for investor questions):

**Q**: "Why only 1.5% in 5 years?"

**A**: "Conservative because:
1. Market fragmented (50+ competitors)
2. Focus on quality (high NPS) not just growth
3. Comparable (Competitor D) achieved 2% in 6 years
4. If we hit 3% (aggressive) → $6M ARR"

**Q**: "What if TAM is smaller?"

**A**: "Even if TAM is 50% smaller ($1.8B), SAM drops to $100M, SOM to $1.5M ARR — still venture-backable."

---
```

### Example 3: Positioning Strategy for New Feature

```markdown
**Trigger**: CTO launches "AI-powered insights", CMO creates positioning

**Process**:

1. **Use positioning template**:

---

# Positioning Statement: AI-Powered Insights

**For** [SMB business owners and managers]
**Who** [spend hours analyzing data but struggle to find actions]
**Our product is** [an AI analytics assistant]
**That** [automatically identifies trends and recommends actions in plain English]
**Unlike** [traditional dashboards that only show charts]
**Our product** [tells you WHAT to do, not just WHAT happened]

---

## Key Messages

**Primary** (Headline):
"Stop staring at dashboards. Start taking action."

**Supporting**:
1. "AI finds insights for you" → "No PhD required"
2. "Plain English recommendations" → "Data, explained like a conversation"
3. "Actionable, not just informative" → "We tell you what to do next"

**Proof Points**:
- "Users save 5+ hours/week" (customer survey)
- "87% of AI insights led to business actions" (internal data)
- "Built by former data analysts who felt the pain"

---

## Differentiation vs Competitors

| Competitor | Their Positioning | Our Counter |
|------------|-------------------|-------------|
| **A** | "Enterprise BI for SMBs" | "You're not enterprise. Why pay for complexity?" |
| **B** | "Beautiful dashboards" | "Pretty charts don't pay bills. We deliver decisions." |
| **C** | "Self-service analytics" | "Self-service = DIY. We do it FOR you with AI." |

---

## Launch Plan

**Phase 1**: Existing customers (Week 1)
- Email: "New: Your AI Data Analyst is Here"
- In-app notification
- Tutorial video

**Phase 2**: Website (Week 2)
- Homepage refresh
- Landing page: `/ai-insights`
- SEO optimization

**Phase 3**: Paid Ads (Week 3-4)
- LinkedIn Ads ($5k budget)
- Google Ads ("ai business analytics")
- ProductHunt launch

**Phase 4**: PR & Content (Ongoing)
- Blog: "How AI Democratizes Analytics for SMBs"
- Guest posts
- Podcast tour

---
```

## Web Search Best Practices

### Effective Query Patterns

**Competitor Intelligence**:
```
✅ "Competitor A new features 2026"
✅ "Competitor B funding announcement"
✅ "Competitor C pricing" site:competitor.com
❌ "competitor news" (too vague)
```

**Market Sizing**:
```
✅ "SMB analytics market size Gartner 2026"
✅ "business intelligence TAM forecast"
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
- Government data (Census, BLS)

**Be Skeptical**:
- Unverified blogs
- Competitor marketing claims
- Outdated data (>2 years)

## Workflow: Continuous Monitoring

### Daily (10 min)

- Quick scan of Google Alerts
- LinkedIn feed (competitor follows)
- ProductHunt (new launches)

### Weekly (1 hour)

- Deep dive on 1-2 competitors
- Track hiring (LinkedIn job posts)
- Check pricing pages (changes?)

### Monthly (3-4 hours)

- Comprehensive report for CEO
- Update knowledge base
- Identify strategic threats

### Quarterly (full day)

- Strategic repositioning review
- Market sizing update
- GTM channel effectiveness

## Integration with Other Skills

### finance-forecasting
- CAC data by channel → informs budget allocation

### board-reporting
- Competitive intel → Board Deck threats slide
- TAM/SAM/SOM → Fundraising presentations

### tech-audit
- Competitor feature gaps → roadmap prioritization

## Best Practices

### 1. Continuous > One-Time

Set up **alerts**:
- Google Alerts (competitor names)
- Feedly (industry keywords)
- LinkedIn (follow competitors)

### 2. Data-Driven, Not Anecdotal

**Bad** ❌:
> "I think customers prefer our UX"

**Good** ✅:
> "87% rated our UX 4-5 stars (vs Competitor A: 67% on G2)"

**Data sources**:
- G2, Capterra (user reviews)
- SimilarWeb (traffic estimates)
- LinkedIn (employee trends)
- Crunchbase (funding history)

### 3. Positioning = Trade-Offs

**You can't be everything.**

**Good**:
- "Simplest analytics for non-technical SMB owners" → embraces "simple"

**Bad**:
- "Simple AND powerful AND cheap AND feature-rich" → nobody believes

**Exercise**: "We sacrifice [X] to be best at [Y]"
- Example: "We sacrifice SQL customization to be easiest no-code solution"

## Troubleshooting

### Problem: "Web search doesn't find competitor info"

**Solution**:
- Try alternative queries (company name variations)
- Check LinkedIn (employee count, hires → growth signal)
- Use site-specific: `site:competitor.com pricing`
- Reach out to CEO/Board (may have insider knowledge)

### Problem: "TAM/SAM/SOM numbers vary widely"

**Solution**:
- Use multiple sources, take average or range
- Explain assumptions: "TAM estimated $3-5B depending on methodology"
- Focus on SAM/SOM (more defendable) instead of TAM

### Problem: "Too many competitors to track"

**Solution**:
- Prioritize: Focus on top 3-5 direct competitors
- Tier system: Tier 1 (track weekly), Tier 2 (monthly), Tier 3 (quarterly)
- Automate alerts (Google Alerts, Feedly)

## Version History

- **2026-02-10**: Adapted for Claude Code CLI
  - Added WebSearch/WebFetch integration
  - Query patterns for effective research
  - Real-time monitoring workflows
- **2026-02-05**: Original GitHub Copilot version
  - Competitor analysis framework
  - Market sizing template
  - Positioning strategy

## Related Files

- `.github/skills/market-analysis/SKILL.md` - Original version
- `[Startup]/knowledge-base/04_Marketing/competitor_list.md` - Competitor database
- `[Startup]/knowledge-base/04_Marketing/user_personas.md` - Target customer profiles
