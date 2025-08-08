"""
Mentor Mode Toolkit for Goose

This toolkit provides AI-powered mentorship that transforms automation into guided learning.
"""

import json
from typing import Any, Dict, List, Optional

# Import the core mentor functionality
from .mentor_engine import MentorEngine, MentorConfig

# Try to import Goose toolkit, fall back to standalone mode if not available
try:
    from goose.toolkit.base import Toolkit, tool
    from rich.panel import Panel
    from rich.markdown import Markdown
    GOOSE_AVAILABLE = True
except ImportError:
    # Fallback for standalone mode
    GOOSE_AVAILABLE = False
    
    # Create mock classes for standalone testing
    class Toolkit:
        def __init__(self, notifier=None, requires=None):
            self.notifier = notifier or MockNotifier()
    
    def tool(func):
        """Mock tool decorator for standalone mode."""
        func._is_tool = True
        return func
    
    class MockNotifier:
        def log(self, content):
            print(content)
    
    class Panel:
        @staticmethod
        def fit(content, title="", border_style=""):
            return f"[{title}] {content}"
    
    class Markdown:
        def __init__(self, content):
            self.content = content
        def __str__(self):
            return self.content


class MentorToolkit(Toolkit):
    """Provides AI-powered mentorship that transforms automation into guided learning."""

    def __init__(self, notifier=None, requires=None):
        super().__init__(notifier, requires)
        self.config = MentorConfig.from_environment()
        self.mentor_engine = MentorEngine(self.config)

    def system_prompt(self) -> str:
        """System prompt that sets up mentoring context."""
        return f"""
You are an AI assistant with mentor mode enabled. Your goal is to transform development assistance 
from pure automation into guided learning experiences.

**Current Configuration:**
- Assistance Level: {self.config.default_assistance_level or 'adaptive'}
- Learning Phase: {self.config.learning_phase}
- Timeline Pressure: {self.config.timeline_pressure}
- Validation Checkpoints: {self.config.enable_validation_checkpoints}

**Guidance Principles:**
1. **GUIDED**: Use Socratic questioning to help users discover solutions
2. **EXPLAINED**: Provide solutions with detailed educational explanations
3. **ASSISTED**: Give quick insights while preserving learning opportunities
4. **AUTOMATED**: Provide direct solutions when appropriate

**When to Use Mentor Mode:**
- User requests involve learning opportunities (security, architecture, best practices)
- Complex technical concepts that benefit from educational approach
- When configuration suggests guided learning approach

**Integration with Tools:**
- Use mentor_analyze_request to determine if mentor intervention is beneficial
- Apply mentor_suggest_assistance_level to adapt your response approach
- Use mentor_learning_check for concept validation when appropriate
- Apply mentor_track_progress to build on previous learning

Remember: The goal is education, not just task completion. Help users understand WHY, not just HOW.
"""

    @tool
    def mentor_analyze_request(self, user_request: str, context: Optional[Dict[str, Any]] = None, 
                              assistance_level: Optional[str] = None) -> str:
        """
        Analyze a user request to determine if mentor intervention would be beneficial and what 
        type of educational approach to take.

        Args:
            user_request (str): The user's request or question
            context (Dict[str, Any], optional): Additional context about the user's situation
            assistance_level (str, optional): Override the default assistance level

        Returns:
            str: Analysis results including learning opportunities and recommended approach
        """
        try:
            # Use mentor engine to analyze the request
            result = self.mentor_engine.analyze_request(user_request, context)
            
            # Override assistance level if provided
            if assistance_level:
                result["assistance_level"] = assistance_level
            
            # Format the result for display
            formatted_result = self._format_mentor_analysis(result)
            
            self.notifier.log(
                Panel.fit(
                    Markdown(f"**Mentor Analysis:**\n{formatted_result}"),
                    title="🎓 Mentor Mode",
                    border_style="blue"
                )
            )
            
            return json.dumps(result, indent=2)
            
        except Exception as e:
            error_msg = f"Error in mentor analysis: {str(e)}"
            self.notifier.log(Panel.fit(Markdown(f"❌ {error_msg}"), title="Mentor Error"))
            return f"Error: {error_msg}"

    @tool
    def mentor_learning_check(self, concept: str, user_explanation: str, 
                             expected_understanding: List[str]) -> str:
        """
        Validate user understanding of a concept through Socratic questioning and provide feedback.

        Args:
            concept (str): The concept being validated
            user_explanation (str): The user's explanation of the concept
            expected_understanding (List[str]): Key points that should be understood

        Returns:
            str: Learning validation results with feedback and follow-up questions
        """
        try:
            result = self.mentor_engine.check_learning(concept, user_explanation, expected_understanding)
            
            formatted_result = self._format_learning_check(result)
            
            self.notifier.log(
                Panel.fit(
                    Markdown(f"**Learning Check:**\n{formatted_result}"),
                    title="🧠 Learning Validation",
                    border_style="green"
                )
            )
            
            return json.dumps(result, indent=2)
            
        except Exception as e:
            error_msg = f"Error in learning check: {str(e)}"
            self.notifier.log(Panel.fit(Markdown(f"❌ {error_msg}"), title="Learning Error"))
            return f"Error: {error_msg}"

    @tool 
    def mentor_track_progress(self, activity: str, success_indicators: Dict[str, Any]) -> str:
        """
        Track learning progress and provide recommendations for continued development.

        Args:
            activity (str): The learning activity or task completed
            success_indicators (Dict[str, Any]): Metrics and indicators of success

        Returns:
            str: Progress analysis with recommendations
        """
        try:
            result = self.mentor_engine.track_progress(activity, success_indicators)
            
            formatted_result = self._format_progress_tracking(result)
            
            self.notifier.log(
                Panel.fit(
                    Markdown(f"**Progress Tracking:**\n{formatted_result}"),
                    title="📈 Learning Progress",
                    border_style="yellow"
                )
            )
            
            return json.dumps(result, indent=2)
            
        except Exception as e:
            error_msg = f"Error in progress tracking: {str(e)}"
            self.notifier.log(Panel.fit(Markdown(f"❌ {error_msg}"), title="Progress Error"))
            return f"Error: {error_msg}"

    @tool
    def mentor_suggest_assistance_level(self, user_request: str, context: Dict[str, Any]) -> str:
        """
        Suggest the optimal assistance level for a given request and context.

        Args:
            user_request (str): The user's request or question
            context (Dict[str, Any]): Context about the user's situation and capabilities

        Returns:
            str: Suggested assistance level with reasoning
        """
        try:
            result = self.mentor_engine.suggest_assistance_level(user_request, context)
            
            formatted_result = self._format_assistance_suggestion(result)
            
            self.notifier.log(
                Panel.fit(
                    Markdown(f"**Assistance Level Suggestion:**\n{formatted_result}"),
                    title="🎯 Adaptive Learning",
                    border_style="cyan"
                )
            )
            
            return json.dumps(result, indent=2)
            
        except Exception as e:
            error_msg = f"Error in assistance suggestion: {str(e)}"
            self.notifier.log(Panel.fit(Markdown(f"❌ {error_msg}"), title="Assistance Error"))
            return f"Error: {error_msg}"

    def _format_mentor_analysis(self, result: Dict[str, Any]) -> str:
        """Format mentor analysis result for display."""
        if result.get("type") == "pass_through":
            return "No mentor intervention needed - proceeding with standard assistance."
        
        lines = []
        if result.get("assistance_level"):
            lines.append(f"**Recommended Level:** {result['assistance_level'].upper()}")
        
        if result.get("learning_opportunities"):
            lines.append(f"**Learning Opportunities:** {', '.join(result['learning_opportunities'])}")
        
        if result.get("educational_context"):
            lines.append(f"**Context:** {result['educational_context']}")
        
        return "\n".join(lines)

    def _format_learning_check(self, result: Dict[str, Any]) -> str:
        """Format learning check result for display."""
        lines = [
            f"**Concept:** {result.get('concept', 'Unknown')}",
            f"**Understanding Score:** {result.get('understanding_score', 0):.2f}/1.0",
            f"**Feedback Type:** {result.get('feedback_type', 'Unknown').replace('_', ' ').title()}"
        ]
        
        if result.get("follow_up_questions"):
            lines.append(f"**Follow-up Questions:** {len(result['follow_up_questions'])} suggested")
        
        return "\n".join(lines)

    def _format_progress_tracking(self, result: Dict[str, Any]) -> str:
        """Format progress tracking result for display."""
        lines = [
            f"**Activity:** {result.get('activity', 'Unknown')}",
        ]
        
        if result.get("analytics"):
            analytics = result["analytics"]
            lines.append(f"**Progress Score:** {analytics.get('overall_score', 0):.2f}/1.0")
        
        if result.get("recommendations"):
            lines.append(f"**Recommendations:** {len(result['recommendations'])} suggestions")
        
        return "\n".join(lines)

    def _format_assistance_suggestion(self, result: Dict[str, Any]) -> str:
        """Format assistance suggestion result for display."""
        lines = [
            f"**Suggested Level:** {result.get('suggested_level', 'Unknown').upper()}",
        ]
        
        if result.get("learning_opportunities"):
            lines.append(f"**Learning Opportunities:** {len(result['learning_opportunities'])} found")
        
        if result.get("reasoning"):
            lines.append(f"**Reasoning:** {result['reasoning'][:100]}...")
        
        return "\n".join(lines)
