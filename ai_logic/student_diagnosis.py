# ai_logic/student_diagnosis.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load your OpenAI API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def classify_student_response(response: str) -> str:
    prompt = f"""
    A student gave the following feedback after missing or leaving class:

    "{response}"

    Categorize it into one of these categories:
    - Personal Issue
    - Technical Issue
    - Content Feedback
    - Teacher-related
    - Others

    Just return the category.
    """

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
