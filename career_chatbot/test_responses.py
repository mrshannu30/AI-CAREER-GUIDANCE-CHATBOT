"""
Test improved response generation
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from app import create_app
from app.models.database import db, User
import json

app = create_app()

with app.test_client() as client:
    # Create test user
    response = client.post('/api/user/create', 
        json={'email': 'test_response@example.com', 'name': 'Test User'},
        content_type='application/json'
    )
    
    data = response.get_json()
    user_id = data['user_id']
    print(f"✅ Created user: {user_id}")
    print()
    
    # Test different messages
    test_messages = [
        ('im pursuing bca', 'Stating their study'),
        ('what im do next', 'Asking what to do next'),
        ('what careers match bca', 'Asking about careers')
    ]
    
    print('=' * 70)
    print('Testing Response Generation')
    print('=' * 70)
    
    for message, description in test_messages:
        print(f'\n📝 Message: "{message}"')
        print(f'📋 Description: {description}')
        print('-' * 70)
        
        response = client.post('/api/chat/message',
            json={'message': message, 'user_id': user_id},
            content_type='application/json'
        )
        
        data = response.get_json()
        if response.status_code == 200:
            print(f'✅ Intent: {data["intent"]}')
            print(f'🤖 Response:\n{data["bot_response"]}')
        else:
            print(f'❌ Error: {data.get("error", "Unknown error")}')
        
        print()

print('=' * 70)
print('✅ Response generation test complete!')
print('=' * 70)
