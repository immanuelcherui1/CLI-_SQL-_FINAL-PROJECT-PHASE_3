import sqlite3
from . import CURSOR,CONN
from profile import Profile

class MilkProfile:
    def __init__(self, date, dairy_farmer_national_id, litres):
        self.date = date
        self.dairy_farmer_national_id = dairy_farmer_national_id
        self.litres = litres

    def save(self):
        CURSOR.execute("INSERT INTO milk_profiles (date, dairy_farmer_national_id, litres) VALUES (?, ?, ?)",
                       (self.date, self.dairy_farmer_national_id, self.litres))
        CONN.commit()
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of MilkProfile instances """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS milk_profiles (
                id INTEGER PRIMARY KEY,
                date TEXT,
                dairy_farmer_national_id INTEGER,
                litres REAL,
                FOREIGN KEY (dairy_farmer_national_id) REFERENCES profile(national_id)
            )
        ''')
        CONN.commit()
    
    @classmethod
    def create(cls, date, dairy_farmer_national_id, litres):
        """ Initialize a new MilkProfile instance and save the object to the database """
        milk_profile = cls(date, dairy_farmer_national_id, litres)
        milk_profile.save()
        return milk_profile
    
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists MilkProfile instances """
        CURSOR.execute("""
            DROP TABLE IF EXISTS milk_profiles;
        """)
        CONN.commit()
