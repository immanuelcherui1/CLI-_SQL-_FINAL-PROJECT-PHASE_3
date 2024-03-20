import sqlite3
from . import CURSOR
from profile import Profile

class TeaProfile:
    def __init__(self, date, pluckers_national_id, kilos):
        self.date = date
        self.pluckers_national_id = pluckers_national_id
        self.kilos = kilos

    def save(self):
        CURSOR.execute("INSERT INTO tea_profile (date, pluckers_national_id, kilos) VALUES (?, ?, ?)",
                       (self.date, self.pluckers_national_id, self.kilos))

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of TeaProfile instances """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS tea_profile (
                id INTEGER PRIMARY KEY,
                date TEXT,
                pluckers_national_id INTEGER,
                kilos REAL,
                FOREIGN KEY (pluckers_national_id) REFERENCES profile(national_id)
            )
        ''')