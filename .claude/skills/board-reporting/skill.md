# Board Reporting Skill

## Overview

**Purpose**: Структурированные шаблоны для квартальных Board Meetings, investor updates и стратегических презентаций. Обеспечивает прозрачность, фокус на key metrics и actionable insights.

**Target Users**: CEO (primary), Board, CFO (contributes financial data)

**Capabilities**:
- Quarterly Board Deck generation (15-slide structure)
- Monthly investor email updates
- Metrics dashboard (standard KPI definitions)
- Fundraising pitch deck structure
- Crisis communication templates

## Required Tools

Claude Code tools used by this skill:
- `Read` - Read financial/product data from knowledge base
- `Write` - Generate Board Decks and investor updates
- `Edit` - Update templates with current data
- `WebSearch` - Research industry benchmarks for context

## Skill Integration

This skill synthesizes data from:
- **finance-forecasting** → Runway, unit economics, scenario analysis
- **tech-audit** → Security posture, tech debt status
- **market-analysis** → Competitive landscape, market sizing
- **CTO updates** → Product roadmap, infrastructure status
- **CMO updates** → GTM strategy, CAC by channel

## Board Deck Structure (15 slides)

### Standard Quarterly Deck

1. **Executive Summary** (1 slide)
   - Top 3 wins
   - Top 2 concerns
   - Required decision/ask

2. **Key Metrics Dashboard** (1 slide)
   - MRR/ARR, Churn, CAC, LTV, LTV/CAC, Runway
   - QoQ growth rates
   - Status indicators (✅/🟡/🔴)

3. **Progress vs OKRs** (1-2 slides)
   - Objective breakdown
   - Key Results with actual vs target
   - Commentary on misses

4. **Financial Update** (2 slides)
   - Revenue breakdown (new/expansion/churn)
   - Burn rate analysis
   - Cash position & runway
   - Scenario analysis (if fundraising needed)

5. **Product/Tech Update** (1-2 slides)
   - Key features shipped
   - Tech debt status
   - Security incidents (if any)
   - Q+1 roadmap preview

6. **GTM & Growth** (1-2 slides)
   - Lead generation trends
   - CAC by channel
   - Customer testimonials
   - Competitive threats

7. **Risks & Mitigation** (1 slide)
   - Top 3 risks
   - Mitigation plans
   - Board guidance needed

8. **Deep Dive Topic** (2-3 slides)
   - Varies by quarter (churn analysis, pivot decision, Series A prep)
   - Data-driven analysis
   - Recommendations

9. **Ask from Board** (1 slide)
   - Strategic guidance questions
   - Network requests (intros)
   - Hiring recommendations
   - Decisions needed today

10. **Appendix** (optional)
    - Additional data/charts

## Usage Examples

### Example 1: Generate Quarterly Board Deck

```markdown
**Trigger**: CEO preparing Q1 2026 Board Meeting

**Process**:

1. **Collect data from C-level** (use Read tool):
   ```
   Read: [Startup]/knowledge-base/02_Finance/runway_results.json
   Read: [Startup]/knowledge-base/02_Finance/unit_economics_results.json
   Read: [Startup]/knowledge-base/01_Strategy/okr_q1_2026.md
   Read: [Startup]/knowledge-base/04_Marketing/competitor_list.md
   ```

2. **Generate deck** using template structure:

---

# Q1 2026 Board Update

**TL;DR**:
✅ Achieved 70% of OKRs (3/4 Key Results met)
✅ MRR grew 15% QoQ ($120k → $138k)
⚠️ Churn increased to 6% (target: <5%) — mitigation in progress

**Focus for Q2**: Reduce churn, scale enterprise sales

---

**Slide 2: Key Metrics Dashboard**

| Metric | Q1 2026 | Q4 2025 | Change | Status |
|--------|---------|---------|--------|--------|
| **MRR** | $138k | $120k | +15% | ✅ |
| **ARR** | $1.66M | $1.44M | +15% | ✅ |
| **Churn** | 6.0% | 4.5% | +1.5pp | 🔴 |
| **CAC** | $550 | $600 | -8% | ✅ |
| **LTV** | $2,100 | $2,400 | -12% | 🟡 |
| **LTV/CAC** | 3.8x | 4.0x | -0.2x | ✅ |
| **Runway** | 14mo | 16mo | -2mo | 🟡 |

**Commentary**: Churn spike due to onboarding complexity (addressed in Q2 roadmap)

---

**Slide 6: Deep Dive - Churn Analysis**

### Why Churn Increased (4.5% → 6%)

**Root Cause Analysis** (data from CFO + CTO):

1. **Onboarding Complexity** (40% of churned users)
   - Users couldn't complete setup in <30 min
   - Missing integrations (Slack, Jira)

2. **Performance Issues** (30%)
   - Dashboard load time >5sec for large datasets
   - Mobile app crashes (Android)

3. **Pricing Misalignment** (20%)
   - SMB customers hitting limits on base tier

4. **Competition** (10%)
   - 2 customers switched to Competitor X (cheaper)

**Mitigation Plan (Q2)**:
- [ ] Ship interactive onboarding tutorial (Week 1)
- [ ] Add Slack/Jira integrations (Week 4)
- [ ] Performance optimization sprint (Weeks 2-3)
- [ ] Pricing tier adjustment (add $49/mo mid-tier)

**Expected Impact**: Churn → 4% by end of Q2

---

**Slide 9: Ask from Board**

1. **Strategic Guidance**: Should we prioritize SMB (current) or test Enterprise?
2. **Network Request**: Intro to 2-3 Series A investors for Q3 fundraising
3. **Hiring**: Recommendation for VP Sales (when? now vs Q3?)

**Decision Needed Today**:
- Approve $50k budget for sales hiring agency
```

