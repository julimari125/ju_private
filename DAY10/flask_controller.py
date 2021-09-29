from flask import Flask,render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    parameter = request.args
    book_name = parameter.get('name','')
    book_kind = parameter.get('kind','')
    db_name = 'python_training.db'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql =  f"SELECT * FROM books WHERE name LIKE '%{book_name}%' AND kind LIKE '%{book_kind}%'"
    books = cursor.execute(sql).fetchall()
    print(books)
    connection.close()
    return render_template('index.html',books = books)


@app.route('/hello')
def hello():
    return render_template('index.html' , book = '坊ちゃん')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create',methods=['POST'])
def create():
    return('create called')

app.run(debug=True)