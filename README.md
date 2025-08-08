# Mentor Mode: AI-Powered Learning Assistant

[![Version](https://img.shields.io/badge/Version-0.1.0-blue)](https://github.com/your-repo/mentor-mode)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Tests](https://img.shields.io/badge/Tests-13%2F13%20Passing-brightgreen)](./tests/)

> 🎯 **Transform AI assistance from automation to guided learning experiences**

## 🚀 Overview

The Mentor Mode MCP Extension integrates educational mentorship capabilities into AI development workflows through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). This extension enables AI agents like Goose to deliver educational guidance rather than just immediate solutions, creating genuine learning opportunities for developers.

### 🎯 The Problem This Solves

Modern AI tools can create a hidden learning deficit: developers become productive quickly but may miss fundamental understanding. This leads to:

- **AI Dependency**: Shipping code without understanding underlying principles
- **Debugging Difficulties**: Struggling when AI suggestions fail
- **Knowledge Gaps**: Poor architectural decisions due to missing foundations
- **Team Impact**: Reduced code review quality and mentoring effectiveness

### ✨ The Solution: Intelligent Educational Mentorship

Instead of traditional AI interactions:
```
Developer: "How do I implement JWT authentication?"
AI: [Delivers complete solution immediately]
```

Mentor Mode creates learning-focused experiences:
```
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
- Goose AI Agent with Desktop application
- MCP-compatible environment

### Development Installation
```bash
git clone https://github.com/your-repo/mentor-mode
cd mentor-mode
pip install -e ".[dev]"
```

### Running Tests
```bash
pytest tests/ -v
```

## 🚀 Quick Start

### 1. Configure Goose Desktop

Add the Mentor Mode extension to your Goose Desktop configuration:

1. Open Goose Desktop
2. Go to **Settings** → **Extensions**
3. Add a new MCP extension with these settings:

```yaml
extensions:
  mentor-mode:
    cmd: python3
    args:
      - -m
      - mentor_mcp.server
    cwd: /path/to/your/mentor-mode
    envs:
      PYTHONPATH: /path/to/your/mentor-mode/src
      # Configuration (see Configuration section below)
      DEFAULT_ASSISTANCE_LEVEL: "guided"
      LEARNING_PHASE: "skill_building"
      TIMELINE_PRESSURE: "low"
    enabled: true
    type: stdio
    timeout: 300
```

### 2. Test the Integration

Try these test requests to verify mentor mode is working:

**For Guided Learning:**
```
"How do I implement JWT authentication in my Node.js API?"
```
*Expected: Socratic questions that guide you to discover the solution*

**For Educational Explanations:**
```
"Explain how to set up error handling in Express.js"
```
*Expected: Detailed step-by-step educational explanation*

## 🔧 Configuration

Configure mentor mode behavior for different developer profiles:

### **New Developer (6 months experience) - Maximum Learning**
```yaml
envs:
  PYTHONPATH: /path/to/mentor-mode/src
  DEFAULT_ASSISTANCE_LEVEL: "guided"
  LEARNING_PHASE: "skill_building"
  TIMELINE_PRESSURE: "low"
  ENABLE_VALIDATION_CHECKPOINTS: "true"
  MAX_GUIDANCE_DEPTH: "5"
  DEFAULT_SKILL_LEVEL: "1"
  DEVELOPER_EXPERIENCE_MONTHS: "6"
```

### **Experienced Developer - Balanced Assistance**
```yaml
envs:
  PYTHONPATH: /path/to/mentor-mode/src
  DEFAULT_ASSISTANCE_LEVEL: "assisted"
  LEARNING_PHASE: "production"
  TIMELINE_PRESSURE: "medium"
  ENABLE_VALIDATION_CHECKPOINTS: "false"
  DEFAULT_SKILL_LEVEL: "4"
```

### **Emergency/Deadline Mode - Minimal Education**
```yaml
envs:
  PYTHONPATH: /path/to/mentor-mode/src
  DEFAULT_ASSISTANCE_LEVEL: "automated"
  LEARNING_PHASE: "production"
  TIMELINE_PRESSURE: "high"
  ENABLE_VALIDATION_CHECKPOINTS: "false"
  MAX_GUIDANCE_DEPTH: "1"
```

### Configuration Reference

| Variable | Values | Default | Description |
|----------|--------|---------|-------------|
| `DEFAULT_ASSISTANCE_LEVEL` | `guided`, `explained`, `assisted`, `automated` | *(auto)* | Override automatic assistance level selection |
| `LEARNING_PHASE` | `onboarding`, `skill_building`, `production` | `skill_building` | Developer's current learning phase |
| `TIMELINE_PRESSURE` | `low`, `medium`, `high` | `low` | Project timeline pressure level |
| `ENABLE_VALIDATION_CHECKPOINTS` | `true`, `false` | `true` | Enable learning validation questions |
| `MAX_GUIDANCE_DEPTH` | `1`-`5` | `3` | Maximum depth of guided learning |
| `FORCE_MENTOR_MODE` | `true`, `false` | `false` | Always trigger educational responses |
| `DEFAULT_SKILL_LEVEL` | `0`-`5` | `1` | Default skill level for new developers |

See [goose-config-examples.md](./goose-config-examples.md) for detailed configuration examples.

## 📚 Tool Documentation

### `mentor_analyze_request`

Analyzes developer requests for learning opportunities and generates appropriate educational responses.

**Parameters:**
- `user_request` (string): The developer's request or question
- `context` (object, optional): Session context including timeline pressure, skills, etc.
- `assistance_level` (string, optional): Override assistance level

**Example Usage:**
```python
result = await mentor_analyze_request(
    user_request="How do I implement JWT authentication in my Node.js API?",
    context={
        "timeline_pressure": "low",
        "learning_phase": "skill_building",
        "skills": {"javascript": 3, "security": 1}
    }
)
```

### `mentor_learning_check`

Validates understanding of concepts through Socratic questioning.

**Parameters:**
- `concept` (string): The concept being validated
- `user_explanation` (string): User's explanation of the concept
- `expected_understanding` (array): Key points that should be understood

### `mentor_track_progress`

Tracks learning progress and provides personalized recommendations.

**Parameters:**
- `activity` (string): The learning activity completed
- `success_indicators` (object): Indicators of success or areas needing improvement

### `mentor_suggest_assistance_level`

Suggests optimal assistance level based on context and developer needs.

**Parameters:**
- `user_request` (string): The developer's request
- `context` (object): Session context and developer information

## 🎯 Learning Opportunity Detection

The system automatically detects educational opportunities in requests containing:

- **Security Concepts**: JWT, authentication, authorization, encryption, HTTPS, CORS
- **Architecture Patterns**: API, REST, microservices, databases, design patterns
- **Best Practices**: Error handling, validation, testing, logging, performance
- **Development Tools**: Git, debugging, deployment, monitoring

## 📊 Success Metrics

Mentor Mode is designed to improve:

- **Learning Effectiveness**: Better retention of concepts and patterns
- **Problem-Solving Skills**: Enhanced analytical and debugging capabilities
- **Knowledge Transfer**: Improved ability to explain and teach concepts
- **Developer Confidence**: Stronger foundation for independent problem-solving
- **Team Impact**: Enhanced code review quality and mentoring effectiveness

## 🧪 Development & Testing

### Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_mcp_server.py -v

# Check test coverage
pytest tests/ --cov=mentor_mcp --cov-report=html
```

### Development Setup
```bash
# Install in development mode
pip install -e ".[dev]"

# Code quality checks
black src/ tests/
ruff src/ tests/
mypy src/
```

## 📁 Project Structure

```
mentor-mode/
├── src/mentor_mcp/           # Main MCP extension code
│   ├── server.py            # MCP server with 4 educational tools
│   ├── mentor_engine.py     # Core educational logic engine
│   └── __init__.py          # Package initialization
├── tests/                   # Test suite
│   ├── test_mcp_server.py   # MCP server and tools tests
│   └── __init__.py          # Test package initialization
├── pyproject.toml           # Python package configuration
├── goose-config-examples.md # Goose configuration examples
├── LICENSE                  # MIT license
└── README.md               # This documentation
```

## 🤝 Contributing

We welcome contributions from developers, educators, and AI researchers!

### Development Workflow
1. Fork the repository
2. Create a feature branch
3. Implement changes with comprehensive tests
4. Ensure all tests pass (`pytest tests/`)
5. Submit pull request with detailed description

### Code Quality Standards
- All new features must include tests
- Code coverage should remain above 90%
- Follow Python PEP 8 style guidelines
- Include docstrings for all public functions

## 📄 License

MIT License - see [LICENSE](./LICENSE) for details.

## 🚀 Future Roadmap

- **Enhanced Learning Analytics**: Detailed progress tracking and skill gap analysis
- **Integration with Popular IDEs**: VS Code and JetBrains extensions
- **Team Learning Dashboards**: Organizational learning insights
- **Custom Learning Paths**: Personalized curricula for different technologies
- **Community Learning Resources**: Shared knowledge base and best practices

---

**Built to empower the next generation of developers through intelligent AI mentorship.** 🚀

### 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/mentor-mode/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/mentor-mode/discussions)
- **Documentation**: See [goose-config-examples.md](./goose-config-examples.md) for configuration details
