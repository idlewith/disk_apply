

# create multiple files


```shell
for i in {1..50}
do
dd if=/dev/urandom of=/root/disk_apply/old/apps/file${i} bs=500M count=5
done
```



# make one file specially

chmod +x file4


# files usage

[cp.py](cp.py) use cp once

[cp_with_subprocess.py](cp_with_subprocess.py) use cp in multiple cores


# vm

```shell
ifconfig
ssh parallels@10.211.55.4
sudo -i 
centos123
```


# solution

## solution 1



What about using a Live System and

```
sudo dd if=/dev/sdx0 of=/dev/sdy0
```

and

```
sudo resize2fs /dev/sdy0
```

afterwards to resize the partition.

With sdx0 being your old partition and sdy0 being the new one.


## solution 2

好吧，我相信您可以使用gnu parallel来完成您的任务。

```
seq 70 | parallel -j70 cp filename
```

