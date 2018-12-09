def jiujiu():
    xx = 9
    for i in range(1, xx + 1):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (i, j, i * j), end='\t')
        print()
jiujiu()

def xiaoxiao():
    print('luoluo')
xiaoxiao()
print(xiaoxiao()) #没有返回值默认返回None

def fib():
    a = [0, 1]
    b = 8
    for i in range(b-2):
        a.append(a[-2]+a[-1])
    return a
dib = fib()
alist = [i * 2 for i in dib]
print(alist)

def fib(n):
    a = [0, 1]
    for i in range(n-2):
        a.append(a[-2]+a[-1])
    return a
a = fib(5)
print(fib(10))
n = int(input('input your number:'))

import sys


print(sys.argv)
