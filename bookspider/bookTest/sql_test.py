import sqlite3

DBpath = '../db.sqlite3'
con = sqlite3.connect(DBpath)
cur = con.cursor()
#cur.execute("SELECT id FROM books_tag WHERE tagname = ?",(item['categoryName'],))
#cur.execute("SELECT id FROM books_tag ")
cur.execute("SELECT * FROM books_tag ")
#cur.execute("show table")
#cur.execute(".table")
#tagID = cur.fetchone()
result = cur.fetchall()

print(result)

