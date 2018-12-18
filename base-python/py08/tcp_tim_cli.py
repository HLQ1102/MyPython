import socket

host = '127.0.0.1'
port = 21567
addr = (host, port)

c = socket.socket()
c.connect(addr)
data1 = 'haha'
c.send(data1.encode())
data = c.recv(1024)
print(data.decode())
c.close()