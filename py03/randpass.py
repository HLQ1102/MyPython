import random
import sys

def randpass(n = 8):
    a = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = ''

    while True:
        d += random.choice(a)
        if len(d) == n:
            break
    print('验证码为：', d)

if __name__ == '__main__':
    n = int(input('请输入你的随机码位数'))
    randpass(n)