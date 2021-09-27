from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return('<h1>hello flask</h1>')


@app.route('/hello')
def hello():
    return ('<h1>hello</h1>')

app.run(debug=True)