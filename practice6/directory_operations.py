import os
import glob

def directory_operations():
    nested_path = os.path.join("nested_root", "sub_dir", "target_folder")
    
    print("--- 1. Creating Nested Directories ---")
    # os.makedirs creates all intermediate-level directories if they don't exist
    os.makedirs(nested_path, exist_ok=True)
    print(f"Created nested path: {nested_path}")

    # Dummy files for demonstration
    open(os.path.join("nested_root", "test1.txt"), "w").close()
    open(os.path.join("nested_root", "test2.log"), "w").close()
    open(os.path.join("nested_root", "test3.txt"), "w").close()

    print("\n--- 2. Listing Files and Folders ---")
    all_contents = os.listdir("nested_root")
    print(f"Contents of 'nested_root': {all_contents}")

    print("\n--- 3. Finding Files by Extension (.txt) ---")
    # Finding files using glob
    txt_files = glob.glob("nested_root/*.txt")
    print("Found .txt files:")
    for file in txt_files:
        print(f" - {file}")

if __name__ == "__main__":
    directory_operations()