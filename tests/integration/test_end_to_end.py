import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_end_to_end_art_generation():
    response = client.post(
        "/api/v1/art",
        json={"prompt": "A forest at sunrise", "style": "impressionist", "output": "./output/forest.png"}
    )
    assert response.status_code == 200
    assert os.path.exists("./output/forest.png")

def test_end_to_end_music_generation():
    response = client.post(
        "/api/v1/music",
        json={"prompt": "Chill beats", "duration": 120, "output": "./output/chill_beats.mp3"}
    )
    assert response.status_code == 200
    assert os.path.exists("./output/chill_beats.mp3")
