import os
import time

aa = os.fork()
if not aa:
    time.sleep(5)
    print('I\'m child!!')
    exit()
#time.sleep(5)
os.waitpid(-1, 0)
print('I\'m perent')
time.sleep(20)
