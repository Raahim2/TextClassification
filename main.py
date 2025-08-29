import os
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests

app = FastAPI(title="Minimal Gemini Content Moderator")

# Replace with your Vertex AI endpoint and API key:
GEMINI_ENDPOINT = os.getenv("GEMINI_ENDPOINT")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "models/gemini-1.5-flash"

class TextModerationRequest(BaseModel):
    email: str
    text: str

def call_gemini_multimodal(text: str, image_bytes: bytes = None):
    """Call Gemini 1.5 Flash with text and optional image, return response JSON."""
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_NAME,
        "instances": [
            {
                "content": [
                    {"mime_type": "text/plain", "data": text}
                ]
            }
        ],
        "parameters": {"json_mode": True}
    }
    if image_bytes:
        payload["instances"][0]["content"].append({
            "mime_type": "image/jpeg",
            "data": image_bytes.decode("latin1")  # simplistic encoding
        })
    resp = requests.post(GEMINI_ENDPOINT, json=payload, headers=headers)
    return resp.json()

@app.post("/api/v1/moderate/text")
async def moderate_text(req: TextModerationRequest):
    gemini_resp = call_gemini_multimodal(req.text)
    return JSONResponse(content={"email": req.email, "gemini_response": gemini_resp})

@app.post("/api/v1/moderate/image")
async def moderate_image(email: str = Form(...), file: UploadFile = File(...)):
    img_bytes = await file.read()
    gemini_resp = call_gemini_multimodal("Please analyze this image.", img_bytes)
    return JSONResponse(content={"email": email, "filename": file.filename, "gemini_response": gemini_resp})
