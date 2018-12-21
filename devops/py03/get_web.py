import sys
from urllib.request import urlopen


def download(url, fname):
    html = urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                # print('download over')
                break
            fobj.write(data)


if __name__ == '__main__':
    url = input('url:')
    fname = input('fname:')
    download(url, fname)

