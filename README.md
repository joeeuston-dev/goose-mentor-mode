# Goose Mentor Mode 🎓

AI-powered mentor extension for Goose that transforms development assistance from automation into guided learning experiences.

[![PyPI version](https://badge.fury.io/py/goose-mentor-mode.svg)](https://badge.fury.io/py/goose-mentor-mode)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **Adaptive Learning Assistance**: Four assistance levels (GUIDED, EXPLAINED, ASSISTED, AUTOMATED)
- **Socratic Questioning**: Helps users discover solutions through guided questions
- **Learning Opportunity Detection**: Automatically identifies educational moments
- **Progress Tracking**: Monitors learning progress and provides recommendations
- **Environment Configuration**: Easy setup through environment variables
- **Goose Integration**: Seamless integration with Goose AI assistant

## 🎉 Now Available on PyPI!

Goose Mentor Mode is officially published and available to the entire Python community! Install it with a single command and start transforming your AI assistance from automation to education.

## 📦 Installation

Goose Mentor Mode is a Goose extension that integrates seamlessly with Goose Desktop.

### 🚀 Quick Install via PyPI (Recommended)

```bash
# Install the package (do NOT use uvx - this is a Goose extension, not a CLI tool)
pip install goose-mentor-mode

# Or if you're using uv in a project
uv add goose-mentor-mode
```

**Note**: This is a Goose extension/toolkit, not a standalone CLI application. Do not try to run it with `uvx` or as a command-line tool.

### 📦 PyPI Package

- **PyPI**: https://pypi.org/project/goose-mentor-mode/
- **Latest Version**: [![PyPI version](https://badge.fury.io/py/goose-mentor-mode.svg)](https://badge.fury.io/py/goose-mentor-mode)

### 🛠️ Development Installation

```bash
# Clone and install for development
git clone https://github.com/joeeuston-dev/goose-mentor-mode.git
cd goose-mentor-mode
uv sync

# Or with pip in development mode
pip install -e .
```

## ⚙️ Configuration

### Goose Desktop Integration

After installing the package, configure it in Goose Desktop:

#### Step 1: Install the Package
```bash
pip install goose-mentor-mode
```

#### Step 2: Configure in Goose Desktop

**Method 1: Through Goose Desktop UI**
1. Open Goose Desktop
2. Go to **Settings** → **Profiles** 
3. Select your profile or create a new one
4. Add `mentor` to the **Toolkits** list
5. Optionally configure environment variables for customization

**Method 2: Direct Profile Configuration**

Add to your Goose profile configuration:

```yaml
toolkits:
  - name: mentor
    package: goose-mentor-mode
```

#### Step 3: Environment Configuration (Optional)

Customize behavior using environment variables:

```bash
# Core Configuration
DEFAULT_ASSISTANCE_LEVEL=guided          # guided|explained|assisted|automated
LEARNING_PHASE=skill_building           # onboarding|skill_building|production
TIMELINE_PRESSURE=low                   # low|medium|high
ENABLE_VALIDATION_CHECKPOINTS=true     # Enable learning validation
MAX_GUIDANCE_DEPTH=3                    # Depth of Socratic questioning
DEVELOPER_EXPERIENCE_MONTHS=6           # Developer experience level
```

**Environment Variable Configuration in Goose Desktop:**
1. Go to Settings → Profiles → [Your Profile]
2. Add environment variables in the Environment section
3. Save and restart Goose Desktop

📖 **For detailed usage examples and scenarios, see [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)**

🎯 **For complete Goose Desktop setup instructions, see [GOOSE_DESKTOP_CONFIG.md](GOOSE_DESKTOP_CONFIG.md)**

## 🎯 Assistance Levels

### 🧭 GUIDED Mode
- **Purpose**: Learning through discovery
- **Approach**: Socratic questioning and guided exploration
- **Best For**: New concepts, skill building, deep understanding
- **Example**: "What do you think JWT stands for? How might stateless authentication work?"

### 📚 EXPLAINED Mode  
- **Purpose**: Education with solutions
- **Approach**: Detailed explanations with implementation
- **Best For**: Time-sensitive tasks with learning value
- **Example**: "Here's how JWT works... [detailed explanation] + working code"

### 🤝 ASSISTED Mode
- **Purpose**: Quick help with learning opportunities
- **Approach**: Direct help with educational context
- **Best For**: Experienced developers needing quick assistance
- **Example**: "Use this JWT library. Key security considerations: [brief points]"

### ⚡ AUTOMATED Mode
- **Purpose**: Direct task completion
- **Approach**: Efficient solutions without educational overhead
- **Best For**: Production pressure, repeated tasks
- **Example**: "Here's the complete JWT implementation."

## 🛠️ Tools

### `mentor_analyze_request`
Analyzes user requests for learning opportunities and recommends assistance levels.

```python
toolkit.mentor_analyze_request(
    user_request="How do I implement JWT authentication?",
    context={"experience_months": 6, "timeline_pressure": "low"}
)
```

### `mentor_learning_check`
Validates understanding through Socratic questioning.

```python
toolkit.mentor_learning_check(
    concept="JWT Authentication",
    user_explanation="JWT is a token that contains user information",
    expected_understanding=["stateless", "secure", "token-based"]
)
```

### `mentor_track_progress`
Tracks learning progress and provides recommendations.

```python
toolkit.mentor_track_progress(
    activity="Implementing JWT authentication",
    success_indicators={"task_completed": True, "time_spent": 30}
)
```

### `mentor_suggest_assistance_level`
Suggests optimal assistance level for given context.

```python
toolkit.mentor_suggest_assistance_level(
    user_request="I need help with AWS Lambda",
    context={"experience_months": 6, "timeline_pressure": "medium"}
)
```

## 🎓 Educational Philosophy

Mentor Mode transforms AI assistance from automation to education:

- **Discovery Over Delivery**: Help users understand *why*, not just *how*
- **Adaptive Learning**: Adjusts approach based on experience and context  
- **Progressive Complexity**: Builds understanding layer by layer
- **Retention Focus**: Emphasizes learning that sticks

## 🔧 Developer Profiles

### New Developer (0-6 months)
```bash
DEFAULT_ASSISTANCE_LEVEL=guided
LEARNING_PHASE=onboarding
TIMELINE_PRESSURE=low
ENABLE_VALIDATION_CHECKPOINTS=true
```

### Developing Skills (6-24 months)
```bash
DEFAULT_ASSISTANCE_LEVEL=explained
LEARNING_PHASE=skill_building
TIMELINE_PRESSURE=medium
ENABLE_VALIDATION_CHECKPOINTS=true
```

### Experienced Developer (24+ months)
```bash
DEFAULT_ASSISTANCE_LEVEL=assisted
LEARNING_PHASE=production
TIMELINE_PRESSURE=medium
ENABLE_VALIDATION_CHECKPOINTS=false
```

## 🧪 Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=goose_mentor_mode

# Run specific test
uv run pytest tests/test_mentor_toolkit.py::TestMentorToolkit::test_mentor_analyze_request
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run tests (`uv run pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for the [Goose AI Assistant](https://github.com/block/goose)
- Inspired by Socratic teaching methods
- Designed for developers who value learning

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/joeeuston-dev/goose-mentor-mode/issues)
- **Documentation**: [GitHub Wiki](https://github.com/joeeuston-dev/goose-mentor-mode/wiki)
- **Discussions**: [GitHub Discussions](https://github.com/joeeuston-dev/goose-mentor-mode/discussions)

---

**Transform your AI assistance from automation to education with Goose Mentor Mode! 🎓✨**
