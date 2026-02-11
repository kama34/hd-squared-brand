# Claude Code Skills

Адаптированные скиллы для работы с Claude Code CLI из оригинальных GitHub Copilot агентов.

## Статус адаптации

**Total**: 30 skills | **Adapted**: 16 (53%) | **Pending**: 14 (47%)

### ✅ Полностью адаптированные (16 скиллов)

#### Finance & Modeling (4)
1. **finance-forecasting** - Финансовое прогнозирование с Python
2. **finance-modeler** - Scenario analysis и projections
3. **finance-unit-economics** - LTV/CAC/churn расчеты
4. **investor-qa-generator** - Investor Q&A preparation

#### Web Development (2)
5. **frontend-development** - HTML5, CSS3, JS ES6+, React, accessibility
6. **backend-development** - Node.js, Python, REST APIs, databases, auth

#### DevOps (1)
7. **devops-cicd** - Docker, CI/CD, automated deployment

#### Technical & Security (1)
8. **tech-audit** - Технический аудит, OWASP, code review

#### CTO Automation (2) 🆕
9. **error-learning** - Автоматическое документирование ошибок
10. **repo-cleanup** - Автоматическая организация файлов

#### Configuration Management (3)
11. **config-validation** - Validate sales funnel configs
12. **config-parser-rules** - Parser rules reference
13. **config-templates** - Config templates

#### Business & Strategy (3)
14. **board-reporting** - Board Decks и investor updates
15. **market-analysis** - Конкурентный анализ и market sizing
16. **mcp-advisor** - Советы по MCP серверам

### 🔄 Требуют адаптации (14 скиллов)

- pitch-questions, pitch-audit
- landing-structure, site-audit, html-fixes, design-language
- marketing-alignment, brand-analysis
- repo-analyzer, repo-agent-suggester, stitch-integration
- experiment-management, prompt-generator-skill, skill-creator

## Структура скилла

Каждый адаптированный скилл содержит:

```
.claude/skills/[skill-name]/
├── skill.md                    # Основная документация
├── [supporting files]          # Python модули, чеклисты, шаблоны
└── README.md (optional)        # Дополнительная документация
```

## Как использовать скиллы

### Метод 1: Прямая ссылка

```
Используя skill finance-forecasting, посчитай runway для Sales AI
```

Claude Code прочитает `D:\Drive\Wiki\.claude\skills\finance-forecasting\skill.md` и выполнит задачу.

### Метод 2: Импорт Python модулей (для finance-forecasting)

```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-forecasting')
from forecast_model import calculate_runway, get_runway_status

runway = calculate_runway(cash_balance=750_000, monthly_burn=50_000)
status = get_runway_status(runway)
print(f"Runway: {runway} months - {status['message']}")
```

### Метод 3: Использование чеклистов (для tech-audit)

```
Используя tech-audit skill, проведи security audit файла Sales AI/site/code4.html
```

Claude Code прочитает `owasp_checklist.md` и выполнит аудит.

### Метод 4: WebSearch интеграция (для market-analysis)

```
Используя market-analysis skill, найди информацию о конкурентах Sales AI
```

Claude Code использует WebSearch для поиска и применит фреймворк из skill.md.

## Детальное описание скиллов

### 1. finance-forecasting

**Назначение**: Финансовое моделирование и расчет метрик для стартапов.

**Возможности**:
- Runway calculation (месяцы до исчерпания cash)
- Cash flow projections
- Scenario analysis (консервативный/базовый/агрессивный)
- SaaS metrics (LTV, CAC, Churn, Magic Number)
- Unit economics health check

**Python модули**:
- `forecast_model.py` - Runway, cash flow, сценарии
- `saas_metrics.py` - LTV, CAC, churn, payback

**Требует**: Python 3.8+, pandas, numpy

**Пример использования**:
```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-forecasting')
from saas_metrics import unit_economics_health_check

health = unit_economics_health_check(
    arpu=120,
    gross_margin=0.75,
    monthly_churn=0.04,
    sales_marketing_spend=120_000,
    new_customers=200
)

print(f"LTV/CAC: {health['metrics']['ltv_cac_ratio']:.1f}x")
print(f"Status: {health['status']['overall']['emoji']} {health['status']['overall']['status']}")
```

