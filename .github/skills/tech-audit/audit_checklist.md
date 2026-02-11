# Code Review Audit Checklist

Систематический чек-лист для code review и технического аудита.

---

## 1. Architecture & Design

### Architecture Compliance
- [ ] Соответствует ли код установленным архитектурным паттернам?
- [ ] Проверены ли ADR (Architecture Decision Records) для контекста?
- [ ] Нет ли нарушений separation of concerns?
- [ ] Правильный ли layer используется? (Controller → Service → Repository pattern)

### SOLID Principles
- [ ] **Single Responsibility**: Каждый класс/функция делает одно
- [ ] **Open/Closed**: Расширяем через наследование/композицию, а не модификацию
- [ ] **Liskov Substitution**: Подклассы взаимозаменяемы с базовым классом
- [ ] **Interface Segregation**: Интерфейсы маленькие и специфичные
- [ ] **Dependency Inversion**: Зависимость от абстракций, а не конкретных реализаций

### Design Patterns
- [ ] Использованы ли подходящие patterns? (Factory, Strategy, Observer, etc.)
- [ ] Нет ли "изобретения велосипеда"? (есть ли стандартный pattern для этой задачи?)

---

## 2. Code Quality

### Naming Conventions
- [ ] **Variables**: Описательные (`userProfile`, а не `x` или `data`)
- [ ] **Functions**: Глагол + существительное (`calculateTotal`, `fetchUsers`)
- [ ] **Classes**: Существительное (`UserService`, `OrderRepository`)
- [ ] **Constants**: UPPER_SNAKE_CASE (`MAX_RETRIES`, `API_KEY`)
- [ ] **Booleans**: Префикс is/has/should (`isActive`, `hasPermission`)

### Readability
- [ ] Код читается как документация? (self-documenting)
- [ ] Комментарии объясняют "почему", а не "что"?
- [ ] Нет избыточных комментариев obvious вещей?
- [ ] Magic numbers заменены на named constants?

### Function/Method Size
- [ ] Функции < 50 строк (guideline, не строгое правило)
- [ ] Функции делают одну вещь (Single Responsibility)
- [ ] Параметров ≤ 3-4 (если больше → объект/структура)

### Class Size
- [ ] Классы < 300 строк (guideline)
- [ ] Класс не "God Object" (не делает всё)

### DRY (Don't Repeat Yourself)
- [ ] Нет ли дублирования кода? (3+ повторений → extract common logic)
- [ ] Повторяющаяся логика вынесена в utility/helper?

### KISS (Keep It Simple, Stupid)
- [ ] Решение максимально простое?
- [ ] Нет ли over-engineering?
- [ ] Можно ли решить проще?

---

## 3. Security (OWASP Top 10)

### Input Validation
- [ ] Все user input валидируются? (тип, длина, формат)
- [ ] Whitelist validation, а не blacklist?
- [ ] Sanitization для output (HTML escaping)?

### Authentication & Authorization
- [ ] Endpoints защищены auth middleware?
- [ ] Authorization checks на доступ к ресурсам (не могу ли я получить чужие данные)?
- [ ] RBAC (Role-Based Access Control) корректен?

### Injection Prevention
- [ ] **SQL Injection**: Parameterized queries? (НЕ string concatenation)
- [ ] **NoSQL Injection**: Валидация перед MongoDB/etc queries?
- [ ] **Command Injection**: Нет `eval()`, `exec()`, `system()` с user input?

### Secrets Management
- [ ] НЕТ hardcoded API keys, passwords, tokens?
- [ ] Secrets в environment variables or secret manager?
- [ ] `.env` файлы в `.gitignore`?

### Cryptography
- [ ] Используются ли secure algorithms? (bcrypt/argon2 для паролей, НЕ MD5/SHA1)
- [ ] HTTPS enforced? (no mixed content)
- [ ] Sensitive data encrypted at rest?

### Error Handling
- [ ] Errors не раскрывают sensitive info? (stacktraces скрыты от user)
- [ ] Generic error messages для user, detailed logs для devs

---

## 4. Performance

### Database Efficiency
- [ ] Нет N+1 queries? (Eager loading используется where appropriate)
- [ ] Indexes на часто запрашиваемых columns?
- [ ] Pagination для больших datasets?
- [ ] Avoid SELECT * (выбирайте только нужные поля)

### Caching
- [ ] Кешируются ли expensive operations?
- [ ] Правильная cache invalidation strategy?
- [ ] TTL (Time To Live) установлен корректно?

