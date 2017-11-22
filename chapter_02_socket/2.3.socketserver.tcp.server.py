#! /usr/bin/env python
# coding: utf-8

from SocketServer import TCPServer, StreamRequestHandler
from time import ctime

HOST = ''
PORT = 27891
ADDR = (HOST, PORT)

class MyRequestHandler(StreamRequestHandler):

    def handle(self):
        print '...connected from: ', self.client_address
        self.wfile.write(
            '[{}] {}'.format(ctime(), self.rfile.readline())
        )

tcp_ser = TCPServer(ADDR, MyRequestHandler)
print 'waiting for connection ...'
tcp_ser.serve_forever()
