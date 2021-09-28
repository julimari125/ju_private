from peewee import *

class Book(Model): 
    name = CharField()
    kind = CharField() 
    class Meta:
        database = SqliteDatabase('python_training.db') 
        table_name = 'books'