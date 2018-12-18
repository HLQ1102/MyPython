import random

def sort(a):
    if len(a) < 2:
        return a
    z = a[0]
    big = []
    samll = []
    for i in a[1:]:
        if i > z:
            big.append(i)
        else:
            samll.append(i)
    return sort(samll) + [z] + sort(big)

if __name__ == '__main__':
    a = [random.randint(1, 100) for i in range(10)]
    # print(a)
    # print(sort(a))

import os
import sys

def list_files(path):
    if os.path.isdir(path):
        content = os.listdir(path)
        for fname in content:
            fname = os.path.join(path, fname)
            if not os.path.isdir(fname):
                print(os.path.join(path, fname))
            list_files(fname)

# if __name__ == '__main__':
#     list_files('/tmp/demo')


def list_files1(path):
    if os.path.isdir(path):
        content = os.listdir(path)
        for fname in content:
            fname = os.path.join(path, fname)
            if not os.path.isdir(fname):
                print(os.path.join(path, fname))
            list_files(fname)

# list_files1('/tmp/demo')
if __name__ == '__main__':
    list_files1('/tmp/demo')