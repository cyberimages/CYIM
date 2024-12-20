from fastapi import FastAPI
from app.routes import art, music, status

app = FastAPI(
    title="CyberGenerateOS API",
    description="API for generating art and music with CyberGenerateOS",
    version="1.0.0",
)

# Include routes
app.include_router(art.router, prefix="/api/v1/art", tags=["Art Generation"])
app.include_router(music.router, prefix="/api/v1/music", tags=["Music Generation"])
app.include_router(status.router, prefix="/api/v1/status", tags=["Server Status"])
