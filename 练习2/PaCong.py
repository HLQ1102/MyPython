

from urllib.request import urlopen

import wget

html = urlopen('https://pic.sogou.com/pics?ie=utf8&p=40230504&interV=kKIOkrELjboMmLkEk7cTkKIRmLkElbYTkKIKmbELjboJmLkEkL8TkKIMkLELjbgRmLkEkLY=_-1780069410&query=%E5%8F%A4%E9%A3%8E%E7%BE%8E%E5%A5%B3&')

wget.download('https://i04piccdn.sogoucdn.com/2d69e199ad48af1e')
