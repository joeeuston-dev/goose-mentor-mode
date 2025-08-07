"""
Simple Goose Extension Test for Mentor Mode

This file tests if we can create a basic Goose tool that:
1. Can be called by Goose
2. Can intercept user requests
3. Can provide educational responses 
4. Can potentially modify conversation flow
"""

from typing import Dict, Any

def mentor_guided_help(user_question: str) -> str:
    """
    Provide guided educational assistance for development questions.
    
    This tool intercepts development questions and provides Socratic-style 
    guidance instead of direct answers to promote learning.
    
    Args:
        user_question: The user's development question or request
        
    Returns:
        Educational guidance with follow-up questions
    """
    
    # Simple educational response generator
    learning_triggers = ["how to", "how do i", "implement", "create", "build", "setup"]
    
    if any(trigger in user_question.lower() for trigger in learning_triggers):
        return f"""
🎓 **Mentor Mode Activated**

Instead of giving you the answer directly, let's learn together!

**Your Question**: {user_question}

**Let's Think Step by Step**:
1. What do you think are the main components needed?
2. Have you worked with similar problems before?
3. What would be your first step?

**Guiding Questions**:
- What have you already tried?
- What specific part are you stuck on?
- What do you expect the outcome to look like?

**Learning Objective**: By thinking through this yourself first, you'll understand the solution better and be able to apply similar thinking to future problems.

Would you like to try answering one of these questions first, or would you prefer a different assistance level?
"""
    else:
        return f"Processing: {user_question} (no educational intervention needed)"

def mentor_assistance_level(level: str = "guided") -> str:
    """
    Set the mentor assistance level for educational responses.
    
    Args:
        level: Assistance level - "guided", "explained", "assisted", or "automated"
        
    Returns:
        Confirmation of assistance level change
    """
    
    level_descriptions = {
        "guided": "Socratic questioning to help you discover the solution",
        "explained": "Step-by-step explanations with reasoning",
        "assisted": "Quick solutions with key insights highlighted", 
        "automated": "Direct answers with minimal educational overhead"
    }
    
    description = level_descriptions.get(level, "Unknown level")
    
    return f"""
🎯 **Mentor Assistance Level Set**: {level.title()}

**What this means**: {description}

**Current Settings**:
- Assistance Level: {level}
- Educational Mode: {"Active" if level != "automated" else "Minimal"}
- Learning Focus: {"High" if level == "guided" else "Medium" if level in ["explained", "assisted"] else "Low"}

Your next development questions will be handled with this assistance level.
"""

# Test if we can call these functions
if __name__ == "__main__":
    print("Testing Mentor Tools:")
    print("\n1. Testing guided help:")
    result1 = mentor_guided_help("How do I create a REST API in Python?")
    print(result1)
    
    print("\n" + "="*60)
    print("2. Testing assistance level setting:")
    result2 = mentor_assistance_level("guided")
    print(result2)
    
    print("\n" + "="*60)
    print("✅ Basic mentor logic works!")
    print("🤔 Key Question: Can Goose actually call these as tools?")
