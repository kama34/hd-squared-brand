# Политики безопасности

## Принципы

1. **Security by Design**: Безопасность — не дополнительная фича, а core requirement.
2. **Defense in Depth**: Множественные слои защиты.
3. **Least Privilege**: Минимальные права доступа по умолчанию.
4. **Assume Breach**: Проектируйте систему так, будто злоумышленник уже внутри.

---

## OWASP Top 10 (2021) — Обязательные проверки

### 1. Broken Access Control
**Риск**: Пользователь получает доступ к чужим данным.

**Обязательные проверки**:
- ✅ Каждый API endpoint проверяет, что `userId` в токене == `userId` запрашиваемых данных
- ✅ RBAC (Role-Based Access Control) для админ-панелей
- ✅ Нет прямых ссылок на ID (используйте UUID или IDOR protection)

**Пример уязвимости**:
```javascript
// ❌ ПЛОХО
app.get('/api/orders/:orderId', (req, res) => {
  const order = db.getOrder(req.params.orderId);
  res.json(order); // Не проверили, что order.userId == req.user.id!
});

// ✅ ХОРОШО
app.get('/api/orders/:orderId', (req, res) => {
  const order = db.getOrder(req.params.orderId);
  if (order.userId !== req.user.id) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  res.json(order);
});
```

---

### 2. Cryptographic Failures
**Риск**: Утечка чувствительных данных (пароли, кредитные карты, PII).

**Обязательные требования**:
- ✅ **HTTPS везде** — никакого HTTP в проде (проверяем через Strict-Transport-Security header)
- ✅ Пароли хешируются через bcrypt/argon2 (НЕ MD5, НЕ SHA1)
- ✅ Секреты (API keys, DB credentials) в переменных окружения, НЕ в коде
- ✅ PII (Personally Identifiable Information) шифруется в БД (если требуется compliance)

**Проверка секретов**:
```bash
# Используйте git-secrets или TruffleHog для сканирования коммитов
npm install -g trufflehog
trufflehog filesystem . --json
```

---

### 3. Injection (SQL, NoSQL, Command)
**Риск**: Злоумышленник выполняет произвольные команды.

**Защита**:
- ✅ **Всегда используйте параметризованные запросы** (Prepared Statements)
- ✅ ORM (Prisma, TypeORM) вместо raw SQL, где возможно
- ✅ Валидация и санитизация всех пользовательских данных

**Пример**:
```javascript
// ❌ SQL Injection уязвимость
const query = `SELECT * FROM users WHERE email = '${req.body.email}'`;
db.query(query);

// ✅ Безопасно
const query = 'SELECT * FROM users WHERE email = ?';
db.query(query, [req.body.email]);
```

---

### 4. Insecure Design
**Риск**: Фундаментальные архitecturные слабости.

**Требования**:
- ✅ Threat modeling для критичных фич (оплата, аутентификация)
- ✅ Rate limiting на API (защита от brute-force)
- ✅ Input validation на фронтенде **И** бекенде (никогда не доверяйте клиенту)

**Rate Limiting пример** (Node.js):
```javascript
const rateLimit = require('express-rate-limit');

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 минут
  max: 5, // Макс 5 попыток
  message: 'Too many login attempts, please try again later.'
});

app.post('/api/login', loginLimiter, authController.login);
```

---

### 5. Security Misconfiguration
**Риск**: Дефолтные пароли, открытые порты, verbose ошибки на проде.

**Чек-лист**:
- ✅ Отключить debug режим в продакшне
- ✅ Удалить дефолтные аккаунты (admin/admin)
- ✅ Минимизировать поверхность атаки (закрыть неиспользуемые порты)
- ✅ Security headers:
  ```
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Content-Security-Policy: default-src 'self'
  ```

**Автоматическая проверка**:
```bash
# Mozilla Observatory
https://observatory.mozilla.org/

# Security Headers Scanner
https://securityheaders.com/
```

---

### 6. Vulnerable and Outdated Components
**Риск**: Использование библиотек с известными CVE.

**Защита**:
- ✅ Регулярный `npm audit` / `pip-audit` (встроить в CI/CD)
- ✅ Dependabot / Renovate для автоматических апдейтов зависимостей
- ✅ Не использовать deprecated пакеты

**CI/CD интеграция** (GitHub Actions):
```yaml
- name: Security audit
  run: npm audit --audit-level=high
```

**Политика**: Critical/High уязвимости должны быть исправлены в течение 7 дней.

---

### 7. Identification and Authentication Failures
**Риск**: Взлом аутентификации (credential stuffing, session hijacking).

**Требования**:
- ✅ Multi-Factor Authentication (MFA) для админов (обязательно)
- ✅ MFA для пользователей (опционально, но рекомендуется)
- ✅ Secure session management:
  - HttpOnly, Secure, SameSite cookies
  - Session timeout (например, 24 часа для веб, 30 дней для мобильных)
- ✅ Password policies:
  - Минимум 12 символов (или passwordless через Magic Links)
  - Проверка на утечку (HaveIBeenPwned API)
  - Не разрешать топ-10k most common passwords

