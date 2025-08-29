# 📌 TextClassification API

A minimal **FastAPI-based Content Moderation API** using **Gemini (or OpenAI)** for text classification.  
Supports text moderation now (image moderation can be added later).

---

## 🚀 Features
- `POST /api/v1/moderate/text` → Classify text into **toxic, spam, harassment, safe**  
- `POST /api/v1/moderate/image` → Stub endpoint for image moderation (Gemini supports images)  
- Built with **FastAPI** + **Uvicorn**  

---

## 📦 Installation

Clone the repo and install dependencies:

```bash
pip install fastapi uvicorn requests
```

## Run

```bash
uvicorn main:app --reload
```
