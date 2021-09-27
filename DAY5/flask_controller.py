from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    db_name = 'python_training.db'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql = 'SELECT * from books'
    book = cursor.execute(sql).fetchone()
    connection.close
    return render_template('index.html', book = book)

@app.route('/hello')
def hello():
    return ('<h1>hello</h1>')

app.run(debug=True)