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
from .mentor_engine import MentorEngine, MentorExtension, MentorConfig


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


class AssistanceSuggestionRequest(BaseModel):
    """Request model for assistance level suggestion."""
    user_request: str
    context: Dict[str, Any]


class MentorMCPServer:
    """MCP server implementation for mentor mode."""
    
    def __init__(self):
        """Initialize the MCP server."""
        self.server = Server("mentor-mode")
        self.config = MentorConfig.from_environment()
        self.mentor_extension = MentorExtension(self.config)
        self.mentor_engine = self.mentor_extension.engine
        
        self._register_tools()
    
    def _register_tools(self):
        """Register MCP tools."""
        
        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            """List available mentor tools."""
            return [
                Tool(
                    name="mentor_analyze_request",
                    description="Analyze developer requests for learning opportunities and generate educational responses",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_request": {
                                "type": "string",
                                "description": "The developer's request or question"
                            },
                            "context": {
                                "type": "object",
                                "description": "Optional session context including timeline pressure, skills, etc.",
                                "properties": {
                                    "timeline_pressure": {"type": "string", "enum": ["low", "medium", "high"]},
                                    "learning_phase": {"type": "string", "enum": ["onboarding", "skill_building", "production"]},
                                    "skills": {"type": "object"},
                                    "complexity_indicators": {"type": "array", "items": {"type": "string"}}
                                }
                            },
                            "assistance_level": {
                                "type": "string",
                                "description": "Override assistance level",
                                "enum": ["guided", "explained", "assisted", "automated"]
                            }
                        },
                        "required": ["user_request"]
                    }
                ),
                Tool(
                    name="mentor_learning_check",
                    description="Validate understanding of concepts through Socratic questioning",
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
                            "user_request": {
                                "type": "string",
                                "description": "The developer's request"
                            },
                            "context": {
                                "type": "object",
                                "description": "Session context and developer information",
                                "properties": {
                                    "timeline_pressure": {"type": "string", "enum": ["low", "medium", "high"]},
                                    "learning_phase": {"type": "string", "enum": ["onboarding", "skill_building", "production"]},
                                    "skills": {"type": "object"},
                                    "complexity_indicators": {"type": "array", "items": {"type": "string"}}
                                }
                            }
                        },
                        "required": ["user_request", "context"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> Sequence[TextContent]:
            """Handle tool calls."""
            try:
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
            except Exception as e:
                error_response = {
                    "type": "error",
                    "error": str(e),
                    "tool": name
                }
                return [TextContent(type="text", text=json.dumps(error_response, indent=2))]
    
    async def _handle_analyze_request(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Handle mentor analysis requests."""
        request = MentorAnalysisRequest(**arguments)
        
        # Process through mentor engine
        result = self.mentor_engine.analyze_request(
            user_request=request.user_request,
            context=request.context
        )
        
        # If assistance level override is provided, update the result
        if request.assistance_level:
            if result.get("type") == "mentor_response":
                result["assistance_level"] = request.assistance_level
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    async def _handle_learning_check(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Handle learning validation requests."""
        request = LearningCheckRequest(**arguments)
        
        # Process through mentor engine
        result = self.mentor_engine.check_learning(
            concept=request.concept,
            user_explanation=request.user_explanation,
            expected_understanding=request.expected_understanding
        )
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    async def _handle_track_progress(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Handle progress tracking requests."""
        request = ProgressTrackingRequest(**arguments)
        
        # Process through mentor engine
        result = self.mentor_engine.track_progress(
            activity=request.activity,
            success_indicators=request.success_indicators
        )
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    async def _handle_suggest_assistance_level(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Handle assistance level suggestion requests."""
        request = AssistanceSuggestionRequest(**arguments)
        
        # Process through mentor engine
        result = self.mentor_engine.suggest_assistance_level(
            user_request=request.user_request,
            context=request.context
        )
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    def _assess_understanding(self, explanation: str, expected_points: List[str]) -> float:
        """Assess understanding based on explanation."""
        return self.mentor_engine._assess_understanding(explanation, expected_points)
    
    def _generate_follow_up_questions(self, concept: str, understanding_score: float) -> List[str]:
        """Generate follow-up questions based on understanding level."""
        return self.mentor_engine._generate_follow_up_questions(concept, understanding_score)


async def main():
    """Main entry point for the MCP server."""
    mentor_server = MentorMCPServer()
    
    # Use stdio_server to serve the MCP server over stdio
    async with stdio_server() as (read_stream, write_stream):
        await mentor_server.server.run(
            read_stream, 
            write_stream, 
            mentor_server.server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
