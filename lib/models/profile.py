import sqlite3
from . import CURSOR

# Create Profiles table if not exists
CURSOR.execute('''
    CREATE TABLE IF NOT EXISTS profiles (
        id INTEGER PRIMARY KEY,
        name TEXT,
        national_id TEXT UNIQUE
    )
''')
