import urllib

from flask import Flask, jsonify
from jinja2 import Template, Environment
from werkzeug.routing import BaseConverter
from werkzeug.wrappers import Response


class ListConverter(BaseConverter):

    def __init__(self, url_map, seperator='+'):
        super(ListConverter, self).__init__(url_map)
        self.seperator = urllib.unquote(seperator)

    def to_python(self, value):  # url -> python object
        return value.split(self.seperator)

    def to_url(self, values):
        return self.seperator.join(
            super(BaseConverter, self).to_url(value) for value in values
        )


app = Flask(__name__)
app.url_map.converters['list'] = ListConverter


@app.route('/<list():params>')
def one(params):
    print 'params ', params
    return 'params {}'


@app.route('/a/')
def a():
    return 'a'


@app.route('/b')
def b():
    return 'b'

@app.route('/c/')
def c():
    return Response('c')


class JsonResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response, environ)


app.response_class = JsonResponse


@app.route('/')
def hello_world():
    return {'message': 'hello'}


@app.route('/custom_headers')
def cus():
    return {'headers': [1, 2, 3]}, 201, [('X-Request-Id', '100')]

@app.route('/d')
def d():
    t = Template('wocao {{wocao}}')
    env = Environment()
    t2 = env.from_string(
        source="wocao {{wocao2}}",
        globals={"wocao2": "wodaye"}
    )
    return t2.render(wocao="nidaye!")


app.run(debug=True)