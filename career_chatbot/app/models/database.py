from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """User model to store student/user information"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    current_study = db.Column(db.String(200))
    current_skills = db.Column(db.Text)  # JSON string
    work_experience = db.Column(db.Text)  # JSON string
    study_status = db.Column(db.String(50), default='studying')  # studying, completed
    preferences = db.Column(db.Text)  # JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    conversation_history = db.relationship('ConversationHistory', backref='user', lazy=True, cascade='all, delete-orphan')
    career_recommendations = db.relationship('CareerRecommendation', backref='user', lazy=True, cascade='all, delete-orphan')

class ConversationHistory(db.Model):
    """Store conversation history between user and chatbot"""
    __tablename__ = 'conversation_history'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_message = db.Column(db.Text, nullable=False)
    bot_response = db.Column(db.Text, nullable=False)
    intent = db.Column(db.String(100))  # classified intent
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Career(db.Model):
    """Career paths and information"""
    __tablename__ = 'careers'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text)
    required_skills = db.Column(db.Text)  # JSON string
    required_education = db.Column(db.Text)  # JSON string
    average_salary = db.Column(db.String(100))
    job_growth_rate = db.Column(db.String(50))
    related_fields = db.Column(db.Text)  # JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CareerRecommendation(db.Model):
    """Store career recommendations for users"""
    __tablename__ = 'career_recommendations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    career_id = db.Column(db.Integer, db.ForeignKey('careers.id'), nullable=False)
    match_score = db.Column(db.Float)  # 0-100
    reasoning = db.Column(db.Text)
    next_steps = db.Column(db.Text)  # JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    career = db.relationship('Career', backref='recommendations')
