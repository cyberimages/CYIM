import shutil
import datetime
import os

def backup_data(source="../output", destination="../backup"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(destination, f"backup_{timestamp}")

    if os.path.exists(source):
        print(f"Backing up data from {source} to {backup_path}...")
        shutil.copytree(source, backup_path)
        print("Backup completed successfully.")
    else:
        print(f"Source folder {source} does not exist. Nothing to back up.")

if __name__ == "__main__":
    backup_data()
