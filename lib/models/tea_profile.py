import sqlite3
from . import CURSOR, CONN
from profile import Profile

class TeaProfile:
    def __init__(self,id, date, pluckers_national_id, kilos):
        self.id = id
        self.date = date
        self.pluckers_national_id = pluckers_national_id
        self.kilos = kilos

    def save(self):
        CURSOR.execute("INSERT INTO tea_profiles (date, pluckers_national_id, kilos) VALUES (?, ?, ?)",
                       (self.date, self.pluckers_national_id, self.kilos))
        CONN.commit()
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of TeaProfile instances """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS tea_profiles (
                id INTEGER PRIMARY KEY,
                date TEXT,
                pluckers_national_id INTEGER,
                kilos REAL,
                FOREIGN KEY (pluckers_national_id) REFERENCES profiles(national_id)
            )
        ''')
        CONN.commit()

    
    @classmethod
    def create(cls, date, pluckers_national_id, kilos):
        """ Initialize a new TeaProfile instance and save the object to the database """
        tea_profile = cls(None,date, pluckers_national_id, kilos)
        tea_profile.save()
        return tea_profile
    
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists TeaProfile instances """
        CURSOR.execute("""
            DROP TABLE IF EXISTS tea_profiles;
        """)
        CONN.commit()
        
    @classmethod
    def get_all(cls):
        """ Retrieve all tea profiles from the database """
        CURSOR.execute("""
            SELECT profiles.name AS PLUCKERS_NAME, tea_profiles.date AS PLUCKING_DATE, tea_profiles.kilos AS KILOS
            FROM tea_profiles 
            JOIN profiles ON tea_profiles.pluckers_national_id = profiles.national_id
        """)
        return CURSOR.fetchall()
    
    @classmethod
    def find_by_national_id(cls, plucker_national_id):
        """ Retrieve tea profiles from the database by plucker's national_id """
        CURSOR.execute("SELECT * FROM tea_profiles WHERE pluckers_national_id=?", (plucker_national_id,))
        rows = CURSOR.fetchall()
        if rows:
            return [cls(*row) for row in rows]
        else:
            return None
