import os
import re
import urllib.request

import requests

headers = {}
headers['Referer']: 'https://www.pexels.com/search/beautiful%20girl/'
headers['User-Agent']: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'


def get_img_url(url):
    tempfile = './haha.html'
    try:
        req = urllib.request.Request(url, headers)
        html = urllib.request.urlopen(req)
        with open(tempfile, 'wb') as fobj:
            while True:
                data = html.read(1024)
                if not data:
                    break
                fobj.write(data)
    except Exception:
        with open(tempfile, 'w', errors='ignore') as f:
            html = requests.get(url)
            f.write(html.text)

    img_patt = '(http|https)://[-\w./]+(\.jpg|\.jpeg|\.png)'
    cpatt = re.compile(img_patt)
    result = []  # 把所有的匹配存入该列表
    with open(tempfile, encoding='utf-8', errors='ignore') as fobj:  # 打开文件时，可以指定字符集
        for line in fobj:
            match_objs = cpatt.finditer(line)  # 找到一行中的多个模式
            for m in match_objs:
                result.append(m.group())
    os.remove(tempfile)
    print(result)
    print(len(result))
    return result


if __name__ == '__main__':
    url = 'https://www.pexels.com/search/beautiful%20girl/'
    get_img_url(url)
