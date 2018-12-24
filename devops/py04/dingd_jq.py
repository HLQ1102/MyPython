import requests
import json
import sys

def ding_talk(url, content="我就是我,  @18081450559 是不一样的烟火"):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": [
                "18081450559"
            ],
            "isAtAll": False
        }
    }
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    return r.json()


def pic(url, content):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "link",
        "link": {
            "text": "我是当当图书",
            "title": "自定义机器人协议",
            "picUrl": "http://img3m2.ddimg.cn/20/7/25164632-1_b_3.jpg",
            "messageUrl": "http://search.dangdang.com/?key=python%D7%D4%B6%AF%BB%AF%D4%CB%CE%AC&act=input"
        }
    }
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    return r.json()


def markdown(url, content):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "markdown",
        "markdown": {"title": content,
                     "text": "####   \n > 9度，@18081450559 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](http://www.thinkpage.cn/) "
                     },
        "at": {
            "atMobiles": [
                "18081450559"
            ],
            "isAtAll": False
        }
    }
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    return r.json()


if __name__ == '__main__':
    url_wang = 'https://oapi.dingtalk.com/robot/send?access_token=8c25c037b3967dbae110cb6f85fbc7e4b99ad36b4dba390d870e9e86eb7b049b'
    url_yan = 'https://oapi.dingtalk.com/robot/send?access_token=ac5c1b7f00b952ac53cd08ae7d78cb53e99fd5d343174e2d819818801156d7f1'
    content = sys.argv[1]
    # print(ding_talk(url_wang, content))
    print(markdown(url_wang, content))



