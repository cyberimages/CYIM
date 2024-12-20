from fastapi import APIRouter, HTTPException
from app.models.music_model import generate_music

router = APIRouter()

@router.post("/")
async def create_music(prompt: str, duration: int = 300, output: str = "./output/music.mp3"):
    """
    Generate music based on a prompt and duration.
    - `prompt`: Description of the music to generate
    - `duration`: Length of the track in seconds (default: 300 seconds)
    - `output`: Path to save the generated music
    """
    try:
        result = generate_music(prompt, duration, output)
        return {"message": "Music generated successfully!", "output": output, "details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
