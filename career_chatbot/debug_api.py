"""
Debug script to test API endpoints
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from app import create_app
from app.models.database import db, User
from ml_models.nlp_processor import NLPProcessor

# Initialize app
app = create_app()

print("=" * 60)
print("API Debug Test")
print("=" * 60)

# Test 1: Check if NLP processor loads
print("\n1️⃣ Testing NLP Processor...")
try:
    nlp = NLPProcessor()
    test_intent = nlp.classify_and_extract("I'm pursuing BCA")
    print(f"✅ NLP working: {test_intent}")
except Exception as e:
    print(f"❌ NLP Error: {e}")

# Test 2: Create a test user
print("\n2️⃣ Creating test user...")
with app.app_context():
    try:
        # Check if test user exists
        test_user = User.query.filter_by(email='test_api@example.com').first()
        if test_user:
            print(f"✅ Test user already exists: ID {test_user.id}")
            user_id = test_user.id
        else:
            user = User(
                email='test_api@example.com',
                name='API Test User',
                current_study='BCA',
                current_skills=json.dumps([]),
                work_experience=json.dumps([]),
                preferences=json.dumps({})
            )
            db.session.add(user)
            db.session.commit()
            print(f"✅ Test user created: ID {user.id}")
            user_id = user.id
    except Exception as e:
        print(f"❌ User creation error: {e}")
        sys.exit(1)

# Test 3: Test API endpoint locally
print("\n3️⃣ Testing API endpoint...")
with app.test_client() as client:
    try:
        response = client.post('/api/chat/message', 
            json={
                'message': "I'm pursuing BCA",
                'user_id': user_id
            },
            content_type='application/json'
        )
        print(f"✅ API Response Status: {response.status_code}")
        print(f"✅ API Response: {response.get_json()}")
    except Exception as e:
        print(f"❌ API Error: {e}")

print("\n" + "=" * 60)
print("Debug test complete!")
print("=" * 60)
