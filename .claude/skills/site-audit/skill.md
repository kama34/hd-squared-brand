# Site Audit Skill

## Overview

**Purpose**: Технический и контентный аудит сайта по чек-листам: SEO, accessibility (WCAG), privacy/legal, analytics, performance.

**Target Users**: CTO (primary), CMO (SEO/analytics), CEO (compliance)

**Capabilities**:
- SEO audit (meta tags, headings, canonical, sitemap)
- Accessibility audit (WCAG basics, alt text, aria-labels, contrast)
- Privacy/legal compliance (GDPR, cookie consent)
- Analytics tracking verification
- Performance recommendations

## Required Tools

- `Read` - Read HTML/CSS files
- `Grep` - Search for missing tags, patterns
- `Bash` - Run Lighthouse CLI, accessibility checkers
- `Write` - Save audit report

## Usage Example: Sales AI Landing Page Audit

```bash
"Используя site-audit skill, audit Sales AI/site/code4.html"

**Process**:
1. Read HTML file
2. Check against audit checklist
3. Generate findings report

---

## Site Audit Report: Sales AI Landing Page

**URL**: Sales AI/site/code4.html
**Date**: 2026-02-10
**Auditor**: CTO

---

### SUMMARY

**Checks Passed**: 12/20 (60%)
**Critical Issues**: 3
**Medium Issues**: 5
**Low Priority**: 2

**Overall Grade**: 🟡 C (Needs Improvement)

---

### SEO AUDIT

#### ✅ PASSED (5/8)

1. **Title Tag Present**: ✅
   ```html
   <title>Sales AI - AI Analytics for SMBs</title>
   ```

2. **Meta Description Present**: ✅
   ```html
   <meta name="description" content="Turn data into decisions in 5 minutes...">
   ```

3. **H1 Tag Present**: ✅
   ```html
   <h1>Turn Data Into Decisions in 5 Minutes</h1>
   ```

4. **Semantic HTML**: ✅ (Uses header, main, section, footer)

5. **Responsive Meta Tag**: ✅
   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   ```

#### 🔴 FAILED (3/8)

**ISSUE #1**: Missing Canonical URL 🔴 CRITICAL
**Criticality**: HIGH
**Problem**: No canonical tag → duplicate content risk if site accessible via multiple URLs

**Fix**:
```html
<link rel="canonical" href="https://salesai.com/">
```

**ISSUE #2**: Missing robots.txt reference ⚠️ MEDIUM
**Criticality**: MEDIUM
**Problem**: No robots meta tag or robots.txt file detected

**Fix**:
```html
<!-- In <head> -->
<meta name="robots" content="index, follow">

<!-- Create robots.txt file -->
User-agent: *
Allow: /
Sitemap: https://salesai.com/sitemap.xml
```

**ISSUE #3**: Missing Structured Data (Schema.org) 🟢 LOW
**Criticality**: LOW (but recommended)
**Problem**: No schema markup for better rich snippets in search

**Fix**:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Sales AI",
  "applicationCategory": "BusinessApplication",
  "offers": {
    "@type": "Offer",
    "price": "29",
    "priceCurrency": "USD"
  }
}
</script>
```

---

### ACCESSIBILITY AUDIT (WCAG 2.1 Level AA)

#### ✅ PASSED (3/10)

1. **Language Declared**: ✅
   ```html
   <html lang="en">
   ```

2. **Semantic Landmarks**: ✅ (header, main, footer present)

3. **Keyboard Navigation**: ✅ (Tabindex not misused)

#### 🔴 FAILED (7/10)

**ISSUE #4**: Missing Alt Text on Images 🔴 CRITICAL
**Criticality**: HIGH (WCAG 1.1.1 violation)
**Problem**: 5 images found without alt attributes

**Affected Images**:
```html
<!-- Line 45 -->
<img src="hero-screenshot.png">
<!-- Should be: -->
<img src="hero-screenshot.png" alt="Sales AI dashboard showing AI-generated insight example">

