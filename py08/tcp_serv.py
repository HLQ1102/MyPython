# import socket
#
# host = ''     # 代表0.0.0.0
# port = 12345  # 应该大于1024
# addr = (host, port)
# s = socket.socket()  # 默认使用TCP协议
# # 设置套接字选项，使得服务程序结束后可立即再启动
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind(addr)
# s.listen(1)  # 一般只能写到5以内，表示允许多少客户端排队访问
# cli_sock, cli_addr = s.accept()
# print('客户端：', cli_addr)
# data = cli_sock.recv(1024)  # 相当于fobj.read(1024)
# print(data)
# print(data.decode())
# sdata = '欢迎!\r\n'
# cli_sock.send(sdata.encode())   # 放送的数据必需是bytes类型，二进制
# cli_sock.close()
# s.close()



import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()  # 建立socket对象
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  # 这里value设置为1，表示将SO_REUSEADDR标记为TRUE，
  # 操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。
s.bind(addr) # 绑定socket

s.listen(1)
cli_sock, cli_addr = s.accept()  #接受来自客户端的链接，
print('链接', cli_addr)
data = cli_sock.recv(1024)  # 接受开自客户端的数据
print(data)     # 在屏幕上打印来自客户端的数据，bytes数据类型
print(data.decode())    # data.decode() 方法将bytes数据转化成字符串类型
sdata = '在的\r\n'  # 准备发给客户端的数据
cli_sock.send(sdata.encode()) # sdata.encode() 方法将字符串的数据转化成bytes类型
cli_sock.close()  # 关闭客户段的socket
s.close()     # 关闭服务端的socket