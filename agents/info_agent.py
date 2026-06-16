from utils.openrouter import chat
from utils.prompts import INFO_COLLECTION_PROMPT, TOPIC_RESEARCH_PROMPT


def extract_information(document_text):
    try:
        prompt = INFO_COLLECTION_PROMPT.format(text=document_text)
        result = chat(prompt)

        if result['status'] == 'success':
            return {
                'status': 'success',
                'extracted_info': result['content'],
                'model_used': 'openrouter'
            }
        else:
            return {
                'status': 'error',
                'error_message': f"Information agent error: {result['error_message']}",
                'extracted_info': None
            }

    except Exception as e:
        return {
            'status': 'error',
            'error_message': f"Information agent error: {str(e)}",
            'extracted_info': None
        }


def collect_topic_information(topic):
    try:
        prompt = TOPIC_RESEARCH_PROMPT.format(topic=topic)
        result = chat(prompt)

        if result['status'] == 'success':
            return {
                'status': 'success',
                'research': result['content'],
                'topic': topic
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


def extract_entities_and_facts(document_text):
    try:
        prompt = f"""Extract all important entities (people, organizations, concepts, products) and key facts from this text.
Format as:

ENTITIES:
- (list each entity)

FACTS:
- (list each important fact)

Text:
{document_text}"""

        result = chat(prompt)

        if result['status'] == 'success':
            return {
                'status': 'success',
                'entities_and_facts': result['content']
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


def generate_report(document_text, report_type='comprehensive'):
    try:
        if report_type == 'executive':
            prompt = f"""Create an executive report of this document including:
1. Overview
2. Key Findings
3. Recommendations
4. Next Steps

Document:
{document_text}"""
        elif report_type == 'action_items':
            prompt = f"""Extract all action items and tasks from this document.
Format as a prioritized action list.

Document:
{document_text}"""
        else:
            prompt = f"""Create a comprehensive report analyzing:
1. Content Overview
2. Main Themes
3. Key Data Points
4. Critical Information
5. Implications

Document:
{document_text}"""

        result = chat(prompt)

        if result['status'] == 'success':
            return {
                'status': 'success',
                'report': result['content'],
                'report_type': report_type
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
