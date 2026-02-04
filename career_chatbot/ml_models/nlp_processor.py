import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib
import os

class IntentClassifier:
    """Classify user intent from messages"""
    
    def __init__(self):
        self.intents = [
            'career_guidance',
            'skill_assessment',
            'career_exploration',
            'study_path',
            'job_search',
            'skill_development',
            'salary_info',
            'education_path',
            'general_info',
            'greetings'
        ]
        
        self.training_data = {
            'greetings': [
                'hello', 'hi', 'hey', 'greetings', 'how are you',
                'what is your name', 'introduce yourself', 'who are you'
            ],
            'career_guidance': [
                'guide me', 'career guidance', 'help with career', 'build career',
                'career advice', 'what should i do next', 'what do i do next', 'what next',
                'career planning', 'career path', 'im pursuing', 'studying', 'in college'
            ],
            'skill_assessment': [
                'assess my skills', 'what are my strengths', 'evaluate skills',
                'skill test', 'analyze my abilities', 'my capabilities', 'rate my skills'
            ],
            'career_exploration': [
                'explore careers', 'what careers', 'career options', 'different careers',
                'career choices', 'job roles', 'professions', 'career match'
            ],
            'study_path': [
                'what to study', 'which course', 'study path', 'education',
                'degree', 'qualification', 'learning path', 'best degree'
            ],
            'job_search': [
                'find job', 'job hunting', 'apply job', 'job opening',
                'recruitment', 'hiring', 'vacancy', 'hiring companies'
            ],
            'skill_development': [
                'develop skills', 'learn new', 'improve skills', 'upskilling',
                'training', 'certification', 'learn', 'skills to learn'
            ],
            'salary_info': [
                'salary', 'pay', 'compensation', 'earnings', 'income',
                'how much', 'wage', 'salary range'
            ],
            'education_path': [
                'education', 'academic', 'university', 'college', 'school',
                'study', 'learning'
            ],
            'general_info': [
                'tell me', 'information', 'explain', 'what is', 'how does',
                'describe', 'details'
            ]
        }
        
        self.model = self._train_classifier()
    
    def _train_classifier(self):
        """Train intent classifier"""
        X = []
        y = []
        
        for intent, phrases in self.training_data.items():
            for phrase in phrases:
                X.append(phrase)
                y.append(intent)
        
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(lowercase=True, stop_words='english')),
            ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
        ])
        
        pipeline.fit(X, y)
        return pipeline
    
    def predict_intent(self, text):
        """Predict intent from user input"""
        intent = self.model.predict([text.lower()])[0]
        confidence = max(self.model.predict_proba([text.lower()])[0])
        return intent, confidence


class NLPProcessor:
    """Process natural language to extract information"""
    
    def __init__(self):
        self.intent_classifier = IntentClassifier()
    
    def extract_field_of_study(self, text):
        """Extract field of study from text"""
        fields = [
            'computer science', 'engineering', 'business', 'medicine',
            'arts', 'science', 'commerce', 'law', 'nursing',
            'psychology', 'education', 'architecture', 'finance',
            'marketing', 'data science', 'artificial intelligence',
            'machine learning', 'software engineering', 'information technology',
            'bca', 'b.tech', 'b.sc', 'ba', 'bba', 'bcom', 'mca', 'mba',
            'computer applications', 'it', 'ece', 'civil', 'mechanical',
            'electrical', 'electronics'
        ]
        
        text_lower = text.lower().replace('.', '')
        for field in fields:
            if field in text_lower:
                return field
        return None
    
    def extract_skills(self, text):
        """Extract skills mentioned in text"""
        skills_list = [
            'python', 'java', 'c++', 'javascript', 'sql', 'database',
            'web development', 'mobile development', 'ui/ux', 'data analysis',
            'machine learning', 'communication', 'leadership', 'project management',
            'problem solving', 'critical thinking', 'teamwork', 'creativity',
            'public speaking', 'writing', 'research', 'analytics',
            'excel', 'power bi', 'tableau', 'git', 'docker', 'cloud'
        ]
        
        text_lower = text.lower()
        found_skills = []
        for skill in skills_list:
            if skill in text_lower:
                found_skills.append(skill)
        
        return found_skills
    
    def extract_experience_level(self, text):
        """Extract experience level from text"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['beginner', 'no experience', 'just started', 'new to']):
            return 'beginner'
        elif any(word in text_lower for word in ['intermediate', 'some experience', 'few years', 'worked']):
            return 'intermediate'
        elif any(word in text_lower for word in ['advanced', 'expert', 'senior', 'many years', 'extensive']):
            return 'advanced'
        
        return 'beginner'
    
    def classify_and_extract(self, text):
        """Classify intent and extract relevant information"""
        intent, confidence = self.intent_classifier.predict_intent(text)
        
        field_of_study = self.extract_field_of_study(text)
        skills = self.extract_skills(text)
        experience_level = self.extract_experience_level(text)
        
        return {
            'intent': intent,
            'confidence': float(confidence),
            'field_of_study': field_of_study,
            'skills': skills,
            'experience_level': experience_level,
            'text': text
        }
