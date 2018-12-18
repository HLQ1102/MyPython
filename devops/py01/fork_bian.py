from os import fork

# print('haha')
# fork()
# print('nnn')

'''
1.父进程
'''

import os

print('start')
for i in range(3):
    a = os.fork()
    if not a:
        print('I\'m child')
        exit()
# print('end')