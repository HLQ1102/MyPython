#!/usr/bin/env python3
# 输出指定文件夹内的文件的绝对路径

import os

for root,dirs,files in os.walk('/tmp/'):  # 指定文夹/tmp/
    for name in files:
        print(os.path.join(root,name))
