#! /usr/bin/env python
# coding: utf-8

from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM, socket

so = socket(AF_INET, SOCK_STREAM)

print so.family, so.type, so.proto

so.bind(('127.0.0.1', 8888))

so.listen(5)

while True:

    cs = so.accept()

    cs.