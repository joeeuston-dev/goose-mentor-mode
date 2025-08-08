"""
Mentor Mode MCP Extension

An educational AI assistant that transforms development assistance from automation 
to guided learning experiences through the Model Context Protocol (MCP).
"""

__version__ = "0.1.0"

from .server import MentorMCPServer, main
from .mentor_engine import (
    MentorEngine, 
    MentorExtension, 
    MentorConfig,
    AssistanceLevel,
    LearningPhase,
    TimelinePressure,
    DeveloperContext
)

__all__ = [
    "MentorMCPServer",
    "main",
    "MentorEngine",
    "MentorExtension", 
    "MentorConfig",
    "AssistanceLevel",
    "LearningPhase",
    "TimelinePressure",
    "DeveloperContext"
]
