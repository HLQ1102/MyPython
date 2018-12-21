import re
import os
# import sys
from urllib.request import urlopen


def download(url, fname):
    html = urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)


def find_patt(fname, patt, code='utf8'):
    cpatt = re.compile(patt)
    result = []
    with open(fname, encoding=code) as fobj:
        for line in fobj:
            match_objs = cpatt.finditer(line)
            for m in match_objs:
                n = m.group()
                result.append(n)
    return result


if __name__ == '__main__':
    net163 = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B7%E7%C9%A7%C3%C0%C5%AE&fr=ala&ala=1&alatpl=cover&pos=0&hs=2&xthttps=111111'
    html163 = '/tmp/baidugf.html'
    download(net163, html163)  # 下载网易首页
    # img_patt = '(http|https)://[-\w/]+(\.jpg|\.jpeg|\.png|\.gif)'
    img_patt = '(http|https)://[-\w./]+(\.jpg|\.jpeg|\.png|\.gif)'
    img_list = find_patt(html163, img_patt)
    # print(img_list)
    img_dir = '/tmp/myimg1'
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    print(len(img_list))
    for img in img_list:
        aa = img.split('/')[-1]
        aa = os.path.join(img_dir, aa)
        # print(img)
        download(img, aa)
