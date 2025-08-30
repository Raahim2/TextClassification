from fastapi import APIRouter
from app.schemas import TextModerationRequest, ImageModerationRequest, ModerationResponse
from app.services import classify_text, classify_image

router = APIRouter()

@router.post("/moderate/text", response_model=ModerationResponse)
async def moderate_text(payload: TextModerationRequest):
    classification, confidence, reasoning = classify_text(payload.text)
    return ModerationResponse(
        classification=classification,
        confidence=confidence,
        reasoning=reasoning
    )

@router.post("/moderate/image", response_model=ModerationResponse)
async def moderate_image(payload: ImageModerationRequest):
    classification, confidence, reasoning = classify_image(payload.image_url)
    return ModerationResponse(
        classification=classification,
        confidence=confidence,
        reasoning=reasoning
    )
