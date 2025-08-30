import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load env variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Categories we expect
CATEGORIES = ["toxic", "spam", "harassment", "safe"]

# Create Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def classify_text(text: str):
    prompt = f"""
    You are a content moderation AI. 
    Classify the following text into one of: {CATEGORIES}.
    Return JSON with fields: classification, confidence (0-1), reasoning.

    Text: {text}
    """

    response = model.generate_content(prompt)
    try:
        import json
        result = json.loads(response.text)
        return (
            result.get("classification", "safe"),
            float(result.get("confidence", 0.8)),
            result.get("reasoning", "No reasoning provided"),
        )
    except Exception:
        # Fallback if parsing fails
        return "safe", 0.8, "Default safe classification"

def classify_image(image_url: str):
    prompt = f"""
    You are a content moderation AI. 
    Analyze this image (given as URL: {image_url}) and classify into: {CATEGORIES}.
    Return JSON with fields: classification, confidence (0-1), reasoning.
    """

    response = model.generate_content(prompt)
    try:
        import json
        result = json.loads(response.text)
        return (
            result.get("classification", "safe"),
            float(result.get("confidence", 0.8)),
            result.get("reasoning", "No reasoning provided"),
        )
    except Exception:
        return "safe", 0.8, "Default safe classification"
