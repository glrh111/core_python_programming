#! /usr/bin/env python
# coding: utf-8

from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFSIZE = 1024
ADDR = (HOST, PORT)

udp_ser_sock = socket(AF_INET, SOCK_DGRAM)
udp_ser_sock.bind(ADDR)

socketpair()
create_connection()

while True:
    print 'Waiting for connection ...'

    data, addr = udp_ser_sock.recvfrom(BUFSIZE)
    print '...received data from: ', addr
    udp_ser_sock.sendto(
        '[{}] {}'.format(ctime(), data), addr
    )

udp_ser_sock.close()