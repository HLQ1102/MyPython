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
    rscmd(host='192.168.1.11', user='root', passwd='123456', cmd='id root;id xiao')




