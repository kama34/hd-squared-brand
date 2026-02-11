# Frontend Development Skill

## Overview

**Purpose**: Comprehensive frontend development expertise для создания, редактирования и оптимизации современных веб-сайтов и приложений. Включает HTML5, CSS3, JavaScript (ES6+), фреймворки (React/Vue/Angular), UI/UX best practices, accessibility, performance optimization.

**Target Users**: CTO (primary), UI/UX Designer (collaboration)

**Capabilities**:
- HTML5 semantic markup & accessibility (WCAG 2.1)
- CSS3 (Flexbox, Grid, animations, responsive design)
- JavaScript (ES6+, DOM, async/await, Fetch API, modules)
- Frontend frameworks (React, Vue, Angular patterns)
- Build tools (Webpack, Vite, Parcel)
- CSS frameworks (Tailwind CSS, Bootstrap, Material UI)
- Performance optimization (Core Web Vitals, lazy loading, code splitting)
- Browser compatibility & polyfills
- Testing (Jest, Cypress, Playwright)
- State management (Redux, Zustand, Context API)

## Required Tools

- `Read` - Read HTML/CSS/JS files
- `Edit` - Modify code files
- `Write` - Create new components
- `Grep` - Search for patterns, unused code
- `Glob` - Find files by extension
- `Bash` - Run build tools, linters, tests
- `mcp__playwright__*` - Browser automation for testing
- `mcp__ide__getDiagnostics` - Get linter errors

## Core Knowledge Areas

### 1. HTML5 Semantic Markup

#### Best Practices

**✅ GOOD** - Semantic structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Compelling description under 160 chars">
  <title>Page Title | Brand Name</title>

  <!-- Preconnect to external domains -->
  <link rel="preconnect" href="https://fonts.googleapis.com">

  <!-- Critical CSS inline -->
  <style>
    /* Above-the-fold critical CSS here */
  </style>

  <!-- Defer non-critical CSS -->
  <link rel="stylesheet" href="styles.css" media="print" onload="this.media='all'">
</head>
<body>
  <!-- Skip to main content for keyboard users -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <header>
    <nav aria-label="Primary navigation">
      <ul role="list">
        <li><a href="/" aria-current="page">Home</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    </nav>
  </header>

  <main id="main-content">
    <article>
      <h1>Main Heading</h1>
      <section>
        <h2>Section Title</h2>
        <p>Content goes here</p>
      </section>
    </article>
  </main>

  <aside aria-label="Related links">
    <!-- Secondary content -->
  </aside>

  <footer>
    <p>&copy; 2026 Company Name</p>
  </footer>

  <!-- Scripts at end of body for performance -->
  <script src="app.js" defer></script>
</body>
</html>
```

**❌ BAD** - Non-semantic divs:
```html
<div class="header">
  <div class="nav">...</div>
</div>
<div class="content">
  <div class="article">...</div>
</div>
<div class="footer">...</div>
```

#### HTML5 Semantic Elements Checklist

- [ ] `<header>` - Site/section header
- [ ] `<nav>` - Navigation menus
- [ ] `<main>` - Main content (one per page)
- [ ] `<article>` - Self-contained content
- [ ] `<section>` - Thematic grouping
- [ ] `<aside>` - Sidebar/tangential content
- [ ] `<footer>` - Site/section footer
- [ ] `<figure>` + `<figcaption>` - Images with captions
- [ ] `<details>` + `<summary>` - Expandable content
- [ ] `<time>` - Dates/times with datetime attribute

#### Forms Best Practices

**✅ GOOD** - Accessible form:
```html
<form action="/submit" method="POST" novalidate>
  <div class="form-group">
    <label for="email">Email Address <span aria-label="required">*</span></label>
    <input
      type="email"
      id="email"
      name="email"
      required
      aria-required="true"
      aria-describedby="email-help email-error"
      autocomplete="email"
    >
    <small id="email-help">We'll never share your email</small>
    <span id="email-error" role="alert" aria-live="polite"></span>
  </div>

  <div class="form-group">
    <fieldset>
      <legend>Choose plan</legend>
      <label>
        <input type="radio" name="plan" value="basic" required>
        Basic - $9/month
      </label>
      <label>
        <input type="radio" name="plan" value="pro">
        Pro - $29/month
      </label>
    </fieldset>
  </div>

  <button type="submit">Submit</button>
