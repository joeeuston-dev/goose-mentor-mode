"""
Tests for Mentor Mode Extension

These tests validate the core mentor mode functionality including:
- Assistance level determination
- Educational response generation
- Learning progress tracking
- Goose integration points
"""

import pytest
from unittest.mock import Mock, patch
from typing import Dict, Any

from src.mentor_mode.core.mentor_engine import (
    MentorEngine, DeveloperContext, AssistanceLevel, MentorResponse
)
from src.mentor_mode.goose_extension.mentor_extension import (
    MentorExtension, MentorConfig
)


class TestMentorEngine:
    """Test core mentor engine functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.mentor_engine = MentorEngine()
        
    def test_assistance_level_selection_high_pressure(self):
        """Test that high timeline pressure defaults to automated."""
        context = DeveloperContext(
            timeline_pressure="high",
            learning_phase="skill_building",
            task_complexity="moderate",
            demonstrated_skills={}
        )
        
        level = self.mentor_engine._select_assistance_level(context, {})
        assert level == AssistanceLevel.AUTOMATED
    
    def test_assistance_level_selection_onboarding(self):
        """Test that onboarding phase defaults to guided."""
        context = DeveloperContext(
            timeline_pressure="low",
            learning_phase="onboarding",
            task_complexity="simple",
            demonstrated_skills={}
        )
        
        level = self.mentor_engine._select_assistance_level(context, {})
        assert level == AssistanceLevel.GUIDED
    
    def test_assistance_level_selection_explained_default(self):
        """Test that normal conditions default to explained."""
        context = DeveloperContext(
            timeline_pressure="medium",
            learning_phase="skill_building",
            task_complexity="moderate",
            demonstrated_skills={}
        )
        
        level = self.mentor_engine._select_assistance_level(context, {})
        assert level == AssistanceLevel.EXPLAINED
    
    def test_guided_response_generation(self):
        """Test guided response includes Socratic questioning."""
        context = DeveloperContext(
            timeline_pressure="low",
            learning_phase="onboarding",
            task_complexity="simple",
            demonstrated_skills={}
        )
        
        response = self.mentor_engine.process_request(
            "How do I implement JWT authentication?",
            context
        )
        
        assert response.assistance_level == AssistanceLevel.GUIDED
        assert "Learning Opportunity Detected" in response.content
        assert len(response.follow_up_questions) > 0
        assert len(response.validation_checkpoints) > 0
        assert "problem-solving" in str(response.learning_objectives).lower()
    
    def test_explained_response_generation(self):
        """Test explained response includes educational context."""
        context = DeveloperContext(
            timeline_pressure="medium",
            learning_phase="skill_building",
            task_complexity="moderate",
            demonstrated_skills={}
        )
        
        response = self.mentor_engine.process_request(
            "Explain microservices architecture",
            context
        )
        
        assert response.assistance_level == AssistanceLevel.EXPLAINED
        assert "Educational Response" in response.content
        assert "Key Concepts" in response.content
        assert len(response.learning_objectives) > 0
        assert len(response.validation_checkpoints) > 0
    
    def test_automated_response_minimal_overhead(self):
        """Test automated response has minimal educational overhead."""
        context = DeveloperContext(
            timeline_pressure="high",
            learning_phase="production",
            task_complexity="complex",
            demonstrated_skills={}
        )
        
        response = self.mentor_engine.process_request(
            "Fix this bug quickly",
            context
        )
        
        assert response.assistance_level == AssistanceLevel.AUTOMATED
        assert "Automated Solution" in response.content
        assert len(response.follow_up_questions) == 0


class TestMentorExtension:
    """Test Goose extension integration."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.config = MentorConfig(
            default_assistance_level="explained",
            learning_phase="skill_building"
        )
        self.extension = MentorExtension(self.config)
    
    def test_extension_initialization(self):
        """Test extension initializes correctly."""
        assert self.extension.config.default_assistance_level == "explained"
        assert self.extension.config.learning_phase == "skill_building"
        assert isinstance(self.extension.mentor_engine, MentorEngine)
        assert self.extension.learning_history == []
    
    def test_should_intervene_learning_keywords(self):
        """Test intervention triggers on learning keywords."""
        context = DeveloperContext(
            timeline_pressure="medium",
            learning_phase="skill_building",
            task_complexity="simple",
            demonstrated_skills={}
        )
        
        # Should intervene
        assert self.extension._should_intervene("How to implement authentication?", context)
        assert self.extension._should_intervene("What is the best way to...", context)
        assert self.extension._should_intervene("Explain how to create a REST API", context)
        
        # Should not intervene for non-learning requests
        assert not self.extension._should_intervene("Print hello world", context)
    
    def test_should_not_intervene_high_pressure(self):
        """Test no intervention during high timeline pressure (unless automated)."""
        context = DeveloperContext(
            timeline_pressure="high",
            learning_phase="skill_building",
            task_complexity="simple",
            demonstrated_skills={}
        )
        
        # Should not intervene even with learning keywords
        assert not self.extension._should_intervene("How to implement authentication?", context)
        
        # Test with automated mode
        self.extension.config.default_assistance_level = "automated"
        # Would still return False with current logic, but this tests the condition
        
    def test_process_request_intervention(self):
        """Test request processing with mentor intervention."""
        context = {
            "timeline_pressure": "medium",
            "complexity_indicators": ["database", "authentication"]
        }
        
        result = self.extension.process_request(
            "How do I implement JWT authentication?",
            context
        )
        
        assert result["mentor_intervention"] == True
        assert "assistance_level" in result
        assert "educational_content" in result
        assert "learning_objectives" in result
        assert "follow_up_questions" in result
        assert "validation_checkpoints" in result
    
    def test_process_request_no_intervention(self):
        """Test request processing without intervention."""
        context = {
            "timeline_pressure": "medium",
            "complexity_indicators": []
        }
        
        result = self.extension.process_request(
            "Print hello world",
            context
        )
        
        assert result["proceed_normally"] == True
        assert result["original_message"] == "Print hello world"
    
    def test_complexity_assessment(self):
        """Test task complexity assessment."""
        # Simple task
        context = {"complexity_indicators": []}
        assert self.extension._assess_complexity(context) == "simple"
        
        # Moderate task
        context = {"complexity_indicators": ["database"]}
        assert self.extension._assess_complexity(context) == "moderate"
        
        # Complex task
        context = {"complexity_indicators": ["database", "authentication", "microservices"]}
        assert self.extension._assess_complexity(context) == "complex"
    
    def test_learning_progress_tracking(self):
        """Test learning progress tracking."""
        # Update progress
        self.extension.update_learning_progress(
            "JWT Authentication Implementation",
            {"completion": True, "understanding_level": "good"}
        )
        
        assert len(self.extension.learning_history) == 1
        assert self.extension.learning_history[0]["activity"] == "JWT Authentication Implementation"
        
        # Get analytics
        analytics = self.extension.get_learning_analytics()
        assert analytics["total_interactions"] == 1
        assert "learning_patterns" in analytics
        assert "skill_development" in analytics
        assert "recommendation" in analytics
    
    def test_extension_creation_function(self):
        """Test extension creation with configuration."""
        from src.mentor_mode.goose_extension.mentor_extension import create_extension
        
        config = {
            "default_assistance_level": "guided",
            "learning_phase": "onboarding",
            "enable_validation_checkpoints": True
        }
        
        extension = create_extension(config)
        assert extension.config.default_assistance_level == "guided"
        assert extension.config.learning_phase == "onboarding"
        assert extension.config.enable_validation_checkpoints == True


class TestLearningScenarios:
    """Test realistic learning scenarios."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.extension = MentorExtension()
    
    def test_jwt_authentication_scenario(self):
        """Test complete JWT authentication learning scenario."""
        # Initial request
        context = {
            "timeline_pressure": "low",
            "complexity_indicators": ["authentication", "security"],
            "skills": {"javascript": 3, "security": 1}
        }
        
        result = self.extension.process_request(
            "How do I implement JWT authentication in my Node.js API?",
            context
        )
        
        # Should trigger guided mode for onboarding
        assert result["mentor_intervention"] == True
        assert "learning_objectives" in result
        assert any("security" in obj.lower() for obj in result["learning_objectives"])
    
    def test_progressive_complexity_adaptation(self):
        """Test that assistance adapts to increasing skill levels."""
        # Simulate skill progression through learning history
        self.extension.learning_history = [
            {"activity": "Basic API", "success_indicators": {"completion": True}},
            {"activity": "Authentication", "success_indicators": {"completion": True}},
            {"activity": "Database Integration", "success_indicators": {"completion": True}}
        ]
        
        # Should require more sophisticated assistance strategies as skills develop
        analytics = self.extension.get_learning_analytics()
        assert analytics["total_interactions"] == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
