"""
Tests for Mentor Mode MCP Server
"""

import pytest
import json
from unittest.mock import AsyncMock, MagicMock

from mentor_mcp.server import MentorMCPServer


class TestMentorMCPServer:
    """Test suite for the MCP server implementation."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.server = MentorMCPServer()
    
    @pytest.mark.asyncio
    async def test_mentor_analyze_request_with_learning_opportunity(self):
        """Test analysis of request with learning opportunities."""
        arguments = {
            "user_request": "How do I implement JWT authentication in my Node.js API?",
            "context": {
                "timeline_pressure": "low",
                "learning_phase": "skill_building",
                "complexity_indicators": ["authentication", "security"],
                "skills": {"javascript": 3, "security": 1}
            }
        }
        
        result = await self.server._handle_analyze_request(arguments)
        
        # Should return educational response
        assert len(result) == 1
        response_data = json.loads(result[0].text)
        
        assert response_data["type"] == "mentor_response"
        assert "assistance_level" in response_data
        assert "educational_content" in response_data
        assert "learning_objectives" in response_data
        assert any("security" in obj.lower() for obj in response_data["learning_objectives"])
    
    @pytest.mark.asyncio
    async def test_mentor_analyze_request_no_intervention(self):
        """Test analysis of request that doesn't trigger intervention."""
        arguments = {
            "user_request": "What time is it?",
            "context": {
                "timeline_pressure": "high",
                "learning_phase": "production"
            }
        }
        
        result = await self.server._handle_analyze_request(arguments)
        
        # Should return pass-through response
        assert len(result) == 1
        response_data = json.loads(result[0].text)
        
        assert response_data["type"] == "pass_through"
        assert "No mentor intervention needed" in response_data["message"]
    
    @pytest.mark.asyncio
    async def test_mentor_learning_check_excellent_understanding(self):
        """Test learning check with excellent understanding."""
        arguments = {
            "concept": "JWT Authentication",
            "user_explanation": "JWT is a stateless authentication token that contains user information and security claims, providing secure API access without server-side sessions.",
            "expected_understanding": ["stateless authentication", "security considerations", "token structure"]
        }
        
        result = await self.server._handle_learning_check(arguments)
        
        assert len(result) == 1
        response_data = json.loads(result[0].text)
        
        assert response_data["type"] == "learning_feedback"
        assert response_data["understanding_score"] > 0.6  # Should have good understanding
        assert response_data["feedback_type"] in ["good_understanding", "excellent_understanding"]
    
    @pytest.mark.asyncio
    async def test_mentor_learning_check_needs_reinforcement(self):
        """Test learning check with understanding that needs reinforcement."""
        arguments = {
            "concept": "JWT Authentication",
            "user_explanation": "JWT is a token.",
            "expected_understanding": ["stateless authentication", "security considerations", "token structure"]
        }
        
        result = await self.server._handle_learning_check(arguments)
        
        assert len(result) == 1
        response_data = json.loads(result[0].text)
        
        assert response_data["type"] == "learning_feedback"
        assert response_data["understanding_score"] < 0.6  # Should have poor understanding
        assert response_data["feedback_type"] == "needs_reinforcement"
        assert len(response_data["follow_up_questions"]) > 0
    
    @pytest.mark.asyncio
    async def test_mentor_track_progress(self):
        """Test progress tracking functionality."""
        arguments = {
            "activity": "JWT Implementation Tutorial",
            "success_indicators": {
                "completed": True,
                "time_spent": 30,
                "concepts_learned": ["authentication", "security"],
                "understanding_demonstrated": True
            }
        }
        
        result = await self.server._handle_track_progress(arguments)
        
        assert len(result) == 1
        response_data = json.loads(result[0].text)
        
        assert response_data["type"] == "progress_update"
        assert response_data["activity"] == "JWT Implementation Tutorial"
        assert "analytics" in response_data
    
    @pytest.mark.asyncio
    async def test_mentor_suggest_assistance_level_guided(self):
        """Test assistance level suggestion for guided mode."""
        arguments = {
            "user_request": "How do I implement authentication?",
            "context": {
                "timeline_pressure": "low",
                "learning_phase": "onboarding",
                "complexity_indicators": ["authentication", "security"],
                "skills": {"security": 1}
            }
        }
        
        result = await self.server._handle_suggest_assistance_level(arguments)
        
        assert len(result) == 1
        response_data = json.loads(result[0].text)
        
        assert response_data["type"] == "assistance_suggestion"
        assert response_data["suggested_level"] == "guided"
        assert "learning_opportunities" in response_data
        assert "reasoning" in response_data
    
    @pytest.mark.asyncio
    async def test_mentor_suggest_assistance_level_automated(self):
        """Test assistance level suggestion for automated mode."""
        arguments = {
            "user_request": "Quick fix needed for authentication",
            "context": {
                "timeline_pressure": "high",
                "learning_phase": "production",
                "complexity_indicators": [],
                "skills": {"security": 5}
            }
        }
        
        result = await self.server._handle_suggest_assistance_level(arguments)
        
        assert len(result) == 1
        response_data = json.loads(result[0].text)
        
        assert response_data["type"] == "assistance_suggestion"
        assert response_data["suggested_level"] == "automated"
        assert "reasoning" in response_data
    
    def test_assess_understanding_high_score(self):
        """Test understanding assessment with high score."""
        explanation = "JWT provides stateless authentication using tokens with security claims"
        expected_points = ["stateless authentication", "security", "tokens"]
        
        score = self.server._assess_understanding(explanation, expected_points)
        
        assert score > 0.8  # Should score highly
    
    def test_assess_understanding_low_score(self):
        """Test understanding assessment with low score."""
        explanation = "JWT is a thing"
        expected_points = ["stateless authentication", "security considerations", "token structure"]
        
        score = self.server._assess_understanding(explanation, expected_points)
        
        assert score < 0.4  # Should score poorly
    
    def test_generate_follow_up_questions_excellent(self):
        """Test follow-up question generation for excellent understanding."""
        questions = self.server._generate_follow_up_questions("JWT Authentication", 0.9)
        
        assert len(questions) == 3
        assert any("different context" in q for q in questions)
        assert any("limitations" in q.lower() or "edge cases" in q.lower() for q in questions)
    
    def test_generate_follow_up_questions_needs_work(self):
        """Test follow-up question generation for poor understanding."""
        questions = self.server._generate_follow_up_questions("JWT Authentication", 0.3)
        
        assert len(questions) == 3
        assert any("main purpose" in q.lower() for q in questions)
        assert any("your own words" in q.lower() for q in questions)


class TestMentorMCPIntegration:
    """Test MCP integration aspects."""
    
    def test_tool_registration(self):
        """Test that all required tools are registered."""
        server = MentorMCPServer()
        
        # Verify server has the mentor tools registered
        # Note: In a real test, we'd test the actual MCP tool registration
        # This is a simplified version
        assert hasattr(server, '_handle_analyze_request')
        assert hasattr(server, '_handle_learning_check')
        assert hasattr(server, '_handle_track_progress')
        assert hasattr(server, '_handle_suggest_assistance_level')
    
    def test_server_initialization(self):
        """Test server initializes correctly."""
        server = MentorMCPServer()
        
        assert server.mentor_extension is not None
        assert server.mentor_engine is not None
        assert server.server.name == "mentor-mode"
