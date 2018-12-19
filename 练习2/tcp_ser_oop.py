import socket
import os
from time import strftime

def so(host = '0.0.0.0', port = 12345):
    addr = (host, port)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(2)
    cli_sock, addr = s.accept()
    return cli_sock,addr
    
def run(cli_sock, addr):
    cdata = cli_sock.recv(1024)
    print(cdata.decode())
    sdata = 'hello\r\n'
    cli_sock.send(sdata.encode())
    cli_sock.close()
    s.close()

if __name__ == '__main__':
    s = socket.socket()
    while True:
        run(*so())
