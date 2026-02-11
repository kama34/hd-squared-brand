# Определение технологического стека

## Текущий стек

### Frontend
**[ЗАПОЛНИТЬ: Выберите ваш стек]**

Примеры популярных стеков:
- **React** + TypeScript + Next.js + Tailwind CSS
- **Vue.js** + Nuxt + Vuetify
- **Svelte** + SvelteKit

**Наш выбор**:
- Framework: [ЗАПОЛНИТЬ]
- Язык: [ЗАПОЛНИТЬ: JavaScript / TypeScript]
- UI библиотека: [ЗАПОЛНИТЬ]
- State management: [ЗАПОЛНИТЬ: Redux / Zustand / Pinia / etc.]
- Build tool: [ЗАПОЛНИТЬ: Vite / Webpack / etc.]

**Обоснование**: [ЗАПОЛНИТЬ: Почему именно этот стек?]

---

### Backend
**[ЗАПОЛНИТЬ: Выберите ваш стек]**

Примеры:
- **Node.js** + Express/Fastify + TypeScript
- **Python** + FastAPI / Django
- **Go** + Gin/Echo
- **Ruby** + Rails
- **Java/Kotlin** + Spring Boot

**Наш выбор**:
- Язык/Runtime: [ЗАПОЛНИТЬ]
- Framework: [ЗАПОЛНИТЬ]
- API стиль: [ЗАПОЛНИТЬ: REST / GraphQL / gRPC]
- ORM: [ЗАПОЛНИТЬ: Prisma / TypeORM / SQLAlchemy / etc.]

**Обоснование**: [ЗАПОЛНИТЬ]

---

### База данных
**Primary DB**: [ЗАПОЛНИТЬ: PostgreSQL / MySQL / MongoDB / etc.]

**Дополнительные хранилища**:
- Cache: [ЗАПОЛНИТЬ: Redis / Memcached / none]
- Search: [ЗАПОЛНИТЬ: Elasticsearch / Algolia / none]
- Analytics: [ЗАПОЛНИТЬ: ClickHouse / BigQuery / none]
- File storage: [ЗАПОЛНИТЬ: S3 / GCS / Cloudflare R2]

**Миграции**: [ЗАПОЛНИТЬ: инструмент - Prisma Migrate / Flyway / Alembic]

---

### Infrastructure & DevOps

**Cloud Provider**: [ЗАПОЛНИТЬ: AWS / GCP / Azure / DigitalOcean / Vercel]

**Ключевые сервисы**:
- Compute: [ЗАПОЛНИТЬ: EC2 / Cloud Run / App Service / Kubernetes]
- Database: [ЗАПОЛНИТЬ: RDS / Cloud SQL / Managed DB]
- CDN: [ЗАПОЛНИТЬ: CloudFront / Cloudflare / Fastly]
- Monitoring: [ЗАПОЛНИТЬ: DataDog / New Relic / Sentry]
- Logging: [ЗАПОЛNИТЬ: CloudWatch / Logtail / Papertrail]

**CI/CD**:
- Pipeline: [ЗАПОЛНИТЬ: GitHub Actions / GitLab CI / CircleCI]
- Deployment: [ЗАПОЛНИТЬ: Vercel / Railway / Kubernetes / Docker]

**IaC (Infrastructure as Code)**:
- Tool: [ЗАПОЛНИТЬ: Terraform / Pulumi / CloudFormation / none]

---

### Внешние сервисы и API

**Аутентификация**:
- [ЗАПОЛНИТЬ: Auth0 / Clerk / Firebase Auth / Custom JWT]

**Платежи**:
- [ЗАПОЛНИТЬ: Stripe / Paddle / Lemon Squeezy]

**Email**:
- Transactional: [ЗАПОЛНИТЬ: SendGrid / Postmark / Resend]
- Marketing: [ЗАПОЛНИТЬ: Mailchimp / ConvertKit / Customer.io]

**Analytics**:
- Product: [ЗАПОЛНИТЬ: Mixpanel / Amplitude / PostHog]
- Web: [ЗАПОЛНИТЬ: Google Analytics / Plausible]

