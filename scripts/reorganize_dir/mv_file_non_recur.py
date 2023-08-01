import os
import shutil
import time
# import json

# Defining Functions

def extensions(**kwargs):
    """
    Create a dictionary object containing key-value pairs of extensions.

    This function takes keyword arguments to specify different categories
    of file extensions. Each keyword represents a category, and the value
    associated with the keyword is a list of extensions belonging to that category.

    Args:
        **kwargs: Keyword arguments representing file categories and their extensions.

    Returns:
        dict: A dictionary object with file categories as keys and lists of extensions as values.
    """
    exten = {}
    for k, v in kwargs.items():
        exten[k] = v
    return exten

# Create a dictionary containing key value pairs of extension lists
# EXTENSIONS is a constant, DO NOT CHANGE VARIABLE NAME, its referenced in subsequent functions

EXTENSIONS = extensions(
                        Images = [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".tiff", ".svg"],
                        Videos = [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
                        Music = [".mp3", ".wav", ".flac", ".m4a", ".aac"],
                        Documents = [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls", ".txt"],
                        Archives = [".zip", ".tgz", ".rar", ".tar", ".gz"],
                        Executable = [".exe", ".msi", ".bat", ".sh"],
                        Programs = [".py", ".c", ".cpp", ".php", ".java", ".html", ".css", ".js"],
                        Design = [".psd", ".ai", ".xd", ".sketch"]
                        )

# print out EXTENSION DICTIONARY as a string to verify with sorted keys
# ext_string = json.dumps(EXTENSIONS,  indent=1, sort_keys=True) # uncomment out the json module import to run this 
# print(ext_string)

def root_dir():
    """
    Prompts the user to enter the root directory path and validates it.
    Returns:
        str: The valid root directory path.
    """
    while True:
        root_directory = input('Enter (absolute) file path (e.g., C:\User\Name\Desktop\Root): ')

        if not os.path.isdir(root_directory):
            print('Enter a valid path, check for / and \ in your path name.')
        else:
            return root_directory

def set_root_dir(root):
    """
    Changes the current working directory to the root directory and returns the list of files in it.
    Args:
        root (str): The root directory path.
    Returns:
        list: A list of files in the root directory.
    """
    os.chdir(root)
    all_dir_content = os.listdir()
    return all_dir_content

def list_files_only(files, root):
    """
    Yield files from a list that are only regular files (not directories).

    This function takes a list of file names and a root directory as input.
    It iterates through each file in the list and checks if it is a regular file
    (not a directory). If it is, the file name is yielded as an output.

    Args:
        files (list): A list of file names.
        root (str): The root directory path.

    Yields:
        str: A file name that is a regular file (not a directory).
    """
    for file in files:
        try:
            path = os.path.join(root, file)
            if os.path.isfile(path):
                yield file
        except Exception as e:
            print('Error processing file: {}'.format(e))

def sort_keys(file):
    """
    Matches the file extension with the predefined extensions and returns the corresponding keys.
    Args:
        file (str): The file name.
    Returns:
        list: A list of matching keys (folder names).
    """
    matching_keys = []
    for key, extensions in EXTENSIONS.items():
        for ext in extensions:
            if file.endswith(ext):
                matching_keys.append(key)
                break
    return matching_keys

def file_organize(files, root):
    """
    Sorts the files into respective folders based on their extensions.
    Args:
        files (list): The list of files to be sorted.
        root (str): The root directory path.
    """
    # this is the folder created within the root dir to contain the new sorting folders created with the keys
    sort_folder = 'SortedFolder'
    # the destination folder for files with extentions not included in the files extensions
    destination_other = os.path.join(root, sort_folder, 'others')

    # Create the 'others' folder if it doesn't exist
    if not os.path.exists(destination_other):
        os.makedirs(destination_other)

    for file in files:
        matching_keys = sort_keys(file)

        if matching_keys:
            for key in matching_keys:
                # this is the destination folder for files with extntions included in the extention dictionary
                destination = os.path.join(root, sort_folder, key)

                # Create the destination folder if it doesn't exist
                if not os.path.exists(destination):
                    os.makedirs(destination)
                # check if file already exist in destination directory
                if os.path.exists(os.path.join(destination, file)):
                    print()
                    print('{} already exists in {}'.format(file, destination))
                else:
                    try:
                        print()
                        print('Copying file to: {}'.format(destination))
                        # shutil.move(file, destination) # using shutil.move will permanently move the file 
                        # so careful and make sure the destination path is created and is a directory
                        shutil.copy(file, destination)
                        print('File successfully copied to: {}'.format(destination))
                    except Exception as e:
                        print('Error: {}'.format(e))
                        
        else:
            # check if file already exist in destination directory
            if os.path.exists(os.path.join(destination_other, file)):
                    print()
                    print('{} already exists in {}'.format(file, destination_other))
            else:
                try:
                    print()
                    print('Copying file to: {}'.format(destination_other))
                    # shutil.move(file, destination)
                    shutil.copy(file, destination_other)
                    print('File successfully copied to: {}'.format(destination_other))
                except Exception as e:
                    print('Error: {}'.format(e))

if __name__ == '__main__':
    start_time = time.time()
    root_dir = root_dir()
    file_list = set_root_dir(root_dir)
    lists = list_files_only(file_list, root_dir)
    file_organize(lists, root_dir)
    end_time = time.time()
    run_time = end_time - start_time
    print()
    print('***** Execution Time *****')
    print('         {:.2f} seconds'.format(run_time))