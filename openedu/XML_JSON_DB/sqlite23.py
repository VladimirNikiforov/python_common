import sqlite3
import os
import datetime
db_path='C:/winpython/notebooks/XML_JSON_DB/'
db_file='db001.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()
con.text_factory=bytes
cur=con.cursor()

try:
	print(cur.execute('''select * from books'''))
	print(cur.fetchone())
except sqlite3.DatabaseError as error:
	print(error)
else:
	print('Ok')
print(con.total_changes)
con.commit()
cur.close()
con.close()