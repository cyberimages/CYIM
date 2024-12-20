import pytest
from app.models.music_model import generate_music

def test_generate_music_success():
    result = generate_music(prompt="Ambient track", duration=180, output="./output/test_music.mp3")
    assert result["prompt"] == "Ambient track"
    assert result["duration"] == 180
    assert result["output_path"].endswith("test_music.mp3")

def test_generate_music_invalid_duration():
    with pytest.raises(ValueError):
        generate_music(prompt="Jazz melody", duration=-10, output="./output/test_music.mp3")
