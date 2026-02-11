# Config Parser Rules Skill

## Overview
**Purpose**: Reference guide for sales funnel config parser rules and limitations
**Target Users**: Config Editor agent
**Capabilities**:
- Quick rule lookup
- Examples of correct/incorrect usage
- Common mistake patterns
- Parser behavior explanation

## Required Tools
- `Read` - Read this reference file (no external tools needed)

## Usage

This is a **REFERENCE SKILL** - use it when:
1. Explaining WHY a config pattern is invalid
2. Providing examples of correct usage
3. Troubleshooting parser errors
4. Educating users about parser limitations

**Example invocation**:
```
"Check config-parser-rules skill for variable nesting examples"
→ Returns section on nested variables with ✅/❌ examples
```

---

## Parser Rules

### Rule #1: Variable Syntax - Curly Braces Only

**RULE**: Variables MUST use `{variable_name}` syntax

✅ **CORRECT:**
```json
{
  "prompt": "Welcome to {company_name}!",
  "variables": {
    "company_name": "Dental Clinic"
  }
}
```

❌ **INCORRECT:**
```json
// Wrong - dollar sign syntax
{
  "prompt": "Welcome to $company_name!"
}

// Wrong - percent syntax
{
  "prompt": "Welcome to %company_name%!"
}

// Wrong - double brackets
{
  "prompt": "Welcome to {{company_name}}!"
}
```

**Parser Behavior**: Only recognizes `{variable_name}` pattern. Other syntaxes treated as literal text.

---

### Rule #2: Variable Names - Alphanumeric and Underscores Only

**RULE**: Variable names: `[a-zA-Z0-9_]+` (letters, numbers, underscores)

✅ **CORRECT:**
```
{company_name}
{price_2024}
{service_type_1}
{COMPANY}
```

❌ **INCORRECT:**
```
{company-name}     // Hyphen not allowed
{company.name}     // Dot not allowed
{company name}     // Space not allowed
{company@name}     // Special chars not allowed
{company[0]}       // Brackets not allowed
```

**Parser Behavior**: Invalid chars → variable not recognized → treated as literal text.

---

### Rule #3: Local Scope - Stage-Level Variables

**RULE**: Variables defined in one stage are NOT visible to other stages

✅ **CORRECT:**
```json
{
  "stages": {
    "Welcome": {
      "system_prompt": {
        "prompt": "Welcome to {company}!",
        "variables": {
          "company": "Clinic"
        }
      }
    },
    "Qualification": {
      "system_prompt": {
        "prompt": "At {company}, we offer...",
        "variables": {
          "company": "Clinic"  // Duplicate - required!
        }
      }
    }
  }
}
```

❌ **INCORRECT:**
```json
{
  "stages": {
    "Welcome": {
      "system_prompt": {
        "variables": {
          "company": "Clinic"
        }
      }
    },
    "Qualification": {
      "system_prompt": {
        "prompt": "At {company}, we offer...",  // ERROR!
        "variables": {}  // {company} not defined here!
      }
    }
  }
}
```

**Parser Behavior**: Each stage processes variables independently. Cross-stage references → variable not found → treated as literal `{company}`.

**Solution**: Duplicate shared variables to each stage that needs them.

---

### Rule #4: No Variable Nesting

**RULE**: Variable values CANNOT contain other variable references

✅ **CORRECT:**
```json
{
  "prompt": "Welcome to {company_name}! {greeting_message}",
  "variables": {
    "company_name": "Dental Clinic",
    "greeting_message": "We are here to help"
  }
}
```

❌ **INCORRECT:**
```json
{
  "variables": {
    "company": "Dental Clinic",
    "greeting": "Welcome to {company}!"  // NESTING - invalid!
  }
}
```

**Why Invalid**: Parser performs single-pass substitution. Doesn't re-parse variable values.

**Parser Behavior**: Variable value `"Welcome to {company}!"` inserted AS-IS into prompt. The `{company}` inside remains literal text.

**Output**: `"Welcome to {company}!"` (literal, not substituted)

