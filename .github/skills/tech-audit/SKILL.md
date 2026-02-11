# Tech Audit Skill

## Overview

**Purpose**: Обеспечить CTO систематическим подходом к code review, архитектурным решениям и проверке безопасности. Этот навык предоставляет чек-листы и best practices для поддержания высокого качества кодовой базы.

**Target Users**: @CTO (primary), @CEO (для понимания технического состояния)

**Dependencies**: VS Code extensions (ESLint, Pylint, etc.), Git, codebase access

---

## Components

### 1. `audit_checklist.md`

Мастер-чеклист для code review и технического аудита.

**Sections**:
- Code Review Standards (Nit/Suggestion/Blocking taxonomy)
- Security Audit (OWASP Top 10 checklist)
- Architecture Patterns (SOLID, DRY, KISS validation)
- Performance Audit (N+1 queries, caching, optimization)
- Test Coverage Audit (unit/integration/e2e requirements)

### 2. `code_review_template.md`

Стандартизированный шаблон для PR review.

**Structure**:
```markdown
## Code Review: [PR Title]

**PR**: #[number]  
**Author**: @[developer]  
**Reviewer**: @CTO  
**Date**: YYYY-MM-DD

### Summary
[One-line описание изменений]

### Architecture Impact
- [ ] Изменения архитектуры документированы в ADR?
- [ ] Соблюдены архитектурные принципы (.github/knowledge-base/03_Tech/)?
- [ ] Нет нарушений separation of concerns?

### Security  
- [ ] Нет hardcoded credentials/secrets?
- [ ] Input validation присутствует?
- [ ] SQL injection защита (parameterized queries)?
- [ ] XSS защита (output escaping)?

### Code Quality
- [ ] Код соответствует naming conventions?
- [ ] Нет дублирования (DRY)?
- [ ] Функции < 50 строк, классы < 300 строк?
- [ ] Комментарии объясняют "почему", а не "что"?

### Testing
- [ ] Тесты покрывают новый код? (target ≥70%)
- [ ] Edge cases протестированы?
- [ ] Tests проходят в CI?

### Performance
- [ ] Нет N+1 queries?
- [ ] Database indexes на новых queries?
- [ ] Caching уместен и реализован?

### Comments

**Nit** (не блокирует мерж):
- [filename:line] - [комментарий]

**Suggestion** (рекомендация):
- [filename:line] - [комментарий]

**Blocking** (требует исправления):
- [filename:line] - [комментарий]

### Decision
- [ ] ✅ Approved
- [ ] 🔄 Approved with changes (minor nits)
- [ ] ⛔ Changes requested (blocking issues)
```

### 3. `owasp_checklist.md`

OWASP Top 10 security checklist для аудита.

**Covers**:
1. Broken Access Control
2. Cryptographic Failures
3. Injection (SQL, NoSQL, Command)
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)

### 4. `naming_conventions.md`

Стандарты именования для различных языков.

**Patterns**:
- **Functions/Methods**: `camelCase` (JS/TS), `snake_case` (Python)
- **Classes**: `PascalCase` (all languages)
- **Constants**: `UPPER_SNAKE_CASE` (all languages)
- **Private members**: `_leadingUnderscore` (Python), `#private` (JS)
- **Booleans**: Префиксы `is`, `has`, `should` (e.g., `isActive`, `hasPermission`)

---

## Use Cases

### Use Case 1: Code Review для Feature PR

**Scenario**: Developer submits PR #42 с новой фичей "User Profile Editing".

**CTO Process**:

1. **Используйте шаблон code_review_template.md**

2. **Architecture Impact Audit**:
   - Проверьте, не нарушает ли PR существующую архитектуру
   - Если добавлен новый паттерн, должен ли быть создан ADR?
   - Пример проблемы: Бизнес-логика в Controller (должна быть в Service)

