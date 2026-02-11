# Config Templates Skill

## Overview
**Purpose**: Ready-to-use templates for creating new sales funnel configuration files
**Target Users**: Config Editor agent
**Capabilities**:
- New config scaffolding
- Stage templates (Welcome, Qualification, Core_Product, etc.)
- Common variable patterns
- Best practice examples

## Required Tools
- `Write` - Create new config files from templates
- `Edit` - Insert templates into existing configs

## Usage

**When to use this skill:**
1. Creating a new sales funnel config from scratch
2. Adding a new stage to existing config
3. Need examples of correct variable usage
4. Setting up common patterns (pricing, contact info, etc.)

**Example invocations:**
```
"Use config-templates skill to create new config for dental clinic"
→ Returns full config template with placeholder values

"Use config-templates skill to add Warming stage"
→ Returns Warming stage template ready to insert
```

---

## Full Config Template

### Minimal Sales Funnel Config

```json
{
  "agent_name": "AGENT_NAME_HERE",
  "config": {
    "company_name": "COMPANY_NAME_HERE",
    "router": {
      "model": "gpt-5-nano",
      "required_fields": {
        "intents": {
          "type": "List[str]",
          "description": "Possible user intents: 'ask_price', 'ready_to_buy', 'general_question', 'objection'"
        },
        "temperature": {
          "type": "Literal[cold|warm|hot]",
          "description": "Lead temperature based on buying signals"
        },
        "engagement_score": {
          "type": "float",
          "description": "Engagement level 0.0-10.0"
        },
        "stage": {
          "type": "Literal[Welcome|Qualification|Core_Product|human_handoff]",
          "description": "Next stage to route to"
        }
      },
      "system_prompt": {
        "prompt": "You are a sales funnel router. Analyze conversation and route to appropriate stage.\n\nEnabled stages: {enabled_stages}\n\nRouting rules:\n{routing_rules}",
        "variables": {
          "enabled_stages": "Welcome, Qualification, Core_Product, human_handoff",
          "routing_rules": "Welcome → Qualification (when name collected)\nQualification → Core_Product (when qualified)\nCore_Product → human_handoff (when ready)"
        }
      }
    },
    "stages": {
      "Welcome": {
        "enabled": true,
        "model": "gpt-5-nano",
        "stage_config": {
          "required_fields_to_collect": ["name"],
          "exit_to_stage": "Qualification"
        },
        "system_prompt": {
          "prompt": "Welcome to {company_name}! I'm your virtual assistant.\n\n{greeting_message}\n\nHow may I address you?",
          "variables": {
            "company_name": "COMPANY_NAME_HERE",
            "greeting_message": "We're here to help you with your questions."
          }
        },
        "required_fields": {
          "response_to_user": {
            "type": "str",
            "description": "Greeting + name request. MAX 3 sentences."
          },
          "name": {
            "type": "str",
            "description": "User's first name"
          }
        }
      },
      "Qualification": {
        "enabled": true,
        "model": "gpt-5-chat-latest",
        "stage_config": {
          "required_fields_to_collect": ["timeline", "pain_points"],
          "exit_to_stage": "Core_Product"
        },
        "system_prompt": {
          "prompt": "You are qualifying the lead for {company_name}.\n\nGoals:\n{qualification_goals}\n\nQuestions to ask:\n{qualification_questions}",
          "variables": {
            "company_name": "COMPANY_NAME_HERE",
            "qualification_goals": "- Understand customer needs\n- Identify pain points\n- Determine timeline\n- Assess budget (if relevant)",
            "qualification_questions": "1. What problem are you trying to solve?\n2. When do you need a solution?\n3. What have you tried before?"
          }
        },
        "required_fields": {
          "response_to_user": {
            "type": "str",
            "description": "Qualification question"
          },
          "timeline": {
            "type": "str",
            "description": "When customer needs solution"
          },
          "pain_points": {
            "type": "List[str]",
            "description": "Customer problems/goals"
          }
        }
      },
      "Core_Product": {
        "enabled": true,
        "model": "gpt-5-chat-latest",
        "stage_config": {
          "required_fields_to_collect": ["client_full_name", "client_phone"],
          "exit_to_stage": "human_handoff"
        },
        "system_prompt": {
          "prompt": "Present {company_name} solution to customer.\n\nProduct benefits:\n{product_benefits}\n\nPricing:\n{pricing_info}\n\nNext steps:\n{next_steps}",
          "variables": {
            "company_name": "COMPANY_NAME_HERE",
            "product_benefits": "- Benefit 1: [describe]\n- Benefit 2: [describe]\n- Benefit 3: [describe]",
            "pricing_info": "Starting from [PRICE] [CURRENCY]",
            "next_steps": "1. Collect contact info\n2. Transfer to manager"
          }
        },
        "required_fields": {
          "response_to_user": {
            "type": "str",
            "description": "Product presentation"
          },
          "client_full_name": {
            "type": "str",
            "description": "Customer full name"
          },
          "client_phone": {
            "type": "str",
            "description": "Customer phone number"
          }
        }
      },
      "human_handoff": {
        "enabled": true,
        "model": "gpt-5-nano",
        "stage_config": {},
        "system_prompt": {
          "prompt": "Thank customer and confirm manager will contact them.\n\n{handoff_message}",
          "variables": {
            "handoff_message": "Thank you! Our manager will contact you within 24 hours at {client_phone}."
          }
        },
        "required_fields": {
          "response_to_user": {
            "type": "str",
            "description": "Handoff confirmation message"
          }
        }
      }
    }
  }
}
```

