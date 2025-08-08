# Goose Desktop Configuration Examples

## 🎯 Environment Variable Setup for Different Developer Profiles

### **New Developer (6 months experience) - GUIDED Learning**

Add this to your Goose Desktop Extensions configuration:

```yaml
extensions:
  mentor-mode:
    args:
    - -m
    - mentor_mcp.server
    bundled: null
    cmd: python3
    description: AI-powered learning mentorship for guided development experiences
    enabled: true
    env_keys: []
    envs:
      PYTHONPATH: /Users/jeuston/SOURCE/goose-mentor-mode/src:/Users/jeuston/SOURCE/goose-mentor-mode/mcp-mentor/src
      # NEW: Environment variable configuration
      DEFAULT_ASSISTANCE_LEVEL: "guided"
      LEARNING_PHASE: "skill_building"
      TIMELINE_PRESSURE: "low"
      ENABLE_VALIDATION_CHECKPOINTS: "true"
      MAX_GUIDANCE_DEPTH: "5"
      DEFAULT_SKILL_LEVEL: "1"
      DEVELOPER_EXPERIENCE_MONTHS: "6"
    name: mentor-mode
    timeout: 300
    type: stdio
    cwd: /Users/jeuston/SOURCE/goose-mentor-mode
```

### **Experienced Developer (Production Mode) - ASSISTED**

```yaml
extensions:
  mentor-mode:
    envs:
      PYTHONPATH: /Users/jeuston/SOURCE/goose-mentor-mode/src:/Users/jeuston/SOURCE/goose-mentor-mode/mcp-mentor/src
      DEFAULT_ASSISTANCE_LEVEL: "assisted"
      LEARNING_PHASE: "production"
      TIMELINE_PRESSURE: "medium"
      ENABLE_VALIDATION_CHECKPOINTS: "false"
      DEFAULT_SKILL_LEVEL: "4"
      DEVELOPER_EXPERIENCE_MONTHS: "36"
```

### **Learning Session Mode - EXPLAINED with Maximum Education**

```yaml
extensions:
  mentor-mode:
    envs:
      PYTHONPATH: /Users/jeuston/SOURCE/goose-mentor-mode/src:/Users/jeuston/SOURCE/goose-mentor-mode/mcp-mentor/src
      DEFAULT_ASSISTANCE_LEVEL: "explained"
      LEARNING_PHASE: "skill_building"
      TIMELINE_PRESSURE: "low"
      FORCE_MENTOR_MODE: "true"           # Always trigger educational responses
      ENABLE_VALIDATION_CHECKPOINTS: "true"
      MAX_GUIDANCE_DEPTH: "5"
```

### **Emergency/Deadline Mode - AUTOMATED**

```yaml
extensions:
  mentor-mode:
    envs:
      PYTHONPATH: /Users/jeuston/SOURCE/goose-mentor-mode/src:/Users/jeuston/SOURCE/goose-mentor-mode/mcp-mentor/src
      DEFAULT_ASSISTANCE_LEVEL: "automated"
      LEARNING_PHASE: "production"
      TIMELINE_PRESSURE: "high"
      ENABLE_VALIDATION_CHECKPOINTS: "false"
      MAX_GUIDANCE_DEPTH: "1"
```

## 🔧 How to Apply Configuration

### **Method 1: Goose Desktop UI**
1. Open Goose Desktop
2. Go to Settings → Extensions
3. Find "mentor-mode" extension
4. Click Edit/Configure
5. Add environment variables to the `envs` section

### **Method 2: Direct Config File Edit**
1. Locate your Goose config file (usually `~/.config/goose/config.yaml`)
2. Find the `extensions` → `mentor-mode` section
3. Add/modify the `envs` section with your desired variables

## 🧪 Testing Your Configuration

After applying configuration, test it with these requests:

### **Test GUIDED Mode:**
```
"How do I implement JWT authentication in my API?"
```
**Expected**: Socratic questions that guide you to discover the solution

### **Test EXPLAINED Mode:**
```
"Explain how to set up error handling in Express.js"
```
**Expected**: Detailed educational explanation with step-by-step reasoning

### **Test ASSISTED Mode:**
```
"I need to add input validation to this endpoint quickly"
```
**Expected**: Quick solution with key insights highlighted

### **Test AUTOMATED Mode:**
```
"Fix this syntax error in my JavaScript code"
```
**Expected**: Direct solution with minimal educational overhead

## 🎯 Configuration Reference

| Variable | Purpose | Values | Best For |
|----------|---------|--------|----------|
| `DEFAULT_ASSISTANCE_LEVEL` | Override automatic selection | `guided`, `explained`, `assisted`, `automated` | Setting consistent learning experience |
| `LEARNING_PHASE` | Developer's learning stage | `onboarding`, `skill_building`, `production` | Matching educational depth to experience |
| `TIMELINE_PRESSURE` | Project pressure level | `low`, `medium`, `high` | Balancing learning vs. delivery speed |
| `FORCE_MENTOR_MODE` | Always provide education | `true`, `false` | Dedicated learning sessions |
| `ENABLE_VALIDATION_CHECKPOINTS` | Learning validation questions | `true`, `false` | Ensuring concept understanding |
| `MAX_GUIDANCE_DEPTH` | Learning depth levels | `1`-`5` | Controlling complexity of guidance |

## ✅ Validation Checklist

After configuring, verify:

- [ ] Environment variables appear in mentor tool responses (`config_applied` section)
- [ ] Assistance level matches your configuration
- [ ] Learning phase and timeline pressure are correctly detected
- [ ] Validation checkpoints enabled/disabled as configured
- [ ] Force mentor mode working if enabled

## 🚀 Quick Start for Your New Developer

**Copy this exact configuration for a 6-month developer:**

```yaml
envs:
  PYTHONPATH: /Users/jeuston/SOURCE/goose-mentor-mode/src:/Users/jeuston/SOURCE/goose-mentor-mode/mcp-mentor/src
  DEFAULT_ASSISTANCE_LEVEL: "guided"
  LEARNING_PHASE: "skill_building"
  TIMELINE_PRESSURE: "low"
  ENABLE_VALIDATION_CHECKPOINTS: "true"
  MAX_GUIDANCE_DEPTH: "4"
  DEFAULT_SKILL_LEVEL: "1"
  DEVELOPER_EXPERIENCE_MONTHS: "6"
```

This will provide maximum learning benefit with guided discovery and validation checkpoints! 🎯
