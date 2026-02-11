# MCP Advisor Skill

## Overview

**Purpose**: Анализировать проект и рекомендовать релевантные MCP (Model Context Protocol) серверы для интеграции. Помогает автоматизировать доступ к внешним сервисам и данным.

**Target Users**: CTO (primary), CEO (понимание возможностей автоматизации)

**Capabilities**:
- Analyze repository structure and identify automation opportunities
- Recommend MCP servers based on tech stack and needs
- Provide setup instructions for MCP integration
- Troubleshoot MCP connection issues

## Required Tools

Claude Code tools used by this skill:
- `Glob` - Find files to analyze project structure
- `Read` - Read package.json, requirements.txt, docker-compose.yml
- `Grep` - Search for API usage patterns
- `Bash` - Check installed MCP servers, test connections
- `WebSearch` - Find latest MCP servers and documentation

## What are MCP Servers?

Model Context Protocol servers extend Claude Code's capabilities by:
- Accessing external APIs (GitHub, Jira, Slack)
- Reading specialized file formats (PDFs, databases)
- Automating browser interactions (Playwright)
- Searching the web (Brave Search)
- Querying databases (PostgreSQL, MongoDB)

**Benefit**: Instead of manual API calls, Claude Code gets direct access through MCP.

## Common MCP Servers

### 1. brave-search
**Purpose**: Web search for competitive research, market intel
**Use Cases**: CMO competitive analysis, market sizing research
**Setup**: Requires BRAVE_API_KEY environment variable

### 2. playwright
**Purpose**: Browser automation, screenshots, web scraping
**Use Cases**: Landing page testing, competitor website analysis
**Setup**: Auto-installs, no API key needed

### 3. github
**Purpose**: Direct GitHub API access (PRs, issues, repos)
**Use Cases**: CTO code review, CEO project tracking
**Setup**: Requires GitHub personal access token

### 4. postgres
**Purpose**: Query PostgreSQL databases directly
**Use Cases**: CFO financial analysis, data extraction
**Setup**: Requires database connection string

### 5. filesystem
**Purpose**: Advanced file operations beyond standard tools
**Use Cases**: Bulk file operations, complex searches
**Setup**: No configuration needed

### 6. git
**Purpose**: Git operations (commit history, blame, diffs)
**Use Cases**: CTO architecture decisions, code archaeology
**Setup**: Auto-detects git repo

### 7. puppeteer
**Purpose**: Similar to Playwright (browser automation)
**Use Cases**: E2E testing, screenshot generation
**Setup**: Auto-installs

### 8. slack
**Purpose**: Read/send Slack messages, search history
**Use Cases**: Team communication, notifications
**Setup**: Requires Slack app token

### 9. google-drive
**Purpose**: Access Google Docs, Sheets
**Use Cases**: Board meeting notes, financial models
**Setup**: Requires Google OAuth credentials

## Usage Examples

### Example 1: Analyze Project and Recommend MCPs

```markdown
**Trigger**: CTO wants to know which MCPs would benefit the project

**Process**:

1. **Analyze tech stack** (use Glob + Read):
   ```
   Find: package.json, requirements.txt, docker-compose.yml
   Read: Check for database usage, external APIs
   ```

2. **Search for API patterns** (use Grep):
   ```
   Pattern: "requests\.get|fetch\(|axios\."
   Pattern: "github\.com/|api\.github\.com"
   Pattern: "postgresql://|mongodb://"
   ```

3. **Generate recommendations**:

---

## MCP Recommendations for [Startup Name]

**Date**: 2026-02-10
**Analyst**: @CTO

### Project Analysis

**Tech Stack Detected**:
- Language: Python, JavaScript
- Database: PostgreSQL
- APIs Used: GitHub API, Stripe API
- Frontend: React (landing page)

---

### Recommended MCPs

#### 1. brave-search (HIGH PRIORITY)
**Why**: CMO needs competitive research
**Use Cases**:
- Monthly competitor analysis
- Market sizing for fundraising
- Industry trend tracking

**Setup**:
```bash
# Get API key: https://brave.com/search/api/
export BRAVE_API_KEY="your-key-here"

# Add to ~/.claude/mcp.json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${env:BRAVE_API_KEY}"
      }
    }
  }
}
```

**Estimated ROI**: Save 3-5 hours/week on manual research

---

#### 2. playwright (HIGH PRIORITY)
**Why**: Automate landing page testing
**Use Cases**:
- Screenshot landing page (desktop/mobile)
- Accessibility audits
- Competitor website analysis

**Setup**:
```bash
# Add to ~/.claude/mcp.json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"]
    }
  }
}
```

**Estimated ROI**: Save 2-3 hours/week on manual testing

---

#### 3. github (MEDIUM PRIORITY)
**Why**: Direct GitHub API access for code review
**Use Cases**:
- Automated PR reviews
- Issue tracking
- Release management

**Setup**:
```bash
# Create token: https://github.com/settings/tokens
export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"

