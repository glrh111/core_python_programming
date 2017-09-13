#! /usr/bin/env python
# coding: utf-8

from twisted.internet import protocol, reactor
from time import ctime

PORT = 8888

class TSServProtocol(protocol.Protocol):

    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from: ', clnt

    def dataReceived(self, data):
        self.transport.write(
            '[{}] {}'.format(ctime(), data)
        )

factory = protocol.Factory()      # 每次接入连接时,都能制造协议的一个实例
factory.protocol = TSServProtocol
print 'waiting for connection ...'
reactor.listenTCP(PORT, factory)
reactor.run()
