import os
from dotenv import load_dotenv

import google.generativeai as genai
from ollama import chat

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development")
print("APP_ENV =", APP_ENV)

if APP_ENV == "development":

    genai.configure(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    gemini_model = genai.GenerativeModel(
        "gemini-3.1-flash-lite"
    )


def generate_answer(prompt):

    if APP_ENV == "development":

        response = gemini_model.generate_content(
            prompt
        )

        return response.text

    else:

        response = chat(
            model="qwen3:8b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]