import os
import time

print('starting...')
retval = os.fork()
if not retval:
    print('in child')
    time.sleep(10)
result = os.waitpid(-1, 1)
print(result)
time.sleep(15)
print('done')