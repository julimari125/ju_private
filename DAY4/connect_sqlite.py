import sqlite3
db_name = 'python_training.db'
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
cursor.execute('INSERT INTO books (name, kind) VALUES ("python入門","プログラミング")')
connection.commit()
connection.close()