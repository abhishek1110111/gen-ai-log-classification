from dotenv import load_dotenv
from groq import Groq
import re

load_dotenv()  # it load all variable from .env
client  = Groq()

def classification_with_llm(log_msg):
    ''' Classify the given log message using LLM model.'''
    prompt = f'''Classify the log message into one of these categories: 
        (1) Workflow Error, (2) Deprecation Warning.
        If you can't figure out a category, use "Unclassified".
        Put the category inside <category> </category> tags. 
        Log message: {log_msg}'''
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
    content = completion.choices[0].message.content
    print(content)
    match = re.search(r'<category>(.*)<\/category>', content, flags=re.DOTALL)
    category = "Unclassified"
    if match:
        category = match.group(1)

    return category

if __name__ == "__main__":
    print(classification_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classification_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classification_with_llm("System reboot initiated by user 12345."))