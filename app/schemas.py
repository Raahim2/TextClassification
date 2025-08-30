from pydantic import BaseModel, EmailStr

class TextModerationRequest(BaseModel):
    email: EmailStr
    text: str

class ImageModerationRequest(BaseModel):
    email: EmailStr
    image_url: str  

class ModerationResponse(BaseModel):
    classification: str
    confidence: float
    reasoning: str
