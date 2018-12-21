from urllib.request import quote, urlopen, Request

print(quote('你好'))

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
baidu = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='
hi = quote('风骚美女')
html = Request(baidu + hi, headers=header)
data = urlopen(html)
with open('/tmp/baidu.html', 'wb') as fobj:
    fobj.write(data.read())
