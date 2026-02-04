"""
OpenAI Integration for Career Chatbot
"""
import os
from openai import OpenAI
import json

class AICareerAdvisor:
    """Use OpenAI to provide intelligent career guidance"""
    
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("⚠️ OPENAI_API_KEY not found in .env file. Please add it.")
        
        # Initialize OpenAI client with just API key to avoid version conflicts
        self.client = OpenAI(api_key=api_key, timeout=30.0)
        self.model = "gpt-3.5-turbo"  # Cost-effective model
        self.conversation_history = []
    
    def get_career_guidance(self, user_message, user_profile=None, intent=None):
        """Get AI-powered career guidance response"""
        
        # Build context from user profile
        context = self._build_context(user_profile, intent)
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Create system prompt
        system_prompt = """You are an expert career guidance counselor with deep knowledge of:
- Career paths and job markets
- Skill development and learning strategies
- Educational programs (BCA, B.Tech, MBA, etc.)
- Industry trends and future job prospects
- Salary ranges and career growth

Your role:
1. Understand the user's background (field of study, skills, interests)
2. Provide personalized career recommendations
3. Suggest practical next steps and learning paths
4. Be encouraging and supportive
5. Give specific, actionable advice

Always:
- Be conversational and friendly
- Ask clarifying questions when needed
- Provide realistic salary ranges
- Mention multiple career options
- Include concrete next steps

Current user context:
""" + context
        
        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    *self.conversation_history
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            # Extract response
            assistant_message = response.choices[0].message.content
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}. Please try again."
    
    def _build_context(self, user_profile, intent):
        """Build context string from user profile"""
        if not user_profile:
            return "No user profile information available yet."
        
        context_parts = []
        
        if user_profile.get('name'):
            context_parts.append(f"User name: {user_profile['name']}")
        
        if user_profile.get('field_of_study'):
            context_parts.append(f"Field of study: {user_profile['field_of_study']}")
        
        if user_profile.get('current_skills'):
            skills = user_profile['current_skills']
            if isinstance(skills, str):
                skills = json.loads(skills)
            if skills:
                context_parts.append(f"Current skills: {', '.join(skills)}")
        
        if user_profile.get('interests'):
            context_parts.append(f"Interests: {user_profile['interests']}")
        
        if user_profile.get('experience_level'):
            context_parts.append(f"Experience level: {user_profile['experience_level']}")
        
        if intent:
            context_parts.append(f"Current conversation intent: {intent}")
        
        return "\n".join(context_parts) if context_parts else "New user, no background information yet."
    
    def extract_suggestions_from_response(self, response):
        """Extract actionable suggestions from AI response"""
        suggestions = []
        
        # Parse response for action items
        if "learn" in response.lower() or "skill" in response.lower():
            suggestions.append({
                "label": "📚 Learn recommended skills",
                "text": "What skills should I focus on learning first?"
            })
        
        if "career" in response.lower() or "job" in response.lower():
            suggestions.append({
                "label": "💼 Explore career options",
                "text": "Tell me more about the career options you mentioned"
            })
        
        if "project" in response.lower() or "portfolio" in response.lower():
            suggestions.append({
                "label": "🛠️ Build portfolio projects",
                "text": "What projects should I build for my portfolio?"
            })
        
        if "internship" in response.lower() or "experience" in response.lower():
            suggestions.append({
                "label": "🏢 Get practical experience",
                "text": "How can I gain practical work experience?"
            })
        
        if "interview" in response.lower() or "job search" in response.lower():
            suggestions.append({
                "label": "💬 Prepare for interviews",
                "text": "How should I prepare for job interviews?"
            })
        
        # If no suggestions extracted, provide defaults
        if not suggestions:
            suggestions = [
                {"label": "📖 Tell me more", "text": "Can you elaborate on that?"},
                {"label": "🎯 What's next?", "text": "What should I do next?"},
                {"label": "💡 Other options", "text": "Are there other career paths I should consider?"}
            ]
        
        return suggestions[:3]  # Return top 3 suggestions
    
    def clear_history(self):
        """Clear conversation history for new user"""
        self.conversation_history = []


# Global instance
_advisor = None

def get_advisor():
    """Get or create AI advisor instance"""
    global _advisor
    if _advisor is None:
        try:
            _advisor = AICareerAdvisor()
        except ValueError as e:
            print(f"⚠️ AI Advisor initialization failed: {e}")
            return None
    return _advisor