**Другие интеграции**:
- [ЗАПОЛНИТЬ: перечислите ключевые сторонние API]

---

### Development Tools

**Version Control**: Git + [ЗАПОЛНИТЬ: GitHub / GitLab / Bitbucket]

**Project Management**:
- [ЗАПОЛНИТЬ: Linear / Jira / Asana / GitHub Projects]

**Communication**:
- [ЗАПОЛНИТЬ: Slack / Discord / Microsoft Teams]

**Documentation**:
- [ЗАПОЛНИТЬ: Notion / Confluence / GitBook]

**Design**:
- [ЗАПОЛНИТЬ: Figma / Sketch / Adobe XD]

---

## Принципы выбора технологий

### 1. **Время до маркетинга (Time to Market)**
На ранних стадиях скорость важнее "идеальной" архитектуры.

**Приоритет**: Фреймворки с готовыми решениями (Rails, Django, Next.js) > Low-level инструменты

### 2. **Доступность талантов**
Если стек слишком экзотический, будет сложно нанимать.

**Правило**: Используйте популярные технологии, если нет веских причин выбрать нишевые.

### 3. **Масштабируемость (но не преждевременная)**
Не оптимизируйте для 1M пользователей, когда у вас 100.

**Стратегия**: Выбирайте технологии, которые позволят масштабироваться **когда понадобится**, но не усложняйте архитектуру заранее.

### 4. **Стоимость инфраструктуры**
На стадии Seed каждый доллар важен.

**Benchmark**: Инфраструктура не должна превышать 10-15% от MRR на ранних стадиях.

### 5. **Developer Experience (DX)**
Счастливые разработчики = быстрая доставка фич.

**Инвестируйте в**: TypeScript, линтеры, CI/CD, хорошие dev-environments.

---

## Запрещенные практики

❌ **Микросервисы на стадии MVP** — Overengineering. Начните с монолита.  
❌ **Хардкод секретов в коде** — Используйте переменные окружения.  
❌ **Деплой без тестов** — Минимум unit-тесты для критичных путей.  
❌ **Использование deprecated библиотек** — Проверяйте поддержку перед включением.  
❌ **Vendor lock-in без причины** — Используйте стандарты (SQL, S3-compatible storage).

---

## Процесс принятия решений

### Когда добавляем новую технологию:

**Шаблон ADR (Architecture Decision Record)**:

```markdown
# ADR-XXX: [Название решения]

## Контекст
[Какую проблему решаем?]

## Рассмотренные варианты
1. Вариант A - [плюсы/минусы]
2. Вариант B - [плюсы/минусы]

## Решение
[Что выбрали и почему]

## Последствия
[Как это повлияет на кодовую базу, команду, бюджет]

## Статус
[Предложено / Принято / Отклонено / Устарело]

Дата: YYYY-MM-DD
Автор: @CTO / Engineering Team
```

Сохраняйте ADR в `.github/knowledge-base/03_Tech/architecture_decisions/`

---

## Roadmap миграций

**Запланированные изменения**: [ЗАПОЛНИТЬ]

Пример:
- **Q2 2024**: Миграция с JavaScript на TypeScript
- **Q3 2024**: Переход с монолита на modular monolith
- **2025**: Оценка Kubernetes (если > 100k пользователей)

**Правило**: Любая миграция должна иметь ясное business justification от @CFO.

---

## Мониторинг технического долга

**Еженедельно @CTO оценивает**:
- Code coverage (цель: >70% для критичных модулей)
- Build time (цель: <5 минут для CI)
- Deploy frequency (цель: ≥1 раз в день для продакшна)
- Mean Time to Recovery (MTTR) при инцидентах

**Квартально @CTO + @CEO решают**:
- Выделять ли спринт на рефакторинг?
- Требуется ли апгрейд зависимостей?

---

**Владелец**: CTO  
**Использование**:  
- Онбординг новых разработчиков
- Оценка совместимости при выборе библиотек
- Обоснование технических решений перед @Board

**Последнее обновление**: 2026-02-05
