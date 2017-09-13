#! /usr/bin/env python
# coding: utf-8

from socket import *
from time import ctime

HOST = 'glrh11.com'
PORT = 80
BUFSIZE = 1024
ADDR = (HOST, PORT)



while True:
    tcp_cli_sock = socket(AF_INET, SOCK_STREAM)
    tcp_cli_sock.connect(ADDR)
    data = raw_input('> ')

    if not data:
        break

    tcp_cli_sock.send(data)

    r_data = tcp_cli_sock.recv(1045)
    if not r_data:
        break

    print r_data

    tcp_cli_sock.close()