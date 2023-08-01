import os

# Understading how os.walk works

def process_directory(root, subdirs, files):
    """
    Example function to process a directory using os.walk.

    Args:
        root (str): The current directory path.
        subdirs (list): A list of subdirectory names in the current directory.
        files (list): A list of file names in the current directory.
    """
    print(f"Processing directory: {root}")

    # Iterate over subdirectories
    for subdir in subdirs:
        subdir_path = os.path.join(root, subdir)
        print(f"Subdirectory: {subdir_path}")

    # Iterate over files
    for file in files:
        file_path = os.path.join(root, file)
        print(f"File: {file_path}")

# Example usage of os.walk
root_directory = r"C:\Users\dane\Desktop\WHO"
os.makedirs(root_directory)

for root, subdirs, files in os.walk(root_directory):
    process_directory(root, subdirs, files)