import os
import shutil

def organize_files(directory):
    # os.listdir -> Returns the files under that directory
    for filename in os.listdir(directory):
        # os.path.join -> The return value is the concatenation of path
        # os.path.isfile -> Checks is that file and return bool accordingly
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split(".")[-1]
            destination_folder = os.path.join(directory, file_extension)
            os.makedirs(destination_folder, exist_ok=True)
            # shutil.move() -> Moves the file from source to destination
            shutil.move(os.path.join(directory, filename), os.path.join(destination_folder, filename))


directory_to_organize = "/Sample File Organize"
organize_files(directory_to_organize)
