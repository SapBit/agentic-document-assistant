from utils.openrouter import chat
from utils.prompts import DOCUMENT_CHECK_PROMPT


def check_and_improve_document(document_text):
    try:
        prompt = DOCUMENT_CHECK_PROMPT.format(text=document_text)
        result = chat(prompt)

        if result['status'] == 'success':
            return {
                'status': 'success',
                'analysis': result['content'],
                'model_used': result.get('model_used', 'openrouter')
            }
        else:
            return {
                'status': 'error',
                'error_message': f"Document agent error: {result['error_message']}",
                'analysis': None
            }

    except Exception as e:
        return {
            'status': 'error',
            'error_message': f"Document agent error: {str(e)}",
            'analysis': None
        }


def rewrite_section(section_text, instruction):
    try:
        prompt = f"""You are a professional writer. Rewrite the following text according to the instruction.

Instruction: {instruction}

Original text:
{section_text}

Provide only the rewritten text, no explanations."""

        result = chat(prompt)

        if result['status'] == 'success':
            return {
                'status': 'success',
                'rewritten_text': result['content']
            }
        else:
            return {
                'status': 'error',
                'error_message': result['error_message']
            }

    except Exception as e:
        return {
            'status': 'error',
            'error_message': str(e)
        }
