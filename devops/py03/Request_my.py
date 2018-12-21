from urllib.request import Request, urlopen
# 使用Request更改访问的浏览器


header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
html = Request('http://127.0.0.1', headers=header)
data = urlopen(html).read()

print(data)
