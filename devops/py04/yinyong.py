import requests

sname = '/tmp/xx.jpg'
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1545470480573&di=6e32402ccb4a6217eb4b01db5fdde994&imgtype=0&src=http%3A%2F%2Ff.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F83025aafa40f4bfb669be3ed0e4f78f0f736183b.jpg'
x = requests.get(url)
with open(sname, 'wb') as f:
    f.write(x.content)

r = requests.get('http://www.weather.com.cn/data/zs/101271301.html')
r.encoding = 'utf8'
print(r.json())

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
r = requests.get('http://127.0.0.1', headers=headers)

sogou = 'https://image.sogou.com/web'
params = {'query': '古风美女'}
x = requests.get(sogou, params=params)
with open('/tmp/sog.html', 'wb') as f:
    f.write(x.content)

sogou = ''
x = requests.get(sogou, headers=headers)
with open('/tmp/sog.html', 'wb') as f:
    f.write(x.content)