**Интеграция с агентами**:
- **@CFO** - primary user, ОБЯЗАН использовать для всех расчетов (Code-First Rule)
- **@CEO** - запрашивает отчеты от CFO
- **@Board** - получает результаты через CFO

---

### 2. tech-audit

**Назначение**: Систематический подход к code review и security audits.

**Возможности**:
- Code review с таксономией (Nit/Suggestion/Blocking)
- Security audit (OWASP Top 10)
- Architecture review (SOLID, design patterns)
- Performance audit (N+1 queries, caching)
- Test coverage analysis

**Чеклисты**:
- `audit_checklist.md` - Master checklist (Architecture, Security, Performance)
- `owasp_checklist.md` - OWASP Top 10 детальный аудит

**Инструменты Claude Code**:
- `Read` - чтение кода
- `Grep` - поиск паттернов (hardcoded secrets, SQL injection)
- `mcp__ide__getDiagnostics` - linter diagnostics
- `Bash` - запуск security scanners (bandit, npm audit)

**Пример использования**:
```
Используя tech-audit skill, проведи code review PR #42.

Выполни:
1. Read измененных файлов
2. Grep для поиска security patterns (SQL injection, hardcoded keys)
3. Проверь по audit_checklist.md
4. Сгенерируй review report с категориями (Nit/Suggestion/Blocking)
```

**Интеграция с агентами**:
- **@CTO** - primary user, code review, security audits
- **@CEO** - получает security reports для Board
- **@Board** - high-level security posture

---

### 3. board-reporting

**Назначение**: Шаблоны для Board Meetings, investor updates, fundraising.

**Возможности**:
- Quarterly Board Deck (15-slide structure)
- Monthly investor email updates
- Metrics dashboard (KPI definitions)
- Fundraising pitch deck structure
- Series A preparation

**Структура Board Deck**:
1. Executive Summary (TL;DR)
2. Key Metrics Dashboard
3. Progress vs OKRs
4. Financial Update (от @CFO)
5. Product/Tech Update (от @CTO)
6. GTM & Growth (от @CMO)
7. Risks & Mitigation
8. Deep Dive Topic (varies by quarter)
9. Ask from Board

**Интеграция данных**:
- **finance-forecasting** → Runway, unit economics
- **tech-audit** → Security posture, tech debt
- **market-analysis** → Competitive landscape

**Пример использования**:
```
Используя board-reporting skill, создай Q1 2026 Board Deck для Sales AI.

Собери данные:
- Read: Sales AI/knowledge-base/02_Finance/runway_results.json
- Read: Sales AI/knowledge-base/01_Strategy/okr_q1_2026.md
- Read: Sales AI/knowledge-base/04_Marketing/competitor_list.md

Сгенерируй deck по структуре из skill.md
```

**Интеграция с агентами**:
- **@CEO** - primary user, создает все Board materials
- **@CFO** - предоставляет financial slides
- **@CTO** - предоставляет product/tech slides
- **@CMO** - предоставляет GTM slides
- **@Board** - primary audience

---

### 4. market-analysis

**Назначение**: Конкурентная разведка, market sizing, positioning.

**Возможности**:
- Competitive intelligence (SWOT, feature matrix, pricing)
- Market sizing (TAM/SAM/SOM)
- Positioning strategy
- GTM channel analysis
- Real-time competitor monitoring

**Фреймворки**:
- Competitor Analysis Framework (SWOT + feature matrix)
- Market Sizing Methodology (TAM/SAM/SOM)
- Positioning Template

**Инструменты Claude Code**:
- `WebSearch` - поиск конкурентов, market reports
- `WebFetch` - парсинг competitor websites
- `Write` - сохранение research findings

**Пример использования**:
```
Используя market-analysis skill, проведи monthly competitive analysis для Sales AI.

WebSearch queries:
- "Competitor A new features 2026"
- "Competitor B funding announcement"
- "SaaS analytics market size Gartner 2026"

Сгенерируй отчет по структуре из skill.md:
- Executive Summary (Top threats/opportunities)
- Competitor updates (A, B, C)
- Positioning matrix
- Recommendations for CEO
```

