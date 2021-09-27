from flask import Flask,render_template, request,redirect
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
    sql = f"SELECT * from books WHERE name LIKE '%{book_name}%' AND kind LIKE '%{book_kind}%'"
    books = cursor.execute(sql).fetchall()
    connection.close
    return render_template('index.html', books = books )

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    params = request.form
    print(params)
    db_name = 'python_training.db'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql = f"INSERT INTO books (name,kind) VALUES ('{params['name']}','{params['kind']}')"
    connection.execute(sql)
    connection.commit()
    connection.close()
    return redirect('/')

@app.route('/<int:id>/edit')
def edit(id):
    print(id)
    return render_template('edit.html', id = id)


app.run(debug=True)