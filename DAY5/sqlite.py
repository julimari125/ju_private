import sqlite3

class Sqlite:
    def __init__(self):
        self.connection = sqlite3.connect('python_training.db')

    def __del__(self): 
        self.connection.close()

    def execute(self, sql): 
        self.connection.cursor().execute(sql) 
        self.connection.commit()

    def fetch_all(self, sql):
        return self.connection.cursor().execute(sql).fetchall()
    
    def fetch_one(self, sql):
        return self.connection.cursor().execute(sql).fetchone()