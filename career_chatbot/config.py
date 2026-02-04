import os
from datetime import timedelta

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # Database configuration
    DB_TYPE = os.environ.get('DB_TYPE', 'sqlite')
    
    if DB_TYPE == 'mysql':
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            f"mysql+pymysql://{os.environ.get('DB_USER', 'root')}:{os.environ.get('DB_PASSWORD', 'password')}@{os.environ.get('DB_HOST', 'localhost')}:{os.environ.get('DB_PORT', 3306)}/{os.environ.get('DB_NAME', 'career_chatbot')}"
    else:
        # SQLite - store in project root
        db_path = os.path.join(os.path.dirname(__file__), 'career_chatbot.db')
        SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_ECHO = True  # Log all SQL queries

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