**Placeholders to replace:**
- `AGENT_NAME_HERE` - unique agent identifier
- `COMPANY_NAME_HERE` - company name
- `[describe]` - benefit descriptions
- `[PRICE]` - actual price
- `[CURRENCY]` - currency (USD, EUR, RUB, etc.)

---

## Stage Templates

### Welcome Stage Template

```json
{
  "Welcome": {
    "enabled": true,
    "model": "gpt-5-nano",
    "stage_config": {
      "required_fields_to_collect": ["name"],
      "exit_to_stage": "Qualification"
    },
    "system_prompt": {
      "prompt": "Welcome to {company_name}!\n\n{greeting}\n\nHow may I address you?",
      "variables": {
        "company_name": "YOUR_COMPANY",
        "greeting": "I'm your virtual assistant, here to help."
      }
    },
    "required_fields": {
      "response_to_user": {
        "type": "str",
        "description": "Greeting + name request"
      },
      "name": {
        "type": "str",
        "description": "User's first name"
      }
    }
  }
}
```

**Key Variables:**
- `company_name` - used in greeting
- `greeting` - customizable welcome message

---

### Qualification Stage Template

```json
{
  "Qualification": {
    "enabled": true,
    "model": "gpt-5-chat-latest",
    "stage_config": {
      "required_fields_to_collect": ["timeline", "pain_points", "budget"],
      "exit_to_stage": "Core_Product"
    },
    "system_prompt": {
      "prompt": "You are qualifying leads for {company_name}.\n\nAsk about:\n{qualification_checklist}\n\nCurrent conversation: {conversation_context}",
      "variables": {
        "company_name": "YOUR_COMPANY",
        "qualification_checklist": "- Customer needs\n- Timeline\n- Budget range\n- Decision makers",
        "conversation_context": "Customer expressed interest in [TOPIC]"
      }
    },
    "required_fields": {
      "response_to_user": {
        "type": "str",
        "description": "Qualification question"
      },
      "timeline": {
        "type": "str",
        "description": "Urgency: urgent/this_month/exploring"
      },
      "pain_points": {
        "type": "List[str]",
        "description": "Customer problems (min 1 element)"
      },
      "budget": {
        "type": "str",
        "description": "Budget range or 'not_mentioned'"
      }
    }
  }
}
```

---

### Warming Stage Template (Optional)

```json
{
  "Warming": {
    "enabled": false,
    "model": "gpt-5-chat-latest",
    "stage_config": {
      "max_iterations": 3,
      "exit_to_stage": "Core_Product"
    },
    "system_prompt": {
      "prompt": "Warm up the lead with value propositions.\n\n{value_props}\n\nAddressing objections:\n{objection_handling}",
      "variables": {
        "value_props": "- Social proof: [testimonials]\n- Case studies: [examples]\n- Benefits: [list]",
        "objection_handling": "Common objections and responses"
      }
    },
    "required_fields": {
      "response_to_user": {
        "type": "str",
        "description": "Warming message with value prop"
      },
      "client_wants_details": {
        "type": "bool",
        "description": "Did customer request more info?"
      }
    }
  }
}
```

---

### Core_Product Stage Template

