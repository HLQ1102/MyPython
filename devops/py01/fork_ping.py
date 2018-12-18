import subprocess
import os
import time

def ping(host):
    a = subprocess.call(
        'ping -c 2 %s &> /dev/null' % host,
        shell=True
    )
    if a == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    ips = ('176.204.13.%s' % i for i in range(1,255))
    print(time.strftime('%H:%M:%S'))
    for ip in ips:
        pid = os.fork()
        if not pid:
            ping(ip)
            exit()

    # for i in bb:
    #     print(i)

