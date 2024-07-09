import sqlite3 
db = sqlite3.connect('form.db')
con = db.cursor()
#cursor.execute("CREATE TABLE MOVIES (title TEXT ,genre TEXT,year INTEGER)")
con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,firstname TEXT ,lastname TEXT,email TEXT,phone INTEGER,reasonforcontact TEXT)")
db.commit()
db.close()