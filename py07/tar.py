import os
import pickle as pic
import tarfile
import time
import hashlib
import datetime

def tarfact(tarfls, tarfname):
    # tar = tarfile.open('/tmp/per.tar.gz', 'w:gz')
    tar = tarfile.open(tarfname, 'w:gz')
    for file in tarfls:
        tar.add(file)
    tar.close()


def bianlifile():
    a = []
    for path, folders, files in os.walk('/tmp/demo'):
        for file in files:
            a.append(os.path.join(path, file))
    return a

def check_md5(fls):
    a = {}
    for fname in fls:
        m = hashlib.md5()
        with open(fname, 'rb') as fobj:
            while True:
                data = fobj.read(4096)
                if not data:
                    break
                m.update(data)
        a[fname] = m.hexdigest()
    with open('data.data', 'wb') as f:
        pic.dump(a, f)
    return a

def BiJiao(oldf, new):
    bianhua = []
    with open(oldf, 'rb') as of:
        old = pic.load(of)
    # with open(newf, 'rb') as nf:
    #     new = pic.load(nf)
    for i in new:
        if i not in old:
            bianhua.append(i)
        if new[i] != old[i]:
            bianhua.append(i)
    return bianhua

def shwo_menu():
    today = datetime.datetime.today()
    tarfname = '/tmp/security-%s.tar.gz' % time.strftime('%Y-%m-%d')
    nowfile = bianlifile()
    if today.today() == 1:
        check_md5(nowfile)
        tarfact(bianlifile(), tarfname)
    else:
        oldf = '/tmp/security-%s-%s-%s.tar.gz' % (today.year, today.month, today.day - 1)
        bianhua = BiJiao(oldf, nowfile)
        tarfact(nowfile, tarfname)


if __name__ == '__main__':

    new = check_md5(bianlifile())
    data = check_md5(bianlifile())
    print(data)
    ww = '/tmp/wanquan.txt'
    with open(ww, 'wb') as fobj:
        pic.dump(check_md5(bianlifile()), fobj)
    # BiJiao()
    # with open('/tmp/wanquan.txt', 'rb') as f:
    #     x = pic.load(f)
    # print(x)