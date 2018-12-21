import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.11', username='root', password='123456')
result = ssh.exec_command('ls /etc/')
print(result[0])
# for i in result[0]:
#     print(i, end='')

ssh.close()
