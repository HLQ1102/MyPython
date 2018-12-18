import datetime
import hashlib
import os
import pickle as pic
import tarfile
import time


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


# 使用递归的方法遍历文件夹
# def list_files(path, ls=[]):
#     if os.path.isdir(path):
#         content = os.listdir(path)
#         for fname in content:
#             fname = os.path.join(path, fname)
#             if not os.path.isdir(fname):
#                 ls.append(os.path.join(path, fname))
#                 # print(ls[-1])
#             list_files(fname)
#     return ls


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
    with open('data-%s.data' % time.strftime('%Y-%m-%d'), 'wb') as f:
        pic.dump(a, f)
    return 'data-%s.data' % time.strftime('%Y-%m-%d')


def BiJiao(newf, oldf='data.data'):
    bianhua = []
    with open(oldf, 'rb') as of:
        old = pic.load(of)
    with open(newf, 'rb') as nf:
        new = pic.load(nf)
    for i in new:
        if i not in old:
            bianhua.append(i)
        else:
            if new[i] != old[i]:
                bianhua.append(i)
    return bianhua


def show_menu():
    today = datetime.datetime.today()
    tarfname = '/tmp/security-%s.tar.gz' % time.strftime('%Y-%m-%d')
    nowfile = bianlifile()
    check = check_md5(nowfile)
    if today.today() == 1:
        tarfact(bianlifile(), tarfname)
    else:
        today_data = 'data-%s-%s-%s.data' % (today.year, today.month, today.day)
        yesterday_data = 'data-%s-%s-%s.data' % (today.year, today.month, today.day - 1)
        bianhua = BiJiao(today_data, yesterday_data)
        tarfact(bianhua, tarfname)


if __name__ == '__main__':
    show_menu()

    # 以下三句是对list_files函数的测试
    # bb = list_files('/tmp/demo')
    # for i in bb:
    #     print(i)

    # for i in b:
    #     print(i)
    # BiJiao('/tmp/security-2018-12-14.tar.gz', bianlifile())
    # show_menu()
    #     tarfname = '/tmp/security-%s.tar.gz' % time.strftime('%Y-%m-%d')
    #     tarfact(bianlifile(), tarfname)
    #     check_md5(bianlifile())
    #     a = BiJiao('data-2018-12-15.data', 'data-2018-12-14.data')
    #     print(a)
    # new = check_md5(bianlifile())
    # data = check_md5(bianlifile())
    # print(data)
    # ww = '/tmp/wanquan.txt'
    # with open(ww, 'wb') as fobj:
    #     pic.dump(check_md5(bianlifile()), fobj)
    # BiJiao()
    # with open('/tmp/wanquan.txt', 'rb') as f:
    #     x = pic.load(f)
    # print(x)
