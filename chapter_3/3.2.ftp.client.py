#! /usr/bin/env python
# coding: utf-8

import ftplib
import os
import socket


HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print 'ERROR: can not reach {}'.format(HOST)
        return

    print '*** Connected to host [{}]'.format(HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: can not login anonymously'
        f.quit()
        return
    print '*** Logged in as "anonymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: can not CD to [{}]'.format(DIRN)
        f.quit()
        return
    print '*** Changed to [{}]'.format(DIRN)

    try:
        f.retrbinary('RETR {}'.format(FILE), open(FILE, 'wb').write)
    except ftplib.error_perm:
        print 'ERROR: can not read file [{}]'.format(FILE)
        os.unlink(FILE)
    else:
        print 'Downloaded CWD to  [{}]'.format(FILE)

    f.quit()


if __name__ == '__main__':
    main()
