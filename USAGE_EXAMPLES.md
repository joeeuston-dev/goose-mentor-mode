# Goose Mentor Mode - Usage Examples 🎓

This document provides comprehensive examples of how to use Goose Mentor Mode in real development scenarios.

## 🚀 Quick Start Guide

### 1. Installation & Setup

```bash
# Install the package
pip install goose-mentor-mode

# Configure in Goose Desktop
# Go to Settings → Profiles → Add toolkit: mentor (package: goose-mentor-mode)
```

### 2. Basic Usage - No Configuration

Once installed, Mentor Mode automatically analyzes your requests and provides appropriate assistance:

```
You: "How do I implement JWT authentication?"

Goose (with Mentor Mode): 
🎓 Learning Opportunity Detected: Security & Authentication

I notice you're asking about JWT authentication. This is a great learning opportunity! 
Let me guide you through this step by step.

Before I provide the solution, let me ask you a few questions to help you discover the concepts:

1. What do you think JWT stands for, and why might it be useful for authentication?
2. What are the key differences between session-based and token-based authentication?
3. What security considerations should we keep in mind when implementing JWT?

[Continues with Socratic questioning...]
```

## 🎯 Assistance Level Examples

### 🧭 GUIDED Mode (Maximum Learning)

**Configuration:**
```bash
DEFAULT_ASSISTANCE_LEVEL=guided
LEARNING_PHASE=onboarding
ENABLE_VALIDATION_CHECKPOINTS=true
```

**Example Interaction:**
```
You: "I need to add error handling to my Express.js API"

Goose: 🎓 GUIDED Learning Mode Activated

Great question! Error handling is crucial for robust APIs. Let's explore this together.

First, let me ask you some discovery questions:

1. What types of errors do you think might occur in an API?
2. How do you think users should receive error information?
3. What's the difference between operational errors and programmer errors?

Think about these, and then tell me what you discover. This will help you build a deeper understanding of error handling patterns.

Once you've thought through these concepts, I'll guide you through implementing a comprehensive error handling strategy.
```

### 📚 EXPLAINED Mode (Education + Solution)

**Configuration:**
```bash
DEFAULT_ASSISTANCE_LEVEL=explained
LEARNING_PHASE=skill_building
TIMELINE_PRESSURE=medium
```

**Example Interaction:**
```
You: "Help me set up input validation for user registration"

Goose: 📚 EXPLAINED Learning Mode

Input validation is critical for security and data integrity. Let me explain the key concepts and then show you how to implement it.

## Why Input Validation Matters:
1. **Security**: Prevents injection attacks and malicious input
2. **Data Quality**: Ensures your database receives clean, consistent data
3. **User Experience**: Provides clear feedback about invalid input

## Validation Strategy:
1. **Client-side**: Fast feedback, but never trust it for security
2. **Server-side**: The real security barrier - always required
3. **Database constraints**: Final safety net

Here's how to implement comprehensive validation:

```javascript
// 1. Schema Definition
const userRegistrationSchema = {
  email: {
    type: 'string',
    format: 'email',
    required: true
  },
  password: {
    type: 'string',
    minLength: 8,
    pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/
  }
  // ... detailed implementation
}
```

[Continues with detailed explanation and working code...]

**Key Learning Points:**
- Always validate on the server
- Use established validation libraries
- Provide meaningful error messages
- Consider security implications of each validation rule
```

### 🤝 ASSISTED Mode (Quick Help + Learning)

**Configuration:**
```bash
DEFAULT_ASSISTANCE_LEVEL=assisted
LEARNING_PHASE=production
TIMELINE_PRESSURE=medium
```

**Example Interaction:**
```
You: "Quick help with setting up CORS in Express"

Goose: 🤝 ASSISTED Mode

Here's a quick CORS setup with key insights:

```javascript
const cors = require('cors');

app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(',') || 'http://localhost:3000',
  credentials: true,
  optionsSuccessStatus: 200
}));
```

**Key Security Considerations:**
- Never use `origin: '*'` with `credentials: true`
- Always specify exact origins in production
- Consider preflight OPTIONS requests for complex requests

**Pro Tip:** Use environment variables for origins to avoid hardcoding across environments.

Need anything specific about CORS policies or security?
```

### ⚡ AUTOMATED Mode (Direct Solutions)

**Configuration:**
```bash
DEFAULT_ASSISTANCE_LEVEL=automated
TIMELINE_PRESSURE=high
ENABLE_VALIDATION_CHECKPOINTS=false
```

