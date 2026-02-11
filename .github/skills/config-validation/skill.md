# Config Validation Skill

## Overview
**Purpose**: Validate and edit sales funnel configuration files (JSON format) with strict variable scoping rules
**Target Users**: Config Editor agent
**Capabilities**:
- Variable syntax validation (`{variable_name}` format)
- Variable scope checking (stage-local variables)
- Unused variable cleanup
- Nested variable detection and prevention
- Dot notation prevention
- Pydantic schema compliance validation

## Required Tools
- `Read` - Read config files
- `Edit` - Edit config files
- `Grep` - Search for variable patterns
- `Bash` - Run validation scripts (if available)

## Usage Examples

### Example 1: Add Variable to Stage
**Context**: [Sales AI] User wants to add `greeting_message` variable to Welcome stage

**Input**:
```
"Add greeting_message='Hello valued customer' to Welcome stage in bildanov_config.json"
```

**Workflow**:
1. Read `Sales AI/configs/bildanov/bildanov_config.json`
2. Locate `stages.Welcome.system_prompt`
3. Add variable to `variables` section:
   ```json
   "variables": {
     ...existing...,
     "greeting_message": "Hello valued customer"
   }
   ```
4. Use variable in `prompt`: `{greeting_message}`
5. Run cleanup algorithm (check for unused vars)
6. Validate syntax (no nesting, no dots, local scope)

**Output**:
```markdown
✅ Added variable 'greeting_message' to Welcome stage

**Changes:**
- Added to `variables`: "greeting_message": "Hello valued customer"
- Used in prompt: {greeting_message}

**Cleanup:**
- No unused variables detected

**Validation:**
✅ Variable syntax correct
✅ No nested variables
✅ No dot notation
✅ Local scope respected
```

---

### Example 2: Validate Config File
**Context**: User finished editing config and wants validation

**Input**:
```
"Validate bildanov_config.json for all parser rules"
```

**Workflow**:
1. Read config file
2. Extract all `{variable}` references from ALL prompts
3. Check each variable exists in SAME stage's `variables` section
4. Check for nested variables in values
5. Check for dot notation patterns
6. Check for unused variables (defined but not referenced)
7. Validate schema structure

**Output**:
```markdown
## Validation Report: bildanov_config.json

### ✅ PASSED (42 checks)
- All variables properly defined
- No nested variables detected
- No dot notation found
- Local scope respected for all stages

### ⚠️ WARNINGS (2)
1. **Unused variable in Welcome stage:**
   - Variable: `old_company_name`
   - Defined but not used in prompt
   - **Action**: Remove from variables section

2. **Unused variable in Qualification stage:**
   - Variable: `deprecated_field`
   - Defined but not used
   - **Action**: Remove

### 🔧 Recommended Cleanup:
```json
// Remove these lines:
stages.Welcome.system_prompt.variables.old_company_name
stages.Qualification.system_prompt.variables.deprecated_field
```

---

### Example 3: Fix Nested Variable Error
**Context**: Config has invalid nested variable (variable referencing another variable)

**Input**:
```json
{
  "variables": {
    "company": "Dental Clinic",
    "greeting": "Welcome to {company}"  // INVALID!
  }
}
```

**Workflow**:
1. Detect nested variable pattern: `{company}` inside value of `greeting`
2. Explain why it's invalid (parser doesn't substitute)
3. Suggest fix: flatten the structure

**Output**:
```markdown
❌ ERROR: Nested variable detected

**Location:** stages.Welcome.system_prompt.variables.greeting
**Problem:** Variable "greeting" contains "{company}" reference
**Why invalid:** Parser does NOT support variable nesting

**Current (INVALID):**
```json
{
  "company": "Dental Clinic",
  "greeting": "Welcome to {company}"
}
```

**Fix Option 1 - Flatten (recommended):**
```json
{
  "company": "Dental Clinic",
  "greeting": "Welcome to Dental Clinic"
}
```

**Fix Option 2 - Use directly in prompt:**
Remove `greeting` variable and use in prompt:
```
"prompt": "Welcome to {company}! ..."
```

