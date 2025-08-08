"""
Mentor Mode MCP Extension

Provides educational AI mentorship capabilities through the Model Context Protocol (MCP),
transforming AI assistance from automation to guided learning experiences.
"""

from .server import MentorMCPServer, main

__version__ = "0.1.0"
__all__ = ["MentorMCPServer", "main"]
