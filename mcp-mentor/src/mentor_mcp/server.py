"""
Mentor Mode MCP Server

This module implements the Model Context Protocol (MCP) server for Mentor Mode,
providing educational AI assistance through sophisticated tool integration.
"""

import asyncio
import json
import os
from typing import Any, Dict, List, Optional, Sequence
from contextlib import AsyncExitStack

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolRequest,
    CallToolResult,
)
from pydantic import BaseModel

# Import our mentor mode logic
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src'))

from mentor_mode.core.mentor_engine import MentorEngine, DeveloperContext, AssistanceLevel
from mentor_mode.goose_extension.mentor_extension import MentorExtension, MentorConfig


class MentorAnalysisRequest(BaseModel):
    """Request model for mentor analysis."""
    user_request: str
    context: Optional[Dict[str, Any]] = None
    assistance_level: Optional[str] = None


class LearningCheckRequest(BaseModel):
    """Request model for learning validation."""
    concept: str
    user_explanation: str
    expected_understanding: List[str]


class ProgressTrackingRequest(BaseModel):
    """Request model for progress tracking."""
    activity: str
    success_indicators: Dict[str, Any]


class MentorMCPServer:
    """
    MCP Server implementation for Mentor Mode.
    
    Provides educational tools that can be integrated with Goose to transform
    AI assistance from automation to guided learning experiences.
    """
    
    def __init__(self):
        self.server = Server("mentor-mode")
        
        # Load configuration from environment variables
        self.config = self._load_env_config()
        
        # Initialize mentor components with configuration
        self.mentor_extension = MentorExtension()
        self.mentor_engine = MentorEngine()
        
        # Register tools
        self._register_tools()
    
    def _load_env_config(self) -> Dict[str, Any]:
        """Load configuration from environment variables."""
        config = {
            # Default assistance level (overrides automatic selection)
            "default_assistance_level": os.getenv("DEFAULT_ASSISTANCE_LEVEL", "").lower(),
            
            # Default developer context settings
            "default_learning_phase": os.getenv("LEARNING_PHASE", "skill_building").lower(),
            "default_timeline_pressure": os.getenv("TIMELINE_PRESSURE", "low").lower(),
            
            # Feature flags
            "enable_validation_checkpoints": os.getenv("ENABLE_VALIDATION_CHECKPOINTS", "true").lower() == "true",
            "max_guidance_depth": int(os.getenv("MAX_GUIDANCE_DEPTH", "3")),
            "force_mentor_mode": os.getenv("FORCE_MENTOR_MODE", "false").lower() == "true",
            
            # Skill level defaults (for new developers)
            "default_skill_level": int(os.getenv("DEFAULT_SKILL_LEVEL", "1")),  # 0-5 scale
            "developer_experience_months": int(os.getenv("DEVELOPER_EXPERIENCE_MONTHS", "12")),
        }
        
        # Validate enum values
        valid_assistance_levels = ["", "guided", "explained", "assisted", "automated"]
        valid_learning_phases = ["onboarding", "skill_building", "production"]
        valid_timeline_pressures = ["low", "medium", "high"]
        
        if config["default_assistance_level"] not in valid_assistance_levels:
            print(f"Warning: Invalid DEFAULT_ASSISTANCE_LEVEL '{config['default_assistance_level']}'. Using automatic selection.")
            config["default_assistance_level"] = ""
        
        if config["default_learning_phase"] not in valid_learning_phases:
            print(f"Warning: Invalid LEARNING_PHASE '{config['default_learning_phase']}'. Using 'skill_building'.")
            config["default_learning_phase"] = "skill_building"
        
        if config["default_timeline_pressure"] not in valid_timeline_pressures:
            print(f"Warning: Invalid TIMELINE_PRESSURE '{config['default_timeline_pressure']}'. Using 'low'.")
            config["default_timeline_pressure"] = "low"
        
        # Log configuration (excluding sensitive data)
        print(f"Mentor Mode Configuration Loaded:")
        print(f"  - Default Assistance Level: {config['default_assistance_level'] or 'AUTO'}")
        print(f"  - Learning Phase: {config['default_learning_phase']}")
        print(f"  - Timeline Pressure: {config['default_timeline_pressure']}")
        print(f"  - Validation Checkpoints: {config['enable_validation_checkpoints']}")
        print(f"  - Force Mentor Mode: {config['force_mentor_mode']}")
        
        return config
        
    def _register_tools(self) -> None:
        """Register all mentor mode tools with the MCP server."""
        
        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            """List available mentor mode tools."""
            return [
                Tool(
                    name="mentor_analyze_request",
                    description="Analyze a developer request for learning opportunities and generate educational response",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_request": {
                                "type": "string",
                                "description": "The developer's request or question"
                            },
                            "context": {
                                "type": "object",
                                "description": "Session context including timeline pressure, skills, etc.",
                                "properties": {
                                    "timeline_pressure": {"type": "string", "enum": ["low", "medium", "high"]},
                                    "learning_phase": {"type": "string", "enum": ["onboarding", "skill_building", "production"]},
                                    "complexity_indicators": {"type": "array", "items": {"type": "string"}},
                                    "skills": {"type": "object"}
                                }
                            },
                            "assistance_level": {
                                "type": "string",
                                "enum": ["guided", "explained", "assisted", "automated"],
                                "description": "Override assistance level if specified"
                            }
                        },
                        "required": ["user_request"]
                    }
                ),
                Tool(
                    name="mentor_learning_check",
                    description="Validate understanding of a concept through Socratic questioning",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "concept": {
                                "type": "string",
                                "description": "The concept being validated"
                            },
                            "user_explanation": {
                                "type": "string",
                                "description": "User's explanation of the concept"
                            },
                            "expected_understanding": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "Key points that should be understood"
                            }
                        },
                        "required": ["concept", "user_explanation", "expected_understanding"]
                    }
                ),
                Tool(
                    name="mentor_track_progress",
                    description="Track learning progress and provide recommendations",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "activity": {
                                "type": "string",
                                "description": "The learning activity completed"
                            },
                            "success_indicators": {
                                "type": "object",
                                "description": "Indicators of success or areas needing improvement"
                            }
                        },
                        "required": ["activity", "success_indicators"]
                    }
                ),
                Tool(
                    name="mentor_suggest_assistance_level",
                    description="Suggest appropriate assistance level based on context",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_request": {"type": "string"},
                            "context": {"type": "object"}
                        },
                        "required": ["user_request", "context"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> Sequence[TextContent]:
            """Handle tool calls from MCP clients."""
            
            if name == "mentor_analyze_request":
                return await self._handle_analyze_request(arguments)
            elif name == "mentor_learning_check":
                return await self._handle_learning_check(arguments)
            elif name == "mentor_track_progress":
                return await self._handle_track_progress(arguments)
            elif name == "mentor_suggest_assistance_level":
                return await self._handle_suggest_assistance_level(arguments)
            else:
                raise ValueError(f"Unknown tool: {name}")
    
    async def _handle_analyze_request(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Handle mentor analysis request."""
        try:
            request = MentorAnalysisRequest(**arguments)
            
            # Build context with environment variable defaults
            context = self._merge_context_with_config(request.context or {})
            
            # Apply environment variable overrides
            if request.assistance_level is None and self.config["default_assistance_level"]:
                request.assistance_level = self.config["default_assistance_level"]
            
            # Force mentor mode if configured
            if self.config["force_mentor_mode"]:
                context["force_mentor_intervention"] = True
            
            # Process through mentor extension
            result = self.mentor_extension.process_request(
                user_message=request.user_request,
                context=context
            )
            
            # Override assistance level if specified in config
            if request.assistance_level:
                if result.get("mentor_intervention"):
                    result["assistance_level"] = request.assistance_level
            
            # Format response for MCP
            if result.get("mentor_intervention"):
                response = {
                    "type": "mentor_response",
                    "assistance_level": result["assistance_level"],
                    "educational_content": result["educational_content"],
                    "learning_objectives": result["learning_objectives"],
                    "follow_up_questions": result["follow_up_questions"],
                    "validation_checkpoints": result["validation_checkpoints"],
                    "progress_indicators": result["progress_indicators"],
                    "config_applied": {
                        "assistance_level_source": "environment" if self.config["default_assistance_level"] else "automatic",
                        "learning_phase": context.get("learning_phase"),
                        "timeline_pressure": context.get("timeline_pressure")
                    }
                }
            else:
                response = {
                    "type": "pass_through",
                    "message": "No mentor intervention needed - proceed with normal processing",
                    "config_applied": {
                        "assistance_level_source": "environment" if self.config["default_assistance_level"] else "automatic"
                    }
                }
            
            return [TextContent(type="text", text=json.dumps(response, indent=2))]
            
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {str(e)}")]
    
    def _merge_context_with_config(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Merge user context with environment variable defaults."""
        merged = {}
        
        # Apply environment defaults first
        merged["learning_phase"] = self.config["default_learning_phase"]
        merged["timeline_pressure"] = self.config["default_timeline_pressure"]
        
        # Add skill defaults if not provided
        if "skills" not in context:
            merged["skills"] = {
                "default_level": self.config["default_skill_level"],
                "experience_months": self.config["developer_experience_months"]
            }
        
        # Override with user-provided context
        merged.update(context)
        
        # Add configuration flags
        merged["enable_validation_checkpoints"] = self.config["enable_validation_checkpoints"]
        merged["max_guidance_depth"] = self.config["max_guidance_depth"]
        
        return merged
    
    async def _handle_learning_check(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Handle learning validation check."""
        try:
            request = LearningCheckRequest(**arguments)
            
            # Analyze user's explanation
            understanding_score = self._assess_understanding(
                request.user_explanation,
                request.expected_understanding
            )
            
            # Generate follow-up questions or validation
            response = self._generate_learning_feedback(
                request.concept,
                request.user_explanation,
                understanding_score,
                request.expected_understanding
            )
            
            return [TextContent(type="text", text=json.dumps(response, indent=2))]
            
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {str(e)}")]
    
    async def _handle_track_progress(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Handle progress tracking."""
        try:
            request = ProgressTrackingRequest(**arguments)
            
            # Update progress in mentor extension
            self.mentor_extension.update_learning_progress(
                request.activity,
                request.success_indicators
            )
            
            # Get analytics and recommendations
            analytics = self.mentor_extension.get_learning_analytics()
            
            response = {
                "type": "progress_update",
                "activity": request.activity,
                "success_indicators": request.success_indicators,
                "analytics": analytics
            }
            
            return [TextContent(type="text", text=json.dumps(response, indent=2))]
            
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {str(e)}")]
    
    async def _handle_suggest_assistance_level(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Handle assistance level suggestion."""
        try:
            user_request = arguments["user_request"]
            context = arguments["context"]
            
            # Build developer context
            developer_context = self.mentor_extension._build_developer_context(context)
            
            # Get learning opportunities
            opportunities = self.mentor_engine._identify_learning_opportunities(user_request)
            
            # Suggest assistance level
            suggested_level = self.mentor_engine._select_assistance_level(
                developer_context, 
                opportunities
            )
            
            response = {
                "type": "assistance_suggestion",
                "suggested_level": suggested_level.value,
                "learning_opportunities": opportunities,
                "reasoning": self._explain_assistance_level_reasoning(
                    suggested_level, 
                    developer_context, 
                    opportunities
                )
            }
            
            return [TextContent(type="text", text=json.dumps(response, indent=2))]
            
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {str(e)}")]
    
    def _assess_understanding(self, explanation: str, expected_points: List[str]) -> float:
        """Assess quality of user's understanding based on their explanation."""
        # Simple keyword-based assessment (would be enhanced with NLP)
        explanation_lower = explanation.lower()
        points_covered = 0
        
        for point in expected_points:
            # Simple keyword matching - would be enhanced with semantic analysis
            if any(keyword.lower() in explanation_lower for keyword in point.split()):
                points_covered += 1
        
        return points_covered / len(expected_points) if expected_points else 0.0
    
    def _generate_learning_feedback(
        self, 
        concept: str, 
        explanation: str, 
        score: float, 
        expected_points: List[str]
    ) -> Dict[str, Any]:
        """Generate educational feedback based on understanding assessment."""
        
        if score >= 0.8:
            feedback_type = "excellent_understanding"
            message = f"Excellent understanding of {concept}! You've demonstrated strong grasp of the key concepts."
            next_steps = [
                f"Try applying {concept} to a different scenario",
                "Explore advanced aspects or edge cases",
                "Teach the concept to someone else to reinforce learning"
            ]
        elif score >= 0.6:
            feedback_type = "good_understanding"
            message = f"Good understanding of {concept}. You've covered most key points."
            missing_points = [point for point in expected_points 
                            if not any(keyword.lower() in explanation.lower() 
                                     for keyword in point.split())]
            next_steps = [
                f"Consider exploring: {', '.join(missing_points[:2])}",
                "Practice with additional examples",
                "Review the connection between concepts"
            ]
        else:
            feedback_type = "needs_reinforcement"
            message = f"You're on the right track with {concept}, but let's strengthen your understanding."
            next_steps = [
                "Let's break down the concept into smaller parts",
                "Would you like to explore some examples together?",
                "What specific aspects would you like to understand better?"
            ]
        
        return {
            "type": "learning_feedback",
            "concept": concept,
            "understanding_score": score,
            "feedback_type": feedback_type,
            "message": message,
            "next_steps": next_steps,
            "follow_up_questions": self._generate_follow_up_questions(concept, score)
        }
    
    def _generate_follow_up_questions(self, concept: str, score: float) -> List[str]:
        """Generate appropriate follow-up questions based on understanding level."""
        if score >= 0.8:
            return [
                f"How would you apply {concept} in a different context?",
                f"What are some potential limitations or edge cases with {concept}?",
                f"How does {concept} relate to other concepts you've learned?"
            ]
        elif score >= 0.6:
            return [
                f"Can you explain the key benefits of using {concept}?",
                f"What problems does {concept} solve?",
                f"How would you know when to apply {concept}?"
            ]
        else:
            return [
                f"What do you think is the main purpose of {concept}?",
                f"Can you describe {concept} in your own words?",
                f"What questions do you have about {concept}?"
            ]
    
    def _explain_assistance_level_reasoning(
        self, 
        level: AssistanceLevel, 
        context: DeveloperContext, 
        opportunities: Dict[str, Any]
    ) -> str:
        """Explain why a particular assistance level was suggested."""
        
        reasons = []
        
        if context.timeline_pressure == "high":
            reasons.append("High timeline pressure detected")
        if context.learning_phase == "onboarding":
            reasons.append("Developer in onboarding phase - maximum learning benefit")
        if opportunities["complexity_score"] > 2:
            reasons.append("High complexity detected - multiple learning opportunities")
        if opportunities["security_considerations"]:
            reasons.append("Security concepts involved - important learning area")
        
        base_explanation = f"Suggested {level.value} mode based on: {', '.join(reasons)}"
        
        if level == AssistanceLevel.GUIDED:
            return f"{base_explanation}. This will maximize learning through discovery and problem-solving."
        elif level == AssistanceLevel.EXPLAINED:
            return f"{base_explanation}. This will provide detailed educational context while solving the problem."
        elif level == AssistanceLevel.ASSISTED:
            return f"{base_explanation}. This will provide quick solution with key insights highlighted."
        else:  # AUTOMATED
            return f"{base_explanation}. This will prioritize efficiency while noting learning opportunities."

    async def run(self) -> None:
        """Run the MCP server."""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream, 
                write_stream, 
                self.server.create_initialization_options()
            )


def main() -> None:
    """Main entry point for the MCP server."""
    server = MentorMCPServer()
    asyncio.run(server.run())


if __name__ == "__main__":
    main()