3. **Send to Board** 1 week before meeting (use Write tool):
   ```
   Write to: [Startup]/knowledge-base/05_Board/board_deck_q1_2026.md
   ```

4. **Email to Board**:
   ```
   Subject: Q1 2026 Board Meeting - Pre-Read Materials

   Hi Board,

   Attached is the Q1 2026 Board Deck for our meeting on April 10th.

   **TL;DR**:
   - ✅ Revenue growth continues (+15% QoQ)
   - 🔴 Churn spiked to 6% (detailed RCA on slide 6)
   - 💡 Requesting guidance on SMB vs Enterprise strategy

   Please review before the meeting. Happy to answer questions async.

   Best,
   [CEO Name]
   ```

### Example 2: Monthly Investor Update

```markdown
**Trigger**: CEO sends monthly email (first week of month)

**Template**:

---

Subject: [Company Name] - February 2026 Update

Hi [Investor Name],

Here's the monthly update for February 2026.

---

**TL;DR**:
✅ MRR crossed $140k (+16% QoQ)
✅ Shipped 2 major features (Slack integration, mobile v2)
⚠️ Churn still elevated at 5.8% (down from 6%, but not at target)

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
   - Most requested feature (40% of users asked)
   - Early adoption: 30% connected within first week

2. **Mobile App V2 Launched** (Feb 20)
   - Fixed crash issues (Android)
   - Performance: load time -40%
   - App Store rating: 3.8 → 4.2 stars

3. **First Enterprise Deal Closed** ($2k MRR)
   - 50-seat contract with [Company X]
   - Validates upmarket potential

---

**🚧 Challenges**:

1. **Churn Still Above Target** (target: <5%)
   - Progress: 6.0% → 5.8%, but slow
   - New tutorial deployed (Feb 28) — too early to see impact

2. **Hiring Delays**
   - VP Sales search ongoing (3 candidates in final round)
   - Decision expected by March 15

---

**🙏 Ask**:

If you know strong VP Sales candidates (B2B SaaS, SMB focus, $1-5M ARR stage), I'd appreciate intros. Job description: [link]

---

**📅 Next Update**: March 5, 2026

Best,
[CEO Name]

---
```

### Example 3: Series A Pitch Deck

```markdown
**Difference from Board Deck**:

| Board Deck | Investor Deck |
|------------|---------------|
| Focus: Operations & risks | Focus: Vision & opportunity |
| Audience knows company | First impression |
| Honest about problems | Highlight strengths |
| 15 slides | 12 slides |

**Series A Deck Structure**:

1. **Problem** - "SMBs waste 10 hours/week on manual reporting"
2. **Solution** - "Automated analytics in 5 minutes"
3. **Market Size** - TAM: $10B, SAM: $2B, SOM: $200M
4. **Product Demo** - Screenshots + key differentiators
5. **Traction** - MRR growth chart, customer logos
6. **Business Model** - Pricing, LTV/CAC = 3.8x
7. **Competition** - Positioning matrix
8. **Go-to-Market** - Channels distribution
9. **Team** - Co-founders + key hires
10. **Financials** - 3-year projection (conservative/base/aggressive)
11. **The Ask** - "Raising $5M Series A at $25M pre-money"
12. **Use of Funds** - 50% Sales, 30% R&D, 20% Ops
```

