import shutil

# src = "/dev/sdb"
# dst = "/dev/sdc"
src = "/opt/huawei/"
dst = "/opt/test/"

shutil.disk_usage(src)
shutil.copytree(src, dst, symlinks=True)
