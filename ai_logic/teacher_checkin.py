# ai_logic/teacher_checkin.py

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def classify_teacher_checkin(response: str) -> str:
    prompt = f"""
    A teacher submitted this pre-class check-in:

    "{response}"

    Classify it into one of the following categories:
    - Ready
    - Needs Support
    - At Risk

    Only return the category name.
    """

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
