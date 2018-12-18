import sys
#
# date  = input('请输入一个文件的路径：')
# date1 = input('您打算将文件放在哪：')
# with open(date, 'r') as f:
#     date = f.read()
# f1 = open(date1, 'w+')
# f1.write(date)
# print('复制文件/etc/passwd到/root/下成功')

# 实现复制一个文件
# src_dir = input('请输入一个文件的路径：')
# dst_dir = input('您打算将文件放在哪：')
#
# src_fobj = open(src_dir, 'rb')
# dst_fobj = open(dst_dir, 'wb')
#
# while True:
#     data = src_fobj.read(4096)
#     if not data:
#         break
#     dst_fobj.write(data)
#
# src_fobj.close()
# dst_fobj.close()

import os
src_dir = '/bin/ls'
dst_dir = '/tmp/ls1'
log = True

with open(src_dir, 'rb') as src_fobj:
        with open(dst_dir, 'wb') as dst_fobj:
            while log:
                data = src_fobj.read(4096)
                if not data:
                    log = False
                    continue
                dst_fobj.write(data)
            else:
                os.chmod(dst_dir, 755)
