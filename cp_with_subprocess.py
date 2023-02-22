# encoding: utf-8
import multiprocessing
import os
import time
from subprocess import PIPE, Popen

old_path = "/opt/huawei"
new_path = "/opt/test"


def run(command):
    stdout, stderr = Popen(command, stdout=PIPE, shell=True).communicate()
    return stdout.decode("utf-8")


def main():
    make_dirs()
    file_list = get_all_files()
    command_list = gen_cp_command(file_list)
    return command_list


def make_dirs():
    command = "find /opt/huawei/ -type d|sed  's/\/opt\/huawei\///g'|xargs -I {} mkdir -p /opt/test/{}"
    run(command)


def get_all_files():
    command = "find /opt/huawei -type f"
    files = run(command)
    file_list = []
    for f in files.split("\n"):
        if f:
            file_list.append(f)

    command = "find /opt/huawei -type l"
    links = run(command)
    link_list = []
    for l in links.split("\n"):
        if l:
            link_list.append(l)

    return file_list + link_list


def gen_cp_command(file_list):
    command_list = []
    for f in file_list:
        d = f.replace(old_path, new_path)
        command = f"sudo cp -a  {f} {d}"
        command_list.append(command)
    return command_list


if __name__ == "__main__":
    start = time.time()
    command_list = main()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    pool.map(run, command_list)
    pool.close()
    pool.join()

    print(time.time() - start)
