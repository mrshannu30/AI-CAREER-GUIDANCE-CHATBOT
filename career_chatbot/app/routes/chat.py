"""
Chat route and handler
"""
from flask import Blueprint, request, jsonify, session
from app.models.database import db, User, ConversationHistory, Career, CareerRecommendation
from ml_models.nlp_processor import NLPProcessor
from ml_models.career_recommender import CareerRecommendationEngine
from app.utils.response_generator import ChatbotResponseGenerator
from app.utils.groq_service import get_advisor
import json
from datetime import datetime

chat_bp = Blueprint('chat', __name__, url_prefix='/api/chat')

# Initialize ML components
nlp = NLPProcessor()
recommender = CareerRecommendationEngine()
response_gen = ChatbotResponseGenerator()
advisor = get_advisor()

@chat_bp.route('/message', methods=['POST'])
def handle_message():
    """Handle user message and generate bot response"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        user_id = data.get('user_id')
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get or create user
        if not user_id:
            user_id = session.get('user_id')
        
        if not user_id:
            return jsonify({'error': 'User ID required'}), 400
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        # Process message with NLP
        processed_data = nlp.classify_and_extract(user_message)
        intent = processed_data['intent']
        
        # Update user profile with extracted information
        if processed_data['field_of_study']:
            user.current_study = processed_data['field_of_study']
        
        if processed_data['skills']:
            current_skills = json.loads(user.current_skills or '[]')
            current_skills.extend(processed_data['skills'])
            user.current_skills = json.dumps(list(set(current_skills)))
        
        db.session.commit()
        
        # Use Groq for intelligent responses
        if advisor:
            # Build user profile for AI context
            user_profile = {
                'name': user.name,
                'field_of_study': user.current_study,
                'current_skills': user.current_skills,
                'experience_level': processed_data.get('experience_level', 'beginner')
            }
            
            # Get AI-powered response
            bot_response = advisor.get_career_guidance(
                user_message=user_message,
                user_profile=user_profile,
                intent=intent
            )
            
            # Extract suggestions from AI response
            suggestions = advisor.extract_suggestions_from_response(bot_response)
        else:
            # Fallback to rule-based generation if AI is not available
            bot_response, suggestions = generate_contextual_response(
                intent,
                user_message,
                user,
                processed_data
            )
        
        # Save conversation history
        conversation = ConversationHistory(
            user_id=user_id,
            user_message=user_message,
            bot_response=bot_response,
            intent=intent
        )
        db.session.add(conversation)
        db.session.commit()
        
        response_data = {
            'user_message': user_message,
            'bot_response': bot_response,
            'intent': intent,
            'confidence': processed_data['confidence']
        }
        
        # Add suggestions if available
        if suggestions:
            response_data['suggestions'] = suggestions
        
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def generate_contextual_response(intent, user_message, user, processed_data):
    """Generate contextual response based on intent and user state"""
    
    text_lower = user_message.lower()
    suggestions = []
    
    if intent == 'greetings':
        response = response_gen.generate_response('greetings')
        suggestions = [
            {'label': '🎓 Continue Studies', 'text': 'I want to continue my studies'},
            {'label': '💼 Find a Job', 'text': 'I want to find a job'}
        ]
        return response, suggestions
    
    elif intent == 'skill_assessment':
        user_skills = json.loads(user.current_skills or '[]')
        if user_skills:
            response = f"Great! I can see you have skills in: {', '.join(user_skills)}. Would you like to develop additional skills or explore careers that match these?"
            suggestions = [
                {'label': '📚 Develop More Skills', 'text': 'I want to develop more skills'},
                {'label': '🔍 Explore Careers', 'text': 'What careers match my skills'}
            ]
            return response, suggestions
        response = response_gen.generate_response('skill_assessment')
        return response, []
    
    elif intent == 'career_exploration':
        user_skills = json.loads(user.current_skills or '[]')
        user_education = user.current_study or 'not specified'
        experience = processed_data.get('experience_level', 'beginner')
        
        user_profile = {
            'skills': user_skills,
            'education': user_education,
            'experience_level': experience
        }
        
        recommendations = recommender.generate_recommendations(user_profile)
        
        if recommendations:
            response = response_gen.generate_recommendation_response(recommendations)
            suggestions = [
                {'label': '📖 Tell me more about Web Developer', 'text': 'Tell me more about Web Developer career'},
                {'label': '🚀 What skills do I need to develop', 'text': 'What skills should I develop for this career'}
            ]
            return response, suggestions
        response = response_gen.generate_response('career_exploration')
        return response, []
    
    elif intent == 'career_guidance':
        # Check if user is stating their study
        if 'pursuing' in text_lower or 'studying' in text_lower or 'doing' in text_lower:
            field_of_study = processed_data.get('field_of_study')
            if field_of_study:
                user.current_study = field_of_study
                db.session.commit()
                
                response = f"Great! I see you're pursuing **{field_of_study.upper()}**! That's an excellent field with plenty of career opportunities. Let me explore some career paths that would be perfect for you.\n\nTo give you the best recommendations, I need to know:\n1. **Your Skills**: What technical or professional skills do you have?\n2. **Your Interests**: What areas interest you most?\n\nFor example, for BCA students:\n- Skills: Python, JavaScript, Databases, Web Development\n- Interests: Web Development, Data Science, Cloud Computing, Mobile Apps"
                
                suggestions = [
                    {'label': '💻 My skills: Python, Java, Web Development', 'text': 'I have skills in Python, Java, and Web Development'},
                    {'label': '🎯 I\'m interested in: Data Science & AI', 'text': 'I\'m most interested in Data Science and AI careers'},
                    {'label': '📝 Tell me what I should learn', 'text': 'What skills should I develop for a good career'}
                ]
                return response, suggestions
        
        # Check if user is asking what to do next
        if any(phrase in text_lower for phrase in ['what do i do', 'what next', 'what should i do', 'how do i', 'what path']):
            user_study = user.current_study or processed_data.get('field_of_study')
            
            if user_study:
                response = f"Perfect! Since you're pursuing **{user_study}**, here's what I recommend:\n\n1. **Build Core Skills**: Focus on in-demand programming languages and tools\n2. **Gain Practical Experience**: Work on projects, internships, or freelancing\n3. **Learn In-Demand Tools**: Master frameworks and platforms\n4. **Build a Portfolio**: Create projects to showcase your skills\n5. **Network & Interview**: Connect with professionals and practice interviews\n\nWhat would you like to focus on first?"
                
                suggestions = [
                    {'label': '🎓 Continue studies', 'text': 'I want to continue my higher studies'},
                    {'label': '💼 Start job search', 'text': 'I want to start looking for a job'}
                ]
                return response, suggestions
            else:
                response = "I'd like to help you plan your career! Could you tell me:\n1. What are you currently studying?\n2. What are your main interests?\n3. What skills do you have?"
                return response, []
        
        # General career guidance - collect user information
        user_study = user.current_study or processed_data.get('field_of_study')
        
        if not user_study:
            response = "I'd like to help you plan your career! Could you tell me:\n1. **What are you studying or planning to study?**\n2. **What are your main interests?**\n3. **What skills do you have or want to develop?**"
            suggestions = [
                {'label': '📚 I\'m studying BCA', 'text': 'I\'m pursuing BCA'},
                {'label': '📚 I\'m studying B.Tech', 'text': 'I\'m doing B.Tech in Computer Science'},
                {'label': '🤔 Help me decide', 'text': 'I\'m not sure what to study'}
            ]
            return response, suggestions
        
        # Generate full career guidance
        user_skills = json.loads(user.current_skills or '[]')
        experience = processed_data.get('experience_level', 'beginner')
        
        user_profile = {
            'skills': user_skills,
            'education': user_study,
            'experience_level': experience
        }
        
        recommendations = recommender.generate_recommendations(user_profile)
        
        if recommendations:
            top_career = recommendations[0]['career']
            next_steps = recommender.generate_next_steps(user_profile, top_career)
            
            response = response_gen.generate_recommendation_response(recommendations)
            response += "\n" + response_gen.generate_next_steps_response(next_steps)
            
            # Save recommendations
            for rec in recommendations[:3]:
                career = Career.query.filter_by(title=rec['career']).first()
                if not career:
                    career = Career(title=rec['career'], description=rec['description'])
                    db.session.add(career)
                    db.session.flush()
                
                career_rec = CareerRecommendation(
                    user_id=user.id,
                    career_id=career.id,
                    match_score=rec['score'],
                    reasoning=f"Skill match: {rec['skill_match']:.0f}%, Education match: {rec['education_match']:.0f}%",
                    next_steps=json.dumps(next_steps)
                )
                db.session.add(career_rec)
            db.session.commit()
            
            suggestions = [
                {'label': '📖 Tell me more about Web Developer', 'text': 'Tell me more about Web Developer career'},
                {'label': '🚀 What skills do I need', 'text': 'What skills should I develop for this career'}
            ]
            return response, suggestions
        
        response = "Let me learn more about you to provide better guidance. What specific career areas interest you?"
        return response, []
    
    elif intent == 'study_path':
        field = processed_data.get('field_of_study')
        if field:
            response = response_gen.generate_study_plan(field)
        else:
            response = response_gen.generate_response('study_path')
        return response, []
    
    elif intent == 'skill_development':
        user_skills = json.loads(user.current_skills or '[]')
        if not user_skills:
            response = "To help with skill development, tell me which skills you already have and which ones you'd like to develop next?"
        else:
            response = f"Great! You already have: {', '.join(user_skills)}. Which new skills would you like to learn? Consider: Cloud technologies, AI/ML, Mobile Development, or other areas?"
        suggestions = [
            {'label': '☁️ Cloud Computing', 'text': 'I want to learn Cloud Computing'},
            {'label': '🤖 AI and Machine Learning', 'text': 'I\'m interested in AI and ML'}
        ]
        return response, suggestions
    
    elif intent == 'salary_info':
        response = response_gen.generate_response('salary_info')
        return response, []
    
    elif intent == 'job_search':
        response = response_gen.generate_response('job_search')
        return response, []
    
    else:
        response = response_gen.generate_response('general_info')
        return response, []


@chat_bp.route('/get-recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    """Get career recommendations for a user"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        user_skills = json.loads(user.current_skills or '[]')
        user_profile = {
            'skills': user_skills,
            'education': user.current_study or 'general',
            'experience_level': 'beginner'
        }
        
        recommendations = recommender.generate_recommendations(user_profile)
        
        return jsonify({
            'recommendations': recommendations
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@chat_bp.route('/get-conversation-history/<int:user_id>', methods=['GET'])
def get_conversation_history(user_id):
    """Get conversation history for a user"""
    try:
        conversations = ConversationHistory.query.filter_by(user_id=user_id).all()
        
        history = [{
            'user_message': conv.user_message,
            'bot_response': conv.bot_response,
            'intent': conv.intent,
            'timestamp': conv.timestamp.isoformat()
        } for conv in conversations]
        
        return jsonify({'history': history})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
