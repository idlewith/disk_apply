import os


def find_leaf_directories(root):
    for dirpath, dirnames, filenames in os.walk(root):
        if not dirnames:
            # If a directory contains no subdirectories, it is considered a "leaf directory"
            print(dirpath)


b = "/opt/huawei"
find_leaf_directories(b)
