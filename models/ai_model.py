import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_ai_for_recipe(prompt):
    "Send a prompt to Gemini API and return its response"
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else str(response)

    except Exception as e:
        return f"An error occured: {e}"