**Интеграция с агентами**:
- **@CMO** - primary user, competitive intelligence
- **@CEO** - получает insights для стратегических решений
- **@Board** - competitive updates на Board Meetings
- **@CTO** - feature gap analysis для roadmap

---

### 5. mcp-advisor

**Назначение**: Рекомендации по MCP (Model Context Protocol) серверам.

**Возможности**:
- Analyze repository для выявления automation opportunities
- Recommend MCP servers по tech stack
- Setup instructions для MCP integration
- Troubleshoot MCP connection issues

**Распространенные MCP серверы**:
- **brave-search** - Web search (для CMO)
- **playwright** - Browser automation (для CTO)
- **github** - GitHub API access
- **postgres** - Database queries
- **slack** - Team communication

**Пример использования**:
```
Используя mcp-advisor skill, проанализируй Sales AI и порекомендуй MCP серверы.

Процесс:
1. Glob: Найди package.json, requirements.txt
2. Grep: Поиск API usage patterns
3. Сгенерируй recommendations с приоритетами (HIGH/MEDIUM/LOW)
4. Предоставь setup instructions
```

**Интеграция с агентами**:
- **@CTO** - primary user, MCP setup и troubleshooting
- **@CEO** - понимание automation possibilities
- **@CMO** - использует brave-search MCP

---

## Workflows: Использование скиллов в реальных сценариях

### Сценарий 1: CFO готовит weekly financial report

```
1. Trigger: @CEO запрашивает финансовый update

2. Команда для Claude Code:
   "Используя finance-forecasting skill, создай weekly report для Sales AI"

3. Claude Code выполняет:
   - Read: Sales AI/knowledge-base/02_Finance/runway_results.json
   - Import: forecast_model.py, saas_metrics.py
   - Execute Python: calculate_runway, unit_economics_health_check
   - Generate Markdown report
   - Write: Sales AI/knowledge-base/02_Finance/reports/weekly_2026_02_10.md

4. Результат: Formatted financial report с runway, LTV/CAC, recommendations
```

### Сценарий 2: CTO проводит security audit

```
1. Trigger: @CEO запрашивает security audit перед penetration test

2. Команда для Claude Code:
   "Используя tech-audit skill, проведи OWASP Top 10 audit для Sales AI"

3. Claude Code выполняет:
   - Read: owasp_checklist.md
   - Glob: "Sales AI/site/**/*.html"
   - Grep: Поиск hardcoded secrets, SQL injection patterns
   - Bash: npm audit (если есть package.json)
   - Generate security report с приоритетами (Critical/High/Medium/Low)

4. Результат: Security audit report для CEO/Board
```

### Сценарий 3: CEO готовит Board Meeting

```
1. Trigger: Quarterly Board Meeting через неделю

2. Команда для Claude Code:
   "Используя board-reporting skill, создай Q1 2026 Board Deck для Sales AI"

3. Claude Code выполняет:
   - Collect data from multiple sources:
     - finance-forecasting skill → Runway, unit economics
     - market-analysis skill → Competitive intel
   - Generate 15-slide deck по структуре из skill.md
   - Write: Sales AI/knowledge-base/05_Board/board_deck_q1_2026.md

4. Результат: Complete Board Deck ready for presentation
```

### Сценарий 4: CMO анализирует конкурентов

```
1. Trigger: Monthly competitive intelligence update

2. Команда для Claude Code:
   "Используя market-analysis skill, проведи competitive analysis для Sales AI"

3. Claude Code выполняет:
   - WebSearch:
     - "Competitor A new features 2026"
     - "Competitor B funding announcement"
   - WebFetch: Competitor pricing pages
   - Generate report по competitor_analysis_framework
   - Write: Sales AI/knowledge-base/04_Marketing/competitive_intel_2026_02.md

4. Результат: Competitive intelligence report с threats/opportunities
```

## Интеграция скиллов между собой

### finance-forecasting → board-reporting
Финансовые метрики из finance-forecasting автоматически включаются в Board Deck.

### tech-audit → board-reporting
Security audit results → Tech slide в Board Deck.

