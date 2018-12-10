import subprocess
import sys
import string
import random

def useradd(user, password, fname):
    info = '''username: %s
passwd: %s \n
''' % (user, password)
    subprocess.call('useradd %s' % user, shell=True)
    subprocess.call('echo %s | passwd --stdin %s' % (password, user), shell=True)
    with open(fname, 'a') as fobj:
        fobj.write(info)

def randpass(n = 8):
    a = string.ascii_letters + string.digits
    b = ''
    while True:
        b += random.choice(a)
        if len(b) == n:
            break
    return b

def user_check(user):
    a = subprocess.call('id %s > /dev/null' % user, shell=True)
    if a != 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    fname = '/tmp/1.txt'
    username = sys.argv[1]
    if user_check(username):
        print('用户已存在')
        exit(1)
    password = randpass()
    useradd(username, password, fname)