"""
Goose Mentor Mode MCP Server

This MCP server provides AI-powered mentoring capabilities for Goose,
transforming automation into guided learning experiences.
"""

import os
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

from goose_mentor_mode.mentor_engine import MentorEngine

# Initialize the MCP server
mcp = FastMCP("goose-mentor-mode")

# Initialize the mentor engine (create fresh instance)
mentor_engine = MentorEngine()

@mcp.tool()
def mentor_analyze_request(request: str, context: Optional[str] = None) -> Dict[str, Any]:
    """
    Analyze a user request for learning opportunities and suggest optimal assistance levels.
    
    Args:
        request: The user's request or question
        context: Optional context about the current task or project
        
    Returns:
        Analysis including learning opportunities, suggested assistance level, and educational context
    """
    try:
        # Merge environment configuration if available
        env_context = _get_environment_context()
        full_context = {
            **(context if isinstance(context, dict) else {}),
            **env_context
        }
        
        analysis = mentor_engine.analyze_request(request, full_context)
        return {
            "analysis": analysis,
            "status": "success"
        }
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Error analyzing request: {str(e)}")) from e

@mcp.tool()
def mentor_learning_check(
    concept: str, 
    user_response: Optional[str] = None,
    assistance_level: str = "guided"
) -> Dict[str, Any]:
    """
    Validate user understanding through Socratic questioning and provide learning feedback.
    
    Args:
        concept: The concept or topic to validate understanding for
        user_response: User's response to previous questions (optional)
        assistance_level: Level of assistance (guided, explained, assisted, automated)
        
    Returns:
        Learning validation results with questions, feedback, and next steps
    """
    try:
        # Merge environment configuration
        env_context = _get_environment_context()
        
        validation = mentor_engine.validate_learning(
            concept, 
            user_response=user_response, 
            assistance_level=assistance_level, 
            context=env_context
        )
        return {
            "validation": validation,
            "status": "success"
        }
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Error validating learning: {str(e)}")) from e

@mcp.tool()
def mentor_track_progress(
    topic: str, 
    interaction_data: Dict[str, Any],
    session_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Track learning progress and provide recommendations for continued development.
    
    Args:
        topic: The learning topic or subject area
        interaction_data: Data about the learning interaction
        session_id: Optional session identifier for progress tracking
        
    Returns:
        Progress tracking results with recommendations and metrics
    """
    try:
        # Merge environment configuration
        env_context = _get_environment_context()
        
        progress = mentor_engine.track_progress(
            topic, 
            interaction_data, 
            session_id=session_id,
            context=env_context
        )
        return {
            "progress": progress,
            "status": "success"
        }
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Error tracking progress: {str(e)}")) from e

@mcp.tool()
def mentor_suggest_assistance_level(
    request: str,
    user_profile: Optional[Dict[str, Any]] = None,
    context: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Suggest the optimal assistance level based on request complexity and user profile.
    
    Args:
        request: The user's request or task
        user_profile: Optional user profile information
        context: Optional context about the current situation
        
    Returns:
        Suggested assistance level with reasoning and alternative options
    """
    try:
        # Merge environment configuration and user profile
        env_context = _get_environment_context()
        full_context = {
            **(context or {}),
            **env_context
        }
        full_profile = {
            **(user_profile or {}),
            **_get_environment_profile()
        }
        
        suggestion = mentor_engine.suggest_assistance_level(
            request, 
            user_profile=full_profile, 
            context=full_context
        )
        return {
            "suggestion": suggestion,
            "status": "success"
        }
    except Exception as e:
        print(f"Error in mentor_suggest_assistance_level: {e}")
        return {
            "error": f"Error suggesting assistance level: {str(e)}",
            "status": "error"
        }

def _get_environment_context() -> Dict[str, Any]:
    """Get context configuration from environment variables."""
    return {
        "learning_phase": os.getenv("LEARNING_PHASE", "skill_building"),
        "timeline_pressure": os.getenv("TIMELINE_PRESSURE", "medium"),
        "enable_validation_checkpoints": os.getenv("ENABLE_VALIDATION_CHECKPOINTS", "true").lower() == "true",
        "max_guidance_depth": int(os.getenv("MAX_GUIDANCE_DEPTH", "3")),
        "force_mentor_mode": os.getenv("FORCE_MENTOR_MODE", "false").lower() == "true",
    }

def _get_environment_profile() -> Dict[str, Any]:
    """Get user profile from environment variables."""
    profile = {}
    
    if os.getenv("DEFAULT_SKILL_LEVEL"):
        profile["skill_level"] = int(os.getenv("DEFAULT_SKILL_LEVEL"))
    
    if os.getenv("DEVELOPER_EXPERIENCE_MONTHS"):
        profile["experience_months"] = int(os.getenv("DEVELOPER_EXPERIENCE_MONTHS"))
    
    # Override assistance level if set
    if os.getenv("DEFAULT_ASSISTANCE_LEVEL"):
        profile["preferred_assistance_level"] = os.getenv("DEFAULT_ASSISTANCE_LEVEL")
    
    return profile