# Add to ~/.claude/mcp.json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

**Estimated ROI**: Save 1-2 hours/week on PR management

---

#### 4. postgres (LOW PRIORITY - Future)
**Why**: Direct database queries (when needed)
**Use Cases**:
- CFO ad-hoc financial queries
- Data extraction for reports

**Setup**: Defer until production database launched

---

### NOT Recommended (Yet)

**slack**: No Slack workspace currently
**google-drive**: No Google Drive usage detected
**mongo**: Using PostgreSQL, not MongoDB

---

### Implementation Plan

**Phase 1** (This Week):
- Set up brave-search (1 hour)
- Set up playwright (30 min)
- Test both with sample queries

**Phase 2** (Next Sprint):
- Set up github MCP (1 hour)
- Train team on usage

**Total Setup Time**: ~3 hours
**Expected Weekly Savings**: 6-10 hours

---
```

### Example 2: Troubleshoot MCP Connection

```markdown
**Problem**: "brave-search MCP not working"

**Diagnosis Steps**:

1. **Check MCP config** (use Read):
   ```
   Read: ~/.claude/mcp.json
   # or
   Read: C:\Users\[user]\.claude\mcp.json
   ```

2. **Verify environment variable** (use Bash):
   ```bash
   # Unix/Mac
   echo $BRAVE_API_KEY

   # Windows
   echo %BRAVE_API_KEY%
   ```

3. **Test MCP server manually** (use Bash):
   ```bash
   # Test if server starts
   npx @modelcontextprotocol/server-brave-search
   ```

4. **Common Issues**:

**Issue 1**: "API key not found"
- **Cause**: BRAVE_API_KEY not set
- **Fix**:
  ```bash
  # Windows PowerShell
  setx BRAVE_API_KEY "your-key-here"
  # Restart VS Code/terminal

  # Unix/Mac
  export BRAVE_API_KEY="your-key-here"
  # Add to ~/.bashrc or ~/.zshrc for persistence
  ```

**Issue 2**: "MCP server not responding"
- **Cause**: npm/npx not installed
- **Fix**:
  ```bash
  # Check Node.js installation
  node --version
  npm --version

  # Install if missing: https://nodejs.org/
  ```

**Issue 3**: "Permission denied"
- **Cause**: MCP config file permissions
- **Fix**:
  ```bash
  # Unix/Mac
  chmod 644 ~/.claude/mcp.json

  # Windows
  # Check file isn't read-only (Properties → Attributes)
  ```

---
```

### Example 3: MCP Server Discovery

```markdown
**Trigger**: CTO wants to know what new MCPs are available

**Process**:

1. **Search for official MCP servers** (use WebSearch):
   ```
   Query: "Model Context Protocol servers list 2026"
   Query: "MCP server registry"
   Query: "@modelcontextprotocol npm packages"
   ```

2. **Check MCP documentation**:
   ```
   Query: "Claude MCP servers documentation"
   ```

3. **Generate discovery report**:

---

## New MCP Servers Available (Q1 2026)

### Recently Released

**1. jira**
- **Purpose**: Jira issue management
- **Use Cases**: Project tracking, sprint planning
- **Relevance**: MEDIUM (if we adopt Jira for project management)

**2. aws**
- **Purpose**: AWS service management
- **Use Cases**: Infrastructure operations, cost monitoring
- **Relevance**: LOW (not using AWS yet)

**3. linear**
- **Purpose**: Linear issue tracker integration
- **Use Cases**: Similar to Jira
- **Relevance**: LOW (using GitHub Issues)

**4. notion**
- **Purpose**: Notion workspace access
- **Use Cases**: Knowledge base, team wiki
- **Relevance**: LOW (not using Notion)

**5. confluence**
- **Purpose**: Atlassian Confluence integration
- **Use Cases**: Documentation, technical specs
- **Relevance**: LOW (not using Confluence)

---

### Recommendations

**Currently**: Focus on brave-search and playwright (high ROI)

**Future Consideration**:
- **github** → when code review volume increases
- **slack** → if we adopt Slack for team chat
- **jira/linear** → if we need advanced project management

**Re-evaluate**: Q3 2026 (after Series A, team growth)

