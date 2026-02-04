"""
Quick start guide and testing script
"""

import sys
import json

# Test the NLP Processor
print("=" * 60)
print("Testing NLP Processor...")
print("=" * 60)

try:
    from ml_models.nlp_processor import NLPProcessor
    
    nlp = NLPProcessor()
    
    # Test samples
    test_messages = [
        "Hello, I'm studying computer science",
        "I have skills in Python and machine learning",
        "What careers are available for data scientists?",
        "Help me build my career",
        "I'm a beginner with no experience",
    ]
    
    for msg in test_messages:
        result = nlp.classify_and_extract(msg)
        print(f"\nMessage: {msg}")
        print(f"Intent: {result['intent']} (confidence: {result['confidence']:.2f})")
        print(f"Skills detected: {result['skills']}")
        print(f"Field of study: {result['field_of_study']}")
        print(f"Experience level: {result['experience_level']}")
    
    print("\n✓ NLP Processor working correctly!")

except Exception as e:
    print(f"✗ Error testing NLP: {e}")
    import traceback
    traceback.print_exc()

# Test Career Recommender
print("\n" + "=" * 60)
print("Testing Career Recommender...")
print("=" * 60)

try:
    from ml_models.career_recommender import CareerRecommendationEngine
    
    recommender = CareerRecommendationEngine()
    
    # Test user profile
    user_profile = {
        'skills': ['python', 'machine learning', 'data analysis', 'sql'],
        'education': 'computer science',
        'experience_level': 'intermediate'
    }
    
    recommendations = recommender.generate_recommendations(user_profile)
    
    print(f"\nUser Profile: {user_profile}")
    print("\nTop Recommendations:")
    
    for i, rec in enumerate(recommendations[:3], 1):
        print(f"\n{i}. {rec['career']}")
        print(f"   Match Score: {rec['score']:.1f}%")
        print(f"   Description: {rec['description']}")
        print(f"   Salary: {rec['salary_range']}")
        print(f"   Growth: {rec['growth_rate']}")
    
    # Test next steps
    print("\n\nNext Steps for Top Career:")
    next_steps = recommender.generate_next_steps(user_profile, recommendations[0]['career'])
    for i, step in enumerate(next_steps, 1):
        print(f"\n{i}. {step['action']} (Priority: {step['priority']})")
        print(f"   {step['description']}")
        print(f"   Timeline: {step['timeline']}")
    
    print("\n✓ Career Recommender working correctly!")

except Exception as e:
    print(f"✗ Error testing Career Recommender: {e}")
    import traceback
    traceback.print_exc()

# Test Response Generator
print("\n" + "=" * 60)
print("Testing Response Generator...")
print("=" * 60)

try:
    from app.utils.response_generator import ChatbotResponseGenerator
    
    response_gen = ChatbotResponseGenerator()
    
    # Test various intents
    intents = ['greetings', 'career_guidance', 'skill_assessment', 'career_exploration']
    
    for intent in intents:
        response = response_gen.generate_response(intent)
        print(f"\nIntent: {intent}")
        print(f"Response: {response[:80]}..." if len(response) > 80 else f"Response: {response}")
    
    print("\n✓ Response Generator working correctly!")

except Exception as e:
    print(f"✗ Error testing Response Generator: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("All tests completed!")
print("=" * 60)
print("\nNext steps:")
print("1. Install dependencies: pip install -r requirements.txt")
print("2. Run the application: python run.py")
print("3. Open browser at: http://localhost:5000")
