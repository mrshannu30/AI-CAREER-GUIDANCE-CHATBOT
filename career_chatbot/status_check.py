"""
Quick Status Check - Run this to verify everything
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("\n" + "="*70)
print("🔍 CHATBOT SYSTEM STATUS CHECK")
print("="*70)

# 1. Check imports
print("\n1️⃣ Checking imports...")
try:
    from flask import Flask
    print("   ✅ Flask is installed")
except:
    print("   ❌ Flask NOT found")

try:
    from app import create_app
    print("   ✅ Flask app can be created")
except Exception as e:
    print(f"   ❌ App creation error: {e}")
    sys.exit(1)

# 2. Check database
print("\n2️⃣ Checking database...")
try:
    from app.models.database import db, User, Career
    app = create_app()
    with app.app_context():
        user_count = User.query.count()
        career_count = Career.query.count()
    print(f"   ✅ Database is working")
    print(f"   📚 Users: {user_count}")
    print(f"   🎯 Careers: {career_count}")
except Exception as e:
    print(f"   ❌ Database error: {e}")

# 3. Check ML models
print("\n3️⃣ Checking ML Models...")
try:
    from ml_models.nlp_processor import NLPProcessor
    nlp = NLPProcessor()
    result = nlp.classify_and_extract("test message")
    print(f"   ✅ NLP Processor working")
    print(f"   Intent: {result['intent']}")
except Exception as e:
    print(f"   ❌ NLP Error: {e}")

try:
    from ml_models.career_recommender import CareerRecommendationEngine
    rec = CareerRecommendationEngine()
    print(f"   ✅ Career Recommender loaded")
except Exception as e:
    print(f"   ❌ Recommender Error: {e}")

# 4. Check API endpoints
print("\n4️⃣ Checking API Endpoints...")
try:
    from app.routes.chat import chat_bp
    from app.routes.user import user_bp
    print(f"   ✅ Chat routes loaded")
    print(f"   ✅ User routes loaded")
except Exception as e:
    print(f"   ❌ Route error: {e}")

# 5. Check static files
print("\n5️⃣ Checking static files...")
import os
static_path = os.path.join(os.path.dirname(__file__), 'app', 'static')
if os.path.exists(os.path.join(static_path, 'js', 'chat.js')):
    print(f"   ✅ chat.js found")
else:
    print(f"   ❌ chat.js NOT found")

if os.path.exists(os.path.join(static_path, 'css', 'chat.css')):
    print(f"   ✅ chat.css found")
else:
    print(f"   ❌ chat.css NOT found")

# 6. Test API
print("\n6️⃣ Testing API Endpoints...")
try:
    app = create_app()
    with app.test_client() as client:
        response = client.get('/')
        if response.status_code == 200:
            print(f"   ✅ / endpoint working (status: 200)")
        else:
            print(f"   ⚠️  / endpoint returned {response.status_code}")
        
        response = client.get('/chat')
        if response.status_code == 200:
            print(f"   ✅ /chat endpoint working (status: 200)")
        else:
            print(f"   ⚠️  /chat endpoint returned {response.status_code}")
except Exception as e:
    print(f"   ❌ API test error: {e}")

print("\n" + "="*70)
print("✅ STATUS CHECK COMPLETE!")
print("="*70)

print("""
Next Steps:
1. If all checks pass ✅, refresh your browser with Ctrl+F5
2. Ensure Flask server is running: python run.py
3. Go to: http://localhost:5000
4. Complete the email/name setup
5. Send a message

If any checks failed ❌:
- Check the error message above
- Run: python run.py
- Review the error logs
- Check DATABASE_SETUP.md for database issues
""")
print()
