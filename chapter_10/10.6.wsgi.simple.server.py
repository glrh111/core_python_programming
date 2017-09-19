# coding: utf-8

"""服务器实现示例
"""

import StringIO
import sys

def run_wsgi_app(app, environ):
    body = StringIO.StringIO()

    def start_response(status, headers):
        body.write('Status: {}\r\n'.format(status))
        for header in headers:
            body.write('{}: {}\r\n'.format(header[0], header[1]))
        return body.write

    iterable = app(environ, start_response)
    try:
        if not body.getvalue():
            raise RuntimeError("start_response() not called by app!")
        body.write('\r\n{}\r\n'.format(
            '\r\n'.join(line for line in iterable)
        ))
    finally:
        if hasattr(iterable, 'close') and callable(iterable.close):
            iterable.close()

    sys.stdout.write(body.getvalue())
    sys.stdout.flush()