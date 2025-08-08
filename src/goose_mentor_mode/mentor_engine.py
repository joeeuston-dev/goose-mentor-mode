"""
Core mentor engine for educational AI assistance.
"""

import os
import re
from enum import Enum
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


class AssistanceLevel(str, Enum):
    """Assistance levels for mentor mode."""
    GUIDED = "guided"
    EXPLAINED = "explained"
    ASSISTED = "assisted"
    AUTOMATED = "automated"


class LearningPhase(str, Enum):
    """Learning phases for developers."""
    ONBOARDING = "onboarding"
    SKILL_BUILDING = "skill_building"
    PRODUCTION = "production"


class TimelinePressure(str, Enum):
    """Timeline pressure levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class DeveloperContext:
    """Context information about the developer and current situation."""
    timeline_pressure: str = "low"
    learning_phase: str = "skill_building"
    skills: Dict[str, int] = field(default_factory=dict)
    complexity_indicators: List[str] = field(default_factory=list)


@dataclass
class MentorConfig:
    """Configuration for mentor mode behavior."""
    default_assistance_level: Optional[str] = None
    learning_phase: str = "skill_building"
    timeline_pressure: str = "low"
    enable_validation_checkpoints: bool = True
    max_guidance_depth: int = 3
    force_mentor_mode: bool = False
    default_skill_level: int = 1
    developer_experience_months: int = 12

    @classmethod
    def from_environment(cls) -> 'MentorConfig':
        """Create config from environment variables."""
        return cls(
            default_assistance_level=os.environ.get('DEFAULT_ASSISTANCE_LEVEL'),
            learning_phase=os.environ.get('LEARNING_PHASE', 'skill_building'),
            timeline_pressure=os.environ.get('TIMELINE_PRESSURE', 'low'),
            enable_validation_checkpoints=os.environ.get('ENABLE_VALIDATION_CHECKPOINTS', 'true').lower() == 'true',
            max_guidance_depth=int(os.environ.get('MAX_GUIDANCE_DEPTH', '3')),
            force_mentor_mode=os.environ.get('FORCE_MENTOR_MODE', 'false').lower() == 'true',
            default_skill_level=int(os.environ.get('DEFAULT_SKILL_LEVEL', '1')),
            developer_experience_months=int(os.environ.get('DEVELOPER_EXPERIENCE_MONTHS', '12'))
        )


class MentorEngine:
    """Core mentor engine for educational AI assistance."""
    
    def __init__(self, config: Optional[MentorConfig] = None):
        """Initialize the mentor engine."""
        self.config = config or MentorConfig.from_environment()
        
        # Learning opportunity detection patterns
        self.security_patterns = [
            'jwt', 'authentication', 'auth', 'oauth', 'security', 'encryption', 
            'https', 'ssl', 'tls', 'cors', 'csrf', 'xss', 'sql injection',
            'password', 'hash', 'bcrypt', 'token', 'session'
        ]
        
        self.architecture_patterns = [
            'api', 'rest', 'graphql', 'microservice', 'database', 'schema',
            'design pattern', 'mvc', 'mvvm', 'repository pattern', 'dependency injection',
            'solid principles', 'architecture', 'scalability', 'performance'
        ]
        
        self.best_practice_patterns = [
            'error handling', 'validation', 'testing', 'unit test', 'integration test',
            'logging', 'monitoring', 'debugging', 'code review', 'documentation',
            'clean code', 'refactoring', 'optimization', 'best practice'
        ]
    
    def analyze_request(self, user_request: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Analyze a user request for learning opportunities."""
        # Merge context with config defaults
        merged_context = self._merge_context(context)
        
        # Detect learning opportunities
        learning_opportunities = self._detect_learning_opportunities(user_request)
        
        # Determine if intervention is needed
        if not learning_opportunities and not self.config.force_mentor_mode:
            return {
                "type": "pass_through",
                "message": "No mentor intervention needed for this request."
            }
        
        # Determine assistance level
        assistance_level = self._determine_assistance_level(user_request, merged_context, learning_opportunities)
        
        # Generate educational response
        return self._generate_educational_response(user_request, merged_context, assistance_level, learning_opportunities)
    
    def check_learning(self, concept: str, user_explanation: str, expected_understanding: List[str]) -> Dict[str, Any]:
        """Check understanding and provide feedback."""
        # Assess understanding score
        understanding_score = self._assess_understanding(user_explanation, expected_understanding)
        
        # Determine feedback type
        if understanding_score >= 0.8:
            feedback_type = "excellent_understanding"
        elif understanding_score >= 0.6:
            feedback_type = "good_understanding"
        else:
            feedback_type = "needs_reinforcement"
        
        # Generate follow-up questions
        follow_up_questions = self._generate_follow_up_questions(concept, understanding_score)
        
        return {
            "type": "learning_feedback",
            "concept": concept,
            "understanding_score": understanding_score,
            "feedback_type": feedback_type,
            "feedback": self._generate_understanding_feedback(feedback_type, understanding_score),
            "follow_up_questions": follow_up_questions,
            "next_steps": self._suggest_next_steps(concept, understanding_score)
        }
    
    def track_progress(self, activity: str, success_indicators: Dict[str, Any]) -> Dict[str, Any]:
        """Track learning progress and provide recommendations."""
        # Analyze success indicators
        analytics = self._analyze_progress(success_indicators)
        
        # Generate recommendations
        recommendations = self._generate_progress_recommendations(activity, analytics)
        
        return {
            "type": "progress_update",
            "activity": activity,
            "analytics": analytics,
            "recommendations": recommendations,
            "timestamp": "current_time"  # In real implementation, use actual timestamp
        }
    
    def suggest_assistance_level(self, user_request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Suggest optimal assistance level."""
        # Detect learning opportunities
        learning_opportunities = self._detect_learning_opportunities(user_request)
        
        # Determine suggested level
        suggested_level = self._determine_assistance_level(user_request, context, learning_opportunities)
        
        # Generate reasoning
        reasoning = self._generate_assistance_reasoning(suggested_level, context, learning_opportunities)
        
        return {
            "type": "assistance_suggestion",
            "suggested_level": suggested_level,
            "learning_opportunities": learning_opportunities,
            "reasoning": reasoning,
            "config_applied": {
                "default_assistance_level": self.config.default_assistance_level,
                "learning_phase": self.config.learning_phase,
                "timeline_pressure": self.config.timeline_pressure
            }
        }
    
    def _merge_context(self, context: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Merge provided context with config defaults."""
        merged = {
            "timeline_pressure": self.config.timeline_pressure,
            "learning_phase": self.config.learning_phase,
            "skills": {},
            "complexity_indicators": []
        }
        
        if context:
            merged.update(context)
        
        return merged
    
    def _detect_learning_opportunities(self, user_request: str) -> List[str]:
        """Detect learning opportunities in the request."""
        request_lower = user_request.lower()
        opportunities = []
        
        # Check for security concepts
        for pattern in self.security_patterns:
            if pattern in request_lower:
                opportunities.append("security")
                break
        
        # Check for architecture patterns
        for pattern in self.architecture_patterns:
            if pattern in request_lower:
                opportunities.append("architecture")
                break
        
        # Check for best practices
        for pattern in self.best_practice_patterns:
            if pattern in request_lower:
                opportunities.append("best_practices")
                break
        
        return opportunities
    
    def _determine_assistance_level(self, user_request: str, context: Dict[str, Any], opportunities: List[str]) -> str:
        """Determine the appropriate assistance level."""
        # Check for environment override
        if self.config.default_assistance_level:
            return self.config.default_assistance_level
        
        # High timeline pressure -> more automated
        if context.get("timeline_pressure") == "high":
            return AssistanceLevel.AUTOMATED
        
        # Learning opportunities + low pressure -> more guided
        if opportunities and context.get("timeline_pressure") == "low":
            if context.get("learning_phase") == "onboarding":
                return AssistanceLevel.GUIDED
            else:
                return AssistanceLevel.EXPLAINED
        
        # Production phase -> assisted
        if context.get("learning_phase") == "production":
            return AssistanceLevel.ASSISTED
        
        # Default
        return AssistanceLevel.EXPLAINED
    
    def _generate_educational_response(self, user_request: str, context: Dict[str, Any], 
                                     assistance_level: str, opportunities: List[str]) -> Dict[str, Any]:
        """Generate an educational response based on assistance level."""
        # Generate learning objectives based on opportunities
        learning_objectives = []
        if "security" in opportunities:
            learning_objectives.append("Understand security principles and best practices")
        if "architecture" in opportunities:
            learning_objectives.append("Learn architectural patterns and design principles")
        if "best_practices" in opportunities:
            learning_objectives.append("Apply development best practices")
        
        # Generate content based on assistance level
        if assistance_level == AssistanceLevel.GUIDED:
            educational_content = f"🔍 **GUIDED LEARNING OPPORTUNITY**\n\nGreat question! Let's explore this step-by-step. Before I share my approach, what do you think are the key considerations for: {user_request}?\n\nTake a moment to think about:\n- What are the main components involved?\n- What potential challenges might we face?\n- What security/best practices should we consider?"
            follow_up_questions = [
                "What approach would you try first?",
                "What potential issues do you foresee?",
                "How would you ensure this solution is secure and maintainable?"
            ]
        elif assistance_level == AssistanceLevel.EXPLAINED:
            educational_content = f"📚 **EDUCATIONAL EXPLANATION**\n\nLet me walk you through this step-by-step with detailed reasoning...\n\nFor your request: {user_request}\n\nHere's my approach with educational context:\n[Detailed explanation would go here]"
            follow_up_questions = [
                "Can you explain why this approach works?",
                "What would happen if we changed X?",
                "How would you adapt this for a different scenario?"
            ]
        elif assistance_level == AssistanceLevel.ASSISTED:
            educational_content = f"⚡ **QUICK SOLUTION WITH INSIGHTS**\n\nHere's the solution with key learning points highlighted:\n[Solution with insights would go here]"
            follow_up_questions = [
                "What's the most important concept here?",
                "How would you extend this solution?"
            ]
        else:  # AUTOMATED
            educational_content = f"🤖 **EFFICIENT SOLUTION**\n\nHere's the direct solution:\n[Direct solution would go here]"
            follow_up_questions = []
        
        return {
            "type": "mentor_response",
            "assistance_level": assistance_level,
            "educational_content": educational_content,
            "learning_objectives": learning_objectives,
            "follow_up_questions": follow_up_questions,
            "validation_checkpoints": [
                "Can explain the solution approach",
                "Understands key concepts involved"
            ] if self.config.enable_validation_checkpoints else []
        }
    
    def _assess_understanding(self, explanation: str, expected_points: List[str]) -> float:
        """Assess understanding based on explanation."""
        if not explanation or not expected_points:
            return 0.0
        
        explanation_lower = explanation.lower()
        matches = 0
        
        for point in expected_points:
            # Check if any key words from the expected point are mentioned
            point_words = point.lower().split()
            if any(word in explanation_lower for word in point_words):
                matches += 1
        
        # Calculate score based on matches and explanation length
        base_score = matches / len(expected_points)
        
        # Adjust for explanation quality (length as a proxy)
        if len(explanation) < 20:
            base_score *= 0.7  # Penalize very short explanations
        elif len(explanation) > 100:
            base_score *= 1.1  # Reward detailed explanations
        
        return min(1.0, base_score)
    
    def _generate_follow_up_questions(self, concept: str, understanding_score: float) -> List[str]:
        """Generate follow-up questions based on understanding level."""
        if understanding_score >= 0.8:
            # Excellent understanding - advanced questions
            return [
                f"How would you apply {concept} in a different context?",
                f"What are the limitations or edge cases of {concept}?",
                f"How would you explain {concept} to someone else?"
            ]
        elif understanding_score >= 0.6:
            # Good understanding - reinforcement questions
            return [
                f"Can you give an example of {concept} in practice?",
                f"What would happen if we didn't use {concept}?",
                f"What are the benefits of {concept}?"
            ]
        else:
            # Needs work - foundational questions
            return [
                f"What do you think is the main purpose of {concept}?",
                f"Can you describe {concept} in your own words?",
                f"What problem does {concept} solve?"
            ]
    
    def _generate_understanding_feedback(self, feedback_type: str, score: float) -> str:
        """Generate feedback based on understanding assessment."""
        if feedback_type == "excellent_understanding":
            return f"🎉 Excellent understanding! (Score: {score:.1f}) You've grasped the key concepts well."
        elif feedback_type == "good_understanding":
            return f"👍 Good understanding! (Score: {score:.1f}) You have the main ideas down."
        else:
            return f"🔄 Let's work on this together. (Score: {score:.1f}) There's room for improvement in understanding."
    
    def _suggest_next_steps(self, concept: str, understanding_score: float) -> List[str]:
        """Suggest next steps based on understanding."""
        if understanding_score >= 0.8:
            return [
                f"Try implementing {concept} in a real project",
                f"Research advanced applications of {concept}",
                f"Teach {concept} to someone else"
            ]
        elif understanding_score >= 0.6:
            return [
                f"Practice implementing {concept} with examples",
                f"Read more about {concept} best practices",
                f"Ask clarifying questions about unclear aspects"
            ]
        else:
            return [
                f"Review the fundamentals of {concept}",
                f"Work through basic examples step-by-step",
                f"Discuss {concept} with a mentor or peer"
            ]
    
    def _analyze_progress(self, success_indicators: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze progress based on success indicators."""
        analytics = {
            "completion_rate": 1.0 if success_indicators.get("completed", False) else 0.5,
            "time_efficiency": "good",  # Could be calculated from time_spent
            "concepts_mastered": success_indicators.get("concepts_learned", []),
            "understanding_demonstrated": success_indicators.get("understanding_demonstrated", False)
        }
        
        # Calculate overall score
        overall_score = 0.0
        if analytics["completion_rate"] > 0.8:
            overall_score += 0.4
        if analytics["understanding_demonstrated"]:
            overall_score += 0.3
        if len(analytics["concepts_mastered"]) > 0:
            overall_score += 0.3
        
        analytics["overall_score"] = overall_score
        return analytics
    
    def _generate_progress_recommendations(self, activity: str, analytics: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on progress analysis."""
        recommendations = []
        
        if analytics["overall_score"] >= 0.8:
            recommendations.append("🎉 Excellent progress! Consider tackling more advanced topics.")
            recommendations.append("📚 Share your knowledge with peers or write about what you learned.")
        elif analytics["overall_score"] >= 0.6:
            recommendations.append("👍 Good progress! Keep practicing these concepts.")
            recommendations.append("🔍 Review any areas where you felt uncertain.")
        else:
            recommendations.append("🔄 Take time to reinforce the fundamental concepts.")
            recommendations.append("🤝 Consider getting additional help or clarification.")
        
        return recommendations
    
    def _generate_assistance_reasoning(self, suggested_level: str, context: Dict[str, Any], 
                                     opportunities: List[str]) -> str:
        """Generate reasoning for assistance level suggestion."""
        reasons = []
        
        # Context-based reasoning
        if context.get("timeline_pressure") == "high":
            reasons.append("High timeline pressure suggests automated assistance")
        elif context.get("timeline_pressure") == "low":
            reasons.append("Low timeline pressure allows for guided learning")
        
        if context.get("learning_phase") == "onboarding":
            reasons.append("Onboarding phase benefits from guided discovery")
        elif context.get("learning_phase") == "production":
            reasons.append("Production phase requires efficient solutions")
        
        # Opportunity-based reasoning
        if opportunities:
            reasons.append(f"Learning opportunities detected: {', '.join(opportunities)}")
        
        return "; ".join(reasons)


class MentorExtension:
    """Extension class that wraps the mentor engine for Goose integration."""
    
    def __init__(self, config: Optional[MentorConfig] = None):
        """Initialize the mentor extension."""
        self.config = config or MentorConfig.from_environment()
        self.engine = MentorEngine(self.config)
    
    def process_request(self, user_request: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Process a user request through the mentor system."""
        return self.engine.analyze_request(user_request, context)
    
    def validate_learning(self, concept: str, user_explanation: str, expected_understanding: List[str]) -> Dict[str, Any]:
        """Validate learning through the mentor system."""
        return self.engine.check_learning(concept, user_explanation, expected_understanding)
    
    def track_progress(self, activity: str, success_indicators: Dict[str, Any]) -> Dict[str, Any]:
        """Track progress through the mentor system."""
        return self.engine.track_progress(activity, success_indicators)
    
    def suggest_assistance_level(self, user_request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Suggest assistance level through the mentor system."""
        return self.engine.suggest_assistance_level(user_request, context)
