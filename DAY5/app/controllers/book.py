
from flask import Flask,render_template, request,redirect,Blueprint
from utils.sqlite import Sqlite
from models.book import Book
app = Blueprint('book',__name__)


@app.route('/')
def index():
    parameter = request.args
    book_name = parameter.get('name','')
    book_kind = parameter.get('kind','')
    sql = f"SELECT * from books WHERE name LIKE '%{book_name}%' AND kind LIKE '%{book_kind}%'"
    books = Sqlite().fetch_all(sql)
    return render_template('books/index.html', books = books )

@app.route('/new')
def new():
    return render_template('books/new.html')

@app.route('/create', methods=['POST'])
def create():
    params = request.form
    print(params)
    sql = f"INSERT INTO books (name,kind) VALUES ('{params['name']}','{params['kind']}')"
    Sqlite().execute(sql)
    return redirect('/')

@app.route('/<int:id>/edit')
def edit(id):
    book = Book.get_by_id(id)
    print(book)
    return render_template('books/edit.html', book = book)


@app.route('/<int:id>/update', methods=['POST'])
def update(id):
    params = request.form
    sql = f"UPDATE books SET name = '{params['name']}', kind = '{params['kind']}'  WHERE id = {id}"
    Sqlite().execute(sql)
    return redirect('/')

@app.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    sql = f"DELETE FROM books WHERE id = { id }"
    Sqlite().execute(sql)
    return redirect('/')

# app.run(debug=True)