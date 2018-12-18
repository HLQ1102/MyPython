import subprocess
import threading
import time

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self, *args, **kwargs):
        a = subprocess.call(
            'ping -c 2 %s &> /dev/null' % self.host,
            shell=True
        )
        if a == 0:
            print('%s:up' % self.host)
        else:
            print('%s:down' % self.host)
    def xx(self):
        print(self.host)


if __name__ == '__main__':
    ips = ('176.204.13.%s' % i for i in range(1,255))
    print(time.strftime('%H:%M:%S'))
    for ip in ips:
        t = threading.Thread(target=Ping(ip))  # 创建工作线程
        # t.start()    # target(ip) ==> 执行__call__方法
        tt = Ping(ip)
        Ping.xx(tt)