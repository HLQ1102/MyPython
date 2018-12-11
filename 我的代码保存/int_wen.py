#!/usr/bin/env python3
# n位数排序

def put_num(n = 3):
    a = []
    for i in range(1,n + 1):
        c = int(input('please input %s number: ' % i))
        a.append(c)
        a.sort()
    return a

# def paixu(b):
#     for i in range(len(b)-1):
#         if b[i] > b[i + 1]:
#             b = b[i + 1]
#             b[i + 1] = a[i]
#             b[i] = b
#     return b

if __name__ == '__main__':
    cc = input('')
    print(put_num())