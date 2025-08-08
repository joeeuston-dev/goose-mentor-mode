# Mentor Mode MCP Extension

[![Version](https://img.shields.io/badge/Version-0.1.0-blue)](https://github.com/your-repo/mentor-mode)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)

> 🎯 **Transform AI assistance from automation to guided learning experiences**

## 🚀 Overview

The Mentor Mode MCP Extension integrates educational mentorship capabilities into AI development workflows through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). This extension provides sophisticated tools that enable AI agents like Goose to deliver educational guidance rather than just solutions.

### Key Innovation

Instead of traditional AI interactions that immediately provide solutions, Mentor Mode creates learning-focused experiences:

```
Traditional AI:
Developer: "How do I implement JWT authentication?"
AI: [Delivers complete solution immediately]

Mentor Mode:
Developer: "How do I implement JWT authentication?"
AI: "Great learning opportunity! Let's explore this step-by-step. What do you think 
     are the main security considerations we need to address first?"
```

## 🎯 Features

### 🧠 **Intelligent Learning Opportunity Detection**
- Analyzes requests for educational value
- Identifies security concepts, architectural patterns, and best practices
- Context-aware assistance level selection

### 🎓 **Four Assistance Levels**
- **🔍 Guided**: Socratic questioning for maximum learning
- **📚 Explained**: Detailed educational explanations with solutions
- **⚡ Assisted**: Quick solutions with key insights highlighted
- **🤖 Automated**: Efficient solutions with minimal educational overhead

### 🔧 **Comprehensive Tool Suite**
- `mentor_analyze_request`: Analyze requests for learning opportunities
- `mentor_learning_check`: Validate understanding through Socratic questioning
- `mentor_track_progress`: Track learning progress and provide recommendations
- `mentor_suggest_assistance_level`: Suggest appropriate assistance levels

### 📊 **Learning Analytics**
- Progress tracking across sessions
- Skill development assessment
- Personalized learning recommendations

## 🛠 Installation

### Prerequisites
- Python 3.8+
- Goose AI Agent
- MCP-compatible environment

### Install via pip
```bash
pip install mentor-mcp
```

### Development Installation
```bash
git clone https://github.com/your-repo/mentor-mode
cd mentor-mode/mcp-mentor
pip install -e ".[dev]"
```

## 🚀 Quick Start

### 1. Configure Goose to use Mentor Mode MCP
Add to your Goose configuration:

```json
{
  "mcpServers": {
    "mentor-mode": {
      "command": "python",
      "args": ["-m", "mentor_mcp.server"],
      "env": {}
    }
  }
}
```

### 2. Basic Usage Examples

```python
# Educational analysis of a request
result = await mentor_analyze_request(
    user_request="How do I implement JWT authentication in my Node.js API?",
    context={
        "timeline_pressure": "low",
        "learning_phase": "skill_building",
        "skills": {"javascript": 3, "security": 1}
    }
)

# Learning validation
feedback = await mentor_learning_check(
    concept="JWT Authentication",
    user_explanation="JWT is a token that contains user information...",
    expected_understanding=["stateless authentication", "security considerations", "token structure"]
)

# Progress tracking
progress = await mentor_track_progress(
    activity="JWT Implementation",
    success_indicators={"completed": True, "understood_security": True}
)
```

## 📚 Tool Documentation

### `mentor_analyze_request`

Analyzes developer requests for learning opportunities and generates appropriate educational responses.

**Parameters:**
- `user_request` (string): The developer's request or question
- `context` (object, optional): Session context including timeline pressure, skills, etc.
- `assistance_level` (string, optional): Override assistance level

**Example Response:**
```json
{
  "type": "mentor_response",
  "assistance_level": "explained",
  "educational_content": "📚 Let's implement JWT authentication step-by-step...",
  "learning_objectives": [
    "Understand security principles and best practices",
    "Learn authentication patterns"
  ],
  "follow_up_questions": [
    "Can you explain why this approach works?",
    "What security considerations should we address?"
  ],
  "validation_checkpoints": [
    "Can explain the solution approach",
    "Understands key security concepts"
  ]
}
```

### `mentor_learning_check`

Validates understanding of concepts through Socratic questioning and provides educational feedback.

**Parameters:**
- `concept` (string): The concept being validated
- `user_explanation` (string): User's explanation of the concept
- `expected_understanding` (array): Key points that should be understood

### `mentor_track_progress`

Tracks learning progress and provides personalized recommendations for continued development.

**Parameters:**
- `activity` (string): The learning activity completed
- `success_indicators` (object): Indicators of success or areas needing improvement

### `mentor_suggest_assistance_level`

Analyzes context and suggests the most appropriate assistance level for maximum learning benefit.

**Parameters:**
- `user_request` (string): The developer's request
- `context` (object): Session context and developer information

## 🎯 Integration Examples

### Goose Integration

When integrated with Goose, Mentor Mode can automatically detect learning opportunities:

```typescript
// Goose detects a learning-oriented request
const mentorResponse = await tools.mentor_analyze_request({
  user_request: "Help me understand async/await in JavaScript",
  context: {
    timeline_pressure: "low",
    learning_phase: "skill_building"
  }
});

if (mentorResponse.type === "mentor_response") {
  // Provide educational guidance instead of direct solution
  return mentorResponse.educational_content;
}
```

### Custom Learning Workflows

```python
# Progressive learning workflow
async def guided_learning_session(topic: str, user_context: dict):
    # 1. Analyze learning opportunity
    analysis = await mentor_analyze_request(
        user_request=f"I want to learn about {topic}",
        context=user_context
    )
    
    # 2. Deliver educational content
    print(analysis["educational_content"])
    
    # 3. Validate understanding
    user_explanation = input("Please explain your understanding: ")
    feedback = await mentor_learning_check(
        concept=topic,
        user_explanation=user_explanation,
        expected_understanding=analysis["learning_objectives"]
    )
    
    # 4. Track progress
    await mentor_track_progress(
        activity=f"{topic} Learning Session",
        success_indicators={"understanding_score": feedback["understanding_score"]}
    )
    
    return feedback
```

## 🔧 Configuration

### Environment Variable Configuration

Configure mentor mode behavior through environment variables in your Goose Desktop UI:

```yaml
extensions:
  mentor-mode:
    envs:
      # Core Configuration
      DEFAULT_ASSISTANCE_LEVEL: "guided"          # guided, explained, assisted, automated
      LEARNING_PHASE: "skill_building"            # onboarding, skill_building, production
      TIMELINE_PRESSURE: "low"                    # low, medium, high
      
      # Feature Control
      ENABLE_VALIDATION_CHECKPOINTS: "true"      # true, false
      MAX_GUIDANCE_DEPTH: "3"                    # 1-5 depth levels
      FORCE_MENTOR_MODE: "false"                 # true, false (always trigger mentor mode)
      
      # Developer Defaults
      DEFAULT_SKILL_LEVEL: "1"                   # 0-5 skill scale
      DEVELOPER_EXPERIENCE_MONTHS: "6"           # months of experience
```

### Configuration Examples

#### **For New Developer (6 months experience)**
```yaml
envs:
  DEFAULT_ASSISTANCE_LEVEL: "guided"
  LEARNING_PHASE: "skill_building"
  TIMELINE_PRESSURE: "low"
  ENABLE_VALIDATION_CHECKPOINTS: "true"
  DEFAULT_SKILL_LEVEL: "1"
  DEVELOPER_EXPERIENCE_MONTHS: "6"
```

#### **For Experienced Developer (under pressure)**
```yaml
envs:
  DEFAULT_ASSISTANCE_LEVEL: "assisted"
  LEARNING_PHASE: "production"
  TIMELINE_PRESSURE: "high"
  ENABLE_VALIDATION_CHECKPOINTS: "false"
  DEFAULT_SKILL_LEVEL: "4"
```

#### **For Learning-Focused Sessions**
```yaml
envs:
  DEFAULT_ASSISTANCE_LEVEL: "explained"
  LEARNING_PHASE: "skill_building"
  TIMELINE_PRESSURE: "low"
  FORCE_MENTOR_MODE: "true"              # Always provide educational context
  MAX_GUIDANCE_DEPTH: "5"                # Maximum learning depth
```

### Environment Variable Reference

| Variable | Values | Default | Description |
|----------|--------|---------|-------------|
| `DEFAULT_ASSISTANCE_LEVEL` | `guided`, `explained`, `assisted`, `automated`, *(empty)* | *(auto)* | Override automatic assistance level selection |
| `LEARNING_PHASE` | `onboarding`, `skill_building`, `production` | `skill_building` | Developer's current learning phase |
| `TIMELINE_PRESSURE` | `low`, `medium`, `high` | `low` | Project timeline pressure level |
| `ENABLE_VALIDATION_CHECKPOINTS` | `true`, `false` | `true` | Enable learning validation questions |
| `MAX_GUIDANCE_DEPTH` | `1`-`5` | `3` | Maximum depth of guided learning |
| `FORCE_MENTOR_MODE` | `true`, `false` | `false` | Always trigger educational responses |
| `DEFAULT_SKILL_LEVEL` | `0`-`5` | `1` | Default skill level for new developers |
| `DEVELOPER_EXPERIENCE_MONTHS` | *integer* | `12` | Developer experience in months |

### Assistance Level Customization

```python
# Override default assistance level selection
mentor_config = {
    "default_assistance_level": "guided",  # guided, explained, assisted, automated
    "learning_phase": "skill_building",    # onboarding, skill_building, production
    "enable_validation_checkpoints": True,
    "max_guidance_depth": 3
}
```

### Learning Opportunity Detection

The system automatically detects:
- **Security Concepts**: JWT, authentication, authorization, encryption, etc.
- **Architecture Patterns**: API, REST, microservices, databases, etc.
- **Best Practices**: Error handling, validation, testing, logging, etc.

## 📈 Learning Analytics

Track educational effectiveness:

```python
analytics = await mentor_track_progress(
    activity="API Development Session",
    success_indicators={
        "concepts_learned": ["JWT", "REST APIs", "error handling"],
        "time_spent": 45,
        "understanding_demonstrated": True
    }
)

print(f"Learning Analytics: {analytics['analytics']}")
```

## 🤝 Contributing

We welcome contributions from developers, educators, and AI researchers!

### Development Setup
```bash
git clone https://github.com/your-repo/mentor-mode
cd mentor-mode/mcp-mentor
pip install -e ".[dev]"
pytest
```

### Code Quality
```bash
black src/ tests/
ruff src/ tests/
mypy src/
```

## 📄 License

MIT License - see [LICENSE](../LICENSE) for details.

## 🎯 Success Metrics

Mentor Mode is designed to improve:
- **Learning Effectiveness**: Better retention of concepts and patterns
- **Problem-Solving Skills**: Enhanced analytical and debugging capabilities
- **Knowledge Transfer**: Improved ability to explain and teach concepts
- **Developer Confidence**: Stronger foundation for independent problem-solving

---

**Built to empower the next generation of developers through intelligent AI mentorship.** 🚀