<!-- Line 203 -->
<img src="customer-logo-1.png">
<!-- Should be: -->
<img src="customer-logo-1.png" alt="Company A logo">
```

**Fix**: Add descriptive alt text to ALL images

**ISSUE #5**: Buttons Without Aria-Labels 🔴 CRITICAL
**Criticality**: HIGH
**Problem**: Icon-only buttons lack labels for screen readers

**Affected Elements**:
```html
<!-- Line 89 -->
<button class="menu-toggle">☰</button>
<!-- Should be: -->
<button class="menu-toggle" aria-label="Open navigation menu">☰</button>

<!-- Line 156 -->
<button class="play-video">▶</button>
<!-- Should be: -->
<button class="play-video" aria-label="Play product demo video">▶</button>
```

**ISSUE #6**: Insufficient Color Contrast ⚠️ MEDIUM
**Criticality**: MEDIUM (WCAG 1.4.3)
**Problem**: CTA button text has low contrast (2.8:1, minimum: 4.5:1)

**Affected Element**:
```css
/* Line 234 in style.css */
.cta-button {
  background: #4CAF50;
  color: #A8E6A3; /* Too light! */
}

/* Fix: */
.cta-button {
  background: #4CAF50;
  color: #FFFFFF; /* Contrast: 4.6:1 ✅ */
}
```

**Tool**: Check with WebAIM Contrast Checker

**ISSUE #7**: Form Inputs Missing Labels ⚠️ MEDIUM
**Criticality**: MEDIUM
**Problem**: Email input lacks associated <label>

**Affected Element**:
```html
<!-- Line 312 -->
<input type="email" placeholder="Enter your email">

<!-- Fix: -->
<label for="email-signup">Email Address</label>
<input type="email" id="email-signup" placeholder="Enter your email">
<!-- OR use aria-label if visual label undesired -->
<input type="email" aria-label="Email address for trial signup" placeholder="Enter your email">
```

**ISSUE #8**: Skip to Main Content Link Missing 🟢 LOW
**Criticality**: LOW (but best practice)
**Problem**: No skip link for keyboard users

**Fix**:
```html
<!-- Add as first element in <body> -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<style>
.skip-link {
  position: absolute;
  left: -9999px;
  top: 0;
}
.skip-link:focus {
  left: 0;
  z-index: 9999;
  background: #000;
  color: #fff;
  padding: 10px;
}
</style>

<!-- Then add id to main -->
<main id="main-content">
```

---

### PRIVACY & LEGAL COMPLIANCE

#### ✅ PASSED (2/3)

1. **Privacy Policy Link**: ✅ (Found in footer)
2. **HTTPS Enforced**: ✅ (Assuming deployed with SSL)

#### 🔴 FAILED (1/3)

**ISSUE #9**: Cookie Consent Banner Missing ⚠️ MEDIUM
**Criticality**: MEDIUM (GDPR/CCPA requirement if tracking users)
**Problem**: Google Analytics detected but no cookie consent banner

**Fix**:
```html
<!-- Add cookie consent banner -->
<div id="cookie-banner" style="display:none;">
  <p>We use cookies to improve your experience. <a href="/privacy">Learn more</a></p>
  <button onclick="acceptCookies()">Accept</button>
  <button onclick="rejectCookies()">Decline</button>
</div>

<script>
function acceptCookies() {
  localStorage.setItem('cookieConsent', 'true');
  document.getElementById('cookie-banner').style.display = 'none';
  // Initialize analytics here
}

function rejectCookies() {
  localStorage.setItem('cookieConsent', 'false');
  document.getElementById('cookie-banner').style.display = 'none';
}

