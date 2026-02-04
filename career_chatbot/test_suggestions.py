"""
Test suggestions with API
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from app import create_app
import json

app = create_app()

with app.test_client() as client:
    # Create test user
    response = client.post('/api/user/create', 
        json={'email': 'test_suggestions@example.com', 'name': 'Test User'},
        content_type='application/json'
    )
    
    user_id = response.get_json()['user_id']
    
    print('=' * 70)
    print('Testing Suggestions Feature')
    print('=' * 70)
    
    # Test message
    response = client.post('/api/chat/message',
        json={'message': 'im pursuing bca', 'user_id': user_id},
        content_type='application/json'
    )
    
    data = response.get_json()
    print(f'\n✅ Response Status: {response.status_code}')
    print(f'\n🤖 Bot Response:')
    print(data['bot_response'])
    
    if 'suggestions' in data:
        print(f'\n📌 Suggestions:')
        for i, sug in enumerate(data['suggestions'], 1):
            print(f'   {i}. {sug["label"]}')
            print(f'      -> {sug["text"]}')
    else:
        print('\n⚠️ No suggestions in response')

print('\n' + '=' * 70)
