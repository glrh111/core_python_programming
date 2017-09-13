#! /usr/bin/env python
# coding: utf-8

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21568
BUFSIZE = 1024
ADDR = (HOST, PORT)

udp_cli_sock = socket(AF_INET, SOCK_DGRAM)


while True:
    data = raw_input('> ')

    if not data:
        break

    udp_cli_sock.sendto(data, ADDR)

    r_data = udp_cli_sock.recvfrom(BUFSIZE)
    if not r_data:
        break

    print r_data

udp_cli_sock.close()