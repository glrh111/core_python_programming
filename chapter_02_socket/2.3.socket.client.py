#! /usr/bin/env python
# coding: utf-8

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcp_cli_sock = socket(AF_INET, SOCK_STREAM)
tcp_cli_sock.connect(ADDR)

ip = gethostbyname('glrh11.com')
print ip
print htonl(255)
print inet_pton(AF_INET, ip)

while True:
    data = raw_input('> ')

    if not data:
        break

    tcp_cli_sock.send(data)

    r_data = tcp_cli_sock.recv(1024)
    if not r_data:
        break

    print r_data

tcp_cli_sock.close()