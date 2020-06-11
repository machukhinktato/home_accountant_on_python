import sqlite3

db = sqlite3.connect('fin_keeper.db')
command = db.cursor()
command.execute("""CREATE TABLE IF NOT EXISTS category (
    category_id INTEGER NOT NULL PRIMARY KEY , 
    classification TEXT,
    name TEXT, /* there shall be a UNIQUE */ 
    value INTEGER
) """)
db.commit()

category_id = 1
classification = 'expense'
name = 'products'
value = 10000


command.execute("SELECT category_id FROM category")
if command.fetchone() is None:
    command.execute(
        "INSERT INTO category VALUES (?, ?, ?, ?)",
        (category_id, classification, name, value))
    db.commit()
else:
    print('wow')