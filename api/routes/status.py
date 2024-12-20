from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_status():
    """
    Get the status of the server.
    """
    return {"status": "Server is running", "uptime": "24h"}
