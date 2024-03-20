import sqlite3
from . import CURSOR
from profile import Profile

class MilkProfile:
    def __init__(self, date, dairy_farmer_national_id, litres):
        self.date = date
        self.dairy_farmer_national_id = dairy_farmer_national_id
        self.litres = litres

    def save(self):
        CURSOR.execute("INSERT INTO milk_profile (date, dairy_farmer_national_id, litres) VALUES (?, ?, ?)",
                       (self.date, self.dairy_farmer_national_id, self.litres))

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of MilkProfile instances """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS milk_profile (
                id INTEGER PRIMARY KEY,
                date TEXT,
                dairy_farmer_national_id INTEGER,
                litres REAL,
                FOREIGN KEY (dairy_farmer_national_id) REFERENCES profile(national_id)
            )
        ''')
