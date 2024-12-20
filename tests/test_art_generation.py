import pytest
from app.models.art_model import generate_art

def test_generate_art_success():
    result = generate_art(prompt="A sunset over mountains", style="realistic", output="./output/test_art.png")
    assert result["prompt"] == "A sunset over mountains"
    assert result["style"] == "realistic"
    assert result["output_path"].endswith("test_art.png")

def test_generate_art_invalid_style():
    with pytest.raises(ValueError):
        generate_art(prompt="A futuristic city", style="unknown_style", output="./output/test_art.png")
