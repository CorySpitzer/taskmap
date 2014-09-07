# db_play.py

# Just playing with the sqlite3 interface for now
# From www.pythoncentral.io/introduction-to-sqlite-in-python/

import sqlite3 as sql3

# create a db in RAM - (why is this useful?)
db = sql3.connect(':memory:')
# create or open a file called db1
db1 = sql3.connect('data/db1')

# Gotta close those connections!
db.close()
db1.close()


# get a 'cursor' object, which is kind of like an iterator
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, email TEXT)
''')
db.commit()

# to drop or delete a table:
cursor = db.cursor()
cursor.execute('''DROP TABLE email''')
db.commit()
