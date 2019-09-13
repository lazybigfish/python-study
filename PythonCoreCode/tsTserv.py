from socket import *
from time import ctime

HOST = ''
#host变量为空白，这事对bind()方法的标示，表示可以使用任何可用的地址
PORT = 21567
BUFSIZ = 1024
#该程序缓冲区大小为1kb
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
#创建服务器套接字
tcpSerSock.bind(ADDR)
#绑定到服务器地址
tcpSerSock.listen(5)
#开启监听

while True:
    print('waiting for connection...')
    tcpCliSock,addr = tcpSerSock.accept()
    print('...connected from:',addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send((('[%s] %s' % (ctime(),data.decode())).encode()))
    tcpCliSock.close()
tcpSerSock.close()