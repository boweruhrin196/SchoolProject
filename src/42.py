import os
import glob

def get_file_paths(directory):
    file_paths = []
    for filename in glob.glob(os.path.join(directory, "*")):
        file_paths.append(filename)
    return file_paths

directory = "path_to_your_directory"
file_paths = get_file_paths(directory)
for filepath in file_paths:
    print(filepath)
