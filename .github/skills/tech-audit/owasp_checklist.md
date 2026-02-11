# OWASP Top 10 Security Checklist (2021)

Comprehensive security audit checklist based on OWASP Top 10.

Reference: https://owasp.org/Top10/

---

## 1. Broken Access Control

### Definition
Restrictions on what authenticated users are allowed to do are often not properly enforced.

### Common Vulnerabilities
- **IDOR (Insecure Direct Object References)**: User can access other users' data
  ```
  GET /api/users/123/profile  ← Can I change 123 to 456 and get someone else's profile?
  ```
- **Missing authorization checks**: Endpoint accessible without proper role
- **Privilege escalation**: Regular user can access admin functions

### Checklist
- [ ] All API endpoints have authentication middleware?
- [ ] Authorization checks on resource access (not just authentication)?
- [ ] IDOR prevention (validate user owns resource before returning)?
- [ ] Horizontal privilege escalation prevented?
- [ ] Vertical privilege escalation prevented (user can't become admin)?
- [ ] CORS configured correctly (no wildcard `*` in production)?

### Example Secure Implementation
```javascript
// BAD ❌
app.get('/api/users/:id/profile', authenticate, (req, res) => {
  const profile = await getProfile(req.params.id);  // Any user can access!
  res.json(profile);
});

// GOOD ✅
app.get('/api/users/:id/profile', authenticate, authorize, (req, res) => {
  if (req.user.id !== req.params.id && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  const profile = await getProfile(req.params.id);
  res.json(profile);
});
```

---

## 2. Cryptographic Failures

### Definition
Failures related to cryptography (or lack thereof) leading to exposure of sensitive data.

### Common Vulnerabilities
- Passwords stored in plain text or weak hashing (MD5, SHA1)
- Sensitive data transmitted over HTTP (not HTTPS)
- Weak encryption algorithms
- Hardcoded encryption keys

### Checklist
- [ ] HTTPS enforced everywhere? (HSTS header configured)
- [ ] Passwords hashed with bcrypt/argon2/scrypt (NOT MD5/SHA1)?
- [ ] Bcrypt work factor ≥ 12?
- [ ] Sensitive data encrypted at rest? (database encryption)
- [ ] Encryption keys stored securely (not in code)?
- [ ] TLS 1.2+ used (no SSL, no TLS 1.0/1.1)?
- [ ] Secure random number generation (crypto.randomBytes, not Math.random)?

### Example Secure Implementation
```python
# BAD ❌
import hashlib
password_hash = hashlib.md5(password.encode()).hexdigest()  # Weak!

# GOOD ✅
import bcrypt
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
```

---

## 3. Injection

### Definition
User-supplied data is not validated, filtered, or sanitized by the application.

### Types of Injection
- **SQL Injection**: Malicious SQL in queries
- **NoSQL Injection**: Malicious queries in MongoDB, etc.
- **Command Injection**: OS commands via user input
- **LDAP Injection**
- **XPath Injection**

### Checklist
- [ ] **SQL**: Parameterized queries used (NO string concatenation)?
- [ ] **NoSQL**: Input validated before querying MongoDB/Redis?
- [ ] **Command Injection**: No `eval()`, `exec()`, `system()` with user input?
- [ ] Input validation on type, length, format?
- [ ] Whitelist validation (accept known-good), not blacklist (reject known-bad)?

### Example Secure Implementation

#### SQL Injection Prevention
```python
# BAD ❌
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)  # Vulnerable to SQL injection!

# GOOD ✅
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))  # Parameterized query
```

#### NoSQL Injection Prevention
```javascript
// BAD ❌
const user = await User.findOne({ username: req.body.username });
// If req.body.username = { $ne: null }, returns any user!

// GOOD ✅
const username = String(req.body.username);  // Force string type
const user = await User.findOne({ username: username });
```

#### Command Injection Prevention
```python
# BAD ❌
import os
os.system(f"ping {user_input}")  # Vulnerable! user_input = "8.8.8.8; rm -rf /"

# GOOD ✅
import subprocess
subprocess.run(["ping", "-c", "4", user_input], check=True)  # Safe - args separated
```

---

## 4. Insecure Design

### Definition
Missing or ineffective control design (different from flawed implementation).

### Common Issues
- No threat modeling performed
- Insufficient rate limiting (brute force attacks possible)
- No abuse case testing
- Lack of security requirements in design phase

### Checklist
- [ ] Threat modeling performed for critical flows?
- [ ] Rate limiting on authentication endpoints? (prevent brute force)
- [ ] Rate limiting on expensive operations? (API abuse prevention)
- [ ] Principle of least privilege applied?
- [ ] Security requirements documented?

### Example: Rate Limiting
```javascript
// Using express-rate-limit
const rateLimit = require('express-rate-limit');

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // Max 5 login attempts
  message: 'Too many login attempts, please try again later'
});

app.post('/api/login', loginLimiter, loginHandler);
```

---

## 5. Security Misconfiguration

### Definition
Missing appropriate security hardening or improperly configured permissions.

### Common Issues
- Default credentials still enabled
- Unnecessary features enabled (debugging in production)
- Error messages reveal stack traces
- Security headers missing

### Checklist
- [ ] Default passwords changed?
- [ ] Debugging disabled in production?
- [ ] Detailed error messages hidden from users?
- [ ] Security headers configured?
  - Content-Security-Policy
  - X-Frame-Options: DENY
  - X-Content-Type-Options: nosniff
  - Strict-Transport-Security (HSTS)
- [ ] CORS configured restrictively (not wildcard)?
- [ ] Unnecessary services disabled?

### Example: Security Headers
```javascript
// Using helmet.js
const helmet = require('helmet');

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"]
    }
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}));
```

---

## 6. Vulnerable and Outdated Components

### Definition
Using components (libraries, frameworks) with known vulnerabilities.

### Common Issues
- Outdated dependencies with CVEs
- Using unmaintained libraries
- Not monitoring vulnerability databases

### Checklist
- [ ] Dependencies regularly updated?
- [ ] `npm audit` or equivalent run regularly?
- [ ] Dependabot or Snyk enabled?
- [ ] Unused dependencies removed?
- [ ] Critical vulnerabilities patched within 24-48 hours?

### Example: Dependency Audit
```bash
# Node.js
npm audit
npm audit fix

# Python
pip install safety
safety check

# Check for outdated packages
npm outdated
```

---

## 7. Identification and Authentication Failures

### Definition
Confirmation of user's identity, authentication, and session management.

### Common Issues
- Weak password policy
- Credential stuffing (using leaked passwords)
- No multi-factor authentication (MFA)
- Session IDs exposed in URL
- Sessions don't expire

### Checklist
- [ ] Strong password policy enforced? (min 8 chars, complexity)
- [ ] MFA available for sensitive accounts?
- [ ] Credential stuffing prevention (check against HaveIBeenPwned)?
- [ ] Session IDs regenerated after login?
- [ ] Sessions expire after inactivity?
- [ ] Logout invalidates session?
- [ ] Password reset tokens expire (e.g., 1 hour)?

### Example: Password Policy
```python
import re

def validate_password(password):
    """
    Password must be:
    - At least 8 characters
    - Contains uppercase, lowercase, number, special char
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain lowercase letter"
    
    if not re.search(r'\d', password):
        return False, "Password must contain number"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain special character"
    
    return True, "Password valid"
```

---

## 8. Software and Data Integrity Failures

### Definition
Code and infrastructure that does not protect against integrity violations.

### Common Issues
- Unsigned packages/updates (supply chain attacks)
- CI/CD pipeline compromised
- Insecure deserialization (pickle, YAML, JSON)

### Checklist
- [ ] Dependencies from trusted sources? (official registries)
- [ ] Package integrity verified? (checksums, signatures)
- [ ] CI/CD secrets secured? (not in code, use secret managers)
- [ ] Deserialization safe? (no `pickle.loads()` on untrusted data)
- [ ] Code signing for releases?

### Example: Insecure Deserialization
```python
# BAD ❌
import pickle
user_data = pickle.loads(request.data)  # Can execute arbitrary code!

# GOOD ✅
import json
user_data = json.loads(request.data)  # Safe (only data, no code)
```

---

## 9. Security Logging and Monitoring Failures

### Definition
Without logging and monitoring, breaches cannot be detected.

### Common Issues
- Important events not logged (failed logins, privilege changes)
- Logs not monitored or alerted on
- Logs cleared or tampered with

### Checklist
- [ ] Authentication events logged? (login, logout, failed attempts)
- [ ] Authorization failures logged?
- [ ] Data access logged (who accessed what, when)?
- [ ] Security alerts configured? (e.g., 10 failed logins → alert)
- [ ] Logs tamper-proof? (append-only, centralized)
- [ ] Log retention policy defined (e.g., 90 days)?

### Example: Security Logging
```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'security.log' })
  ]
});

// Log authentication events
app.post('/api/login', (req, res) => {
  const { username, password } = req.body;
  
  if (validateCredentials(username, password)) {
    logger.info('Successful login', { username, ip: req.ip, timestamp: new Date() });
    // Continue login...
  } else {
    logger.warn('Failed login attempt', { username, ip: req.ip, timestamp: new Date() });
    res.status(401).json({ error: 'Invalid credentials' });
  }
});
```

---

## 10. Server-Side Request Forgery (SSRF)

### Definition
Application fetches remote resources without validating user-supplied URL.

### Common Issues
- User can make server fetch internal URLs (e.g., `http://localhost:6379` for Redis)
- Cloud metadata endpoints accessible (`http://169.254.169.254/latest/meta-data/`)

### Checklist
- [ ] User-supplied URLs validated (whitelist of allowed domains)?
- [ ] Internal IPs blocked (127.0.0.1, 10.0.0.0/8, 192.168.0.0/16)?
- [ ] Cloud metadata endpoints blocked?
- [ ] Network segmentation (app server can't access internal services directly)?

### Example: SSRF Prevention
```python
import requests
from urllib.parse import urlparse

ALLOWED_DOMAINS = ['example.com', 'api.trusted-service.com']

def fetch_url(user_url):
    parsed = urlparse(user_url)
    
    # Block internal IPs
    if parsed.hostname in ['localhost', '127.0.0.1'] or \
       parsed.hostname.startswith('192.168.') or \
       parsed.hostname.startswith('10.'):
        raise ValueError("Internal URLs not allowed")
    
    # Whitelist check
    if parsed.hostname not in ALLOWED_DOMAINS:
        raise ValueError("Domain not in whitelist")
    
    # Fetch safely
    response = requests.get(user_url, timeout=5)
    return response.text
```

---

## Summary: Quick Security Audit

Use this as a fast checklist:

- [ ] **Access Control**: Authorization checks on all endpoints?
- [ ] **Crypto**: HTTPS + bcrypt passwords + no hardcoded keys?
- [ ] **Injection**: Parameterized queries + input validation?
- [ ] **Design**: Rate limiting + threat modeling?
- [ ] **Config**: Security headers + no default passwords?
- [ ] **Dependencies**: `npm audit` clean + Dependabot enabled?
- [ ] **Auth**: MFA available + sessions expire?
- [ ] **Integrity**: No insecure deserialization?
- [ ] **Logging**: Auth events logged + alerts configured?
- [ ] **SSRF**: URL validation + internal IPs blocked?

**Risk Assessment**:
- **Critical Issues**: Fix within 24 hours
- **High Issues**: Fix within 1 week
- **Medium Issues**: Fix within 1 month
- **Low Issues**: Track in backlog
