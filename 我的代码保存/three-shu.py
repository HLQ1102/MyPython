#!/usr/bin/env python3
# 四以内的三位数序列
def list():
    a = []
    for i in range(1, 5):
        for j in range(2, 5):
            if i == j :
                continue
            for n in range(3, 5):
                if i == n and j == n :
                    continue
                a.append(i * 100 + j * 10 + n)
    return a

if __name__ == '__main__':
    a = list()
    print('所有三位数的个数为：', len(a), '\n\n序列如下：')
    print(a)