import os
import shutil
import time


# Redifine EXTENSIONS object for your use case
EXTENSIONS = {
    "Images": [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Music": [".mp3", ".wav", ".flac", ".m4a", ".aac"],
    "Documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls", ".txt"],
    "Archives": [".zip", ".tgz", ".rar", ".tar", ".gz"],
    "Executable": [".exe", ".msi", ".bat", ".sh"],
    "Programs": [".py", ".c", ".cpp", ".php", ".java", ".html", ".css", ".js"],
    "Design": [".psd", ".ai", ".xd", ".sketch"]
}

def root_dir():
    """
    Prompts the user to enter the root directory path and validates it.
    Returns:
        str: The valid root directory path.
    """
    while True:
        root_directory = input('Enter file path: ').strip()

        if not os.path.isdir(root_directory):
            print('Enter a valid path, check for / and \\ in your path name.')
        else:
            return root_directory


def organize_files(root_dir):
    """
    Recursively organizes files in the given root directory based on their extensions.

    Args:
        root_dir (str): The root directory path.
    """
    # Feel free to uncomment this out to set the root directory
    # As of now the program works well without this line
    # os.chdir(root_dir)
    for root, dirs, files in os.walk(root_dir):
        # Iterate through files in the current directory
        for file in files:
            try:
                file_path = os.path.join(root, file)
                # use the find_matching_keys() function to create a list of keys from the EXTENSIONS and create new directories with the key names in upper case
                matching_keys = find_matching_keys(file)
                if matching_keys:
                    for key in matching_keys:
                        destination = os.path.join(root, key.upper())
                        # calls the move_file function to move files into the defined destinations
                        move_file(file_path, destination)
                else:
                    destination_other = os.path.join(root, "others")
                    move_file(file_path, destination_other)
            except Exception as e:
                print(f"Error processing file: {file}\n{e}")

def find_matching_keys(file):
    """
    Finds the matching keys (folder names) for a given file based on its extension.

    Args:
        file (str): The file name.

    Returns:
        list: A list of matching keys.
    """
    matching_keys = []
    for key, extensions in EXTENSIONS.items():
        for ext in extensions:
            if file.endswith(ext):
                matching_keys.append(key)
                break
    return matching_keys

def move_file(file_path, destination):
    """
    Moves a file to the specified destination.

    Args:
        file_path (str): The source file path.
        destination (str): The destination directory path.
    """
    # checks if destination path exist, if not creates one
    if not os.path.exists(destination):
        os.makedirs(destination)

    file_name = os.path.basename(file_path)
    destination_path = os.path.join(destination, file_name)

    if os.path.exists(destination_path):
        print(f"{file_name} already exists in {destination}")
    else:
        print(f"Moving file to: {destination}")
        shutil.move(file_path, destination)
        print(f"File successfully moved to: {destination}")

if __name__ == '__main__':
    start_time = time.time()
    root_d = root_dir()
    organize_files(root_d)
    end_time = time.time()
    run_time = end_time - start_time
    print("\n***** Execution Time *****")
    print(f"       {run_time:.2f} seconds")