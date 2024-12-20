import random

def generate_art_sample(output_path="../output/sample_art.png"):
    print(f"Generating sample art and saving to {output_path}...")
    # Mock art generation logic
    with open(output_path, "w") as f:
        f.write("This is a sample art file.")
    print("Sample art generated.")

def generate_music_sample(output_path="../output/sample_music.mp3"):
    print(f"Generating sample music and saving to {output_path}...")
    # Mock music generation logic
    with open(output_path, "w") as f:
        f.write("This is a sample music file.")
    print("Sample music generated.")

if __name__ == "__main__":
    generate_art_sample()
    generate_music_sample()
