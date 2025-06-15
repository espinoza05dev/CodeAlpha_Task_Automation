import os
import shutil

def moveimgs(P_origin,P_destination):
    if os.path.exists(P_origin) and os.path.exists(P_destination):
        for file in os.listdir(P_origin):
            file_path = os.path.join(P_origin, file)
            filepath2 = os.path.join(P_destination, file)
            if os.path.isfile(file_path):
                shutil.move(file_path, filepath2)
                print("Images moved successfully")
    else:
        os.mkdir(P_origin)
        os.mkdir(P_destination)
        print("Paths created")

if __name__ == "__main__":
    path_origin = r"path1"
    path_destination = r"path2"

    moveimgs(path_origin,path_destination)