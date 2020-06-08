import sqlite3

db = sqlite3.connect('fin_keeper.db')
command = db.cursor()
command.execute("""CREATE TABLE IF NOT EXISTS category (
    direction TEXT,
    name TEXT,
    value INTEGER
) """)
db.commit()

direction = 'expense'
name = 'products'
value = 10000


command.execute("SELECT type FROM category")
if command.fetchone() is None:
    command.execute("INSERT INTO category VALUES (?, ?, ?)", (direction, name, value))
    db.commit()
else:
    print('wow')