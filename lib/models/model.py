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
