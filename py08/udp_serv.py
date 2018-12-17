import socket

host = '0.0.0.0' # 监听所有的ip地址
port = 12345     # 应用端口
addr = (host, port)

s = socket.socket(type=socket.SOCK_DGRAM) # SOCK_DGRAM指定了这个Socket的类型是UDP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#设置socket选项，当socket关闭后，本地端用于该socket的端口号立刻就可以被重用。
s.bind(addr)  #绑定 客户端口和地址:

data, cli_addr = s.recvfrom(1024)  # 接受来自客户端的数据
data = data.decode()  # 转化数据编码方式(utf8)
print(data, end='')   # 在屏幕打印数据
s.sendto(b'123?\r\n', cli_addr) # 将数据转化成bytes然后发送给客户端
s.close()  # 关闭套接字

