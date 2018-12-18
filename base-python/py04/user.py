#!/usr/bin/env python3
import shutil
import os

def get_name():
    while True:
        filename = input('请输入文件名：')
        if os.path.isfile(filename):
            print('文件已存在')
            continue
        break
    return filename

def get_content():
    content = []
    while True:
        line = input('(请输入文件内容，输入0结束输入)>')
        if line == '0':
            break
        content.append(line)
    return content

def wfile(filename, content):
    with open(filename, 'w+') as f:
        f.writelines(content)
    return 1

if __name__ == '__main__':
    fname = get_name()
    content = get_content()
    date = [line + '\n' for line in content]
    wfile(fname, date)
