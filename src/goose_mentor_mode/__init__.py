"""
Mentor Mode Goose Extension

An educational AI assistant that transforms development assistance from automation 
to guided learning experiences.
"""

__version__ = "0.1.0"

from .mentor_toolkit import MentorToolkit
from .mentor_engine import (
    MentorEngine, 
    MentorConfig,
    AssistanceLevel,
    LearningPhase,
    TimelinePressure,
    DeveloperContext
)

__all__ = [
    "MentorToolkit",
    "MentorEngine",
    "MentorConfig",
    "AssistanceLevel",
    "LearningPhase",
    "TimelinePressure",
    "DeveloperContext"
]
