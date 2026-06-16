import os
import requests
import json

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = "openrouter/free"

def get_api_key():
    return os.getenv('OPENROUTER_API_KEY')

def get_model():
    return os.getenv('OPENROUTER_MODEL', OPENROUTER_MODEL)

def chat(prompt, system_prompt=None):
    api_key = get_api_key()
    if not api_key:
        return {'status': 'error', 'error_message': 'OPENROUTER_API_KEY not set in .env'}

    messages = []
    if system_prompt:
        messages.append({'role': 'system', 'content': system_prompt})
    messages.append({'role': 'user', 'content': prompt})

    try:
        response = requests.post(
            url=OPENROUTER_URL,
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
            },
            json={
                'model': get_model(),
                'messages': messages,
                'stream': False,
            },
            timeout=120
        )
        response.raise_for_status()
        data = response.json()
        content = data['choices'][0]['message']['content']
        return {'status': 'success', 'content': content}
    except Exception as e:
        return {'status': 'error', 'error_message': str(e)}
