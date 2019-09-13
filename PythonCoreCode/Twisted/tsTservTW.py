from twisted.internet import protocol,reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    #当有客户端链接时候，调用该方法
    def connectionMade(self):
        Clnt = self.Clnt = self.transport.getPeer().host
        print('...connected from:',Clnt)
    #当有数据交换时，调用该方法
    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(),data))


factory = protocol.Factory()
#创建协议工厂，每次有接入都会造一个实例，
factory.protocol = TSServProtocol
print('waiting for connection ...')
reactor.listenTCP(PORT,factory)
reactor.run()