</form>
```

**Form Validation** (Client-side):
```javascript
const form = document.querySelector('form');
const emailInput = document.getElementById('email');
const emailError = document.getElementById('email-error');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  // Validate email
  if (!emailInput.validity.valid) {
    emailError.textContent = emailInput.validationMessage;
    emailError.classList.add('error');
    emailInput.setAttribute('aria-invalid', 'true');
    return;
  }

  // Submit form
  const formData = new FormData(form);
  fetch('/api/submit', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => console.log('Success:', data))
  .catch(error => console.error('Error:', error));
});
```

### 2. CSS3 Modern Layout

#### Flexbox Patterns

**✅ GOOD** - Flexible card layout:
```css
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem; /* Modern gap property */
  justify-content: space-between;
  align-items: stretch;
}

.card {
  flex: 1 1 300px; /* Grow, shrink, basis */
  min-width: 0; /* Prevent overflow */
  display: flex;
  flex-direction: column;
}

.card-content {
  flex: 1; /* Take remaining space */
}

.card-footer {
  margin-top: auto; /* Push to bottom */
}
```

#### CSS Grid Patterns

**✅ GOOD** - Responsive grid layout:
```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;

  /* Named grid areas for complex layouts */
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
}

@media (max-width: 768px) {
  .grid-container {
    grid-template-areas:
      "header"
      "main"
      "sidebar"
      "footer";
  }
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

#### Modern CSS Variables

```css
:root {
  /* Colors */
  --color-primary: #3B82F6;
  --color-primary-dark: #2563EB;
  --color-secondary: #10B981;
  --color-danger: #EF4444;

  /* Spacing (8px base system) */
  --space-1: 0.5rem;  /* 8px */
  --space-2: 1rem;    /* 16px */
  --space-3: 1.5rem;  /* 24px */
  --space-4: 2rem;    /* 32px */
  --space-5: 3rem;    /* 48px */

  /* Typography */
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'Fira Code', 'Courier New', monospace;

  --text-xs: 0.75rem;   /* 12px */
  --text-sm: 0.875rem;  /* 14px */
  --text-base: 1rem;    /* 16px */
  --text-lg: 1.125rem;  /* 18px */
  --text-xl: 1.25rem;   /* 20px */
  --text-2xl: 1.5rem;   /* 24px */
  --text-3xl: 1.875rem; /* 30px */

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);

  /* Border radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
  --radius-full: 9999px;

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 250ms ease;
  --transition-slow: 350ms ease;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #1F2937;
    --color-text: #F9FAFB;
  }
}
```

**Usage**:
```css
.button {
  background-color: var(--color-primary);
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-md);
  transition: background-color var(--transition-base);
}

.button:hover {
  background-color: var(--color-primary-dark);
}
```

#### Responsive Design Breakpoints

```css
/* Mobile-first approach */

/* Base styles (mobile) */
.container {
  padding: 1rem;
}

/* Tablet (768px+) */
@media (min-width: 48rem) {
  .container {
    padding: 2rem;
    max-width: 768px;
    margin: 0 auto;
  }
}

/* Desktop (1024px+) */
@media (min-width: 64rem) {
  .container {
    max-width: 1024px;
  }
}

/* Large desktop (1280px+) */
@media (min-width: 80rem) {
  .container {
    max-width: 1280px;
  }
}

/* Ultra-wide (1536px+) */
@media (min-width: 96rem) {
  .container {
    max-width: 1536px;
  }
}
```

**Container queries** (Modern approach):
```css
.card-container {
  container-type: inline-size;
}

.card {
  display: block;
}

/* When container > 400px */
@container (min-width: 400px) {
  .card {
    display: flex;
    gap: 1rem;
  }
}
```

### 3. JavaScript ES6+ Essentials

#### Modern JavaScript Patterns

**✅ GOOD** - ES6+ patterns:
```javascript
// 1. Destructuring
const { name, email, role = 'user' } = userData;
const [first, second, ...rest] = arrayData;

// 2. Spread operator
const newUser = { ...userData, lastLogin: Date.now() };
const mergedArray = [...array1, ...array2];

// 3. Template literals
const greeting = `Hello, ${name}! Your role is ${role}.`;
const html = `
  <div class="card">
    <h2>${title}</h2>
    <p>${description}</p>
  </div>
`;

// 4. Arrow functions
const double = (x) => x * 2;
const sum = (a, b) => a + b;
const processUser = (user) => ({
  ...user,
  fullName: `${user.firstName} ${user.lastName}`
});

// 5. Async/await
async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed to fetch user:', error);
    throw error;
  }
}

// 6. Modules (ESM)
// utils.js
export const formatDate = (date) => new Intl.DateTimeFormat('en-US').format(date);
export const capitalize = (str) => str.charAt(0).toUpperCase() + str.slice(1);
export default function logger(message) { console.log(message); }

// app.js
import logger, { formatDate, capitalize } from './utils.js';

// 7. Optional chaining & nullish coalescing
const userName = user?.profile?.name ?? 'Anonymous';
const port = process.env.PORT ?? 3000;

// 8. Array methods
const users = [
  { id: 1, name: 'Alice', active: true },
  { id: 2, name: 'Bob', active: false },
  { id: 3, name: 'Charlie', active: true }
];

const activeUsers = users.filter(user => user.active);
const userNames = users.map(user => user.name);
const hasInactiveUser = users.some(user => !user.active);
const allActive = users.every(user => user.active);
const charlie = users.find(user => user.name === 'Charlie');

// 9. Promises
Promise.all([
  fetch('/api/users'),
  fetch('/api/posts'),
  fetch('/api/comments')
])
.then(([users, posts, comments]) => {
  // All requests completed
})
.catch(error => {
  // Any request failed
});

// 10. Classes
class Component {
  constructor(props) {
    this.props = props;
    this.state = {};
  }

  setState(newState) {
    this.state = { ...this.state, ...newState };
    this.render();
  }

  render() {
    // Override in subclass
  }
}
```

#### DOM Manipulation Best Practices

**✅ GOOD** - Efficient DOM manipulation:
```javascript
// 1. Query selectors
const button = document.querySelector('.cta-button');
const allButtons = document.querySelectorAll('button');
const form = document.getElementById('signup-form');

// 2. Event delegation (better performance)
document.querySelector('.todo-list').addEventListener('click', (e) => {
  if (e.target.classList.contains('delete-btn')) {
    e.target.closest('.todo-item').remove();
  }
});

// ❌ BAD - Individual listeners
// document.querySelectorAll('.delete-btn').forEach(btn => {
//   btn.addEventListener('click', handleDelete);
// });

// 3. Creating elements efficiently
function createCard(data) {
  const template = document.getElementById('card-template');
  const card = template.content.cloneNode(true);

  card.querySelector('.card-title').textContent = data.title;
  card.querySelector('.card-description').textContent = data.description;
  card.querySelector('.card-image').src = data.image;

  return card;
}

// 4. Batch DOM updates
const fragment = document.createDocumentFragment();
items.forEach(item => {
  fragment.appendChild(createCard(item));
});
container.appendChild(fragment); // Single reflow

// 5. IntersectionObserver for lazy loading
const imageObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.remove('lazy');
      observer.unobserve(img);
    }
  });
});

document.querySelectorAll('img.lazy').forEach(img => {
  imageObserver.observe(img);
});

// 6. Web Storage API
// LocalStorage (persistent)
localStorage.setItem('user', JSON.stringify(userData));
const user = JSON.parse(localStorage.getItem('user'));

// SessionStorage (per-session)
sessionStorage.setItem('tempData', value);

// 7. Fetch API with abort controller
const controller = new AbortController();

fetch('/api/data', { signal: controller.signal })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => {
    if (error.name === 'AbortError') {
      console.log('Fetch aborted');
    }
  });

// Cancel request
setTimeout(() => controller.abort(), 5000);
```

### 4. React Patterns

#### Functional Components & Hooks

**✅ GOOD** - Modern React patterns:
```jsx
import React, { useState, useEffect, useMemo, useCallback } from 'react';

// 1. Functional component with hooks
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;

    async function loadUser() {
      try {
        setLoading(true);
        const response = await fetch(`/api/users/${userId}`);
        const data = await response.json();

        if (!cancelled) {
          setUser(data);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err.message);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    loadUser();

    // Cleanup
    return () => {
      cancelled = true;
    };
  }, [userId]); // Re-run when userId changes

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!user) return null;

  return (
    <div className="user-profile">
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  );
}

// 2. Custom hooks
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });

  const setStoredValue = (newValue) => {
    try {
      setValue(newValue);
      window.localStorage.setItem(key, JSON.stringify(newValue));
    } catch (error) {
      console.error('Failed to save to localStorage:', error);
    }
  };

  return [value, setStoredValue];
}

// Usage
function App() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');

  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Toggle theme
    </button>
  );
}

// 3. Memoization for performance
function ProductList({ products, onAddToCart }) {
  const [sortBy, setSortBy] = useState('name');

  // useMemo - memoize expensive calculations
  const sortedProducts = useMemo(() => {
    return [...products].sort((a, b) => {
      if (sortBy === 'name') return a.name.localeCompare(b.name);
      if (sortBy === 'price') return a.price - b.price;
      return 0;
    });
  }, [products, sortBy]);

  // useCallback - memoize function references
  const handleAddToCart = useCallback((productId) => {
    onAddToCart(productId);
  }, [onAddToCart]);

  return (
    <div>
      <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
        <option value="name">Sort by name</option>
        <option value="price">Sort by price</option>
      </select>

      {sortedProducts.map(product => (
        <ProductCard
          key={product.id}
          product={product}
          onAddToCart={handleAddToCart}
        />
      ))}
    </div>
  );
}

// 4. Context API for global state
const ThemeContext = React.createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const value = {
    theme,
    toggleTheme: () => setTheme(t => t === 'light' ? 'dark' : 'light')
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

function useTheme() {
  const context = React.useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}

// 5. Error boundary (class component required)
class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
    // Log to error reporting service
  }

  render() {
    if (this.state.hasError) {
      return <div>Something went wrong.</div>;
    }
    return this.props.children;
  }
}
```

### 5. Performance Optimization

#### Core Web Vitals Checklist

**Largest Contentful Paint (LCP)** - Target: < 2.5s
- [ ] Optimize images (WebP, lazy loading, responsive images)
- [ ] Inline critical CSS
- [ ] Preload key resources
- [ ] Use CDN for assets
- [ ] Minimize server response time

**First Input Delay (FID)** - Target: < 100ms
- [ ] Minimize JavaScript execution time
- [ ] Code splitting (load only needed code)
- [ ] Use Web Workers for heavy computation
- [ ] Defer non-critical JavaScript

**Cumulative Layout Shift (CLS)** - Target: < 0.1
- [ ] Set width/height on images and videos
- [ ] Reserve space for ads/embeds
- [ ] Avoid inserting content above existing content
- [ ] Use CSS transform instead of layout properties

#### Image Optimization

```html
<!-- 1. Responsive images -->
<img
  src="image-800.jpg"
  srcset="
    image-400.jpg 400w,
    image-800.jpg 800w,
    image-1200.jpg 1200w
  "
  sizes="(max-width: 600px) 400px, (max-width: 1000px) 800px, 1200px"
  alt="Description"
  loading="lazy"
  decoding="async"
>

<!-- 2. Modern image formats with fallback -->
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Description">
</picture>

<!-- 3. Lazy loading with intersection observer -->
<img
  class="lazy"
  data-src="large-image.jpg"
  src="placeholder.jpg"
  alt="Description"
>

<script>
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.remove('lazy');
      observer.unobserve(img);
    }
  });
});

document.querySelectorAll('img.lazy').forEach(img => observer.observe(img));
</script>
```

#### Code Splitting

```javascript
// 1. Dynamic imports
button.addEventListener('click', async () => {
  const module = await import('./heavy-module.js');
  module.doSomething();
});

// 2. React lazy loading
import React, { lazy, Suspense } from 'react';

const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HeavyComponent />
    </Suspense>
  );
}

// 3. Route-based splitting
const routes = [
  {
    path: '/',
    component: lazy(() => import('./pages/Home'))
  },
  {
    path: '/about',
    component: lazy(() => import('./pages/About'))
  }
];
```

#### Caching Strategies

```javascript
// Service Worker for offline caching
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('v1').then(cache => {
      return cache.addAll([
        '/',
        '/styles.css',
        '/app.js',
        '/offline.html'
      ]);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then(response => {
      // Return cached version or fetch new
      return response || fetch(event.request);
    })
  );
});
```

### 6. Accessibility (WCAG 2.1 Level AA)

#### Accessibility Checklist

**Keyboard Navigation**
- [ ] All interactive elements focusable (no `tabindex="-1"` on buttons)
- [ ] Logical tab order (matches visual order)
- [ ] Visible focus indicators (`:focus` styles)
- [ ] Keyboard shortcuts documented
- [ ] Modal traps focus when open
- [ ] Escape key closes modals

**Screen Reader Support**
- [ ] All images have `alt` text (empty `alt=""` for decorative)
- [ ] Form inputs have associated `<label>` or `aria-label`
- [ ] Icon buttons have `aria-label`
- [ ] ARIA roles used correctly (`role="button"`, `role="navigation"`)
- [ ] ARIA states updated dynamically (`aria-expanded`, `aria-hidden`)
- [ ] Live regions for dynamic content (`aria-live="polite"`)

**Color & Contrast**
- [ ] Text contrast ≥ 4.5:1 for normal text
- [ ] Text contrast ≥ 3:1 for large text (18pt+)
- [ ] UI components contrast ≥ 3:1
- [ ] Don't rely on color alone for information

**Examples**:

```html
<!-- Modal with focus trap -->
<div
  role="dialog"
  aria-labelledby="modal-title"
  aria-modal="true"
  class="modal"
>
  <h2 id="modal-title">Confirm Action</h2>
  <p>Are you sure you want to continue?</p>
  <button>Confirm</button>
  <button aria-label="Close modal">×</button>
</div>

<!-- Accessible dropdown -->
<button
  aria-expanded="false"
  aria-controls="dropdown-menu"
  aria-haspopup="true"
  id="menu-button"
>
  Menu
</button>
<ul id="dropdown-menu" role="menu" aria-labelledby="menu-button" hidden>
  <li role="menuitem"><a href="/profile">Profile</a></li>
  <li role="menuitem"><a href="/settings">Settings</a></li>
</ul>

<!-- Status messages -->
<div role="status" aria-live="polite" aria-atomic="true">
  Item added to cart
</div>

<!-- Loading state -->
<button aria-busy="true">
  <span aria-hidden="true">⏳</span>
  Loading...
</button>
```

### 7. Build Tools & Workflows

#### Vite Configuration (Modern bundler)

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          'vendor': ['react', 'react-dom'],
          'utils': ['lodash', 'date-fns']
        }
      }
    },
    minify: 'terser',
    sourcemap: true
  },
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
});
```

#### Package.json Scripts

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "eslint src --ext .js,.jsx,.ts,.tsx",
    "lint:fix": "eslint src --fix",
    "format": "prettier --write \"src/**/*.{js,jsx,ts,tsx,css}\"",
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest --coverage",
    "type-check": "tsc --noEmit"
  }
}
```

