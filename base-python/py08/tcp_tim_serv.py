import socket
import time

host = '0.0.0.0'
port = 21567
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    cli_sock, cli_addr = s.accept()
    print('链接', cli_addr)
    while True:
        data = cli_sock.recv(1024)
        # print(data)
        data = data.decode()
        print(data.split())
        if not data:
            cli_addr.close()
            break
        sdata = data+str(time.time())+'\r\n'
        # print(sdata)
        cli_sock.send(sdata.encode())
# s.close()