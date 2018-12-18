import socket
from time import strftime

host = ''
port = 12345
addr = (host, port)

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(2)

while True:
    cli_socket, cli_addr = s.accept()
    while True:
        data =cli_socket.recv(1024)
        if data.decode().strip()  == 'quit':
            break
        print(data.decode())
        cdata = '你好[%s]\r\n' % strftime('%H:%M:%S')
        cli_socket.send(cdata.encode())

    cli_socket.close()

# s.close()