## Usage Examples

### Example 1: Build Landing Page from Scratch

**Trigger**: CEO requests new landing page for Sales AI

**Process**:

1. **Read existing design system**:
```bash
Read Sales AI/knowledge-base/04_Marketing/brand_guidelines.md
```

2. **Create semantic HTML structure**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sales AI - AI-Powered Sales Analytics</title>
  <meta name="description" content="Transform your sales data into actionable insights with AI. Start free trial today.">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <nav aria-label="Primary navigation">
      <a href="/" aria-label="Sales AI home">
        <img src="logo.svg" alt="Sales AI logo">
      </a>
      <ul role="list">
        <li><a href="#features">Features</a></li>
        <li><a href="#pricing">Pricing</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <a href="/login" class="btn-secondary">Login</a>
    </nav>
  </header>

  <main id="main-content">
    <section class="hero">
      <h1>Transform Sales Data Into Decisions in 5 Minutes</h1>
      <p>AI-powered analytics for SMBs. No data scientist required.</p>
      <a href="#signup" class="cta-button">Start Free Trial</a>
    </section>

    <section id="features">
      <h2>Features</h2>
      <!-- Feature cards -->
    </section>
  </main>

  <footer>
    <p>&copy; 2026 Sales AI. All rights reserved.</p>
  </footer>

  <script src="app.js" defer></script>
