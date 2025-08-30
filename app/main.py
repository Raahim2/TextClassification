from fastapi import FastAPI
from app.routers import router

app = FastAPI(title="Smart Content Moderator API")

# Register routes
app.include_router(router, prefix="/api/v1")