### market-analysis → board-reporting
TAM/SAM/SOM calculations → Fundraising pitch decks.

### mcp-advisor → market-analysis
brave-search MCP → continuous competitive monitoring.

### finance-forecasting → market-analysis
CAC by channel → GTM budget allocation.

## Best Practices

### 1. Всегда указывайте startup name

```
❌ BAD: "Посчитай runway"
✅ GOOD: "Используя finance-forecasting skill, посчитай runway для Sales AI"
```

### 2. CFO Code-First Rule

```
❌ BAD: @CFO считает "в уме"
✅ GOOD: @CFO использует finance-forecasting skill с Python code
```

### 3. Специфичные запросы

```
❌ BAD: "Проверь безопасность"
✅ GOOD: "Используя tech-audit skill + owasp_checklist.md, проверь Sales AI/site/code4.html на SQL injection и XSS"
```

### 4. Сохраняйте результаты

```
После выполнения расчетов/анализа:
Write: [Startup]/knowledge-base/[category]/[report_name].md

Пример:
Write: Sales AI/knowledge-base/02_Finance/reports/runway_2026_02_10.md
```

## Дальнейшая адаптация

### Оставшиеся 17 скиллов для адаптации

**Finance** (3):
- finance-modeler
- finance-unit-economics
- investor-qa-generator

**Marketing** (2):
- brand-analysis
- marketing-alignment

**Product/Design** (4):
- design-language
- html-fixes
- landing-structure
- site-audit

**Pitch/Strategy** (3):
- pitch-audit
- pitch-questions
- experiment-management

**Development** (3):
- repo-analyzer
- repo-agent-suggester
- prompt-generator-skill

**Integration** (2):
- stitch-integration
- skill-creator

### Процесс адаптации нового скилла

1. **Read оригинальный SKILL.md** из `.github/skills/[name]/`
2. **Определить Claude Code tools**:
   - Python execution → mcp__ide__executeCode
   - File operations → Read/Write/Edit
   - Search → Grep/Glob
   - Web research → WebSearch/WebFetch
   - Diagnostics → mcp__ide__getDiagnostics
3. **Создать skill.md** с разделами:
   - Overview
   - Required Tools
   - Usage Examples
   - Workflows
   - Integration with Other Skills
   - Best Practices
   - Troubleshooting
4. **Скопировать supporting files** (Python, checklists, templates)
5. **Тестировать** на реальных примерах

## Troubleshooting

### Problem: "Skill не найден"

**Проверьте**:
```bash
ls "D:\Drive\Wiki\.claude\skills\[skill-name]\skill.md"
```

**Если отсутствует**: Скопируйте из `.github/skills/` и адаптируйте.

### Problem: "Python модуль не импортируется"

**Решение**:
```python
import sys
sys.path.append('D:/Drive/Wiki/.claude/skills/finance-forecasting')
# Используйте forward slashes, даже на Windows
```

### Problem: "MCP не работает с skill"

**Проверьте**:
1. MCP configured в `~/.claude/mcp.json`
2. Environment variables set (BRAVE_API_KEY, etc.)
3. Restart Claude Code после изменений

### Problem: "Skill работает для одного стартапа, но не для другого"

**Причина**: Hardcoded paths или startup name

**Решение**: Всегда указывайте startup name в запросе:
```
"Для [Startup Name], используя finance-forecasting skill, посчитай runway"
```

## Version History

- **2026-02-10**: Initial adaptation of 5 priority skills
  - finance-forecasting
  - tech-audit
  - board-reporting
  - market-analysis
  - mcp-advisor

## Next Steps

1. **Test adapted skills** на реальных примерах Sales AI
2. **Adapt remaining 17 skills** по мере необходимости
3. **Update agent memories** с инструкциями по использованию skills
4. **Create skill templates** для быстрой адаптации новых skills

## Related Documentation

- `.github/skills/` - Original GitHub Copilot skills
- `.github/agents/` - AI agent definitions (CEO, CFO, CTO, CMO, Board)
- `CLAUDE.md` - Project instructions for Claude Code
- `.claude-helpers/` - Helper documentation (agent-prompts, mcp-guide)
