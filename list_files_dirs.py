import os
import time
import shutil

root_path = "/root/disk_apply"
old_path = os.path.join(root_path, "old")
new_path = os.path.join(root_path, "new")


def copy_tree(src, dst):
    try:
        shutil.copytree(src, dst, symlinks=True)
    except FileExistsError:
        pass


def main():
    for root, dirs, files in os.walk(old_path):
        for dirname in dirs:
            d = os.path.join(root, dirname)
            d2 = d.replace(old_path, new_path)
            copy_tree(d, d2)

        for filename in files:
            f = os.path.join(root, filename)
            f3 = f.replace(old_path, new_path)
            # shutil.copy3(f, f2)


if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)
