import os 
from cryptography.fernet import Fernet


TARGET_DIRECTORY_PATH = "target directory"  
target_directory = os.listdir(TARGET_DIRECTORY_PATH)  # creates a list of file/folders within target directory

key = input("Encryption key>")


def decrypt_files(files):

    for file in files:

        with open(file, 'rb') as target_file:
            contents = target_file.read()
        contents_decrypted = Fernet(key).decrypt(contents)

        with open(file, 'wb') as target_file:
            target_file.write(contents_decrypted)


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
        
    decrypt_files(files)


scour_directory(target_directory)
print(f"Files within directory {TARGET_DIRECTORY_PATH} decrypted using encryption key: {key}")
