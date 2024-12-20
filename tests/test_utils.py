import os
from app.utils.file_utils import save_file

def test_save_file():
    path = "./test_output/sample.txt"
    content = b"Sample content"
    saved_path = save_file(path, content)
    assert os.path.exists(saved_path)
    with open(saved_path, "rb") as f:
        assert f.read() == content
    os.remove(saved_path)
