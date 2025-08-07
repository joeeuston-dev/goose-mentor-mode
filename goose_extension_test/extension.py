"""
Minimal Goose Extension Test

Testing if we can create a working Goose extension that provides mentor tools.
"""

from typing import Dict, Any

def mentor_test_intervention(user_request: str) -> Dict[str, Any]:
    """
    Test mentor intervention tool.
    
    Args:
        user_request: User's development question
        
    Returns:
        Educational response data
    """
    return {
        "status": "mentor_active",
        "original_request": user_request,
        "educational_response": f"🎓 Let's learn together! You asked: {user_request}. What do you think the first step might be?",
        "intervention_type": "guided_learning",
        "test_result": "SUCCESS - This tool was called by Goose!"
    }

def mentor_set_level(level: str = "guided") -> str:
    """
    Set mentor assistance level.
    
    Args:
        level: Assistance level (guided/explained/assisted/automated)
        
    Returns:
        Confirmation message
    """
    return f"✅ Mentor level set to: {level}"

# Extension metadata
__all__ = ["mentor_test_intervention", "mentor_set_level"]