3. **Security Audit** (используйте owasp_checklist.md):
   ```markdown
   ### Security Issues Found:
   
   **🔴 BLOCKING**:
   - `user_controller.py:45` - SQL injection риск:
     ```python
     # BAD ❌
     query = f"SELECT * FROM users WHERE id = {user_id}"
     
     # GOOD ✅
     query = "SELECT * FROM users WHERE id = ?"
     cursor.execute(query, (user_id,))
     ```
   
   **🟡 SUGGESTION**:
   - `auth.js:23` - Password не хешируется с солью (используйте bcrypt, не MD5)
   ```

4. **Code Quality Audit** (используйте naming_conventions.md):
   ```markdown
   ### Code Quality Issues:
   
   **Nit**:
   - `profile.py:12` - Переменная `d` → переименуйте в `profile_data` (clarity)
   - `utils.js:78` - Функция 120 строк → разбейте на меньшие (target <50)
   
   **Suggestion**:
   - `user_service.py:34-56` - Дублирование логики с `admin_service.py:78-98`
     → Выделите в shared utility `validate_user_input()`
   ```

5. **Testing Audit**:
   - Запустите coverage report:
   ```bash
   pytest --cov=app --cov-report=term
   # OR
   npm run test:coverage
   ```
   - Check: Coverage ≥ 70%?
   - Отсутствующие тесты:
   ```markdown
   **🔴 BLOCKING**:
   - Нет тестов для `ProfileController.update_email()` (critical path)
   - Edge case не протестирован: "Что если email уже занят другим пользователем?"
   ```

6. **Performance Audit**:
   - Проверьте database queries (N+1 problem):
   ```python
   # BAD ❌ (N+1 query)
   users = User.query.all()
   for user in users:
       profile = user.profile  # Отдельный query на каждого user!
   
   # GOOD ✅ (eager loading)
   users = User.query.options(joinedload(User.profile)).all()
   ```

7. **Final Decision**:
   ```markdown
   ## Decision: ⛔ Changes Requested
   
   **Blocking Issues** (must fix before merge):
   1. SQL injection vulnerability (user_controller.py:45)
   2. Missing tests for update_email() critical path
   
   **Timeline**: Fix within 24 hours, re-request review
   
   **Suggestions for Future** (не блокирует текущий PR):
   - Рефактор дублирования между user/admin services
   - Split long functions (>50 lines)
   ```

---

### Use Case 2: Security Audit (Quarterly)

**Scenario**: @CEO запрашивает у @CTO: "Готовы ли мы к penetration test? Нет ли критичных уязвимостей?"

**CTO Process**:

1. **Используйте owasp_checklist.md** для систематического аудита

2. **OWASP Top 10 Walk-Through**:

   **Шаг 1: Broken Access Control**
   ```markdown
   ### 1. Broken Access Control Audit
   
   Check:
   - [ ] Все API endpoints имеют authorization middleware?
   - [ ] IDOR защита (не могу ли я получить данные другого user через `/api/users/123`)?
   - [ ] Horizontal privilege escalation prevention
   
   **Findings**:
   ✅ All endpoints protected
   🔴 CRITICAL: `/api/admin/users/:id/delete` не проверяет роль (любой user может удалить!)
   
   **Fix Required**:
   ```javascript
   // Add role check
   router.delete('/admin/users/:id', requireRole('admin'), deleteUser);
   ```
   ```

   **Шаг 2: Cryptographic Failures**
   ```markdown
   ### 2. Cryptographic Failures Audit
   
   Check:
   - [ ] HTTPS везде (no mixed content)?
   - [ ] Sensitive data encrypted at rest (database)?
   - [ ] Password hashing с современным алгоритмом (bcrypt/argon2)?
   
   **Findings**:
   ✅ HTTPS enforced (HSTS config correct)
   🟡 WARNING: Пароли хешируются bcrypt (OK), но work factor = 10 (низковато, recommend 12)
   ⚠️  User PII (email, phone) в plain text в БД → recommend encryption
   ```

   **...продолжить для всех 10 категорий OWASP**

