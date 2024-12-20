import os

def save_file(path: str, content: bytes):
    """
    Save a file to the specified path.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(content)
    return path
