import os
import shutil

def file_writing(filename="sample.txt"):
    # Create a text file and write sample data
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Line 1: Welcome to Python file handling.\n")
        file.write("Line 2: This is a sample text file.\n")
    print(f"Created '{filename}' and wrote initial data.")

    # Append new lines
    with open(filename, "a", encoding="utf-8") as file:
        file.write("Line 3: This line was appended later.\n")
        file.write("Line 4: Verification complete.\n")

    # Verify content immediately
    print("\nVerifying File Contents:")
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())


def read_file(filename="sample.txt"):
    print(f"--- Reading Content from '{filename}' ---")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            # Reading line by line to preserve formatting clean-up if needed
            for line_num, line in enumerate(file, 1):
                print(f"[{line_num}] {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Run 'write_files.py' first.")


def backup(source="sample.txt", backup="sample_backup.txt"):
    if not os.path.exists(source):
        # Create a temporary file if it doesn't exist
        with open(source, "w") as f:
            f.write("Temporary data for backup test.")
        print(f"Created temporary '{source}' for demonstration.")

    # shutil to copy/backup
    shutil.copy(source, backup)

def deletion(file):
    if os.path.exists(file):
        os.remove(file)
        print(f"deleted file: '{file}'")
    else:
        print(f"File '{file}' not found")