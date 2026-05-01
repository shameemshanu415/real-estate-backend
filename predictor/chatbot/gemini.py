import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generate_response(message):
    prompt = f"""
    Answer the question in a clear and slightly detailed way.

    Rules:
    - Use bullet points
    - 5 to 7 points
    - Each point can be 1–2 short sentences
    - Keep it simple but informative
    - No markdown symbols like ** or headings

    Question: {message}
    """

    # 🔥 Try Gemini 2.5 Flash first, then fallback to older models if unavailable
    model_names = [
        "gemini-2.5-flash",       # preferred model
        "gemini-2.0-flash-exp",   # fallback experimental
        "gemini-1.5-flash",       # stable fallback
    ]

    for model_name in model_names:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text.strip()

        except Exception as e:
            err_text = str(e).lower()
            if "503" in err_text or "overloaded" in err_text:
                time.sleep(2)
                continue
            if "not found" in err_text or "404" in err_text or "unsupported" in err_text:
                continue
            return f"Error: {str(e)}"

    return "Server is busy right now. Please try again."