3. **Generate Security Report для @CEO**:
   ```markdown
   ## Security Audit Report (Q1 2026)
   
   **Date**: 2026-02-05  
   **Auditor**: @CTO
   
   ### Executive Summary
   
   **Overall Status**: 🟡 MODERATE RISK
   
   **Critical Issues**: 1  
   **High Priority**: 2  
   **Medium Priority**: 5  
   **Low Priority (Improvements)**: 8
   
   ---
   
   ### Critical Issues (Fix IMMEDIATELY)
   
   **C1: Broken Access Control - Admin Deletion Endpoint**
   - **Risk**: Any authenticated user can delete admin accounts
   - **Impact**: Complete system compromise
   - **Fix**: Add role-based authorization middleware
   - **ETA**: 24 hours
   
   ---
   
   ### High Priority (Fix within 1 week)
   
   **H1: Insufficient Password Hashing Strength**
   - **Risk**: Weak bcrypt work factor (10 → should be 12+)
   - **Impact**: Faster brute-force attacks if DB leaked
   - **Fix**: Increase work factor, migrate existing hashes
   
   **H2: PII in Plain Text**
   - **Risk**: GDPR/CCPA non-compliance if DB breached
   - **Impact**: Legal liability, customer trust loss
   - **Fix**: Implement column-level encryption for email/phone
   
   ---
   
   ### Recommendation
   
   **Before Penetration Test**:
   - Must fix: C1 (critical)
   - Should fix: H1, H2
   
   **Timeline**: 1 week to remediate critical + high, then ready for pentest
   ```

---

### Use Case 3: Architecture Decision Review

**Scenario**: Developer предлагает добавить GraphQL вместо REST API. @CTO должен оценить.

**CTO Process**:

1. **Создайте Architecture Decision Record (ADR)** в `.github/knowledge-base/03_Tech/architecture_decisions/`

2. **Используйте ADR template**:
   ```markdown
   # ADR-005: GraphQL vs REST API
   
   **Date**: 2026-02-05  
   **Status**: Under Review  
   **Deciders**: @CTO, @CEO, Backend Team Lead
   
   ---
   
   ## Context
   
   Current REST API has become complex with:
   - Over-fetching (mobile clients get too much data → slow)
   - Under-fetching (multiple API calls needed → N+1 HTTP requests)
   - Versioning challenges (breaking changes → /api/v2/, /api/v3/)
   
   **Proposal**: Introduce GraphQL alongside REST (gradual migration)
   
   ---
   
   ## Decision Drivers
   
   - Frontend team requests flexible data fetching
   - Mobile performance concerns (cellular networks)
   - Developer experience (easier to iterate on UI)
   - Existing codebase (REST already implemented)
   
   ---
   
   ## Options Considered
   
   ### Option 1: Status Quo (Keep REST Only)
   **Pros**:
   - No migration cost
   - Team already familiar
   - Simple architecture
   
   **Cons**:
   - Performance issues persist
   - Mobile app suffers
   - Complex versioning
   
   **Cost**: $0  
   **Risk**: Low (but doesn't solve problem)
   
   ---
   
   ### Option 2: Full GraphQL Migration
   **Pros**:
   - Solves over/under-fetching
   - Better DX for frontend
   - Single endpoint (/graphql)
   
   **Cons**:
   - High migration cost (rewrite all endpoints)
   - Learning curve
   - Complex caching
   - Harder to secure (vs REST resource-based permissions)
   
   **Cost**: $50k (3 months dev time)  
   **Risk**: High (big-bang migration)
   
   ---
   
   ### Option 3: Hybrid (GraphQL + REST Coexist)
   **Pros**:
   - Gradual migration (low risk)
   - Use GraphQL for new features, keep REST for legacy
   - Flexibility
   
   **Cons**:
   - Complexity (2 API paradigms)
   - Maintenance burden
   
   **Cost**: $15k (1 month setup)  
   **Risk**: Medium
   
   ---
   
   ## Decision
   
   **Chosen Option**: Option 3 (Hybrid)
   
   **Rationale**:
   - Balances benefits vs risk
   - Mobile app can adopt GraphQL immediately (highest ROI)
   - Web app can migrate incrementally
   - Existing integrations (third-party) stay on REST
   
   ---
   
   ## Implementation Plan
   
   **Phase 1** (Month 1):
   - Setup GraphQL server (Apollo Server)
   - Implement 3 core queries (User, Posts, Comments)
   - Mobile app migrates to GraphQL
   
   **Phase 2** (Months 2-3):
   - Migrate remaining mobile endpoints
   - Web app pilot (1-2 pages use GraphQL)
   
   **Phase 3** (Ongoing):
   - New features: GraphQL-first
   - Legacy: Keep REST, deprecate eventually (12-18 months)
   
   ---
   
   ## Consequences
   
   **Positive**:
   - Improved mobile performance
   - Better DX for frontend team
   - Competitive advantage (modern API)
   
   **Negative**:
   - Increased complexity short-term
   - Need to train team on GraphQL
   - Monitoring/security need updates (GraphQL-specific tools)
   
   ---
   
   ## Follow-Up
   
   - **Review Date**: 2026-08-05 (6 months post-launch)
   - **Success Metrics**:
     - Mobile app load time -30%
     - API requests/screen -50%
     - Developer satisfaction survey >4/5
   ```

