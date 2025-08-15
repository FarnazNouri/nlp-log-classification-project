from dotenv import load_dotenv
from groq import Groq
import re

load_dotenv()

groq = Groq()

def classify_with_llm(log_msg):
    prompt = f''' Classify the log message into one of these categories:
    (1) Workflow Error, (2) Deprecation Warning.
    If you can't figure out a category, return "unclassified".
    Only return the category name. No preamble.
    Log message;{log_msg}'''

    try:
        chat_completion = groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        content = chat_completion.choices[0].message.content
        if content:
            return content.strip()
        else:
            return "unclassified"
    except Exception as e:
        print(f"Error from LLM: {e}")
        return "unclassified"
if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))