**Example Interaction:**
```
You: "Fix this TypeScript error in my React component"

Goose: ⚡ AUTOMATED Mode

```typescript
// Fixed TypeScript interface
interface User {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
}

// Updated component with proper typing
const UserProfile: React.FC<{ user: User }> = ({ user }) => {
  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
      <small>Joined: {user.createdAt.toLocaleDateString()}</small>
    </div>
  );
};
```

Error resolved: Added proper interface definition and typed the component props.
```

## 🔧 Environment Configuration Examples

### For New Developer (0-6 months)
```bash
# Maximum learning with guided discovery
DEFAULT_ASSISTANCE_LEVEL=guided
LEARNING_PHASE=onboarding
TIMELINE_PRESSURE=low
ENABLE_VALIDATION_CHECKPOINTS=true
MAX_GUIDANCE_DEPTH=5
DEVELOPER_EXPERIENCE_MONTHS=3
```

**Results in:**
- Socratic questioning for concept discovery
- Step-by-step learning validation
- Deep explanations of underlying principles
- Progressive complexity building

### For Experienced Developer Learning New Tech
```bash
# Balanced learning with practical focus
DEFAULT_ASSISTANCE_LEVEL=explained
LEARNING_PHASE=skill_building
TIMELINE_PRESSURE=medium
ENABLE_VALIDATION_CHECKPOINTS=true
MAX_GUIDANCE_DEPTH=3
DEVELOPER_EXPERIENCE_MONTHS=24
```

**Results in:**
- Detailed explanations with working code
- Context about why solutions work
- Best practices and gotchas highlighted
- Optional deeper dives available

### For Production Work
```bash
# Efficiency-focused with learning opportunities
DEFAULT_ASSISTANCE_LEVEL=assisted
LEARNING_PHASE=production
TIMELINE_PRESSURE=high
ENABLE_VALIDATION_CHECKPOINTS=false
MAX_GUIDANCE_DEPTH=1
DEVELOPER_EXPERIENCE_MONTHS=36
```

**Results in:**
- Quick, working solutions
- Key insights and security considerations
- Minimal educational overhead
- Focus on delivery

## 🎓 Learning Scenarios

### Scenario 1: Learning React Hooks

**Request:** "How do I use useEffect for API calls?"

**GUIDED Response:**
```
🎓 Let's explore useEffect together!

Before we dive into the code, help me understand your current knowledge:

1. What do you think "side effects" means in the context of React?
2. When do you think we'd want to run code after a component renders?
3. What problems might occur if we make API calls without proper lifecycle management?

Once you've thought about these concepts, I'll guide you through building a robust useEffect pattern for API calls.
```

**EXPLAINED Response:**
```
📚 useEffect for API calls is a fundamental React pattern. Let me explain the concepts and show you the implementation.

## Understanding useEffect
useEffect handles "side effects" - operations that affect things outside the component, like API calls, subscriptions, or DOM manipulation.

## The Pattern:
```javascript
useEffect(() => {
  // Effect function
  const fetchData = async () => {
    try {
      const response = await fetch('/api/users');
      const users = await response.json();
      setUsers(users);
    } catch (error) {
      setError(error.message);
    }
  };

  fetchData();
}, []); // Dependency array - controls when effect runs
```

## Key Concepts:
1. **Dependency Array**: Controls when the effect re-runs
2. **Cleanup**: Return a function to clean up subscriptions/listeners
3. **Async Handling**: useEffect can't be async directly, so we create async functions inside

[Detailed explanation continues...]
```

### Scenario 2: Debugging Performance Issues

**Request:** "My React app is slow, how do I optimize it?"

**GUIDED Response:**
```
🔍 Performance optimization is a great skill to develop! Let's approach this systematically.

First, let's identify the problem:
1. What specific slowness are you experiencing? (Initial load, interactions, re-renders?)
2. Have you noticed which parts of your app feel slow?
3. What tools do you think we could use to measure performance?

Understanding the root cause is crucial before applying optimizations. What patterns do you notice in your app's behavior?
```

**EXPLAINED Response:**
```
⚡ React performance optimization follows a systematic approach. Let me walk you through the key strategies:

## 1. Identify the Bottleneck
```javascript
// Use React DevTools Profiler
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration) {
  console.log('Component:', id, 'Phase:', phase, 'Duration:', actualDuration);
}

