import socket

host = ''      # 不指定服务器默认127.0.0.1
port = 12345
addr = (host, port)

s = socket.socket(type=socket.SOCK_DGRAM) # SOCK_DGRAM指定了这个Socket的类型是UDP
data1 = 'haha\r\n'
s.sendto(data1.encode(), addr)        # 转化编码方式(utf8 --> bytes),发送数据

data, ser_addr = s.recvfrom(1024)   # 接受来自服务端的数据
print(data.decode(), end='')   # 转化编码(bytes --> utf8),并打印

s.close()   # 关闭套接字
