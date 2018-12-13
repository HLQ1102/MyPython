import subprocess

c = ['192.168.1.%s' % i for i in range(1,255)]
print(c)
d = [10 + i for i in range(10)]
print(d)

import shutil
import string
string.