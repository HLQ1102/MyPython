import re
from collections import Counter

def count_ip(fname, patt):
    result = Counter()
    fdict = {}
    with open(fname, 'r') as f:
        cpatt = re.compile(patt)
        for line in f:
            # ip = re.match('(\d+\.)+\d+', line).group()
            ip = cpatt.match(line)
            if ip:
                key = ip.group()
                result.update([key])
    return result


class Count():
    def __init__(self, patt):
        self.cpatt = re.compile(patt)
    def count_ip(self, fname):
        fdict = {}
        result = Counter()
        with open(fname, 'r') as f:
            cpatt = re.compile('(\d+.)+\d+')
            for line in f:
                # ip = re.match('(\d+\.)+\d+', line).group()
                ip = cpatt.match(line)
                if ip:
                    key = ip.group()
                    # fdict[key] = fdict.get(key, 0) + 1
                    result.update([key])  # 以[key]整体进行统计，并且按值的大小进行排序
        return result


if __name__ == '__main__':
    ip = '(\d+\.)+\d+'
    # print(count_ip('access_log', ip))
    # patt = count_ip('access_log', ip)
    # print(patt)
    # print(patt.most_common(3))
    aa = Count(ip)
    bb = aa.count_ip('access_log')
    print(bb)
