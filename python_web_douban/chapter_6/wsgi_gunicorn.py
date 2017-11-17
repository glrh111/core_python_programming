from flask import Flask
app = Flask(__name__)

@app.route('/heihei')
def wocao():
    return "nihao"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)