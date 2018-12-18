import time
import os

def add(n=50000000):
    result = 0
    for i in range(1, 1 + n):
        result += i
    return result

if __name__ == '__main__':
    start = time.time()
    n = 8
    for i in range(n):
        retval = os.fork()
        if not retval:
            print(add())
            exit()
    for i in range(n):
        # waitpid第一个参数-1，表示与wait函数相同,处理僵尸进程；
        # 第二个参数，0表示挂起父进程，1表示不挂起
        os.waitpid(-1, 0)  #
    end = time.time()    # 返回一个时间戳，从1970-01-01到这条命令执行时的秒数
    print(end - start)