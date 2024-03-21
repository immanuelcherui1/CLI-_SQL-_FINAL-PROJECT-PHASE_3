import sqlite3
from . import CURSOR,CONN
from profile import Profile

class TenantProfile:
    def __init__(self, tenant_national_id, entry_date, room_no, room_cost):
        self.tenant_national_id = tenant_national_id
        self.entry_date = entry_date
        self.room_no = room_no
        self.room_cost = room_cost

    def save(self):
        CURSOR.execute("INSERT INTO tenant_profiles (tenant_national_id, entry_date, room_no, room_cost) VALUES (?, ?, ?, ?)",
                       (self.tenant_national_id, self.entry_date, self.room_no, self.room_cost))
        CONN.commit()

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of TenantProfile instances """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS tenant_profiles (
                id INTEGER PRIMARY KEY,
                tenant_national_id INTEGER,
                entry_date TEXT,
                room_no INTEGER,
                room_cost REAL,
                FOREIGN KEY (tenant_national_id) REFERENCES profile(national_id)
            )
        ''')
        CONN.commit()
        
    @classmethod
    def create(cls, tenant_national_id, entry_date, room_no, room_cost):
        """ Initialize a new TenantProfile instance and save the object to the database """
        tenant_profile = cls(tenant_national_id, entry_date, room_no, room_cost)
        tenant_profile.save()
        return tenant_profile

    @classmethod
    def get_all(cls):
        """ Retrieve all tenant profiles from the database """
        CURSOR.execute("""
            SELECT tenant_profiles.id, tenant_profiles.entry_date, tenant_profiles.room_no, tenant_profiles.room_cost, profiles.name 
            FROM tenant_profiles 
            JOIN profiles ON tenant_profiles.tenant_national_id = profiles.national_id
        """)
        return CURSOR.fetchall()