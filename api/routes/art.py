from fastapi import APIRouter, HTTPException
from app.models.art_model import generate_art

router = APIRouter()

@router.post("/")
async def create_art(prompt: str, style: str = "default", output: str = "./output/art.png"):
    """
    Generate art based on a prompt and style.
    - `prompt`: Description of the art to generate
    - `style`: Style to apply to the artwork (default: "default")
    - `output`: Path to save the generated art
    """
    try:
        result = generate_art(prompt, style, output)
        return {"message": "Art generated successfully!", "output": output, "details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
