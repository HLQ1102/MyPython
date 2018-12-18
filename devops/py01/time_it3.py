import time
import os
import threading

def add(n=50000000):
    result = 0
    for i in range(1, 1 + n):
        result += i
    print(result)
    return result

if __name__ == '__main__':
    start = time.time()
    n = 2
    alist = []
    for i in range(n):
        t = threading.Thread(target=add)
        t.start()
        alist.append(t)
    for i in alist:
        i.join()
    end = time.time()
    print(end - start)