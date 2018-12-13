#!/usr/bin/env python3
import adduser
import os
import random
import string
import time

# 产生一个10位的随机码
a = adduser.randpass(10)
print(a)

# 打印一个菱形
def pri_ling():
    for i in range(5):
        b = '* ' * (2 * i + 1)
        print(b.center(50))
    for i in list(range(4))[::-1]:
        b = '* ' * (2 * i + 1)
        print(b.center(50))

# 列举当前目录以及所有子目录下的文件，并打印出绝对路径
def list_file():
    for root, dirs, files in os.walk('.', topdown=True):
        for name in files:
            print(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))
        # print(root , 1)
        # print(dirs , 2)
        # print(files , 3)

# 猜数器
def chai_shu():
    list_num = string.digits
    com = int(random.choice(list_num)) * 10 + int(random.choice(list_num))
    while True:
        print('请输入：')
        player = int(input())
        if player > com:
            print('猜大了')
            continue
        elif player < com:
            print('猜小了')
            continue
        print('恭喜你，猜对了')
        break

# 生成磁盘使用情况的日志文件
def check_disk():
    now_time = time.strftime('%Y-%m-%d')
    disk_statu = os.popen('df -h').readlines()
    with open(now_time+'.log', 'w') as fobj:
        for i in disk_statu:
            fobj.write(i)

# 统计出每个IP的访问量有多少
lis = []
f = open('/var/log/secure')


if __name__ == '__main__':
    # pri_ling()
    # list_file()
    # chai_shu()
    print()