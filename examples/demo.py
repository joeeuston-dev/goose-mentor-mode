"""
Mentor Mode Demo

This demo shows Mentor Mode in action with realistic development scenarios,
demonstrating how it adapts educational assistance based on context.
"""

from src.mentor_mode.goose_extension.mentor_extension import MentorExtension, MentorConfig
from src.mentor_mode.core.mentor_engine import DeveloperContext
import json


def demo_scenario(title: str, user_request: str, context: dict, config: MentorConfig = None):
    """Run a demo scenario and display results."""
    print(f"\n{'='*60}")
    print(f"SCENARIO: {title}")
    print(f"{'='*60}")
    print(f"👤 USER REQUEST: {user_request}")
    print(f"🔍 CONTEXT: {json.dumps(context, indent=2)}")
    
    # Create extension with config
    extension = MentorExtension(config or MentorConfig())
    
    # Process request
    result = extension.process_request(user_request, context)
    
    if result.get("mentor_intervention"):
        print(f"\n🎓 MENTOR MODE ACTIVATED")
        print(f"📊 Assistance Level: {result['assistance_level'].upper()}")
        print(f"\n📝 Educational Content:")
        print(result['educational_content'])
        
        if result['learning_objectives']:
            print(f"\n🎯 Learning Objectives:")
            for obj in result['learning_objectives']:
                print(f"   • {obj}")
        
        if result['follow_up_questions']:
            print(f"\n❓ Follow-up Questions:")
            for q in result['follow_up_questions']:
                print(f"   • {q}")
        
        if result['validation_checkpoints']:
            print(f"\n✅ Validation Checkpoints:")
            for checkpoint in result['validation_checkpoints']:
                print(f"   • {checkpoint}")
    else:
        print(f"\n🤖 NORMAL MODE: {result.get('original_message', 'Processing normally')}")


def main():
    """Run comprehensive mentor mode demo."""
    print("🎓 MENTOR MODE DEMONSTRATION")
    print("Showing how AI assistance adapts to learning context and timeline pressure")
    
    # Scenario 1: Junior Developer in Guided Mode
    demo_scenario(
        "Junior Developer Learning JWT Authentication",
        "How do I implement JWT authentication in my Node.js API?",
        {
            "timeline_pressure": "low",
            "complexity_indicators": ["authentication", "security", "tokens"],
            "skills": {"javascript": 2, "security": 1, "apis": 2}
        },
        MentorConfig(learning_phase="onboarding")
    )
    
    # Scenario 2: Experienced Developer in Explained Mode
    demo_scenario(
        "Experienced Developer Learning New Concepts",
        "Explain how to implement microservices with Docker containers",
        {
            "timeline_pressure": "medium", 
            "complexity_indicators": ["microservices", "docker", "containers"],
            "skills": {"javascript": 4, "docker": 2, "architecture": 3}
        },
        MentorConfig(learning_phase="skill_building")
    )
    
    # Scenario 3: Production Crisis - Automated Mode
    demo_scenario(
        "Production Crisis - Need Quick Solution",
        "How do I fix this critical database connection error?",
        {
            "timeline_pressure": "high",
            "complexity_indicators": ["database", "error", "production"],
            "skills": {"javascript": 4, "database": 3, "debugging": 4}
        },
        MentorConfig(learning_phase="production")
    )
    
    # Scenario 4: Quick Task with Learning Insights
    demo_scenario(
        "Moderate Timeline - Quick Solution with Insights",
        "What's the best way to validate email addresses in JavaScript?",
        {
            "timeline_pressure": "medium",
            "complexity_indicators": ["validation", "regex"],
            "skills": {"javascript": 3, "validation": 2}
        },
        MentorConfig(default_assistance_level="assisted")
    )
    
    # Scenario 5: Non-learning Task - Should Pass Through
    demo_scenario(
        "Simple Task - No Educational Value",
        "Print 'Hello World' to console",
        {
            "timeline_pressure": "medium",
            "complexity_indicators": [],
            "skills": {"javascript": 3}
        }
    )
    
    print(f"\n{'='*60}")
    print("DEMO COMPLETE")
    print("Key Observations:")
    print("• Guided mode asks questions for discovery learning")
    print("• Explained mode provides detailed educational context")
    print("• Assisted mode gives quick solutions with key insights")
    print("• Automated mode prioritizes efficiency during time pressure")
    print("• Simple tasks pass through without intervention")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