</body>
</html>
```

3. **Implement responsive CSS with Tailwind or custom**:
```css
/* Mobile-first responsive design */
.hero {
  padding: 2rem 1rem;
  text-align: center;
}

.hero h1 {
  font-size: clamp(2rem, 5vw, 3.5rem); /* Fluid typography */
  margin-bottom: 1rem;
}

@media (min-width: 768px) {
  .hero {
    padding: 4rem 2rem;
  }
}
```

4. **Add interactivity with vanilla JS**:
```javascript
// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    target.scrollIntoView({ behavior: 'smooth' });
  });
});
```

5. **Run site-audit skill** to check quality:
```bash
"Используя site-audit skill, audit Sales AI/site/index.html"
```

### Example 2: Optimize Existing Site Performance

**Trigger**: Site has slow load times (LCP > 4s)

**Process**:

1. **Run Lighthouse audit**:
```bash
npx lighthouse https://salesai.com --view
```

2. **Identify issues**:
- Large images (hero image 2.5 MB)
- Blocking JavaScript
- No lazy loading

3. **Fix images**:
```bash
# Convert to WebP
npm install sharp
node -e "require('sharp')('hero.png').webp({quality: 80}).toFile('hero.webp')"

# Generate responsive sizes
node -e "
  const sharp = require('sharp');
  const sizes = [400, 800, 1200];
  sizes.forEach(size => {
    sharp('hero.png')
      .resize(size)
      .webp({quality: 80})
      .toFile(\`hero-\${size}.webp\`);
  });
"
```

4. **Update HTML**:
```html
<picture>
  <source
    srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
    sizes="(max-width: 600px) 400px, (max-width: 1000px) 800px, 1200px"
    type="image/webp"
  >
  <img src="hero-800.jpg" alt="Sales AI dashboard" loading="eager">
</picture>
```

5. **Defer non-critical JS**:
```html
<!-- Before -->
<script src="analytics.js"></script>

<!-- After -->
<script src="analytics.js" defer></script>
```

6. **Re-run Lighthouse** - verify LCP < 2.5s

### Example 3: Fix Accessibility Issues

**Trigger**: Site audit reveals WCAG violations

**Process**:

1. **Grep for images without alt**:
```bash
grep '<img' --output_mode content | grep -v 'alt='
```

2. **Fix alt text**:
```javascript
// Use Edit tool to add alt text
<img src="feature-1.png">
// Change to:
<img src="feature-1.png" alt="AI-generated sales insights dashboard">
```

3. **Check form labels**:
```bash
grep '<input' --output_mode content -A 2 -B 2
```

4. **Add missing labels**:
```html
<!-- Before -->
<input type="email" placeholder="Email">

<!-- After -->
<label for="email">Email Address</label>
<input type="email" id="email" placeholder="Email">
```

5. **Test with screen reader** (NVDA on Windows, VoiceOver on Mac)

## Integration with Other Skills

### tech-audit
- frontend-development implements → tech-audit reviews
- tech-audit identifies security issues → frontend-development fixes

### site-audit
- frontend-development builds site → site-audit checks quality
- site-audit reports issues → frontend-development optimizes

### design-language
- design-language defines style guide → frontend-development implements
- frontend-development extracts CSS patterns → design-language documents

### backend-development
- frontend-development fetches data → backend-development provides API
- backend-development validates → frontend-development displays errors

## Best Practices

### 1. Mobile-First Design

**❌ BAD** - Desktop-first:
```css
.container {
  width: 1200px;
}

@media (max-width: 768px) {
  .container {
    width: 100%;
  }
}
```

**✅ GOOD** - Mobile-first:
```css
.container {
  width: 100%;
  padding: 1rem;
}

@media (min-width: 768px) {
  .container {
    max-width: 768px;
    margin: 0 auto;
  }
}

@media (min-width: 1200px) {
  .container {
    max-width: 1200px;
  }
}
```

### 2. Component-Based Architecture

**✅ GOOD** - Reusable components:
```javascript
// Button.js
function Button({ variant = 'primary', size = 'medium', children, ...props }) {
  const classes = `btn btn-${variant} btn-${size}`;
  return <button className={classes} {...props}>{children}</button>;
}

// Usage
<Button variant="primary" onClick={handleClick}>Submit</Button>
<Button variant="secondary" size="small">Cancel</Button>
```

### 3. Progressive Enhancement

**✅ GOOD** - Works without JavaScript:
```html
<!-- Form submits even without JS -->
<form action="/api/submit" method="POST">
  <input type="email" name="email" required>
  <button type="submit">Submit</button>
</form>

<script>
// Enhance with JS
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  // AJAX submission
});
</script>
```

### 4. Error Handling in UI

**✅ GOOD** - User-friendly error messages:
```javascript
async function loadData() {
  try {
    const response = await fetch('/api/data');

    if (!response.ok) {
      if (response.status === 404) {
        throw new Error('Data not found. Please check your request.');
      }
      if (response.status === 500) {
        throw new Error('Server error. Please try again later.');
      }
      throw new Error('Something went wrong. Please try again.');
    }

    return await response.json();
  } catch (error) {
    // Show user-friendly error in UI
    showErrorMessage(error.message);

    // Log technical details for debugging
    console.error('Failed to load data:', error);
  }
}
```

## Troubleshooting

### Problem: "Layout shifts on page load (high CLS)"

**Solution**:
1. Set explicit width/height on images:
```html
<img src="hero.jpg" width="1200" height="600" alt="...">
```

2. Reserve space for dynamic content:
```css
.ad-container {
  min-height: 250px; /* Reserve space before ad loads */
}
```

3. Use CSS aspect-ratio:
```css
.video-container {
  aspect-ratio: 16 / 9;
}
```

### Problem: "JavaScript not working in production but works locally"

**Solution**:
1. Check browser console for errors
2. Verify file paths are correct (case-sensitive on Linux servers)
3. Check if JavaScript is minified correctly
4. Ensure Content Security Policy allows scripts
5. Use source maps for debugging minified code

### Problem: "Site not responsive on mobile"

**Solution**:
1. Add viewport meta tag:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

2. Use relative units (rem, %, vw) instead of fixed pixels
3. Test with browser DevTools device emulation
4. Use CSS Grid/Flexbox for flexible layouts

### Problem: "Vite build output directory mismatch with Docker"

**Error в Docker build**:
```
ERROR: "/app/dist": not found
```

**Причина**: vite.config.ts настроен на нестандартную output directory.

**Check vite.config.ts**:
```typescript
// ❌ BAD - нестандартная директория
export default defineConfig({
  build: {
    outDir: 'build',  // Нестандарт
  }
})

// ✅ GOOD - стандартная для Vite
export default defineConfig({
  build: {
    outDir: 'dist',  // Стандарт
  }
})
```

**В Dockerfile**:
```dockerfile
# Должно совпадать с vite.config.ts outDir
COPY --from=builder /app/dist /usr/share/nginx/html
```

**Профилактика**:
- ВСЕГДА использовать стандартный `dist/` для Vite
- Проверять build logs: `npm run build` покажет реальную папку вывода
- Синхронизировать vite.config.ts с Dockerfile

---

## Version History

- **2026-02-10**: Created comprehensive frontend-development skill for CTO
  - HTML5, CSS3, JavaScript ES6+
  - React patterns, performance optimization
  - Accessibility (WCAG 2.1), responsive design
  - Build tools (Vite, Webpack)
  - Integration with tech-audit, site-audit, design-language skills

- **2026-02-10**: Added Vite build output directory mismatch error
  - Common mistake: vite.config.ts outDir doesn't match Dockerfile
  - Solution: Use standard dist/ directory
