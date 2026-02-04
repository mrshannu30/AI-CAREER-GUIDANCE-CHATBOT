"""
Flask app initialization
"""
from flask import Flask, render_template, session, request
from flask_cors import CORS
from config import config
import os
from dotenv import load_dotenv

load_dotenv()

def create_app(config_name='development'):
    """Create Flask application"""
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    from app.models.database import db
    db.init_app(app)
    CORS(app)
    
    # Register blueprints
    from app.routes.chat import chat_bp
    from app.routes.user import user_bp
    
    app.register_blueprint(chat_bp)
    app.register_blueprint(user_bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Routes
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/chat')
    def chat():
        return render_template('chat.html')
    
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500
    
    return app
