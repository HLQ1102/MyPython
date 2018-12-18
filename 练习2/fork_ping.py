import subprocess
import os
import threading

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        re = subprocess.call('ping -c 2 -i 0.2 %s &> /dev/null' % self.host, shell=True)
        if re == 0:
            print('%s:up' % self.host)


if __name__ == '__main__':
    ips = ['176.204.13.%d' % i for i in range(1,255)]
    # for i in ips:
    #     t = threading.Thread(target=ping, args=(i,))
    #     t.start()
        # aa = os.fork()
        # if not aa:
        #     ping(i)
        #     exit()
    for i in ips:
        t = threading.Thread(target=Ping(i))
        t.start()
