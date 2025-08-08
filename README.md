# Goose Mentor Mode 🎓

AI-powered mentor extension for Goose that transforms development assistance from automation into guided learning experiences using the Model Context Protocol (MCP).

[![PyPI version](https://badge.fury.io/py/goose-mentor-mode.svg)](https://badge.fury.io/py/goose-mentor-mode)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **Adaptive Learning Assistance**: Four assistance levels (GUIDED, EXPLAINED, ASSISTED, AUTOMATED)
- **Socratic Questioning**: Helps users discover solutions through guided questions
- **Learning Opportunity Detection**: Automatically identifies educational moments
- **Progress Tracking**: Monitors learning progress and provides recommendations
- **Environment Configuration**: Easy setup through environment variables
- **MCP Integration**: Modern Model Context Protocol extension for Goose Desktop

## 🎉 Now Available on PyPI!

Goose Mentor Mode is officially published and available to the entire Python community! Install it with a single command and start transforming your AI assistance from automation to education.

## 📦 Installation

Goose Mentor Mode is an MCP (Model Context Protocol) extension for Goose Desktop. It runs as a server that Goose communicates with to provide mentoring capabilities.

### 🚀 Quick Install via Goose Desktop (Recommended)

**No manual installation required!** Goose Desktop will automatically install the package when you add it as an extension.

1. Open **Goose Desktop**
2. Click on **Extensions** menu
3. Select **Add Custom Extension**
4. Fill in the extension details:
   - **Extension Name**: `Goose Mentor Mode`
   - **Type**: `STDIO`
   - **Description**: `Goose Mentor Mode makes your goose a Mentor that helps you learn as you work together!`
   - **Command**: `uvx goose-mentor-mode`
5. Click **Add Extension**
6. The extension will be automatically installed and ready to use!

### 📦 PyPI Package

- **PyPI**: https://pypi.org/project/goose-mentor-mode/
- **Latest Version**: [![PyPI version](https://badge.fury.io/py/goose-mentor-mode.svg)](https://badge.fury.io/py/goose-mentor-mode)

### 🛠️ Manual Installation (Development)

For development or manual setup:

```bash
# Clone and install for development
git clone https://github.com/joeeuston-dev/goose-mentor-mode.git
cd goose-mentor-mode
uv sync

# Build and test locally
uv build
uvx --from ./dist/goose_mentor_mode-*.whl goose-mentor-mode --help
```

## ⚙️ Configuration

### Environment Variables (Optional)

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

## 🛠️ MCP Tools

The extension provides four core MCP tools that work seamlessly with Goose:

### `mentor_analyze_request`
Analyzes user requests for learning opportunities and recommends assistance levels.

**Parameters:**
- `request`: The user's request or question
- `context`: Optional context about the current task or project

### `mentor_learning_check`
Validates understanding through Socratic questioning and provides learning feedback.

**Parameters:**
- `concept`: The concept or topic to validate understanding for
- `user_response`: User's response to previous questions (optional)
- `assistance_level`: Level of assistance (guided, explained, assisted, automated)

### `mentor_track_progress`
Tracks learning progress and provides recommendations for continued development.

**Parameters:**
- `topic`: The learning topic or subject area
- `interaction_data`: Data about the learning interaction
- `session_id`: Optional session identifier for progress tracking

### `mentor_suggest_assistance_level`
Suggests the optimal assistance level based on request complexity and user profile.

**Parameters:**
- `request`: The user's request or task
- `user_profile`: Optional user profile information
- `context`: Optional context about the current situation

> **Note**: These tools are automatically available in Goose once the extension is installed. Goose will intelligently use them based on your interactions to provide mentoring assistance.

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
