import telegram
import sys
import requests
import re
from urllib.request import urlopen
import time
import os
from PIL import Image


# 发送消息
def send_text(token, id, content):
    bot = telegram.Bot(token=token)
    Return = bot.send_message(chat_id=id, text=content)

    # return Return


# 发送图片
def send_phtot(token, id, url):
    bot = telegram.Bot(token=token)
    image_list = get_phtot_url(url)
    sum1 = 0
    llist = []
    for photo in image_list:
        if sum1 % 2 == 0:
            time.sleep(1)
        size = len(urlopen(photo).read())
        if size >= 70000:
            llist.append(size)
            sum1 += 1
            bot.send_photo(chat_id=id, photo=photo)
    print('标准是%s' % 70000)
    print("一共发了%d张照片" % sum1)
    print('平均大小是', sum(llist)/len(llist)/1024, 'KB')
    print(llist, len(llist))


# 发送带标题的web连接
def send_titleWeb(token, id, url):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=id, text='<a href = "%s" > %s </a >.' % (url, url),
                     parse_mode=telegram.ParseMode.HTML)


def send_channal(token, id, content):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=id, text=content)


def get_id(token_dict, who):
    w = requests.get("https://api.telegram.org/bot%s/getUpdates" % token_dict[who])
    result = w.json()['result']
    return result


# 判断群组还是个人
def PanDuan(result):
    print('check product.')
    jieguo = []
    for m in result:
        chat = m['message']['chat']
        if chat['id'] < 0:
            print('%s这是一个群组' % chat['title'])
        else:
            print('%s%s这是一个个人' % (chat['first_name'], chat['last_name']))


# 获取所有的图片的URL
def get_phtot_url(url, code='utf-8'):
    html = urlopen(url)
    tempfile = './temp'
    with open(tempfile, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)
    img_patt = '(http|https)://[-\w./]+(\.jpg|\.jpeg|\.png)'
    cpatt = re.compile(img_patt)
    result = []  # 把所有的匹配存入该列表
    with open(tempfile, encoding='utf-8', errors='ignore') as fobj:  # 打开文件时，可以指定字符集
        for line in fobj:
            match_objs = cpatt.finditer(line)  # 找到一行中的多个模式
            for m in match_objs:
                result.append(m.group())  # 将找到的内容追加到列表
    os.remove(tempfile)  # 删除临时文件
    print(result)
    print(len(result))
    return result


# 设定发送函数，使用字典映射来代替switch的选择语句
def send(token, id , content, url, tag):
    switch = {
        'text': send_text,
        'photo': send_phtot,
        'weblink': send_titleWeb,
        'channal': send_channal
    }
    argument = {
        'text': (token, id, content),
        'photo': (token, id, url),
        'weblink': (token, id, url),
        'channal': (token, id, content)
    }
    switch[tag](*argument[tag])  # “*”将元组解释成单个的个体


if __name__ == '__main__':
    token_dict = {"xiaofeng": '704391352:AAHoGlq9Owe8dLQaagShaGRxS2btlzsyN4w'}
    id_dict = {"xiaofeng": 712498831, 'xiaofeng_group': -355111393, 'play_channal': -1001400340255}
    token = token_dict["xiaofeng"]
    id1 = id_dict["xiaofeng"]
    content = '你好，世界'
    # python_bot_send(token, id1, content=content)
    # PanDuan(get_id(token_dict, 'xiaofeng'))
    url = 'http://fight.pcgames.com.cn/659/6598213.html'
    url = 'http://dy.qing5.com/article/4387.html'
    url = 'http://www.3lian.com/desk/2016/11/10768.html'
    url = 'https://telegra.ph/%E6%AF%8F%E6%97%A5%E7%8E%AF%E7%90%83%E8%A7%86%E9%87%8E-03-28'
    # url = 'https://www.7-zip.org/a/7z1900-x64.exe'
    # send(token=token, id=id_dict['play_channal'], url=url, content=content, tag='photo')
    send(token=token, id=id_dict['xiaofeng_group'], url=url, content=content, tag='photo')
