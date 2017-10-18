from werkzeug.wsgi import SharedDataMiddleware
from flask import Flask, request, abort
from flask.views import MethodView

from ext import db, mako
from utils import get_file_path
from models import PasteFile

app = Flask(
    __name__,
    template_folder='../../templates/r',
    static_folder='../../static'
)
app.config.from_object('config')

app.wsgi_app = SharedDataMiddleware(
    app.wsgi_app,
    { '/i/': get_file_path() }
)

mako.init_app(app)
db.init_app(app)


# /
class IndexView(MethodView):

    def get(self):

        return

    def post(self):
        uploaded_file = request.files['file']
        w = request.form.get('w')
        h = request.form.get('h')
        if not uploaded_file:
            return abort(400)

        if w and h:
            paste_file = PasteFile.rsize(uploaded_file, w, h)
        else:
            paste_file = PasteFile.create


app.add_url_rule('/', view_func=IndexView.as_view('index_view'))