### Algorithmic Complexity
- [ ] Algorithms эффективны? (O(n) лучше O(n²))
- [ ] Нет ли nested loops на больших данных?
- [ ] Используются ли appropriate data structures? (hash map vs array для lookups)

### Memory Management
- [ ] Нет memory leaks? (listeners properly cleaned up)
- [ ] Large objects properly disposed?
- [ ] Streaming для больших файлов? (не загружаем всё в память)

---

## 5. Testing

### Test Coverage
- [ ] Coverage ≥ 70%? (run `pytest --cov` or `npm run test:coverage`)
- [ ] Новый код покрыт тестами?
- [ ] Critical paths (authentication, payment, data mutation) 100% покрыты?

### Test Quality
- [ ] **Unit tests**: Functions/classes изолированно (mocked dependencies)
- [ ] **Integration tests**: Components работают вместе (DB, APIs)
- [ ] **E2E tests**: Критичные user flows (signup, checkout)

### Edge Cases
- [ ] Empty input протестирован?
- [ ] Boundary values (min/max) протестированы?
- [ ] Error scenarios (network failure, DB down) протестированы?

### Test Readability
- [ ] Тесты readable? (AAA pattern: Arrange, Act, Assert)
- [ ] Test names описательные? (`test_user_cannot_delete_other_users_posts`)

---

## 6. Error Handling & Logging

### Error Handling
- [ ] Все exceptions обрабатываются?
- [ ] Graceful degradation (app не падает полностью при ошибке)?
- [ ] Retry logic для transient failures? (network timeouts)

### Logging
- [ ] Важные operations логируются? (authentication, errors, business-critical events)
- [ ] Log levels правильные? (DEBUG/INFO/WARNING/ERROR/CRITICAL)
- [ ] Нет логирования sensitive data? (passwords, credit cards, PII)
- [ ] Logs structured? (JSON format для easy parsing)

---

## 7. Documentation

### Code Comments
- [ ] Сложная логика прокомментирована?
- [ ] Public APIs документированы? (docstrings, JSDoc)
- [ ] TODOs с контекстом и owner? (`TODO(@username): reason`)

### API Documentation
- [ ] Endpoints документированы? (Swagger/OpenAPI for REST, GraphQL schema)
- [ ] Request/Response examples приведены?
- [ ] Error codes документированы?

### Changelog
- [ ] Breaking changes задокументированы?
- [ ] Migration guide для major changes?

---

## 8. Dependencies

### Dependency Management
- [ ] Версии зафиксированы? (package-lock.json, poetry.lock, go.sum)
- [ ] Vulnerabilities проверены? (`npm audit`, `safety check`, Dependabot)
- [ ] Unused dependencies удалены?

### Licenses
- [ ] Лицензии dependencies совместимы с проектом?
- [ ] GPL-licensed libraries (если есть) совместимы с commercial use?

---

## 9. Git & Version Control

### Commit Messages
- [ ] Commits atomic? (one logical change per commit)
- [ ] Commit messages descriptive?
  ```
  feat(auth): add password reset via email
  
  - Implement reset token generation
  - Send email with reset link
  - Expire tokens after 1 hour
  
  Closes #123
  ```

### Branch Strategy
- [ ] Feature branch из `main`/`develop`?
- [ ] Branch name descriptive? (`feature/user-profile-edit`, `bugfix/login-timeout`)

### Pull Request
- [ ] PR description объясняет "зчем" и "что"?
- [ ] Связанные issues referenced? (`Closes #42`)
- [ ] Screenshots для UI changes?

---

## 10. CI/CD & DevOps

### CI Pipeline
- [ ] Tests run automatically?
- [ ] Linting checks passing?
- [ ] Build успешен?

### Deployment
- [ ] Zero-downtime deployment strategy? (blue-green, rolling)
- [ ] Rollback plan есть?
- [ ] Database migrations включены?

---

## Review Decision Taxonomy

After completing checklist, categorize issues:

### **Nit** 🟢 (не блокирует merge)
- Мелкие стилистические замечания
- Naming improvements
- Minor refactors

### **Suggestion** 🟡 (рекомендация, не обязательно)
- Возможные улучшения
- Alternative approaches
- Future optimizations

### **Blocking** 🔴 (требует исправления)
- Security vulnerabilities
- Bugs
- Missing tests для критичного кода
- Architecture violations

---

## Final Decision

- [ ] ✅ **Approved** — можно мержить
- [ ] 🔄 **Approved with changes** — мержить можно, но исправить nits после
- [ ] ⛔ **Changes requested** — blocking issues должны быть исправлены

**Timeline for Re-Review**: [укажите срок, например "24 hours"]
