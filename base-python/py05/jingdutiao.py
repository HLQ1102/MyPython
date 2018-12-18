import time
import sys

print('#' * 20, end='')
n = 0
while True:
    print('\r%s@%s' % ('#' * n, '#' * (19 - n)), end='')
    sys.stdout.flush()
    time.sleep(0.3)
    n += 1
    if n == 20:
        n = 0
