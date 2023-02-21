

# create multiple files


```shell
for i in {1..25}
do
dd if=/dev/urandom of=/opt/huawei/apps/file${i} bs=500M count=5
done
```

dd if=/dev/urandom of=/root/disk_apply/old/apps/file${i} bs=500M count=5


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


## solution 3

**prepare**

fdisk

mkfs.ext4 /dev/sdb

mkdir /mnt/newdisk

mount /dev/sdb /mnt/newdisk

df -h


mkfs.ext4 /dev/sdb
mkfs.ext4 /dev/sdc

mkdir /opt/huawei
mkdir /opt/test

mount /dev/sdb /opt/huawei
mount /dev/sdc /opt/test


umount  /opt/test /dev/sdc
rm -rf /opt/test
mkfs.ext4 /dev/sdc




**copy**

dd if=/dev/source of=/dev/target bs=1M

date && dd if=/dev/sdb of=/dev/sdc bs=4M conv=noerror,sync && date

date && dd if=/dev/sdb of=/dev/sdc bs=4M && date

mkdir /opt/test
mount -t ext4 /dev/sdc /opt/test

cp -a --attributes-only /path/to/source/* /path/to/target/

date && cp -a --attributes-only /opt/huawei/* /opt/test && date







