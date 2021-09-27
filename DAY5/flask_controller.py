from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return('hello flask')


@app.route('/hello')
def hello():
    return ('hello')

app.run(debug=True)