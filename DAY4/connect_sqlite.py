import sqlite3
import sys
# db_name = 'python_training.db'
# connection = sqlite3.connect(db_name)
# cursor = connection.cursor()
# cursor.execute('INSERT INTO books (name, kind) VALUES ("python入門","プログラミング")')
# connection.commit()
# connection.close()
args = sys.argv
db_name = 'python_training.db'
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
books = cursor.execute('SELECT * FROM books').fetchall()
print(books)
book = cursor.execute('SELECT * FROM books').fetchone()
print(book)
connection.execute(f"INSERT INTO books(name,kind)VALUES ('{args[1]}','{args[2]}')")
connection.commit()
connection.close()