3. **Escalate to @CEO** для alignment:
   - Требуется $15k budget → @CEO + @CFO approval
   - Стратегический вопрос (API = core product) → @CEO input

4. **После одобрения**:
   - Фиксируйте ADR со статусом "Approved"
   - Делегируйте implementation команде
   - Track metrics (follow-up через 6 месяцев)

---

## Files Structure

```
.github/skills/tech-audit/
├── SKILL.md                     # This file
├── audit_checklist.md           # Master checklist для аудита
├── code_review_template.md      # PR review шаблон
├── owasp_checklist.md           # OWASP Top 10 security checklist
├── naming_conventions.md        # Стандарты именования
└── adr_template.md              # Architecture Decision Record template
```

---

## Best Practices

### 1. Code Review: Конструктивность > Критика

**Bad** ❌:
> "Этот код ужасен, переписывайте полностью."

**Good** ✅:
> "Эта функция делает слишком много (SRP violation). Предлагаю разбить на:  
> 1. `validateInput(data)` — валидация  
> 2. `saveToDatabase(valid_data)` — персистентность  
> 3. `sendNotification(user)` — side effects"

### 2. Используйте данные для приоритизации

**При множественных проблемах** → сортировка по impact:
1. **Security** (critical) → fix immediately
2. **Bugs** (high) → fix within 24-48 hours
3. **Performance** (medium) → fix in next sprint
4. **Code quality/style** (low) → technical debt backlog

### 3. Автоматизируйте что можно

**Linters** (автоматическая проверка):
- ESLint (JavaScript/TypeScript)
- Pylint/Flake8/Black (Python)
- Prettier (formatting)

**Security scanners**:
- Dependabot (dependency vulnerabilities)
- Snyk / OWASP Dependency-Check
- SonarQube (code smells + security)

**CI/CD checks**:
- Automated tests must pass
- Coverage ≥ 70%
- Lint errors = 0

**CTO фокусируется на том, что машина НЕ может** → architecture, design patterns, business logic correctness.

---

## Integration with Agents

### @CTO
- **Primary user** — использует все компоненты навыка
- **Frequency**: Code review (daily), Security audit (quarterly), ADR creation (as needed)

### @CEO
- Получает security audit reports от @CTO
- Принимает участие в ADR для стратегически важных решений (API changes, tech stack pivot)

### @Board
- Получает high-level summary (security posture, tech debt status) на Board Meetings

---

## Troubleshooting

**Problem**: "Code review занимает слишком много времени"

**Solution**:
- Используйте шаблон code_review_template.md (структура ускоряет процесс)
- Делегируйте non-critical reviews Senior Developers
- @CTO focuses на: Security, Architecture, Critical bugs

**Problem**: "Слишком много security issues, не знаем с чего начать"

**Solution**:
- Приоритизируйте по OWASP Risk Rating (High→Medium→Low)
- Fix критичные (OWASP 1-3) в первую очередь
- Track progress в backlog (e.g., "Security Debt" label в GitHub Issues)

---

## Changelog

- **2026-02-05**: Initial version (audit_checklist, code_review_template, OWASP checklist)
- **TBD**: Add automated security scanning integration
- **TBD**: Performance profiling guidelines