**Action**: Apply Fix Option 2 (cleaner)
```

---

### Example 4: Detect Cross-Stage Variable Reference
**Context**: Variable from Welcome stage used in Qualification stage

**Input**:
```json
{
  "stages": {
    "Welcome": {
      "system_prompt": {
        "variables": {"company_name": "Clinic"}
      }
    },
    "Qualification": {
      "system_prompt": {
        "prompt": "At {company_name}, we...",  // INVALID!
        "variables": {}
      }
    }
  }
}
```

**Workflow**:
1. Detect `{company_name}` in Qualification prompt
2. Check if exists in Qualification.variables (NO)
3. Check if exists in other stages (YES - Welcome)
4. Identify as cross-stage reference violation

**Output**:
```markdown
❌ ERROR: Cross-stage variable reference

**Location:** stages.Qualification.system_prompt.prompt
**Variable:** {company_name}
**Problem:** Variable defined in Welcome stage, used in Qualification

**Why invalid:** Variables are stage-local, NOT shared across stages

**Fix:** Duplicate variable to Qualification stage
```json
{
  "stages": {
    "Qualification": {
      "system_prompt": {
        "prompt": "At {company_name}, we...",
        "variables": {
          "company_name": "Clinic"  // Duplicate here
        }
      }
    }
  }
}
```

**Action**: Duplicated variable to Qualification.variables
```

---

## Workflow

### Core Validation Algorithm

```
INPUT: config_file_path

STEP 1: LOAD AND PARSE
  ├─ Read JSON file
  ├─ Parse structure
  └─ Validate JSON syntax

STEP 2: EXTRACT VARIABLES
  For each stage in stages:
    ├─ Extract prompt text
    ├─ Find all {variable} patterns using regex: \{([a-zA-Z0-9_]+)\}
    ├─ Extract variables section (key-value pairs)
    └─ Store mapping: {stage: {references: [], definitions: []}}

STEP 3: VALIDATE VARIABLE SYNTAX
  For each variable reference:
    ├─ Check format: {variable_name} (no dots, no brackets inside)
    ├─ Check exists in SAME stage's variables
    └─ Report missing variables

STEP 4: DETECT NESTED VARIABLES
  For each variable value:
    ├─ Check if contains {anything} pattern
    ├─ If YES → VIOLATION (nested variable)
    └─ Report with fix suggestions

STEP 5: DETECT DOT NOTATION
  For each variable reference:
    ├─ Check if contains dots: {var.property}
    ├─ If YES → VIOLATION (dot notation not supported)
    └─ Report with fix suggestions

STEP 6: DETECT UNUSED VARIABLES
  For each stage:
    ├─ Compare definitions vs references
    ├─ Find defined but not referenced
    └─ Report for cleanup

STEP 7: VALIDATE SCHEMA
  ├─ Check required fields: company_name, router, stages, etc.
  ├─ Check stage structure: enabled, model, system_prompt, required_fields
  └─ Check system_prompt structure: prompt, variables

STEP 8: GENERATE REPORT
  ├─ Summary: passed/warnings/errors
  ├─ Detailed findings with locations
  ├─ Fix suggestions (code snippets)
  └─ Cleanup recommendations

OUTPUT: Validation report (markdown)
```

---

### Variable Cleanup Algorithm

```
TRIGGER: After ANY edit to config file

STEP 1: IDENTIFY SCOPE
  ├─ Which stage was edited?
  └─ Focus on that stage's variables

STEP 2: EXTRACT REFERENCES
  ├─ Read prompt text for edited stage
  ├─ Find all {variable} patterns
  └─ Create list: referenced_vars = [...]

STEP 3: EXTRACT DEFINITIONS
  ├─ Read variables section for edited stage
  └─ Create list: defined_vars = [...]

STEP 4: FIND UNUSED
  unused = defined_vars - referenced_vars

STEP 5: REMOVE UNUSED
  For each var in unused:
    ├─ Remove from variables section
    └─ Log removal

STEP 6: REPORT
  "Cleaned up N unused variables: [list]"
