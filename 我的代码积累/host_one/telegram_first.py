#!/usr/local/bin/python3

import json
import requests
import sys

def send_msg(url, remiders, msg):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    data = {
        "msgtype": "text",
        "at": {
            "atMobiles": remiders,
            "isAtAll": False,
        },
        "text": {
            "content": msg,
        }
    }
    data1 = {
        "text":msg,
    }
    r = requests.post(url, data=json.dumps(data1), headers=headers)
    return r.text


if __name__ == '__main__':
    # msg = sys.argv[1]
    msg = 'haha'
    remiders = []
    url = 'https://api.telegram.org/bot704391352:AAHoGlq9Owe8dLQaagShaGRxS2btlzsyN4w/sendMessage?chat_id=712498831'
    print(send_msg(url, remiders, msg))
