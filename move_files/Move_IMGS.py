import os
import shutil

path_origin = r"path1"
path_destination = r"path2"

if os.path.exists(path_origin) and os.path.exists(path_destination):
    for file in os.listdir(path_origin):
        file_path = os.path.join(path_origin, file)
        filepath2 = os.path.join(path_destination, file)
        if os.path.isfile(file_path):
            shutil.move(file_path, filepath2)
else:
    os.mkdir(path_origin)
    os.mkdir(path_destination)
    print("Paths created")
