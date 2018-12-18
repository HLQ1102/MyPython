import sys
import subprocess
import randpass

def adduser(username, passwd, fname):
    userinfo = "用户名：%s　　密码：%s" % (username, passwd)

    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call(
        'echo %s | passwd --stdin %s' % (passwd, username),
        shell=True
    )
    with open(fname, 'a') as obj:
        obj.write(userinfo)

if __name__ == '__main__':
    fname = '/tmp/1.txt'
    password = randpass.randpass()
    a = sys.argv[1]
    adduser(a, password, fname)