---
```

## Workflow: MCP Setup

### 1. Initial Setup

1. **Check MCP config location**:
   ```bash
   # Unix/Mac
   ls ~/.claude/mcp.json

   # Windows
   dir C:\Users\%USERNAME%\.claude\mcp.json
   ```

2. **Create config if missing**:
   ```bash
   # Unix/Mac
   mkdir -p ~/.claude
   touch ~/.claude/mcp.json

   # Windows
   mkdir C:\Users\%USERNAME%\.claude
   type nul > C:\Users\%USERNAME%\.claude\mcp.json
   ```

3. **Add first MCP server** (example: brave-search):
   ```json
   {
     "mcpServers": {
       "brave-search": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-brave-search"],
         "env": {
           "BRAVE_API_KEY": "${env:BRAVE_API_KEY}"
         }
       }
     }
   }
   ```

4. **Set environment variable**:
   ```bash
   # Windows PowerShell
   setx BRAVE_API_KEY "your-api-key"

   # Unix/Mac (add to ~/.bashrc or ~/.zshrc)
   export BRAVE_API_KEY="your-api-key"
   ```

5. **Restart Claude Code** to load MCP

### 2. Testing MCP Connection

```bash
# Test manually
npx @modelcontextprotocol/server-brave-search

# Should start without errors
# Press Ctrl+C to stop
```

### 3. Using MCP in Claude Code

Once configured, MCPs work automatically:

```
# Example: Using brave-search MCP
"Find latest news about Competitor X"
→ Claude Code uses brave-search MCP automatically

# Example: Using playwright MCP
"Screenshot Sales AI landing page"
→ Claude Code uses playwright MCP automatically
```

## Integration with Other Skills

### market-analysis
- **brave-search MCP** → continuous competitive intelligence
- **playwright MCP** → competitor website analysis

### tech-audit
- **github MCP** → automated PR reviews, code history
- **git MCP** → architecture decisions, blame analysis

### board-reporting
- **google-drive MCP** → access Board meeting notes
- **slack MCP** → team communication metrics

### finance-forecasting
- **postgres MCP** → direct financial data queries
- **google-sheets MCP** → financial model access

## Best Practices

### 1. Security: API Keys

**DO**:
- Store API keys in environment variables
- Use secret managers (1Password, Bitwarden) for backup
- Rotate keys quarterly
- Use separate keys for dev/prod

**DON'T**:
- Hardcode keys in mcp.json
- Commit keys to git
- Share keys via Slack/email
- Use production keys in dev

### 2. Performance: Selective Enabling

**Enable MCPs only when needed**:
- Startup time increases with each MCP
- Unused MCPs consume resources
- Start with 2-3 high-ROI MCPs

### 3. Documentation

**Track MCPs in knowledge base**:
```
[Startup]/knowledge-base/03_Tech/mcp_servers.md

# Active MCP Servers

## brave-search
- Purpose: Competitive research
- Owner: @CMO
- API Key Location: 1Password (search "Brave")
- Setup Date: 2026-02-10

## playwright
- Purpose: Landing page testing
- Owner: @CTO
- Setup Date: 2026-02-10
```

## Troubleshooting

### Problem: "MCP not showing up in Claude Code"

**Solutions**:
1. Check mcp.json syntax (valid JSON?)
2. Restart Claude Code completely
3. Check ~/.claude/logs/ for error messages
4. Verify Node.js/npm installed (required for npx)

### Problem: "MCP times out"

**Solutions**:
1. Check internet connection (MCPs need network access)
2. Verify API key is valid
3. Check MCP server status (might be down)
4. Increase timeout in mcp.json (if configurable)

### Problem: "Too many MCPs, startup slow"

**Solutions**:
1. Disable unused MCPs
2. Keep only 3-5 essential MCPs active
3. Use on-demand MCP loading (future feature)

## Version History

- **2026-02-10**: Adapted for Claude Code CLI
  - Added MCP setup workflows
  - Integration with other skills
  - Troubleshooting guide
- **2026-02-05**: Original GitHub Copilot version
  - Basic MCP recommendations
  - Analysis scripts

## Related Files

- `.github/skills/mcp-advisor/SKILL.md` - Original version
- `.claude-helpers/mcp-guide.md` - Detailed MCP documentation
- `~/.claude/mcp.json` - MCP configuration file

## Useful Links

- MCP Servers Registry: https://github.com/modelcontextprotocol/servers
- Brave Search API: https://brave.com/search/api/
- MCP Documentation: https://modelcontextprotocol.io/
