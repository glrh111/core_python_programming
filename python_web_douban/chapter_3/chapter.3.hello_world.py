#! /usr/bin/env python
# coding: utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run('0.0.0.0', 9000, True)
