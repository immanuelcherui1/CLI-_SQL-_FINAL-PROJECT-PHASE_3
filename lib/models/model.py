import sqlite3
from . import CURSOR

class Model:
    def __init__(self, model):
        self.model = model

    def save(self):
        CURSOR.execute("INSERT INTO models (model) VALUES (?)", (self.model,))

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Model instances """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS models (
                id INTEGER PRIMARY KEY,
                model TEXT
            )
        ''')

    
    @classmethod
    def create(cls, model):
        """ Initialize a new Model instance and save the object to the database """
        model_ = cls(model)
        model_.save()
        return model_