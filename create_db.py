import sqlite3
from variables import DATABASE

db = sqlite3.connect(DATABASE)
command = db.cursor()
command.execute("""CREATE TABLE IF NOT EXISTS category (
    category_id INTEGER NOT NULL PRIMARY KEY, 
    name TEXT,   
    classification TEXT,
    value INTEGER
) """)
db.commit()

category_id = 1
name = 'products'
classification = 'expense'
value = 10000


command.execute("SELECT category_id FROM category")
if command.fetchone() is None:
    command.execute(
        "INSERT INTO category VALUES (?, ?, ?, ?)",
        (category_id, name, classification,  value))
    db.commit()
else:
    print('wow')