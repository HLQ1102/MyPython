import getpass
import os
import sys
import threading

import paramiko


def rscmd(host, user, passwd, cmd, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] OUT\n%s' % (host, out.decode()))
    if err:
        print('[%s] ERR\n%s' % (host, err.decode()))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: %s')
    hostfile = sys.argv[1]
    if not os.path.isfile(hostfile):
        print()
        exit(2)
    cmd = sys.argv[2]

    password = getpass.getpass()
    with open('host') as fobj:
        for host in fobj:
            host = host.strip()
            t = threading.Thread(target=rscmd, args=(host, 'root', password, cmd))
            t.start()
            # rscmd(host=host, user='root', passwd=password, cmd=cmd)