```json
{
  "Core_Product": {
    "enabled": true,
    "model": "gpt-5-chat-latest",
    "stage_config": {
      "required_fields_to_collect": ["client_full_name", "client_phone"],
      "exit_to_stage": "human_handoff"
    },
    "system_prompt": {
      "prompt": "Present {product_name} from {company_name}.\n\nKey features:\n{features}\n\nPricing:\n{pricing}\n\nCall to action:\n{cta}",
      "variables": {
        "company_name": "YOUR_COMPANY",
        "product_name": "YOUR_PRODUCT",
        "features": "- Feature 1\n- Feature 2\n- Feature 3",
        "pricing": "From {price_start} to {price_end}",
        "price_start": "1000",
        "price_end": "5000",
        "cta": "Ready to proceed? Let me collect your contact info."
      }
    },
    "required_fields": {
      "response_to_user": {
        "type": "str",
        "description": "Product presentation + contact request"
      },
      "client_full_name": {
        "type": "str",
        "description": "Full name (First Last)"
      },
      "client_phone": {
        "type": "str",
        "description": "Phone number with country code"
      }
    }
  }
}
```

---

### Objection_Handler Stage Template (Optional)

```json
{
  "Objection_handler": {
    "enabled": false,
    "model": "gpt-5-chat-latest",
    "stage_config": {
      "return_to_previous": true
    },
    "system_prompt": {
      "prompt": "Handle customer objection professionally.\n\nCommon objections:\n{objection_playbook}\n\nTechniques:\n{handling_techniques}",
      "variables": {
        "objection_playbook": "Price: [response]\nTiming: [response]\nCompetitors: [response]",
        "handling_techniques": "- Acknowledge concern\n- Provide evidence\n- Offer alternatives"
      }
    },
    "required_fields": {
      "response_to_user": {
        "type": "str",
        "description": "Objection response"
      },
      "objection_resolved": {
        "type": "bool",
        "description": "Was objection addressed?"
      }
    }
  }
}
```

---

### Knowledge_QA Stage Template (Optional)

```json
{
  "Knowledge_QA": {
    "enabled": false,
    "model": "gpt-5-chat-latest",
    "stage_config": {
      "return_to_previous": true
    },
    "system_prompt": {
      "prompt": "Answer customer question using knowledge base.\n\nTopic: {question_topic}\n\nAnswer guidelines:\n{answer_guidelines}",
      "variables": {
        "question_topic": "[auto-detected]",
        "answer_guidelines": "- Be concise\n- Cite sources\n- Return to sales flow"
      }
    },
    "required_fields": {
      "response_to_user": {
        "type": "str",
        "description": "Answer to question"
      }
    }
  }
}
```

---

## Common Variable Patterns

### Pattern 1: Company Info

```json
{
  "variables": {
    "company_name": "Acme Corp",
    "company_tagline": "Innovation delivered",
    "company_phone": "+1-800-555-0123",
    "company_email": "hello@acme.com",
    "company_website": "acme.com"
  }
}
```

**Usage in prompt:**
```
Welcome to {company_name} - {company_tagline}!
Contact us: {company_phone} or {company_email}
```

---

### Pattern 2: Pricing Variables

```json
{
  "variables": {
    "price_basic": "$99/month",
    "price_professional": "$199/month",
    "price_enterprise": "$499/month",
    "currency": "USD",
    "payment_terms": "monthly or annual"
  }
}
```

**Usage:**
```
Pricing options:
- Basic: {price_basic}
- Professional: {price_professional}
- Enterprise: {price_enterprise}

We accept {payment_terms} payments in {currency}.
```

---

### Pattern 3: Service Features

```json
{
  "variables": {
    "feature_1": "24/7 customer support",
    "feature_2": "Unlimited storage",
    "feature_3": "Advanced analytics",
    "feature_count": "3"
  }
}
```

**Usage:**
```
Our {feature_count} key features:
1. {feature_1}
2. {feature_2}
3. {feature_3}
```

---

### Pattern 4: Timeline Options

```json
{
  "variables": {
    "timeline_urgent": "within 1 week",
    "timeline_soon": "within 1 month",
    "timeline_exploring": "just researching",
    "timeline_question": "When do you need a solution?"
  }
}
```

**Usage:**
```
{timeline_question}
- {timeline_urgent}
- {timeline_soon}
- {timeline_exploring}
```

---

### Pattern 5: Location/Availability

```json
{
  "variables": {
    "location_1": "Moscow",
    "location_2": "Saint Petersburg",
    "location_3": "Samara",
    "availability": "Monday-Friday 9am-6pm",
    "timezone": "UTC+3"
  }
}
```

