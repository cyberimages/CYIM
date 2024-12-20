import os
import shutil

def clean_output_folder(folder="../output"):
    if os.path.exists(folder):
        print(f"Cleaning folder: {folder}")
        shutil.rmtree(folder)
        os.makedirs(folder)
        print(f"Folder {folder} cleaned and recreated.")
    else:
        print(f"Folder {folder} does not exist. Nothing to clean.")

if __name__ == "__main__":
    clean_output_folder()
