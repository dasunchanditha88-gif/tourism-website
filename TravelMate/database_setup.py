import sqlite3

conn = sqlite3.connect('travelmate.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tourists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT,
    budget INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS destinations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    country TEXT,
    cost INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS transport (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    price INTEGER,
    duration TEXT
)
''')

conn.commit()
conn.close()

print("Database and tables created successfully!")
