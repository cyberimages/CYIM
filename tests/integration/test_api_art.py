from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_art_generation_api():
    response = client.post(
        "/api/v1/art",
        json={"prompt": "A cyberpunk city at night", "style": "Cyberpunk", "output": "./output/city.png"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Art generated successfully!"
    assert response.json()["output"].endswith("city.png")