<Profiler id="UserList" onRender={onRenderCallback}>
  <UserList />
</Profiler>
```

## 2. Common Performance Issues & Solutions:

### Unnecessary Re-renders
```javascript
// Problem: Child re-renders when parent updates
// Solution: React.memo for components
const UserCard = React.memo(({ user }) => {
  return <div>{user.name}</div>;
});

// Solution: useCallback for functions
const handleClick = useCallback((userId) => {
  setSelectedUser(userId);
}, []);
```

### Heavy Computations
```javascript
// Solution: useMemo for expensive calculations
const expensiveValue = useMemo(() => {
  return heavyComputation(data);
}, [data]);
```

[Continues with detailed examples and explanations...]
```

## 🧪 Testing Mentor Mode

### Test Different Scenarios

1. **Complex Technical Question** (should trigger GUIDED/EXPLAINED)
   ```
   "How do I implement real-time features with WebSockets?"
   ```

2. **Quick Fix Request** (should trigger ASSISTED/AUTOMATED)
   ```
   "Fix this CSS alignment issue"
   ```

3. **Learning-Focused Query** (should trigger educational mode)
   ```
   "I want to understand how databases work"
   ```

4. **Production Pressure** (should respect timeline urgency)
   ```
   "URGENT: API is returning 500 errors in production"
   ```

### Verify Environment Variables

Check that your configuration is working by looking for these indicators in responses:

- ✅ **Assistance Level**: Should match your `DEFAULT_ASSISTANCE_LEVEL`
- ✅ **Learning Phase**: Should align with `LEARNING_PHASE` setting
- ✅ **Timeline Pressure**: Should respect `TIMELINE_PRESSURE` value
- ✅ **Validation Questions**: Should appear if `ENABLE_VALIDATION_CHECKPOINTS=true`

## 📈 Progressive Learning Examples

### Week 1: New Developer Journey
```bash
# Start with maximum guidance
DEFAULT_ASSISTANCE_LEVEL=guided
DEVELOPER_EXPERIENCE_MONTHS=0
MAX_GUIDANCE_DEPTH=5
```

Requests like "How do I create a function?" result in deep conceptual exploration.

### Week 4: Building Confidence
```bash
# Move to explained mode
DEFAULT_ASSISTANCE_LEVEL=explained
DEVELOPER_EXPERIENCE_MONTHS=1
MAX_GUIDANCE_DEPTH=3
```

Same requests now get detailed explanations with working examples.

### Month 3: Independent Development
```bash
# Transition to assisted mode
DEFAULT_ASSISTANCE_LEVEL=assisted
DEVELOPER_EXPERIENCE_MONTHS=3
MAX_GUIDANCE_DEPTH=2
```

Focus shifts to quick solutions with key insights highlighted.

## 🎯 Advanced Usage Tips

### 1. Learning Session Mode
```bash
# Force educational responses regardless of complexity
FORCE_MENTOR_MODE=true
DEFAULT_ASSISTANCE_LEVEL=explained
```

### 2. Production Mode
```bash
# Minimize educational overhead during critical work
DEFAULT_ASSISTANCE_LEVEL=automated
TIMELINE_PRESSURE=high
ENABLE_VALIDATION_CHECKPOINTS=false
```

### 3. Skill-Building Mode
```bash
# Balanced learning for skill development
DEFAULT_ASSISTANCE_LEVEL=explained
LEARNING_PHASE=skill_building
ENABLE_VALIDATION_CHECKPOINTS=true
```

## 📞 Troubleshooting

### Issue: Not seeing educational responses
**Check:**
- Toolkit properly installed: `mentor` in toolkits list
- Environment variables properly set
- Restart Goose Desktop after configuration changes

### Issue: Too much guidance
**Solution:**
```bash
# Reduce guidance level
DEFAULT_ASSISTANCE_LEVEL=assisted
MAX_GUIDANCE_DEPTH=1
ENABLE_VALIDATION_CHECKPOINTS=false
```

### Issue: Not enough learning depth
**Solution:**
```bash
# Increase learning depth
DEFAULT_ASSISTANCE_LEVEL=guided
MAX_GUIDANCE_DEPTH=5
FORCE_MENTOR_MODE=true
```

---

**🎓 Remember:** Mentor Mode adapts to your learning style and experience level. Don't hesitate to adjust the configuration as you grow and your needs change!
