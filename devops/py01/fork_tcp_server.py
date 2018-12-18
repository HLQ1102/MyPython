import socket
from time import strftime
import os
import threading

class TcpServer:
    def __init__(self, host = '', port = 12345):
        self.addr = (host, port)
        self.s_socket = socket.socket()
        self.s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s_socket.bind(self.addr)
        self.s_socket.listen(1)

    def chat(self, cli_sock):   #  与客户端进行通信的方法
        while True:
            data = cli_sock.recv(1024)
            if data.strip() == b'quit':  # 如果客户端输入quit就退出通信
                break
            data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode())
            cli_sock.send(data.encode())

    # def run(self):
    #     while True:
    #         cli_socket, cli_addr = self.s_socket.accept()
    #         retval = os.fork()   # 将资源拷贝一份，父、子进程都有s_socket和cli_cocket
    #         if not retval:          # 判断，只有子进程能进行执行的语句
    #             self.s_socket.close()   # 子进程关闭s_socket
    #             self.chat(cli_socket)   # 与客户端进行通信
    #             cli_socket.close()      # 退出通信，子进程关闭cli_socket
    #             exit()      # 关闭子进程
    #         cli_socket.close() # 父进程关闭客户端的套接字cli_socket

    def run(self):
        while True:
            cli_socket, cli_addr = self.s_socket.accept()
            t = threading.Thread(target=self.chat(cli_socket), args=(cli_socket,))
            t.start()
            # while True:
            #     result = os.waitpid(-1, 1)
            #     if result[0] == 0:
            #         break
        # s_socket.close()    # 服务器一般不会停止服务

if __name__ == '__main__':
    server = TcpServer()
    server.run()