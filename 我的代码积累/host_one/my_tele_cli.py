from telethon import TelegramClient
from telethon import TelegramClient, sync,events
import socket
import logging
import random
import asyncio
import telethon
from telethon.tl.types import PeerUser, PeerChat, PeerChannel,UpdateNewChannelMessage
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl import types, functions
from telethon import utils


# 登陆验证
def login():
    api_id = 786873
    api_hash = 'd07b4926acbd566243b5caed1068f1f8'
    client = TelegramClient('some_name', api_id, api_hash)
    client.start()
    myself = client.get_me()
    # print(myself)
    return client


#  给某人发信息（信息，文件或图片），默认给自己发信息
def send_something(client, content, file='', who='me'):
    shiti = client.get_entity(who)  # 获得访问该实体的权限
    if file != '':
        client.send_file(shiti.id, file)
    else:
        client.send_message(shiti.id, content)
    messages = client.get_messages(shiti.id)
    print(messages[0].message)
    # print(messages)


# 查询某个人的信息
def send_oldnine(client, usernameORphone, content=''):
    peer = client.get_input_entity(usernameORphone)  # 可更换用户名@username或者手机号
    if content != '':
        client(SendMessageRequest(usernameORphone, content))
    peer = utils.get_input_peer(peer)
    print(peer)


# 发消息给自己的频道
def send_message_channal():
    pass


if __name__ == '__main__':
    client = login()
    content = '你好世界'
    dict_who = {'my_channal': 't.me/xiaofeng_1102', 'xiaofeng_group': -355111393}
    lonami = client.get_entity('me')  # 获得访问该实体的权限
    print(lonami)
    send_something(client, content)
    # client(SendMessageRequest(PeerChannel(lonami.id), 'Hello there!'))
    # client.send_message(lonami.id, 'nihao')
    # print(lonami)
    # my_channel = client.get_entity(PeerChannel('t.me/WebNotes'))
    # print(my_channel)
    # entity = client.get_entity(1140403915)
    # print(entity)
    # client.send_message(1400340255, 'll')
    # print(entity)
    # client(SendMessageRequest(dict_who['my_channal'], 'hello'))
    # client.send_message(dict_who['my_channal'], 'nihao')
