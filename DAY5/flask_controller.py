from flask import Flask,render_template, request
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    parameter = request.args
    print(parameter.get('name'))
    book_name = parameter.get('name','')
    book_kind = parameter.get('kind','')
    db_name = 'python_training.db'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql = 'SELECT * from books'
    books = cursor.execute(sql).fetchall()
    print(books)
    connection.close
    return render_template('index.html', book = book_name, kind = book_kind )

@app.route('/hello')
def hello():
    return ('<h1>hello</h1>')

app.run(debug=True)