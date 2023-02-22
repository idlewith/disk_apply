
/opt/huawei/apps下有25个160M的文件
/opt/huawei/logs/today下有25个160M的文件
/opt/huawei/logs/yesterday下有25个160M的文件

/opt/huawei/logs下有1个软链接

lost+found空目录


```shell
date && rsync --owner --group --archive --copy-links --whole-file --relative --no-compress --progress /opt/huawei/* /opt/test && date
```

这个命令平均38.6秒：第一次38秒，第二次41秒，第3次37秒


```shell
date && cp -ar /opt/huawei/* /opt/test && date
```

这个命令平均15.3秒：第一次16秒，第二次15秒，第3次15秒



```shell
date && tar -C /opt/huawei -c . | tar -C /opt/test -xp && date
```

这个命令平均19秒：第一次19秒，第二次19秒，第3次19秒







