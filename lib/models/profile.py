import sqlite3
from . import CURSOR

class Profile:
    def __init__(self, name, national_id):
        self.name = name
        self.national_id = national_id


    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Profile instances """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY,
                name TEXT,
                national_id INTEGER UNIQUE,
                CONSTRAINT national_id_length CHECK (LENGTH(CAST(national_id AS TEXT)) = 8)
            )
        ''')
    
    def save(self):
        CURSOR.execute("INSERT INTO profiles (name, national_id) VALUES (?, ?)", (self.name, self.national_id))

    
    @classmethod
    def create(cls, name, national_id):
        """ Initialize a new Profile instance and save the object to the database """
        profile = cls(name, national_id)
        profile.save()
        return profile