**Solution - Option 1**: Use both variables in prompt
```json
{
  "prompt": "Welcome to {company}! {greeting}",
  "variables": {
    "company": "Dental Clinic",
    "greeting": "We are here to help"
  }
}
```

**Solution - Option 2**: Flatten the value
```json
{
  "variables": {
    "greeting": "Welcome to Dental Clinic! We are here to help"
  }
}
```

---

### Rule #5: No Dot Notation (Object Properties)

**RULE**: Dot notation NOT supported (`{object.property}` is invalid)

✅ **CORRECT:**
```json
{
  "prompt": "Price: {price_basic}",
  "variables": {
    "price_basic": "1000",
    "price_premium": "2000"
  }
}
```

❌ **INCORRECT:**
```json
{
  "prompt": "Price: {pricing.basic}",
  "variables": {
    "pricing": {
      "basic": "1000",
      "premium": "2000"
    }
  }
}
```

**Why Invalid**: Parser only recognizes flat variable names. Dot treated as part of variable name → lookup fails.

**Parser Behavior**: Looks for variable named `"pricing.basic"` (literal string with dot) → not found → treated as literal text `{pricing.basic}`.

**Solution**: Flatten object into separate variables
```json
{
  "variables": {
    "pricing_basic": "1000",
    "pricing_premium": "2000"
  }
}
```

---

### Rule #6: No Array/Index Access

**RULE**: Array indexing NOT supported (`{array[0]}`, `{list[index]}`)

✅ **CORRECT:**
```json
{
  "prompt": "Service: {service_1}, {service_2}",
  "variables": {
    "service_1": "Consultation",
    "service_2": "Surgery"
  }
}
```

❌ **INCORRECT:**
```json
{
  "prompt": "Service: {services[0]}",
  "variables": {
    "services": ["Consultation", "Surgery"]
  }
}
```

**Why Invalid**: Parser doesn't support array syntax.

**Parser Behavior**: Looks for variable `"services[0]"` (literal with brackets) → not found → literal text.

**Solution**: Flatten array into indexed variables
```json
{
  "variables": {
    "services_0": "Consultation",
    "services_1": "Surgery"
  }
}
```

---

### Rule #7: All Variables Must Be Defined

**RULE**: Every `{variable}` in prompt MUST exist in SAME stage's `variables` section

✅ **CORRECT:**
```json
{
  "prompt": "Contact {company_name} at {phone}",
  "variables": {
    "company_name": "Clinic",
    "phone": "+7 (999) 123-45-67"
  }
}
```

❌ **INCORRECT:**
```json
{
  "prompt": "Contact {company_name} at {phone}",
  "variables": {
    "company_name": "Clinic"
    // {phone} missing!
  }
}
```

**Parser Behavior**: Undefined variable → treated as literal text `{phone}`.

**Output**: `"Contact Clinic at {phone}"` (not substituted)

---

### Rule #8: Unused Variables Should Be Removed

**RULE**: Variables defined but not used in prompt = code smell, should be cleaned up

✅ **GOOD:**
```json
{
  "prompt": "Welcome to {company}!",
  "variables": {
    "company": "Clinic"
  }
  // All variables used ✅
}
```

⚠️ **ACCEPTABLE BUT SUBOPTIMAL:**
```json
{
  "prompt": "Welcome to {company}!",
  "variables": {
    "company": "Clinic",
    "old_greeting": "Hello"  // Defined but not used
  }
}
```

**Why Clean Up**:
- Reduces config file bloat
- Prevents confusion (is it used somewhere?)
- Improves maintainability

**Action**: After ANY edit, run cleanup algorithm to remove unused variables.

---

## Common Mistake Patterns

### Mistake #1: Copy-Paste from Different Stage

**Scenario**: User copies prompt from Welcome to Qualification, forgets to copy variables.

**Result**:
```json
{
  "stages": {
    "Welcome": {
      "system_prompt": {
        "prompt": "Welcome to {company}!",
        "variables": {"company": "Clinic"}
      }
    },
    "Qualification": {
      "system_prompt": {
        "prompt": "Welcome to {company}!",  // Copied prompt
        "variables": {}  // Forgot to copy variables!
      }
    }
  }
}
```

