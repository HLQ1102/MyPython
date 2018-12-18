import random
import os


alist = ['xiao', 'wu', 'jiu']
adict = {'', '', ''}

city = ('成都', '上海')

for ch in alist:
    print(ch, end = '')
print()
# for li in range(1,101,step=3):
#     print(li)
# 斐波那契数列
a = [0, 1]
b = 8
for i in range(b-2):
    a.append(a[-2]+a[-1])
print(a)

# 九九乘法表
# xx = int(input('input number:'))
# xx = 9
# for i in range(1, xx + 1):
#     for j in range(1, i+1):
#         print(j, '*', i, '=', i*j, end='\t' )
#     print('\n')
xx = 9
for i in range(1, xx + 1):
    for j in range(1, i+1):
        print('%d*%d=%d' % (i, j, i*j),end='\t' )
    print()

n = 9
for i in range(n):
    for j in range(n // 2):
        print('*', end='')
    print()
# 快速生成列表
klist = [10 + i for i in range(1,11) if i % 2 == 0]
print('我是快速列表', klist)
# 快速生成ip地址列表
klist1 = ['192.168.' + str(i) for i in range(1, 255)]
print('我是ip地址列表', klist1)

# 读文本文件
a = open('/tmp/passwd')
date = a.read()
print(a.read())
a.close()   # 关闭文件，必须关闭，不然文件会有问题
# print(date)

f = open('/tmp/passwd1', 'r+')
f.seek(0, 2)
f.write('xiaowujiu\n')
f.flush()
data = f.read()
f.close()
print(data)

f = open('/tmp/passwd1', 'r+')
f.seek(3, 0)
f.write('123')
f.flush()
f.seek(0, 2) # 移动到文件的末尾
f.close()

with open('/tmp/passwd1', 'r+') as f:
    line = f.readline()
    f.seek(0, 2)
    f.write('123aaa')
    f.seek(0, 0)
    line1 = f.read()
    f.seek(0, 1)
    f.write('123qqq...A')
    line2 = f.read()
print(line)
print(line1)
print(line2)

with open('/tmp/passwd2', 'r+') as f:
    f.seek(0, 2)
    f.writelines(['123.123.123\n', 'xiaoxiao\n'])

import sys
sys.stdout.write('hello world!!\n')
data = sys.stdin.readline()
print(data)

a = 1
b = 2
print('x=%d' % a)