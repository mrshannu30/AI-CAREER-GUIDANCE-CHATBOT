"""
User management routes
"""
from flask import Blueprint, request, jsonify, session
from app.models.database import db, User
import json

user_bp = Blueprint('user', __name__, url_prefix='/api/user')

@user_bp.route('/create', methods=['POST'])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        email = data.get('email')
        name = data.get('name')
        
        if not email or not name:
            return jsonify({'error': 'Email and name required'}), 400
        
        # Check if user exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            session['user_id'] = existing_user.id
            return jsonify({
                'user_id': existing_user.id,
                'email': existing_user.email,
                'name': existing_user.name,
                'message': 'Welcome back!'
            })
        
        # Create new user
        user = User(
            email=email,
            name=name,
            current_skills=json.dumps([]),
            work_experience=json.dumps([]),
            preferences=json.dumps({})
        )
        db.session.add(user)
        db.session.commit()
        
        session['user_id'] = user.id
        
        return jsonify({
            'user_id': user.id,
            'email': user.email,
            'name': user.name,
            'message': 'User created successfully!'
        }), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/get/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user information"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'current_study': user.current_study,
            'current_skills': json.loads(user.current_skills or '[]'),
            'work_experience': json.loads(user.work_experience or '[]'),
            'study_status': user.study_status,
            'preferences': json.loads(user.preferences or '{}')
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user information"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        data = request.get_json()
        
        if 'name' in data:
            user.name = data['name']
        if 'current_study' in data:
            user.current_study = data['current_study']
        if 'current_skills' in data:
            user.current_skills = json.dumps(data['current_skills'])
        if 'work_experience' in data:
            user.work_experience = json.dumps(data['work_experience'])
        if 'study_status' in data:
            user.study_status = data['study_status']
        if 'preferences' in data:
            user.preferences = json.dumps(data['preferences'])
        
        db.session.commit()
        
        return jsonify({
            'message': 'User updated successfully',
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'current_study': user.current_study,
                'current_skills': json.loads(user.current_skills or '[]'),
                'study_status': user.study_status
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    """Get complete user profile"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'profile': {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'current_study': user.current_study,
                'current_skills': json.loads(user.current_skills or '[]'),
                'work_experience': json.loads(user.work_experience or '[]'),
                'study_status': user.study_status,
                'preferences': json.loads(user.preferences or '{}'),
                'created_at': user.created_at.isoformat(),
                'updated_at': user.updated_at.isoformat()
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
