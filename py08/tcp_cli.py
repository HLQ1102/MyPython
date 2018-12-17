import socket

host = '127.0.0.1'   # 指定要访问的服务端，这里以本地做实验
port = 12345
addr = (host, port)

c = socket.socket()  # 创建套接字
c.connect(addr)  # 建立连接
c.send(b'haha')  # 发送数据，以bytes数据方式发送
data = c.recv(1024)  # 接受数据
print(data.decode())  # 将接受的数据转化成utf8编码方式进行打印
c.close()   # 关闭客户端的套接字