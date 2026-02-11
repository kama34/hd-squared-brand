---
name: site-audit
description: Навык, который выполняет технический и контентный аудит сайта по чек-листам: SEO, доступность, privacy, analytics.
---

Чек-листы и проверки:
- SEO: наличие title, meta description, корректные заголовки, canonical, robots, sitemap.
- Accessibility (WCAG basics): alt у изображений, aria-label у интерактивных элементов, контрастность (рекомендация), семантическая разметка.
- Privacy & Legal: наличие ссылки на privacy policy, корректный cookie-banner, обработка форм и хранение данных.
- Analytics & Tracking: наличие GTM/GA, корректные события для CTA.
- Performance hints: крупные изображения, отсутствие inline CSS блокирующего рендеринг (советы, не обязательные исправления).

Результат:
- `findings`: список проблем с уровнем риска и примером исправления.
- `checks_passed`: краткий список пройденных проверок.
