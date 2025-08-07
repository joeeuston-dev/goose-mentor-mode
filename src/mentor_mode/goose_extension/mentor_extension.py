"""
Mentor Mode Extension for Goose

Provides educational mentoring capabilities that transform AI assistance
from automation to guided learning experiences.
"""

from typing import Dict, Any, Optional, List
from dataclasses import dataclass
import json

from ..core.mentor_engine import MentorEngine, DeveloperContext, AssistanceLevel, MentorResponse


@dataclass 
class MentorConfig:
    """Configuration for Mentor Mode extension."""
    default_assistance_level: str = "explained"
    learning_phase: str = "skill_building"  # onboarding, skill_building, production
    enable_validation_checkpoints: bool = True
    enable_progress_tracking: bool = True
    max_guidance_depth: int = 3
    

class MentorExtension:
    """
    Goose extension that provides educational mentoring capabilities.
    
    This extension intercepts developer requests and injects educational moments
    based on context, timeline pressure, and learning opportunities.
    """
    
    def __init__(self, config: Optional[MentorConfig] = None):
        self.config = config or MentorConfig()
        self.mentor_engine = MentorEngine()
        self.session_context = None
        self.learning_history = []
        
    def process_request(self, 
                       user_message: str, 
                       context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a user request through the mentor lens.
        
        Args:
            user_message: The developer's request
            context: Session context including timeline, task complexity, etc.
            
        Returns:
            Enhanced response with educational guidance
        """
        # Analyze request for learning opportunities
        developer_context = self._build_developer_context(context)
        
        # Check if this request should trigger mentor intervention
        if self._should_intervene(user_message, developer_context):
            # Generate educational response
            mentor_response = self.mentor_engine.process_request(
                user_message, 
                developer_context
            )
            
            # Format response for Goose integration
            return self._format_mentor_response(mentor_response, user_message)
        
        # Pass through for normal processing
        return {"proceed_normally": True, "original_message": user_message}
    
    def _build_developer_context(self, context: Dict[str, Any]) -> DeveloperContext:
        """Build developer context from session information."""
        return DeveloperContext(
            timeline_pressure=context.get("timeline_pressure", "medium"),
            learning_phase=self.config.learning_phase,
            task_complexity=self._assess_complexity(context),
            demonstrated_skills=context.get("skills", {})
        )
    
    def _should_intervene(self, message: str, context: DeveloperContext) -> bool:
        """
        Determine if mentor intervention is appropriate.
        
        Criteria:
        - Learning opportunity present
        - Not in high timeline pressure (unless automated mode)
        - Request complexity matches learning level
        """
        # Simple heuristics for MVP
        learning_keywords = [
            "how to", "why", "what is", "explain", "understand", 
            "implement", "create", "build", "setup", "configure"
        ]
        
        has_learning_opportunity = any(keyword in message.lower() for keyword in learning_keywords)
        
        # Don't intervene if timeline pressure is high unless in automated mode
        if context.timeline_pressure == "high" and self.config.default_assistance_level != "automated":
            return False
            
        return has_learning_opportunity
    
    def _assess_complexity(self, context: Dict[str, Any]) -> str:
        """Assess task complexity from context."""
        # Simple complexity assessment for MVP
        # This would be enhanced with more sophisticated analysis
        
        complexity_indicators = context.get("complexity_indicators", [])
        
        if len(complexity_indicators) >= 3:
            return "complex"
        elif len(complexity_indicators) >= 1:
            return "moderate"
        else:
            return "simple"
    
    def _format_mentor_response(self, response: MentorResponse, original_message: str) -> Dict[str, Any]:
        """Format mentor response for Goose integration."""
        return {
            "mentor_intervention": True,
            "assistance_level": response.assistance_level.value,
            "educational_content": response.content,
            "learning_objectives": response.learning_objectives,
            "follow_up_questions": response.follow_up_questions,
            "validation_checkpoints": response.validation_checkpoints,
            "progress_indicators": response.progress_indicators,
            "original_request": original_message
        }
    
    def update_learning_progress(self, 
                               learning_activity: str, 
                               success_indicators: Dict[str, Any]):
        """Update learning progress tracking."""
        self.learning_history.append({
            "activity": learning_activity,
            "timestamp": None,  # Would add proper timestamp
            "success_indicators": success_indicators
        })
    
    def get_learning_analytics(self) -> Dict[str, Any]:
        """Get learning analytics for progress tracking."""
        return {
            "total_interactions": len(self.learning_history),
            "learning_patterns": self._analyze_learning_patterns(),
            "skill_development": self._assess_skill_development(),
            "recommendation": self._generate_learning_recommendations()
        }
    
    def _analyze_learning_patterns(self) -> Dict[str, Any]:
        """Analyze patterns in learning interactions."""
        # Placeholder for learning pattern analysis
        return {"patterns": "analysis_placeholder"}
    
    def _assess_skill_development(self) -> Dict[str, Any]:
        """Assess skill development over time."""
        # Placeholder for skill development assessment
        return {"skills": "development_placeholder"}
    
    def _generate_learning_recommendations(self) -> List[str]:
        """Generate recommendations for continued learning."""
        # Placeholder for learning recommendations
        return ["Continue practicing fundamental concepts"]


# Extension registration function for Goose
def create_extension(config: Optional[Dict[str, Any]] = None) -> MentorExtension:
    """Create and configure the Mentor Mode extension."""
    mentor_config = MentorConfig()
    
    if config:
        # Update config from provided parameters
        for key, value in config.items():
            if hasattr(mentor_config, key):
                setattr(mentor_config, key, value)
    
    return MentorExtension(mentor_config)
