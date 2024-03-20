import sqlite3
from . import CURSOR
from profile import Profile

class TenantProfile:
    def __init__(self, tenant_national_id, entry_date, room_no, room_cost):
        self.tenant_national_id = tenant_national_id
        self.entry_date = entry_date
        self.room_no = room_no
        self.room_cost = room_cost

    def save(self):
        CURSOR.execute("INSERT INTO tenant_profile (tenant_national_id, entry_date, room_no, room_cost) VALUES (?, ?, ?, ?)",
                       (self.tenant_national_id, self.entry_date, self.room_no, self.room_cost))

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of TenantProfile instances """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS tenant_profile (
                id INTEGER PRIMARY KEY,
                tenant_national_id INTEGER,
                entry_date TEXT,
                room_no INTEGER,
                room_cost REAL,
                FOREIGN KEY (tenant_national_id) REFERENCES profile(national_id)
            )
        ''')
