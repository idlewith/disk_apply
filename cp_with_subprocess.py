# encoding: utf-8
import time
from subprocess import PIPE, Popen
import os
from multiprocessing import Pool


root_path = "/root/disk_apply"
old_path = os.path.join(root_path, "old")
new_path = os.path.join(root_path, "new")


def run(command):
    stdout, stderr = Popen(command, stdout=PIPE, shell=True).communicate()
    return str(stdout)


def copy():
    # old -> new
    command = "sudo cp -ar /root/disk_apply/old/* /root/disk_apply/new"
    output = run(command)
    print(output)


def apply_async_with_callback():
    pool = mp.Pool()
    for i in range(10):
        pool.apply_async(copy, args=(i,))
    pool.close()
    pool.join()


def create_dir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)


def walk_files():
    dirs_out = []
    for root, dirs, files in os.walk(old_path):
        for dirname in dirs:
            dir_absolute = os.path.join(root, dirname)
            dirs_out.append(dir_absolute)

    command_list = []
    dirs_out = dirs_out[:-1]
    for d in dirs_out:
        command = f"cp -ar {d} {new_path}"
        command_list.append(command)
    return command_list


def main():
    command_list = walk_files()
    with Pool(3) as p:
        print(p.map(run, command_list))


if __name__ == "__main__":
    start = time.time()
    # main()

    command_list = walk_files()
    with Pool(3) as p:
        p.apply_async(run, command_list)

    print(time.time() - start)