```

---

## Integration with Other Skills

- **config-parser-rules** - Reference for validation rules and examples
  - Use when explaining WHY something is invalid
  - Link to specific rule in checklist

- **config-templates** - Use when creating new configs
  - Start with template
  - Apply validation rules
  - Ensure compliance

## Best Practices

### 1. Always Validate After Edit
❌ BAD: Edit config → save → done
✅ GOOD: Edit config → run validation → fix issues → save

### 2. Run Cleanup After Every Edit
❌ BAD: Add variable → move on
✅ GOOD: Add variable → run cleanup algorithm → remove unused vars

### 3. Provide Fix Suggestions, Not Just Errors
❌ BAD: "Error: nested variable detected"
✅ GOOD: "Error: nested variable detected. Fix: [code snippet with correct version]"

### 4. Validate Scope Before Suggesting Fixes
❌ BAD: "Add this variable to variables section" (without checking stage)
✅ GOOD: "Add this variable to stages.Welcome.system_prompt.variables section"

### 5. Explain Parser Behavior
❌ BAD: "Don't use nested variables" (no context)
✅ GOOD: "Parser doesn't support nested variables because it performs single-pass substitution"

## Troubleshooting

### Problem: "Variable {X} not found but it exists in config"
**Cause**: Variable defined in DIFFERENT stage (cross-stage reference)
**Solution**:
1. Identify which stage has the variable
2. Duplicate it to the stage where it's used
3. Explain: "Variables are stage-local, must be duplicated"

---

### Problem: "Validation passes but config still breaks at runtime"
**Cause**: Pydantic schema violation (missing required field)
**Solution**:
1. Check schema structure:
   - `company_name` present?
   - `router` structure correct?
   - All stages have `enabled` flag?
   - All `system_prompt` objects have `prompt` field?
2. Validate against Pydantic schema rules

---

### Problem: "How to share variable across all stages?"
**Answer**:
- Parser does NOT support global variables
- **Solution**: Duplicate variable to each stage that needs it
- Example: `company_name` appears in Welcome, Qualification, Core_Product → define it 3 times

---

### Problem: "User wants to use pricing rules as object"
**Context**: User wants `{pricing.basic}` or `{prices[0]}`
**Answer**:
- ❌ NOT supported by parser (no dot notation, no array access)
- ✅ Solution: Flatten into separate variables:
  ```json
  "variables": {
    "price_basic": "1000",
    "price_premium": "2000",
    "price_vip": "3000"
  }
  ```
- Use in prompt: `{price_basic}`, `{price_premium}`, `{price_vip}`

## Variable Syntax Reference

### ✅ VALID Syntax

```json
{
  "prompt": "Welcome to {company_name}! {greeting}",
  "variables": {
    "company_name": "Dental Clinic",
    "greeting": "We are glad to see you"
  }
}
```

**Rules:**
- Simple flat variable names: `{company_name}`
- Only alphanumeric and underscores: `{price_2024}`
- Defined in same stage's `variables` section

---

### ❌ INVALID Syntax

#### Nested Variables
```json
// WRONG
{
  "variables": {
    "company": "Clinic",
    "greeting": "Welcome to {company}"  // Parser won't substitute {company}
  }
}
```

#### Dot Notation
```json
// WRONG
{
  "prompt": "Price: {pricing.basic}",  // Dots not supported
  "variables": {
    "pricing": {"basic": "1000"}
  }
}
```

#### Array Access
```json
// WRONG
{
  "prompt": "Name: {users[0].name}",  // Brackets not supported
  "variables": {
    "users": [{"name": "John"}]
  }
}
```

#### Cross-Stage Reference
```json
// WRONG
{
  "stages": {
    "Welcome": {
      "system_prompt": {
        "variables": {"company": "Clinic"}
      }
    },
    "Qualification": {
      "system_prompt": {
        "prompt": "{company}",  // Not accessible here!
        "variables": {}
      }
    }
  }
}
```

## Validation Checklist

Execute this checklist for EVERY config validation:

- [ ] **JSON Syntax**: File parses correctly as JSON
- [ ] **Schema Structure**: Has required top-level fields (company_name, router, stages)
- [ ] **Variable References**: All `{variable}` exist in SAME stage's `variables`
- [ ] **Variable Syntax**: Only simple flat names (no dots, brackets, special chars except _)
- [ ] **No Nesting**: No `{var}` patterns inside variable values
- [ ] **No Dot Notation**: No `{var.property}` patterns
- [ ] **Local Scope**: No cross-stage variable references
- [ ] **Unused Variables**: All defined variables are used in prompt
- [ ] **Stage Structure**: Each stage has `enabled`, `model`, `system_prompt`, `required_fields`
- [ ] **System Prompt**: Each has `prompt` (string) and optional `variables` (object)

## Version History
- **2026-02-11**: Created for config-editor agent - comprehensive validation skill for sales funnel configs
