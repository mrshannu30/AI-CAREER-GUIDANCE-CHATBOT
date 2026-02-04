"""
Database Initialization Script
Creates all tables and seeds initial data
"""
import os
import sys
import json
from datetime import datetime

# Fix Windows encoding issue
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.models.database import db, Career, User

def init_database():
    """Initialize database with tables and seed data"""
    
    app = create_app('development')
    
    with app.app_context():
        print("🔄 Creating database tables...")
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Check if careers already exist
        existing_careers = Career.query.count()
        if existing_careers > 0:
            print(f"⚠️  Database already has {existing_careers} careers. Skipping seed...")
            return
        
        print("\n🌱 Seeding database with career data...")
        
        careers_data = [
            {
                'title': 'Software Engineer',
                'description': 'Develop software applications and systems',
                'required_skills': ['python', 'java', 'c++', 'javascript', 'sql', 'problem solving', 'algorithm design'],
                'required_education': ['computer science', 'engineering', 'information technology'],
                'average_salary': '$80,000 - $150,000',
                'job_growth_rate': 'High (13%)',
                'related_fields': ['web development', 'mobile development', 'systems design']
            },
            {
                'title': 'Data Scientist',
                'description': 'Analyze data and build machine learning models for insights',
                'required_skills': ['python', 'machine learning', 'data analysis', 'sql', 'statistics', 'analytics', 'tableau'],
                'required_education': ['computer science', 'data science', 'mathematics', 'statistics'],
                'average_salary': '$90,000 - $160,000',
                'job_growth_rate': 'Very High (36%)',
                'related_fields': ['data engineering', 'analytics', 'business intelligence']
            },
            {
                'title': 'AI/ML Engineer',
                'description': 'Build artificial intelligence and machine learning solutions',
                'required_skills': ['python', 'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'data science', 'nlp'],
                'required_education': ['computer science', 'artificial intelligence', 'data science'],
                'average_salary': '$100,000 - $180,000',
                'job_growth_rate': 'Very High (37%)',
                'related_fields': ['computer vision', 'nlp', 'robotics']
            },
            {
                'title': 'Web Developer',
                'description': 'Develop web applications and websites',
                'required_skills': ['javascript', 'html/css', 'web development', 'react', 'node.js', 'database', 'ui/ux'],
                'required_education': ['computer science', 'information technology', 'web development'],
                'average_salary': '$60,000 - $120,000',
                'job_growth_rate': 'High (13%)',
                'related_fields': ['frontend development', 'backend development', 'full-stack']
            },
            {
                'title': 'Mobile App Developer',
                'description': 'Develop mobile applications for iOS and Android',
                'required_skills': ['java', 'swift', 'kotlin', 'mobile development', 'ui/ux', 'problem solving', 'api integration'],
                'required_education': ['computer science', 'information technology'],
                'average_salary': '$70,000 - $130,000',
                'job_growth_rate': 'High (13%)',
                'related_fields': ['cross-platform development', 'game development', 'iot']
            },
            {
                'title': 'Cloud Architect',
                'description': 'Design and manage cloud infrastructure and solutions',
                'required_skills': ['cloud', 'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'infrastructure', 'networking', 'security'],
                'required_education': ['computer science', 'engineering', 'information technology'],
                'average_salary': '$120,000 - $180,000',
                'job_growth_rate': 'Very High (28%)',
                'related_fields': ['devops', 'infrastructure', 'security']
            },
            {
                'title': 'DevOps Engineer',
                'description': 'Automate and manage deployment pipelines and infrastructure',
                'required_skills': ['docker', 'kubernetes', 'ci/cd', 'cloud', 'scripting', 'linux', 'automation', 'git'],
                'required_education': ['computer science', 'information technology'],
                'average_salary': '$85,000 - $140,000',
                'job_growth_rate': 'High (15%)',
                'related_fields': ['cloud engineering', 'infrastructure', 'automation']
            },
            {
                'title': 'Business Analyst',
                'description': 'Analyze business processes and translate requirements',
                'required_skills': ['data analysis', 'analytics', 'communication', 'excel', 'problem solving', 'project management', 'sql'],
                'required_education': ['business', 'commerce', 'information technology', 'economics'],
                'average_salary': '$70,000 - $120,000',
                'job_growth_rate': 'Medium (11%)',
                'related_fields': ['product management', 'project management', 'consulting']
            },
            {
                'title': 'UX/UI Designer',
                'description': 'Design user interfaces and experiences for applications',
                'required_skills': ['ui/ux', 'design', 'creativity', 'prototyping', 'user research', 'figma', 'adobe xd', 'communication'],
                'required_education': ['design', 'arts', 'information technology', 'human-computer interaction'],
                'average_salary': '$65,000 - $120,000',
                'job_growth_rate': 'High (13%)',
                'related_fields': ['interaction design', 'graphic design', 'product design']
            },
            {
                'title': 'Product Manager',
                'description': 'Manage product development and strategy',
                'required_skills': ['project management', 'communication', 'leadership', 'analytics', 'strategic thinking', 'product sense'],
                'required_education': ['business', 'engineering', 'any'],
                'average_salary': '$100,000 - $160,000',
                'job_growth_rate': 'High (11%)',
                'related_fields': ['product strategy', 'business management', 'consulting']
            },
            {
                'title': 'Database Administrator',
                'description': 'Manage, maintain and secure databases',
                'required_skills': ['sql', 'database', 'problem solving', 'linux', 'security', 'backup/recovery', 'monitoring'],
                'required_education': ['computer science', 'information technology'],
                'average_salary': '$75,000 - $130,000',
                'job_growth_rate': 'Medium (8%)',
                'related_fields': ['database design', 'data engineering', 'systems administration']
            },
            {
                'title': 'Security Engineer',
                'description': 'Protect systems and networks from security threats',
                'required_skills': ['security', 'cryptography', 'network', 'problem solving', 'linux', 'penetration testing', 'compliance'],
                'required_education': ['computer science', 'engineering', 'cybersecurity'],
                'average_salary': '$95,000 - $150,000',
                'job_growth_rate': 'Very High (33%)',
                'related_fields': ['penetration testing', 'security architecture', 'compliance']
            }
        ]
        
        for career_data in careers_data:
            career = Career(
                title=career_data['title'],
                description=career_data['description'],
                required_skills=json.dumps(career_data['required_skills']),
                required_education=json.dumps(career_data['required_education']),
                average_salary=career_data['average_salary'],
                job_growth_rate=career_data['job_growth_rate'],
                related_fields=json.dumps(career_data['related_fields'])
            )
            db.session.add(career)
            print(f"  ✅ Added: {career_data['title']}")
        
        db.session.commit()
        print(f"\n✅ Database seeded with {len(careers_data)} careers!")
        print("\n" + "="*60)
        print("DATABASE INITIALIZATION COMPLETE!")
        print("="*60)
        print(f"📊 Tables created: Users, Conversations, Careers, Recommendations")
        print(f"📚 Careers loaded: {len(careers_data)}")
        print(f"🗄️  Database file: career_chatbot.db")
        print("\n✨ Your chatbot is ready to use!")
        print("\nStart the app with: python run.py")
        print("="*60 + "\n")


if __name__ == '__main__':
    try:
        init_database()
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
