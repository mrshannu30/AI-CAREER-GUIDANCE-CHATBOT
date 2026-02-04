"""
Chatbot response generator
"""
import json
from datetime import datetime

class ChatbotResponseGenerator:
    """Generate contextual responses for the chatbot"""
    
    def __init__(self):
        self.responses = self._load_response_templates()
    
    def _load_response_templates(self):
        """Load response templates for different intents"""
        return {
            'greetings': [
                "Hello! I'm your AI Career Guidance Assistant. I'm here to help you plan your career journey. How can I assist you today?",
                "Hi there! Welcome to Career Guidance Bot. Let's explore your career options together. What would you like to know?",
                "Greetings! I'm ready to guide you through your career path. What's on your mind?"
            ],
            'career_guidance': [
                "I'd be happy to guide you! To provide the best career recommendations, could you tell me:\n1. What are you currently studying?\n2. What skills do you have?\n3. What are your interests?",
                "Great! Let's build your career path together. First, help me understand your background. What's your current field of study or expertise?",
                "Career guidance is my specialty! Tell me more about yourself - your education, skills, and career goals."
            ],
            'skill_assessment': [
                "Let's assess your skills! Based on our conversation, I can identify your strengths and areas for improvement. What skills would you like to discuss?",
                "Skill assessment is important for career planning. Tell me about the technical and soft skills you currently possess.",
                "To evaluate your capabilities, please share your key skills and experience."
            ],
            'career_exploration': [
                "There are many exciting career paths available! Based on your profile, here are some careers that might suit you:",
                "Let's explore career options together! Different fields offer unique opportunities. What area interests you?",
                "Career exploration is a great starting point. Tell me what industries or roles interest you."
            ],
            'study_path': [
                "Choosing the right study path is crucial! What subject or field interests you the most?",
                "For career development, the right education is key. What are you thinking of studying?",
                "Let me help you choose the perfect study path. What are your academic interests?"
            ],
            'job_search': [
                "Job searching can be exciting! Based on your profile, I can suggest suitable positions and companies. What type of role interests you?",
                "Let's find the right job for you! Tell me about your experience and what you're looking for in a role.",
                "Job hunting is easier with the right strategy. What roles are you interested in?"
            ],
            'skill_development': [
                "Continuous learning is essential for career growth! What skills would you like to develop further?",
                "Great mindset! Upskilling opens many doors. Which skills should we focus on?",
                "Skill development is a lifetime journey. What new skills interest you?"
            ],
            'salary_info': [
                "Salary expectations are reasonable to discuss! The salary depends on your role, experience, and location. Which career are you interested in?",
                "Based on the career path, here's typical salary information:",
                "Salary ranges vary by role and experience. Tell me which career interests you, and I'll provide salary insights."
            ],
            'education_path': [
                "Education is the foundation of your career. What level of education are you pursuing?",
                "Your educational background matters for career planning. Tell me about your current or planned education.",
                "Let's map out your educational journey. What are you studying?"
            ],
            'general_info': [
                "I'd be happy to provide information! Could you be more specific about what you'd like to know?",
                "Sure! Tell me more about what you'd like to learn.",
                "That's a great question. Provide more details so I can give you the best information."
            ]
        }
    
    def generate_response(self, intent, context=None):
        """Generate a response based on intent"""
        import random
        
        response_list = self.responses.get(intent, self.responses['general_info'])
        return random.choice(response_list)
    
    def generate_recommendation_response(self, recommendations):
        """Generate response with career recommendations"""
        if not recommendations:
            return "Based on your profile, I'm analyzing the best career paths for you. Could you provide more information about your skills?"
        
        response = "Based on your profile, here are the top career recommendations for you:\n\n"
        
        for i, rec in enumerate(recommendations[:3], 1):
            response += f"{i}. **{rec['career']}** (Match: {rec['score']:.0f}%)\n"
            response += f"   - Description: {rec['description']}\n"
            response += f"   - Salary Range: {rec['salary_range']}\n"
            response += f"   - Growth Rate: {rec['growth_rate']}\n"
            if rec['missing_skills']:
                response += f"   - Skills to develop: {', '.join(rec['missing_skills'][:2])}\n"
            response += "\n"
        
        return response
    
    def generate_next_steps_response(self, steps):
        """Generate response with next steps"""
        response = "Here's your personalized career development roadmap:\n\n"
        
        for i, step in enumerate(steps, 1):
            response += f"{i}. **{step['action']}** (Priority: {step['priority']})\n"
            response += f"   - Description: {step['description']}\n"
            response += f"   - Timeline: {step['timeline']}\n\n"
        
        return response
    
    def generate_study_plan(self, field_of_study):
        """Generate a study plan based on field"""
        plans = {
            'computer science': {
                'courses': ['Data Structures', 'Algorithms', 'Database Management', 'Web Development', 'AI/ML'],
                'projects': ['Build a web app', 'Create a data analysis tool', 'Develop ML model'],
                'timeline': '2-3 years'
            },
            'data science': {
                'courses': ['Statistics', 'Data Analysis', 'Machine Learning', 'Big Data', 'Data Visualization'],
                'projects': ['Predictive analysis project', 'Data dashboard', 'Classification model'],
                'timeline': '2-3 years'
            },
            'engineering': {
                'courses': ['Physics', 'Mathematics', 'Systems Design', 'Project Management'],
                'projects': ['Hardware project', 'System optimization', 'Research paper'],
                'timeline': '4 years'
            },
            'business': {
                'courses': ['Management', 'Finance', 'Marketing', 'Business Strategy'],
                'projects': ['Business plan', 'Market analysis', 'Case study'],
                'timeline': '3-4 years'
            }
        }
        
        field_lower = field_of_study.lower() if field_of_study else ''
        
        for key, plan in plans.items():
            if key in field_lower:
                response = f"Study Plan for {field_of_study}:\n\n"
                response += f"**Duration**: {plan['timeline']}\n\n"
                response += "**Key Courses**:\n"
                for course in plan['courses']:
                    response += f"- {course}\n"
                response += "\n**Projects**:\n"
                for project in plan['projects']:
                    response += f"- {project}\n"
                return response
        
        return "I'll create a customized study plan for you. Tell me more about your field of interest!"
