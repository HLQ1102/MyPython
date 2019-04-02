import re
import os
import time
import urllib.request
from urllib.request import urlopen
import requests
from webimg.geturl import get_img_url

import telegram

User_Agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'
headers = {'User-Agent': User_Agent}

data = []
data['cache-control']: "public, max-age=63115200"
data['content-length']: 134322
data['content-type']: "image/gif"
data['date']: "Tue, 02 Apr 2019 03:00:22 GMT"
data['etag']: '1e4c78a9c45c4862'
data['expires']: "Thu, 01 Apr 2021 04:02:16 GMT"
data['last-modified']: "Mon, 01 Apr 2019 16:02:16 GMT"


# 获取图片列表
def get_photo_list():
    global data, headers
    url = 'https://www.persianup.com/fashion/the-beautiful-girl-in-instagram/'
    req = urllib.request.Request(url, data, headers)
    html = urllib.request.urlopen(req)

    tempfile = './temp'
    try:
        req = urllib.request.Request(url, headers)
        html = urllib.request.urlopen(req)
        with open(tempfile, 'wb') as fobj:
            while True:
                data = html.read(1024)
                if not data:
                    break
                fobj.write(data)
    except Exception:
        with open(tempfile, 'w', errors='ignore') as f:
            html = requests.get(url)
            f.write(html.text)
    img_patt = '(http|https)://[-\w./]+(\.jpg|\.jpeg|\.png)'
    cpatt = re.compile(img_patt)
    result = []  # 把所有的匹配存入该列表
    with open(tempfile, encoding='utf-8', errors='ignore') as fobj:  # 打开文件时，可以指定字符集
        for line in fobj:
            match_objs = cpatt.finditer(line)  # 找到一行中的多个模式
            for m in match_objs:
                result.append(m.group())  # 将找到的内容追加到列表
    # os.remove(tempfile)
    print(result)
    print(len(result), '下一个\n')
    return filter_link(result)


# 过滤重复的.jpg或者.jpeg的图片连接
def filter_link(image_list):
    result1 = []
    for photo in image_list:
        photo1 = photo.split('/')[-1]
        if '.jpg' in photo1 or '.jpeg' in photo1:
            if len(result1) == 0:
                result1.append(photo)
            elif result1[-1].split('/')[-1] == photo1:
                continue
            else:
                result1.append(photo)
    for i in result1:
        print(i)
    print(len(result1))
    return result1


def send_phtot(token, id, image_list):
    # global headers
    header = {}
    header['accept']: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
    header['user-agent']: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'

    bot = telegram.Bot(token=token)
    sum1 = 0
    sum2 = 0
    llist = []
    for photo in image_list:
        sum2 += 1
        if '.png' in photo:
            print(photo)
            continue
        if sum1 % 3 == 0:
            time.sleep(2)
        elif sum2 == 11:
            time.sleep(5)
        req = urllib.request.Request(photo, headers=headers)
        size = len(urlopen(req).read())
        if size >= 50000:
            llist.append(size)
            try:
                bot.send_photo(chat_id=id, photo=photo)
                sum2 += 1
            except Exception:
                print('haha')
                continue
    print('标准是%s' % 60000)
    print("一共发了%d张照片" % sum2)
    print(llist, len(llist))
    # print('平均大小是KB' % sum(llist)/len(llist)/1024)
    # print(sum2)


if __name__ == '__main__':
    token_dict = {"xiaofeng": '704391352:AAHoGlq9Owe8dLQaagShaGRxS2btlzsyN4w'}
    id_dict = {"xiaofeng": 712498831, 'xiaofeng_group': -355111393, 'play_channal': -1001400340255}
    # result = get_photo_list()
    # send_phtot(token_dict['xiaofeng'], id_dict['xiaofeng_group'], result)
    url = 'https://www.persianup.com/entertainment/sexy-world-cup-women/'
    url = 'https://kami.com.ph/36927-most-beautiful-celebrities-philippines.html#36927'
    url = 'https://www.maxim.com/women/what-eden-rambo-wants-2018-11'
    url = 'https://www.jooomshaper.com/group/beautiful-girls-wallpapers-for-desktop/'
    # bot = telegram.Bot(token=token_dict['xiaofeng'])
    # bot.send_photo(chat_id=id_dict['xiaofeng_group'], photo='https://i1.wp.com/www.persianup.com/wp-content/uploads/2018/06/DAWyA77XkAE6h7k.jpg')
    result = filter_link(get_img_url(url))
    send_phtot(token_dict['xiaofeng'], id_dict['xiaofeng_group'], result)

    # bot = telegram.Bot(token=token_dict['xiaofeng'])
    # bot.send_photo(chat_id=id_dict['xiaofeng_group'], photo='https://images.pexels.com/photos/1308885/pexels-photo-1308885.jpeg')
