import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

class CareerRecommendationEngine:
    """ML engine for career recommendations based on user profile"""
    
    def __init__(self):
        self.careers_database = self._load_careers_database()
        self.scaler = StandardScaler()
    
    def _load_careers_database(self):
        """Load career database with skills and requirements"""
        return {
            'Software Engineer': {
                'skills': ['python', 'java', 'c++', 'javascript', 'sql', 'problem solving', 'algorithm design'],
                'education': ['computer science', 'engineering', 'information technology'],
                'experience_level': 'intermediate',
                'salary_range': '80000-150000',
                'growth_rate': 'High',
                'description': 'Develop software applications and systems'
            },
            'Data Scientist': {
                'skills': ['python', 'machine learning', 'data analysis', 'sql', 'statistics', 'analytics', 'tableau'],
                'education': ['computer science', 'data science', 'mathematics', 'statistics'],
                'experience_level': 'intermediate',
                'salary_range': '90000-160000',
                'growth_rate': 'Very High',
                'description': 'Analyze data and build ML models for insights'
            },
            'AI/ML Engineer': {
                'skills': ['python', 'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'data science'],
                'education': ['computer science', 'artificial intelligence', 'data science'],
                'experience_level': 'advanced',
                'salary_range': '100000-180000',
                'growth_rate': 'Very High',
                'description': 'Build AI and machine learning solutions'
            },
            'Web Developer': {
                'skills': ['javascript', 'html/css', 'web development', 'react', 'node.js', 'database', 'ui/ux'],
                'education': ['computer science', 'information technology', 'web development'],
                'experience_level': 'beginner',
                'salary_range': '60000-120000',
                'growth_rate': 'High',
                'description': 'Develop web applications and websites'
            },
            'Mobile App Developer': {
                'skills': ['java', 'swift', 'kotlin', 'mobile development', 'ui/ux', 'problem solving'],
                'education': ['computer science', 'information technology'],
                'experience_level': 'intermediate',
                'salary_range': '70000-130000',
                'growth_rate': 'High',
                'description': 'Develop mobile applications'
            },
            'Cloud Architect': {
                'skills': ['cloud', 'aws', 'azure', 'docker', 'kubernetes', 'infrastructure', 'networking'],
                'education': ['computer science', 'engineering'],
                'experience_level': 'advanced',
                'salary_range': '120000-180000',
                'growth_rate': 'Very High',
                'description': 'Design and manage cloud infrastructure'
            },
            'DevOps Engineer': {
                'skills': ['docker', 'kubernetes', 'ci/cd', 'cloud', 'scripting', 'linux', 'automation'],
                'education': ['computer science', 'information technology'],
                'experience_level': 'intermediate',
                'salary_range': '85000-140000',
                'growth_rate': 'High',
                'description': 'Automate and manage deployment pipelines'
            },
            'Business Analyst': {
                'skills': ['data analysis', 'analytics', 'communication', 'excel', 'problem solving', 'project management'],
                'education': ['business', 'commerce', 'information technology'],
                'experience_level': 'intermediate',
                'salary_range': '70000-120000',
                'growth_rate': 'Medium',
                'description': 'Analyze business processes and requirements'
            },
            'UX/UI Designer': {
                'skills': ['ui/ux', 'design', 'creativity', 'prototyping', 'user research', 'figma', 'adobe'],
                'education': ['design', 'arts', 'information technology'],
                'experience_level': 'beginner',
                'salary_range': '65000-120000',
                'growth_rate': 'High',
                'description': 'Design user interfaces and experiences'
            },
            'Product Manager': {
                'skills': ['project management', 'communication', 'leadership', 'analytics', 'strategic thinking'],
                'education': ['business', 'engineering', 'any'],
                'experience_level': 'advanced',
                'salary_range': '100000-160000',
                'growth_rate': 'High',
                'description': 'Manage product development and strategy'
            },
            'Database Administrator': {
                'skills': ['sql', 'database', 'problem solving', 'linux', 'security', 'backup/recovery'],
                'education': ['computer science', 'information technology'],
                'experience_level': 'intermediate',
                'salary_range': '75000-130000',
                'growth_rate': 'Medium',
                'description': 'Manage and maintain databases'
            },
            'Security Engineer': {
                'skills': ['security', 'cryptography', 'network', 'problem solving', 'linux', 'penetration testing'],
                'education': ['computer science', 'engineering'],
                'experience_level': 'advanced',
                'salary_range': '95000-150000',
                'growth_rate': 'Very High',
                'description': 'Protect systems from security threats'
            }
        }
    
    def calculate_skill_match(self, user_skills, career_skills):
        """Calculate skill match score"""
        if not career_skills:
            return 0
        
        user_skills_set = set([s.lower() for s in user_skills])
        career_skills_set = set([s.lower() for s in career_skills])
        
        if not career_skills_set:
            return 0
        
        intersection = user_skills_set.intersection(career_skills_set)
        match_score = len(intersection) / len(career_skills_set)
        
        return match_score * 100
    
    def calculate_education_match(self, user_education, career_education):
        """Calculate education match score"""
        if 'any' in career_education:
            return 100
        
        user_edu_lower = user_education.lower() if user_education else ''
        
        for edu in career_education:
            if edu.lower() in user_edu_lower:
                return 100
        
        return 50  # Partial match
    
    def calculate_experience_match(self, user_exp, career_exp):
        """Calculate experience level match score"""
        experience_levels = {'beginner': 1, 'intermediate': 2, 'advanced': 3}
        
        user_exp_val = experience_levels.get(user_exp, 1)
        career_exp_val = experience_levels.get(career_exp, 1)
        
        if user_exp_val >= career_exp_val:
            return 100
        elif user_exp_val == career_exp_val - 1:
            return 75
        else:
            return 50
    
    def generate_recommendations(self, user_profile):
        """Generate career recommendations based on user profile"""
        recommendations = []
        
        user_skills = user_profile.get('skills', [])
        user_education = user_profile.get('education', '')
        user_experience = user_profile.get('experience_level', 'beginner')
        
        for career_title, career_info in self.careers_database.items():
            skill_score = self.calculate_skill_match(user_skills, career_info['skills'])
            education_score = self.calculate_education_match(user_education, career_info['education'])
            experience_score = self.calculate_experience_match(user_experience, career_info['experience_level'])
            
            # Weighted average: skills (40%), education (30%), experience (30%)
            total_score = (skill_score * 0.4) + (education_score * 0.3) + (experience_score * 0.3)
            
            if total_score > 40:  # Only include if match > 40%
                recommendations.append({
                    'career': career_title,
                    'score': total_score,
                    'skill_match': skill_score,
                    'education_match': education_score,
                    'experience_match': experience_score,
                    'description': career_info['description'],
                    'salary_range': career_info['salary_range'],
                    'growth_rate': career_info['growth_rate'],
                    'missing_skills': list(set(career_info['skills']) - set([s.lower() for s in user_skills]))
                })
        
        # Sort by score descending
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        
        return recommendations[:5]  # Return top 5
    
    def generate_next_steps(self, user_profile, recommended_career):
        """Generate actionable next steps for career development"""
        steps = []
        
        user_skills = set([s.lower() for s in user_profile.get('skills', [])])
        user_experience = user_profile.get('experience_level', 'beginner')
        
        career_info = self.careers_database.get(recommended_career, {})
        missing_skills = list(set([s.lower() for s in career_info.get('skills', [])]) - user_skills)
        
        # Generate steps based on missing skills and experience level
        steps.append({
            'priority': 'High',
            'action': 'Complete relevant education',
            'description': f"Ensure you have completed studies in {', '.join(career_info.get('education', []))}",
            'timeline': '3-6 months'
        })
        
        if missing_skills:
            steps.append({
                'priority': 'High',
                'action': 'Develop key skills',
                'description': f"Learn these skills: {', '.join(missing_skills[:3])}",
                'timeline': '6-12 months'
            })
        
        if user_experience == 'beginner':
            steps.append({
                'priority': 'High',
                'action': 'Build projects',
                'description': 'Create 2-3 portfolio projects to showcase your skills',
                'timeline': '3-6 months'
            })
        
        steps.append({
            'priority': 'Medium',
            'action': 'Get certification',
            'description': f'Consider certifications in {recommended_career}',
            'timeline': '3-6 months'
        })
        
        steps.append({
            'priority': 'Medium',
            'action': 'Network and internship',
            'description': 'Seek internship opportunities and build professional network',
            'timeline': 'Ongoing'
        })
        
        return steps
