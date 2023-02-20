

# create multiple files


```shell
for i in {1..10}
do
dd if=/dev/urandom of=/root/disk_apply/new/file${i} bs=500M count=5;
done
```

# make one file specially

chmod +x file4


# files usage

[cp.py](cp.py) use cp once

[cp_with_subprocess.py](cp_with_subprocess.py) use cp in multiple cores


