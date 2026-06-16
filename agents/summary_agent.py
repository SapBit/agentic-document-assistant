from utils.openrouter import chat
from utils.prompts import SUMMARY_PROMPT


def summarize_document(document_text):
    try:
        prompt = SUMMARY_PROMPT.format(text=document_text)
        result = chat(prompt)

        if result['status'] == 'success':
            return {
                'status': 'success',
                'summary': result['content'],
                'model_used': 'openrouter'
            }
        else:
            return {
                'status': 'error',
                'error_message': f"Summarization agent error: {result['error_message']}",
                'summary': None
            }

    except Exception as e:
        return {
            'status': 'error',
            'error_message': f"Summarization agent error: {str(e)}",
            'summary': None
        }


def create_bullet_summary(document_text, num_points=5):
    try:
        prompt = f"""Create exactly {num_points} bullet points summarizing the most important information in this text.
Format as a simple bulleted list.

Text:
{document_text}"""

        result = chat(prompt)

        if result['status'] == 'success':
            return {
                'status': 'success',
                'bullet_points': result['content']
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


def extract_key_takeaways(document_text):
    try:
        prompt = f"""Extract and list the 3-5 most important key takeaways from this text.
These should be actionable insights or main lessons.

Text:
{document_text}"""

        result = chat(prompt)

        if result['status'] == 'success':
            return {
                'status': 'success',
                'takeaways': result['content']
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
