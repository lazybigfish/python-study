from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)

#该类作为srh的子类，并重写了handle方法，收到客户端的信息是就会启用handle方法
class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:',self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(),self.rfile.readline().decode())).encode())

tcpServ = TCP(ADDR,MyRequestHandler)
print('waiting for connection ...')
tcpServ.serve_forever()