## Workflow: Preparing Board Meeting

**Timeline**: Start 2 weeks before meeting

### Week -2

1. **Send data requests** to C-level:
   - CFO: Financial metrics, scenario analysis
   - CTO: Product updates, tech debt, security status
   - CMO: CAC by channel, competitive intel

2. **Draft Executive Summary** (TL;DR slide)

### Week -1

3. **Compile deck** using data from all sources
4. **Review with CFO** (validate financial accuracy)
5. **Identify deep dive topic** (most important issue)
6. **Send deck to Board** (1 week before meeting)

### Day of Meeting

7. **Present deck** (60-90 minutes)
8. **Discussion** (30-60 minutes)
9. **Action items** (document decisions, next steps)

### Post-Meeting

10. **Send follow-up** email with:
    - Meeting notes
    - Action items
    - Timeline for next steps

## Metrics Definitions Reference

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
Total S&M Spend / New Customers
```

**LTV (Lifetime Value)**:
```
ARPU × Gross Margin × (1 / Monthly Churn)
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
Benchmark: >40 excellent, 30-40 good, <30 needs work
```

**Churn Rate**:
```
(Customers Lost / Customers at Start) × 100%
Benchmark: SaaS SMB <5%, Enterprise <2%
```

## Best Practices

### 1. Executive Summary is Most Important

**Reality**: Board won't read full deck before meeting.

**TL;DR must contain**:
- Top 3 wins
- Top 2 concerns
- Required decision/ask

If Board reads only 1 slide → they understand everything from Executive Summary.

### 2. Visualization > Tables

**Bad** ❌:
```
MRR Jan: $120k
MRR Feb: $135k
MRR Mar: $142k
```

**Good** ✅:
```
[Graph showing upward MRR trend with event annotations]
"MRR grew 18% in Q1 (Slack integration drove 40% of new signups)"
```

### 3. Honesty About Problems (with Solutions)

**Bad** ❌:
> "Churn немного вырос"

**Good** ✅:
> "Churn grew 4.5% → 6% (+33%). Root cause: onboarding complexity. Mitigation: new tutorial + white-glove onboarding. Expected fix by end Q2."

Board values:
- **Transparency** (honesty)
- **Data-driven analysis** (why?)
- **Action plan** (what are we doing?)

### 4. Asks Must Be Specific

**Bad** ❌:
> "Need help with hiring"

**Good** ✅:
> "Need intros to 3 VP Sales candidates with B2B SaaS experience, $1-5M ARR stage. Hiring timeline: decision by end March."

## Integration with Other Skills

### finance-forecasting
- Runway calculations → Cash Position slide
- Unit economics → Metrics Dashboard
- Scenario analysis → Strategic Options

### tech-audit
- Security audit → Tech slide (security posture)
- Tech debt → Roadmap prioritization context

### market-analysis
- TAM/SAM/SOM → Fundraising decks
- Competitive intel → Threats & Opportunities

## Troubleshooting

### Problem: "Board Deck too long (>20 slides)"

**Solution**:
- Target: 15 slides for 90-min meeting
- Move details to Appendix
- One key point per slide
- Use visual hierarchy (headlines tell the story)

### Problem: "Board doesn't read pre-read materials"

**Solution**:
- Make Executive Summary compelling (1 slide tells whole story)
- Send reminder email 2 days before meeting
- Start meeting with 5-min deck walkthrough

### Problem: "Metrics look bad, don't know how to present"

**Solution**:
- Be honest about problems (Board appreciates transparency)
- Focus on: Root cause analysis + Action plan
- Show: "We understand WHY and HOW to fix"
- Avoid: Hiding bad news (always worse when discovered later)

## Version History

- **2026-02-10**: Adapted for Claude Code CLI from GitHub Copilot skill
  - Added Read/Write/Edit tool usage examples
  - Emphasized data synthesis from multiple skills
  - Added WebSearch integration for benchmarking
- **2026-02-05**: Original GitHub Copilot version
  - Board deck template, investor update template
  - Metrics dashboard definitions

## Related Files

- `.github/skills/board-reporting/SKILL.md` - Original GitHub Copilot version
- `[Startup]/knowledge-base/01_Strategy/` - OKR data source
- `[Startup]/knowledge-base/02_Finance/` - Financial data source
- `[Startup]/knowledge-base/05_Board/` - Board meeting archives
