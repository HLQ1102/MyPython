#!/usr/bin/env python3

import os

for root,dirs,files in os.walk('/tmp/'):
    for name in files:
        print(os.path.join(root,name))

for i in range(5):
    print('*' * i, end='')
    print()

b = os.popen('ls').readlines()
for i in range(len(b)):
    print(b[i],end='')
print()