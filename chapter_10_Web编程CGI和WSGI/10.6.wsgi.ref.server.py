# coding: utf-8

from wsgiref.simple_server import WSGIServer, make_server

def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return ["Hello, World!"]

httpd = make_server('', 8888, simple_app)
print 'start app serving on port 8888 ...'
httpd.serve_forever()
