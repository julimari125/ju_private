import sqlite3
import sys
import sys

args = sys.argv
db_name = 'python_training.db'
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
book = cursor.execute('SELECT * FROM books;').fetchone()
print(book)
books = cursor.execute('SELECT * FROM books').fetchall()
print(books)
# cursor.execute('INSERT INTO books (name,kind) VALUES ("python入門","ビジネス")')
# cursor.execute(f"INSERT INTO books (name,kind) VALUES ('{args[1]}','{args[2]}')")
connection.commit()
connection.close()