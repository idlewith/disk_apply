import os
import time
import shutil
from multiprocessing import Pool

root_path = "/root/disk_apply"
old_path = os.path.join(root_path, "old")
new_path = os.path.join(root_path, "new")


def copy_tree(src_dst):
    src, dst = src_dst.split(",")
    try:
        shutil.copytree(src, dst, symlinks=True)
        print(src, dst)
    except (FileExistsError, shutil.Error):
        pass


def main():
    d_d2_list = []
    for root, dirs, files in os.walk(old_path):
        for dirname in dirs:
            d = os.path.join(root, dirname)
            d2 = d.replace(old_path, new_path)
            # d_d2_list.append([d, d2])
            d_d2_list.append(",".join([d, d2]))

        for filename in files:
            f = os.path.join(root, filename)
            f3 = f.replace(old_path, new_path)
            # shutil.copy3(f, f2)

    return d_d2_list


if __name__ == "__main__":
    start = time.time()

    a = main()
    with Pool(5) as p:
        print(p.map(copy_tree, a))

    print(time.time() - start)
