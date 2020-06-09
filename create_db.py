import sqlite3

db = sqlite3.connect('fin_keeper.db')
command = db.cursor()
command.execute("""CREATE TABLE IF NOT EXISTS category (
    category_id PRIMARY KEY, 
    classification TEXT,
    name TEXT,
    value INTEGER
) """)
db.commit()

category_id = 1
direction = 'expense'
name = 'products'
value = 10000


command.execute("SELECT classification FROM category")
if command.fetchone() is None:
    command.execute(
        "INSERT INTO category VALUES (?, ?, ?, ?)",
        (category_id ,direction, name, value))
    db.commit()
else:
    print('wow')