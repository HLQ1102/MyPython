a = 'hlo'
print(a)

b = set('hello')
print(b)
for ch in b:
    print(ch, end='')
print('\n' * 10)



with open('/tmp/mima', 'r') as f:
    mima = set(f)
with open('/tmp/passwd', 'r') as f:
    passwd = set(f)

with open('/tmp/result.txt','w') as f:
    f.writelines(mima - passwd)

import subprocess
subprocess.call('cat /tmp/result.txt', shell=True)


from datetime import datetime, timedelta
a = datetime.strptime('Dec 12 2018', '%b %d %Y')
print(a)

import pickle as pic
a = [{'date':'tmplate', 'in':'template', 'out':'tmeplate', 'yu_e':'template', 'beizhu':'tmplate'}]
with open('/tmp/zhangben1.txt', 'wb+') as f:
    pic.dump(a[-1], f)