// Show banner if no consent stored
if (!localStorage.getItem('cookieConsent')) {
  document.getElementById('cookie-banner').style.display = 'block';
}
</script>
```

---

### ANALYTICS & TRACKING

#### ✅ PASSED (2/4)

1. **Google Analytics Installed**: ✅ (GA4 tag found)
2. **GTM Container**: ✅ (GTM-XXXXXX found)

#### 🔴 FAILED (2/4)

**ISSUE #10**: CTA Click Events Not Tracked ⚠️ MEDIUM
**Criticality**: MEDIUM (can't measure conversion)
**Problem**: No event tracking on "Start Free Trial" buttons

**Fix** (using GTM):
```html
<!-- Add data attributes to CTAs -->
<button class="cta-primary" data-event="cta_click" data-location="hero">
  Start Free Trial
</button>

<!-- GTM Trigger: -->
Trigger Type: Click - All Elements
Trigger Conditions: Click Classes contains "cta-primary"

<!-- GTM Tag: -->
Tag Type: GA4 Event
Event Name: cta_click
Event Parameters:
  - button_location: {{Click Element - data-location}}
```

**ISSUE #11**: Form Submission Not Tracked 🟢 LOW
**Criticality**: LOW
**Problem**: No event for email signup form

**Fix**:
```html
<form onsubmit="trackFormSubmit(event)">
  <input type="email" required>
  <button type="submit">Get Started</button>
</form>

<script>
function trackFormSubmit(event) {
  gtag('event', 'generate_lead', {
    'event_category': 'engagement',
    'event_label': 'email_signup'
  });
}
</script>
```

---

### PERFORMANCE

#### ⚠️ RECOMMENDATIONS (Not Failures, But Improvements)

**REC #1**: Optimize Images
- **hero-screenshot.png**: 2.3 MB → should be <500 KB
- **Fix**: Use WebP format, compress with TinyPNG
- **Expected Impact**: -2 seconds load time

**REC #2**: Minimize CSS
- **style.css**: 150 KB → should be <50 KB
- **Fix**: Remove unused Tailwind classes, minify
- **Expected Impact**: -0.5 seconds load time

**REC #3**: Lazy Load Images
- **Problem**: All images load immediately
- **Fix**: Add `loading="lazy"` to below-fold images
```html
<img src="screenshot.png" alt="..." loading="lazy">
```

**REC #4**: Inline Critical CSS
- **Problem**: CSS blocks initial render
- **Fix**: Inline above-the-fold CSS in <head>
- **Expected Impact**: Faster First Contentful Paint

---

## ACTION PLAN (Prioritized)

### CRITICAL (Fix This Week)
1. ✅ Add alt text to all images (30 min)
2. ✅ Add aria-labels to icon buttons (15 min)
3. ✅ Add canonical URL tag (5 min)
4. ✅ Fix color contrast on CTA button (10 min)

**Total Time**: ~1 hour

### MEDIUM (Fix Next Week)
5. Add form labels (20 min)
6. Implement cookie consent banner (2 hours)
7. Add CTA click tracking (1 hour)
8. Create robots.txt (10 min)

**Total Time**: ~3.5 hours

### LOW (Nice to Have)
9. Add structured data schema (1 hour)
10. Add skip-to-content link (30 min)
11. Optimize images (2 hours)
12. Implement lazy loading (30 min)

**Total Time**: ~4 hours

---

## POST-FIX VERIFICATION

**After implementing fixes, verify with**:
- [ ] Google Lighthouse (target: >90 accessibility score)
- [ ] WAVE Web Accessibility Tool
- [ ] Google Search Console (check for crawl errors)
- [ ] GTM Debug Mode (verify event tracking)

**Re-audit Date**: 2026-02-17 (1 week after fixes)

---
```

## Workflow

1. **Read HTML/CSS files**
2. **Run automated checks** (Lighthouse via Bash)
3. **Manual review** (grep patterns, read source)
4. **Generate findings** with criticality
5. **Prioritize fixes** (Critical → Medium → Low)
6. **Save audit report**

## Integration with Other Skills

- **landing-structure** - Validates structure recommendations
- **html-fixes** - Implements audit findings
- **design-language** - Checks design consistency

## Version History

- **2026-02-10**: Adapted for Claude Code CLI
