from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_music_generation_api():
    response = client.post(
        "/api/v1/music",
        json={"prompt": "Relaxing ambient track", "duration": 300, "output": "./output/music.mp3"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Music generated successfully!"
    assert response.json()["output"].endswith("music.mp3")
