import urllib.request
import urllib.parse
import json

content = 'when you do what you love, you love what you do'

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"

data = {}
data['i'] = content
data['from'] = 'en'
data['to'] = 'zh-CHS'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15510108667005'
data['sign'] = '6da3eb38866498e967fd98450958f513'
data['ts'] = '1551010866700'
data['bv'] = 'ff45f3fcdb2fc717d63404fb1ed57fd3'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'false'
data = urllib.parse.urlencode(data).encode('utf-8')

# data = {'query': 'hello'}
User_Agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'
headers = {'User-Agent': User_Agent}

req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)

print(target['translateResult'][0][0]['tgt'])
