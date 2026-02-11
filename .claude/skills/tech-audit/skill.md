# Tech Audit Skill

## Overview

**Purpose**: Систематический подход к code review, архитектурным решениям и проверке безопасности. Включает OWASP Top 10 checklists и best practices для поддержания высокого качества кодовой базы.

**Target Users**: CTO (primary), CEO (high-level security status)

**Capabilities**:
- Code review (structured PR review с taxonomy: Nit/Suggestion/Blocking)
- Security audit (OWASP Top 10 compliance check)
- Architecture review (SOLID principles, design patterns)
- Performance audit (N+1 queries, caching, optimization)
- Test coverage analysis

## Required Tools

Claude Code tools used by this skill:
- `Read` - Read code files for review
- `Grep` - Search for security patterns (hardcoded secrets, SQL injection patterns)
- `Glob` - Find files by type for comprehensive audits
- `Edit` - Suggest code fixes (security patches, refactoring)
- `mcp__ide__getDiagnostics` - Get linter/compiler diagnostics
- `Bash` - Run linters, test coverage, security scanners

## Components

### 1. audit_checklist.md

Master checklist for comprehensive code review covering:
- Architecture & Design (SOLID principles, design patterns)
- Code Quality (naming, readability, DRY, KISS)
- Security (OWASP Top 10 quick reference)
- Performance (database efficiency, caching, algorithms)
- Testing (coverage requirements, edge cases)
- Error Handling & Logging
- Documentation
- Dependencies
- Git & Version Control
- CI/CD & DevOps

### 2. owasp_checklist.md

Detailed OWASP Top 10 security checklist:
1. Broken Access Control (IDOR, authorization)
2. Cryptographic Failures (HTTPS, password hashing)
3. Injection (SQL, NoSQL, Command)
4. Insecure Design (rate limiting, threat modeling)
5. Security Misconfiguration (headers, defaults)
6. Vulnerable and Outdated Components (dependency audit)
7. Identification and Authentication Failures (MFA, sessions)
8. Software and Data Integrity Failures (supply chain)
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)

## Usage Examples

### Example 1: Code Review for Pull Request

```markdown
**Trigger**: Developer submits PR #42

**Process**:

1. Read PR files using Read tool
2. Check diagnostics with mcp__ide__getDiagnostics
3. Search for security patterns with Grep:
   - Hardcoded secrets: grep "API_KEY|PASSWORD|SECRET" --output_mode content
   - SQL injection risks: grep "execute.*f\"|execute.*%" --output_mode content
   - TODO comments: grep "TODO|FIXME" --output_mode content
4. Review against audit_checklist.md
5. Generate review report

**Review Report Template**:

## Code Review: [PR Title]

**PR**: #42
**Author**: @developer
**Reviewer**: @CTO
**Date**: 2026-02-10

### Summary
[One-line description of changes]

### Architecture Impact
- [ ] Changes documented in ADR?
- [ ] Architecture principles followed?
- [ ] No separation of concerns violations?

### Security (OWASP)
**🔴 BLOCKING**:
- [file:line] - SQL injection risk:
  ```python
  # BAD
  query = f"SELECT * FROM users WHERE id = {user_id}"

  # FIX
  query = "SELECT * FROM users WHERE id = ?"
  cursor.execute(query, (user_id,))
  ```

**🟡 SUGGESTION**:
- [file:line] - Password hashing: use bcrypt instead of MD5

### Code Quality
**Nit**:
- [file:line] - Variable `d` should be `profile_data` for clarity

**Suggestion**:
- [file:line] - Function 120 lines, split into smaller functions (<50 lines)

### Testing
- [ ] Coverage ≥ 70%? Run: pytest --cov or npm run test:coverage
- [ ] Edge cases tested?
- [ ] Tests pass in CI?

### Performance
- [ ] No N+1 queries?
- [ ] Database indexes on new queries?
- [ ] Caching appropriate?

### Decision
- [ ] ✅ Approved
- [ ] 🔄 Approved with changes (minor nits)
- [x] ⛔ Changes requested (blocking issues)

**Blocking Issues**:
1. SQL injection vulnerability (file:line) - MUST FIX
2. Missing tests for critical path - MUST ADD

**Timeline**: Fix within 24 hours, re-request review
```

### Example 2: Security Audit (Quarterly)