**Usage:**
```
We serve: {location_1}, {location_2}, {location_3}
Available: {availability} ({timezone})
```

---

## Best Practice Examples

### Example 1: Multi-Language Support

**WRONG** (trying to use conditionals):
```json
{
  "variables": {
    "greeting": "if (lang == 'en') 'Hello' else 'Привет'"
  }
}
```

**RIGHT** (separate variables):
```json
{
  "variables": {
    "greeting_en": "Hello",
    "greeting_ru": "Привет",
    "greeting": "Привет"
  }
}
```

Use `greeting` for current language. Switch manually when needed.

---

### Example 2: Reusable Text Blocks

```json
{
  "variables": {
    "disclaimer": "Results may vary. Consult with specialist.",
    "privacy_note": "Your data is protected per GDPR.",
    "response_time": "We respond within 24 hours."
  }
}
```

Append to responses:
```
{main_response}

{disclaimer}
{privacy_note}
```

---

### Example 3: Dynamic Lists

**WRONG** (arrays not supported):
```json
{
  "variables": {
    "services": ["Service A", "Service B", "Service C"]
  }
}
```

**RIGHT** (numbered variables):
```json
{
  "variables": {
    "service_1": "Service A",
    "service_2": "Service B",
    "service_3": "Service C",
    "service_count": "3"
  }
}
```

Usage:
```
We offer {service_count} services:
1. {service_1}
2. {service_2}
3. {service_3}
```

---

## Quick Start Workflow

### Creating New Config from Scratch

**Step 1: Copy Full Config Template**
- Use "Minimal Sales Funnel Config" above
- Save as `YOUR_AGENT_config.json`

**Step 2: Replace Placeholders**
```
AGENT_NAME_HERE → your_agent_name
COMPANY_NAME_HERE → Your Company Name
[PRICE] → actual price
[CURRENCY] → USD/EUR/RUB/etc.
```

**Step 3: Customize Stages**
- Enable/disable stages (`"enabled": true/false`)
- Customize prompts and variables
- Adjust required_fields

**Step 4: Validate**
- Use `config-validation` skill
- Check all rules pass
- Test with sample inputs

---

### Adding New Stage to Existing Config

**Step 1: Choose Stage Template**
- Welcome / Qualification / Warming / Core_Product / etc.

**Step 2: Copy Template**
- Paste into `config.stages` object

**Step 3: Update Router**
- Add stage to router's stage enumeration
- Add routing rules for new stage

**Step 4: Set enabled = true**

**Step 5: Validate**
- Check cross-stage variable references
- Ensure no duplicate stage names

---

## Integration with Other Skills

- **config-validation** - Validate templates before use
  - Run validation after inserting template
  - Ensure compliance with all rules

- **config-parser-rules** - Reference when customizing
  - Check rules before adding complex variables
  - Verify syntax compliance

## Best Practices

### 1. Start with Minimal Template
✅ GOOD: Use minimal template → add stages as needed
❌ BAD: Use complex template → remove unused stages

### 2. Validate After Every Template Insert
✅ GOOD: Insert template → validate → fix issues
❌ BAD: Insert multiple templates → validate once (hard to debug)

### 3. Keep Placeholder Pattern Consistent
✅ GOOD: `COMPANY_NAME_HERE`, `[PRICE]`, `YOUR_COMPANY`
❌ BAD: Mix of styles (harder to find/replace)

### 4. Document Custom Variables
✅ GOOD: Add comments explaining purpose (in separate docs)
❌ BAD: Cryptic variable names without context

### 5. Use Semantic Variable Names
✅ GOOD: `price_basic`, `timeline_urgent`, `feature_support`
❌ BAD: `var1`, `temp`, `x`

## Troubleshooting

### Problem: Template variables conflict with existing config

**Cause**: Same variable name, different value

**Solution**:
1. Rename variables in template before inserting
2. Or merge values if appropriate
3. Use stage-specific prefixes: `welcome_greeting`, `qual_greeting`

---

### Problem: Template has more variables than needed

**Solution**:
1. Insert full template
2. Remove unused variables
3. Run cleanup algorithm (config-validation skill)

---

### Problem: Need template for custom stage type

**Solution**:
1. Use closest existing template (e.g., Knowledge_QA for FAQ)
2. Customize prompt and variables
3. Follow same structure pattern
4. Validate with config-validation skill

## Version History
- **2026-02-11**: Created for config-editor agent - comprehensive template collection for sales funnel configs