**Fix**: Copy variables too, or reference config-templates skill for complete stage template.

---

### Mistake #2: Trying to Use Global Variables

**Scenario**: User defines variable once, expects it to work everywhere.

**Result**:
```json
{
  "global_variables": {  // NO SUCH THING!
    "company": "Clinic"
  },
  "stages": {
    "Welcome": {
      "system_prompt": {
        "prompt": "{company}",  // Won't work
        "variables": {}
      }
    }
  }
}
```

**Fix**: No global variables. Duplicate to each stage.

---

### Mistake #3: Using Programming Language Variable Syntax

**Scenario**: User familiar with Python/JS tries to use those syntaxes.

**Result**:
```
f"{company_name}"     # Python f-string - WRONG
${company_name}       # JS template literal - WRONG
%{company_name}s      # Python % formatting - WRONG
{{company_name}}      # Double braces - WRONG
```

**Fix**: Only `{variable_name}` works.

---

### Mistake #4: Assuming Smart Parsing

**Scenario**: User expects parser to handle complex logic.

**Result**:
```json
{
  "variables": {
    "price": "1000",
    "price_with_discount": "{price} * 0.9"  // NO MATH!
  }
}
```

**Parser Reality**: Outputs literal `"{price} * 0.9"` (no evaluation).

**Fix**: Pre-calculate values
```json
{
  "variables": {
    "price": "1000",
    "price_with_discount": "900"
  }
}
```

---

## Quick Troubleshooting Guide

### Symptom: Variable shows as `{variable_name}` in output (literal text)

**Possible Causes:**
1. Variable not defined in `variables` section → **Add it**
2. Variable defined in different stage → **Duplicate to current stage**
3. Typo in variable name (prompt: `{companyName}` vs variables: `{company_name}`) → **Fix typo**
4. Invalid variable name syntax (dots, brackets, special chars) → **Use only alphanumeric + underscores**

---

### Symptom: Variable value contains another variable reference

**Cause**: Nested variable (Rule #4 violation)

**Fix**:
- Option 1: Use both in prompt
- Option 2: Flatten value

**Example**:
```json
// BEFORE (wrong)
{"greeting": "Welcome to {company}!"}

// AFTER - Option 1
{"prompt": "Welcome to {company}! {greeting}"}

// AFTER - Option 2
{"greeting": "Welcome to Dental Clinic!"}
```

---

### Symptom: Variable with dots/brackets not working

**Cause**: Dot notation (Rule #5) or array access (Rule #6) not supported

**Fix**: Flatten structure
```json
// BEFORE
{"pricing": {"basic": "1000"}}

// AFTER
{"pricing_basic": "1000"}
```

---

## Parser Implementation Notes

**How Parser Works (Conceptual Model):**

```
1. Load config JSON
2. For each stage:
   a. Load stage's system_prompt.prompt (string)
   b. Load stage's system_prompt.variables (dict)
   c. For each variable in dict:
      - Find pattern {variable_name} in prompt
      - Replace with variable value (string substitution)
   d. Output final prompt text
3. NO re-parsing of variable values
4. NO cross-stage lookups
5. NO complex expressions/logic
```

**Key Limitation**: Single-pass string substitution only. No evaluation, no nesting, no complex logic.

---

## Schema Validation Rules

Beyond variable rules, config must match Pydantic schema:

### Required Top-Level Fields
```json
{
  "agent_name": "string",
  "config": {
    "company_name": "string",
    "router": { ... },
    "stages": { ... },
    "human_handoff": { ... },
    "state": { ... }
  }
}
```

### Stage Structure
```json
{
  "StageName": {
    "enabled": true,  // boolean required
    "model": "string",
    "stage_config": { ... },
    "system_prompt": {
      "prompt": "string",  // required
      "variables": {}  // optional
    },
    "required_fields": { ... }
  }
}
```

### System Prompt Structure
```json
{
  "system_prompt": {
    "prompt": "string with {variables}",
    "variables": {
      "variable_name": "string value"
    }
  }
}
```

---

## Version History
- **2026-02-11**: Created for config-editor agent - comprehensive parser rules reference
