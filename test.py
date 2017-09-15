#! /usr/bin/env python
# coding: utf-8

import string
import sys
import time

def main():
    s = ('|/-\\')*1000
    for c in s:
        sys.stdout.write(c + '\r')
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    main()