```markdown
**Trigger**: CEO requests security audit before penetration test

**Process**:

1. Use Glob to find all code files:
   ```
   pattern: "**/*.py"  # or *.js, *.go, etc.
   ```

2. Use Grep to search for common vulnerabilities:
   ```
   # Hardcoded secrets
   grep "api[_-]?key.*=.*['\"][a-zA-Z0-9]{20,}" --output_mode files_with_matches

   # Weak crypto
   grep "MD5|SHA1|hashlib\.md5|hashlib\.sha1" --output_mode files_with_matches

   # SQL injection patterns
   grep "execute.*%|execute.*\+|execute.*f\"" --output_mode files_with_matches

   # eval/exec dangers
   grep "eval\(|exec\(" --output_mode files_with_matches
   ```

3. Walk through OWASP Top 10 checklist systematically

4. Run security scanners:
   ```bash
   # Python
   bandit -r . -f json -o security_report.json
   safety check

   # Node.js
   npm audit --json > npm_audit.json
   npx snyk test
   ```

5. Generate security report

**Security Report Template**:

## Security Audit Report (Q1 2026)

**Date**: 2026-02-10
**Auditor**: @CTO
**Scope**: Full codebase security review

### Executive Summary

**Overall Status**: 🟡 MODERATE RISK

**Critical Issues**: 1
**High Priority**: 2
**Medium Priority**: 5
**Low Priority**: 8

---

### Critical Issues (Fix IMMEDIATELY)

**C1: Broken Access Control - Admin Deletion Endpoint**
- **File**: api/admin.py:145
- **Risk**: Any authenticated user can delete admin accounts
- **Impact**: Complete system compromise
- **Evidence**:
  ```python
  @app.route('/admin/users/<id>/delete', methods=['DELETE'])
  @require_auth  # No role check!
  def delete_user(id):
      User.delete(id)
  ```
- **Fix**:
  ```python
  @app.route('/admin/users/<id>/delete', methods=['DELETE'])
  @require_auth
  @require_role('admin')  # Add role check
  def delete_user(id):
      User.delete(id)
  ```
- **ETA**: 24 hours

---

### High Priority (Fix within 1 week)

**H1: Cryptographic Failures - Weak Password Hashing**
- **File**: auth/password.py:23
- **Risk**: bcrypt work factor = 10 (recommended: 12+)
- **Impact**: Faster brute-force if DB leaked
- **Fix**: Increase work factor to 12
- **ETA**: 3 days

**H2: Injection - SQL Injection Risk**
- **File**: models/user.py:89
- **Risk**: String formatting in SQL query
- **Evidence**:
  ```python
  query = f"SELECT * FROM users WHERE email = '{email}'"
  ```
- **Fix**: Use parameterized queries
- **ETA**: 2 days

---

### Recommendations

**Before Penetration Test**:
- Must fix: C1 (critical)
- Should fix: H1, H2 (high priority)

**Timeline**: 1 week to remediate, then ready for pentest

**Next Review**: 2026-05-10 (quarterly)
```

### Example 3: Performance Audit

```bash
# Use Bash tool to run performance analysis tools

# 1. Find N+1 query patterns
echo "Searching for potential N+1 queries..."
# Use Grep to find ORM patterns that commonly cause N+1
grep "for.*in.*\.all\(\)" --output_mode content -A 5

# 2. Check database query performance
# Read Django/Rails query logs or use profiling tools
python manage.py test --debug-sql  # Django example

# 3. Analyze bundle size (frontend)
npm run build -- --analyze

# 4. Check test coverage
pytest --cov=app --cov-report=term --cov-report=html
```

**Performance Report**:

```markdown
## Performance Audit Results

### Database Efficiency
**🔴 CRITICAL: N+1 Query Detected**
- **File**: views/dashboard.py:45
- **Issue**: Loading users in loop
  ```python
  # Current (N+1 problem)
  users = User.query.all()
  for user in users:
      profile = user.profile  # Separate query for each user!

  # Fix (eager loading)
  users = User.query.options(joinedload(User.profile)).all()
  ```
- **Impact**: Dashboard load time 5+ seconds with 1000 users
- **Expected Improvement**: <500ms after fix

### Missing Indexes
- [ ] Add index on `users.email` (frequently queried)
- [ ] Add composite index on `orders(user_id, created_at)`

### Bundle Size
- **Current**: 850KB gzipped
- **Target**: <500KB
- **Recommendation**: Code splitting, lazy loading
```

## Workflows

### Workflow 1: PR Review Process

1. **Trigger**: PR opened or review requested
2. **Read PR description** and linked issues
3. **Read changed files** using Read tool
4. **Run diagnostics** with mcp__ide__getDiagnostics
5. **Search for patterns** with Grep (security, TODOs)
6. **Review against checklist** (audit_checklist.md)
7. **Generate review** using code_review_template
8. **Post review** with categorized feedback (Nit/Suggestion/Blocking)

### Workflow 2: Quarterly Security Audit

1. **Trigger**: Quarterly schedule or CEO request
2. **Scan codebase** with Glob (find all code files)
3. **Search vulnerabilities** with Grep (patterns from OWASP)
4. **Run security tools** with Bash (bandit, npm audit, snyk)
5. **Walk through OWASP checklist** (owasp_checklist.md)
6. **Compile findings** by severity (Critical/High/Medium/Low)
7. **Generate report** for CEO/Board
8. **Track remediation** in tickets

### Workflow 3: Architecture Decision Review

