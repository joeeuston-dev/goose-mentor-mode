"""
Tests for the Mentor Toolkit
"""

import pytest
import json
from goose_mentor_mode import MentorToolkit, MentorConfig


class TestMentorToolkit:
    """Test the MentorToolkit class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.toolkit = MentorToolkit()

    def test_toolkit_initialization(self):
        """Test that the toolkit initializes correctly."""
        assert self.toolkit is not None
        assert self.toolkit.config is not None
        assert self.toolkit.mentor_engine is not None

    def test_mentor_analyze_request(self):
        """Test the mentor_analyze_request tool."""
        result = self.toolkit.mentor_analyze_request(
            "How do I implement JWT authentication?"
        )
        
        # Should return a JSON string
        parsed = json.loads(result)
        assert isinstance(parsed, dict)
        
        # Should have an assistance level
        assert "assistance_level" in parsed or "type" in parsed

    def test_mentor_analyze_request_with_context(self):
        """Test mentor analysis with context."""
        context = {
            "timeline_pressure": "high",
            "experience_months": 3
        }
        
        result = self.toolkit.mentor_analyze_request(
            "How do I implement authentication?",
            context=context
        )
        
        parsed = json.loads(result)
        assert isinstance(parsed, dict)

    def test_mentor_learning_check(self):
        """Test the learning check tool."""
        result = self.toolkit.mentor_learning_check(
            concept="JWT Authentication",
            user_explanation="JWT is a token that contains user information",
            expected_understanding=["stateless", "secure", "token-based"]
        )
        
        parsed = json.loads(result)
        assert isinstance(parsed, dict)
        assert "concept" in parsed
        assert "understanding_score" in parsed

    def test_mentor_track_progress(self):
        """Test the progress tracking tool."""
        success_indicators = {
            "task_completed": True,
            "time_spent": 30,
            "errors_encountered": 2
        }
        
        result = self.toolkit.mentor_track_progress(
            activity="Implementing JWT authentication",
            success_indicators=success_indicators
        )
        
        parsed = json.loads(result)
        assert isinstance(parsed, dict)
        assert "activity" in parsed

    def test_mentor_suggest_assistance_level(self):
        """Test the assistance level suggestion tool."""
        context = {
            "experience_months": 6,
            "timeline_pressure": "medium"
        }
        
        result = self.toolkit.mentor_suggest_assistance_level(
            user_request="I need help with AWS Lambda",
            context=context
        )
        
        parsed = json.loads(result)
        assert isinstance(parsed, dict)
        assert "suggested_level" in parsed

    def test_system_prompt(self):
        """Test that system prompt is generated correctly."""
        prompt = self.toolkit.system_prompt()
        assert isinstance(prompt, str)
        assert len(prompt) > 100
        assert "mentor mode" in prompt.lower()

    def test_environment_configuration(self):
        """Test that environment configuration works."""
        import os
        
        # Set a test environment variable
        os.environ["DEFAULT_ASSISTANCE_LEVEL"] = "guided"
        
        # Create a new toolkit to pick up the environment
        test_toolkit = MentorToolkit()
        
        # Check that config reflects the environment
        assert test_toolkit.config.default_assistance_level == "guided"
        
        # Clean up
        del os.environ["DEFAULT_ASSISTANCE_LEVEL"]


class TestMentorConfig:
    """Test the MentorConfig class."""

    def test_config_from_environment(self):
        """Test configuration from environment variables."""
        import os
        
        # Set test environment variables
        test_vars = {
            "DEFAULT_ASSISTANCE_LEVEL": "explained",
            "LEARNING_PHASE": "skill_building",
            "TIMELINE_PRESSURE": "low",
            "ENABLE_VALIDATION_CHECKPOINTS": "true",
            "MAX_GUIDANCE_DEPTH": "3"
        }
        
        for key, value in test_vars.items():
            os.environ[key] = value
        
        try:
            config = MentorConfig.from_environment()
            
            assert config.default_assistance_level == "explained"
            assert config.learning_phase == "skill_building"
            assert config.timeline_pressure == "low"
            assert config.enable_validation_checkpoints is True
            assert config.max_guidance_depth == 3
            
        finally:
            # Clean up environment variables
            for key in test_vars:
                if key in os.environ:
                    del os.environ[key]

    def test_config_defaults(self):
        """Test default configuration values."""
        config = MentorConfig()
        
        assert config.learning_phase == "skill_building"
        assert config.timeline_pressure == "low"
        assert config.enable_validation_checkpoints is True
        assert config.max_guidance_depth == 3


if __name__ == "__main__":
    pytest.main([__file__])