**Пример cookie config**:
```javascript
res.cookie('sessionId', token, {
  httpOnly: true,
  secure: true, // HTTPS only
  sameSite: 'strict',
  maxAge: 24 * 60 * 60 * 1000 // 24 часа
});
```

---

### 8. Software and Data Integrity Failures
**Риск**: Компрометация CI/CD pipeline, supply chain атаки.

**Защита**:
- ✅ Signed commits (Git commit signing)
- ✅ Проверка integrity хешей для зависимостей (npm lockfile)
- ✅ Code review обязателен для prod веток (защита через branch rules)

**GitHub Branch Protection**:
- Require pull request reviews (минимум 1)
- Require status checks (CI должен пройти)
- Запретить force push в `main`

---

### 9. Security Logging and Monitoring Failures
**Риск**: Не замечаете атаки или взломы.

**Обязательно логировать**:
- ✅ Все authentication события (успехи и провалы)
- ✅ Изменения прав доступа
- ✅ Payment transactions
- ✅ Критичные ошибки (500, database failures)

**НЕ логировать**:
- ❌ Пароли (даже хешированные)
- ❌ Полные номера кредитных карт
- ❌ PII без маскирования

**Инструменты**:
- Sentry — для отслеживания ошибок
- DataDog / Logtail — для централизованного логирования
- Cloudflare / AWS WAF — для мониторинга подозрительного трафика

**Алерты**: Настроить уведомления в Slack/Email при:
- 5+ failed login attempts от одного IP
- Database connection failures
- Unusual spike в 4xx/5xx ошибках

---

### 10. Server-Side Request Forgery (SSRF)
**Риск**: Злоумышленник может заставить ваш сервер делать запросы к внутренним ресурсам.

**Защита**:
- ✅ Whitelist разрешенных доменов для внешних запросов
- ✅ Блокировать внутренние IP (127.0.0.1, 10.0.0.0/8, 192.168.0.0/16)
- ✅ Не принимать user-controlled URLs без валидации

**Пример**:
```javascript
// ❌ ОПАСНО
app.post('/fetch-url', async (req, res) => {
  const data = await fetch(req.body.url); // User может указать http://localhost:6379
  res.json(data);
});

// ✅ БЕЗОПАСНО
const allowedDomains = ['api.example.com', 'cdn.example.com'];
app.post('/fetch-url', async (req, res) => {
  const url = new URL(req.body.url);
  if (!allowedDomains.includes(url.hostname)) {
    return res.status(400).json({ error: 'Invalid domain' });
  }
  const data = await fetch(req.body.url);
  res.json(data);
});
```

---

## Процесс реагирования на инциденты

### При обнаружении уязвимости:

**Severity: Critical/High**
1. **Немедленно** уведомить @CTO и @CEO
2. Создать hotfix branch
3. Зафиксировать в prod в течение 24 часов
4. Post-mortem в течение 48 часов

**Severity: Medium/Low**
1. Создать issue в tracker
2. Включить в следующий спринт
3. Fix в течение 30 дней

### При подозрении на взлом:
1. **Изолировать** скомпрометированные системы
2. **Сохранить** логи для forensics
3. **Уведомить** affected пользователей (если была утечка данных)
4. **Соблюсти** GDPR/CCPA notification requirements (72 часа)

---

## Compliance (если применимо)

### GDPR (для EU пользователей)
- ✅ Право на удаление данных (Right to be forgotten)
- ✅ Экспорт данных в machine-readable формате
- ✅ Согласие на обработку (Consent management)
- ✅ DPA (Data Processing Agreement) с подрядчиками

### SOC 2 (для B2B SaaS)
- Необходимо при работе с enterprise клиентами
- Аудит проводится сторонней фирмой
- Стоимость: $20k-100k в год

### PCI DSS (если храните карты)
- **Лучше НЕ хранить**: используйте Stripe tokenization
- Если необходимо — требуется сертификация (дорого и сложно)

---

## Инструменты безопасности

**Обязательные** (для всех):
- **GitHub Dependabot** — автоматические PR для уязвимых зависимостей
- **npm audit / pip-audit** — в CI/CD pipeline
- **HTTPS Everywhere** — SSL сертификаты (Let's Encrypt бесплатно)

**Рекомендуемые** (Series A+):
- **Snyk** — расширенное сканирование зависимостей + IaC
- **Cloudflare WAF** — защита от DDoS и ботов
- **1Password / Vault** — хранение секретов команды

**Enterprise** (Series B+):
- **Penetration Testing** — ежегодный pentest от третьей стороны
- **Bug Bounty** — HackerOne / Bugcrowd (после достижения PMF)

---

## Обучение команды

**Обязательно для всех разработчиков**:
- Прочитать OWASP Top 10 (https://owasp.org/www-project-top-ten/)
- Пройти Security training (например, Secure Code Warrior)

**Частота**: Ежегодное обновление знаний по security best practices.

---

**Владелец**: CTO  
**Ревью**: Ежеквартально с обновлением под новые угрозы  
**Аудит**: Ежегодный security audit (внешний, при Series A+)

**Последнее обновление**: 2026-02-05