1. **Trigger**: Developer proposes architecture change
2. **Read proposal** (ADR or design doc)
3. **Evaluate trade-offs** (performance, maintainability, cost)
4. **Check alignment** with existing architecture
5. **Create ADR** if approved
6. **Document in** [Startup]/knowledge-base/03_Tech/architecture_decisions/

## Search Patterns for Common Issues

### Security Patterns (use with Grep tool)

```bash
# Hardcoded secrets
pattern: "(api[_-]?key|password|secret|token).*=.*['\"][a-zA-Z0-9]{10,}"

# SQL injection risks
pattern: "(execute|query).*f\"|.*\+.*query"

# Weak crypto
pattern: "MD5|SHA1|hashlib\.md5"

# Command injection
pattern: "os\.system|subprocess\.call.*shell=True"

# eval/exec dangers
pattern: "eval\(|exec\(|pickle\.loads"

# Sensitive data in logs
pattern: "log.*password|print.*api_key"
```

### Code Quality Patterns

```bash
# TODOs needing attention
pattern: "TODO|FIXME|HACK|XXX"

# Magic numbers
pattern: "(?<!\.)\b\d{2,}\b(?!\s*\))" --multiline

# Long functions (>50 lines)
# Use Bash: grep -c "def " file.py and analyze

# Commented code
pattern: "^\s*#.*[=\(\)\[\]]" --multiline
```

## Decision Taxonomy

Categorize all review comments:

### **Nit** 🟢 (не блокирует merge)
- Stylistic improvements
- Minor naming suggestions
- Code formatting
- Non-critical refactors

### **Suggestion** 🟡 (рекомендация)
- Possible improvements
- Alternative approaches
- Future optimizations
- Technical debt notes

### **Blocking** 🔴 (требует исправления)
- Security vulnerabilities
- Bugs (confirmed or likely)
- Missing critical tests
- Architecture violations
- Breaking changes without migration

## Integration with Other Skills

### finance-forecasting
- Security audit prevents data breaches → protects financial data
- Performance optimization → reduces infrastructure costs

### board-reporting
- Security audit results → Board Meeting security slide
- Tech debt status → Quarterly review

### market-analysis
- Competitor security incidents → lessons for our audit

## Best Practices

### 1. Constructive Feedback

**Bad** ❌:
> "This code is terrible, rewrite it completely"

**Good** ✅:
> "This function has multiple responsibilities (SRP violation). Suggest splitting into:
> 1. `validateInput(data)` - validation
> 2. `saveToDatabase(valid_data)` - persistence
> 3. `sendNotification(user)` - side effects"

### 2. Prioritize by Impact

When multiple issues found, sort by:
1. **Security** (critical) → fix immediately
2. **Bugs** (high) → fix within 24-48 hours
3. **Performance** (medium) → fix in next sprint
4. **Code quality** (low) → track in technical debt backlog

### 3. Automate What You Can

**Linters** (automated checks):
- ESLint (JavaScript/TypeScript)
- Pylint/Flake8/Black (Python)
- Prettier (formatting)
- golangci-lint (Go)

**Security scanners**:
- Dependabot (dependency vulnerabilities)
- Snyk / OWASP Dependency-Check
- Bandit (Python security)
- SonarQube (code smells + security)

**CI/CD checks**:
- Tests must pass
- Coverage ≥ 70%
- Lint errors = 0
- Security scan clean

**CTO focuses on what machines CAN'T do** → architecture, business logic correctness, design decisions.

## Troubleshooting

### Problem: "Code review takes too long"

**Solution**:
- Use audit_checklist.md for structure (speeds up process)
- Delegate non-critical reviews to Senior Developers
- CTO focuses on: Security, Architecture, Critical bugs
- Automate with linters/scanners (reduce manual checking)

### Problem: "Too many security issues, don't know where to start"

**Solution**:
- Prioritize by OWASP Risk Rating (Critical→High→Medium→Low)
- Fix OWASP 1-3 (Access Control, Crypto, Injection) first
- Track progress in backlog (e.g., "Security Debt" label)
- Set sprint goals (e.g., "Fix 5 high-priority issues per sprint")

### Problem: "Grep returns too many false positives"

**Solution**:
- Refine patterns with context (`-A 2 -B 2` for surrounding lines)
- Use `--type` parameter to filter file types
- Combine with manual review of results
- Build whitelist of known safe patterns

## Version History

- **2026-02-10**: Adapted for Claude Code CLI from GitHub Copilot skill
  - Added Grep/Glob/Bash integration for automated scanning
  - Added mcp__ide__getDiagnostics for linter integration
  - Updated search patterns for Claude Code usage
- **2026-02-05**: Original GitHub Copilot version
  - audit_checklist.md, owasp_checklist.md
  - SKILL.md documentation

## Related Files

- `audit_checklist.md` - Master code review checklist
- `owasp_checklist.md` - OWASP Top 10 detailed security checklist
- `.github/skills/tech-audit/` - Original GitHub Copilot version
