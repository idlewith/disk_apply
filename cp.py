# encoding: utf-8
import time
from subprocess import PIPE, Popen


def run(command):
    stdout, stderr = Popen(command, stdout=PIPE, shell=True).communicate()
    return str(stdout)


def main():
    # old -> new
    command = "sudo cp -ar /root/disk_apply/old/* /root/disk_apply/new"
    output = run(command)
    print(output)


if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)

