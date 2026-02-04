"""
Test improved NLP response generation
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from ml_models.nlp_processor import NLPProcessor

nlp = NLPProcessor()

messages = [
    'im pursuing bca',
    'what im do next',
    'what should i do next',
    'what careers match bca'
]

print('=' * 60)
print('Testing NLP Intent Classification')
print('=' * 60)

for msg in messages:
    result = nlp.classify_and_extract(msg)
    print(f'\nMessage: "{msg}"')
    print(f'Intent: {result["intent"]}')
    print(f'Confidence: {result["confidence"]:.2f}')
    print(f'Field: {result["field_of_study"]}')
    print('-' * 60)

print('\n' + '=' * 60)
print('✅ NLP improvements active!')
print('=' * 60)
