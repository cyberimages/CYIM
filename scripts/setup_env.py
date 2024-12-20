import os
import subprocess

def install_dependencies():
    print("Installing dependencies...")
    os.system("pip install -r ../requirements.txt")
    os.system("npm install --prefix ../frontend")
    print("Dependencies installed.")

def create_directories():
    print("Creating necessary directories...")
    os.makedirs("../output", exist_ok=True)
    os.makedirs("../logs", exist_ok=True)
    print("Directories created.")

def setup_environment():
    install_dependencies()
    create_directories()
    print("Environment setup complete.")

if __name__ == "__main__":
    setup_environment()
