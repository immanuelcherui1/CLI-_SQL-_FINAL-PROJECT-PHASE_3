import sqlite3
from . import CURSOR,CONN

class Profile:
    def __init__(self, name, national_id,id=None):
        self.id = id
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
        CONN.commit()
    
    def save(self):
        CURSOR.execute("INSERT INTO profiles (name, national_id) VALUES (?, ?)", (self.name, self.national_id))
        CONN.commit()
    
    @classmethod
    def create(cls, name, national_id):
        """ Initialize a new Profile instance and save the object to the database """
        profile = cls(name, national_id)
        profile.save()
        return profile
    
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Profile instances """
        CURSOR.execute("""
            DROP TABLE IF EXISTS profiles;
        """)
        CONN.commit()
    
    @classmethod
    def get_all(cls):
        """ Retrieve all profiles from the database """
        CURSOR.execute("""
            SELECT profiles.name AS NAME, profiles.national_id NATIONAL_ID
            FROM profiles 
			ORDER BY NAME;
        """)
        return CURSOR.fetchall()
    
    
    # def update(self, new_name, new_national_id):
    #     """ Update the attributes of the profile in the database """
    #     self.name = new_name
    #     self.national_id = new_national_id
    #     CURSOR.execute("UPDATE profiles SET name=?, national_id=? WHERE id=?", 
    #                    (self.name, self.national_id, self.id))
    #     CONN.commit()
        
    
    @classmethod
    def find_by_national_id(cls, national_id):
        """ Retrieve a profile from the database by its national_id """
        CURSOR.execute("SELECT * FROM profiles WHERE national_id=?", (national_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        else:
            return None
    
    # def update(self):
    #     """Update the table row corresponding to the current Department instance."""
    #     sql = """
    #         UPDATE departments
    #         SET name = ?, location = ?
    #         WHERE id = ?
    #     """
    #     CURSOR.execute(sql, (self.name, self.location, self.id))
    #     CONN.commit()