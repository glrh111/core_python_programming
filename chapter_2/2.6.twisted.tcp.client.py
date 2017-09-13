#! /usr/bin/env python
# coding: utf-8

from twisted.internet import protocol, reactor
from time import ctime

HOST = 'localhost'
PORT = 8888

class TSClntProtocol(protocol.Protocol):
    def send_data(self):
        data = raw_input('> ')
        if data:
            print '...sending [{}] ...'.format(data)
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.send_data()

    def dataReceived(self, data):
        print data
        self.send_data()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()