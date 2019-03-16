import sqlite3
import os
import datetime
db_path='C:/winpython/notebooks/XML_JSON_DB/'
db_file='db001.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()

var1=("Маршак",)
sql1='''insert into author (name_author)values(?)'''

try:
	cur.execute(sql1,var1)
	cur.execute("select * from author")
	print(cur.fetchall())
	
	con.rollback()
	cur.execute("select * from author")
	print(cur.fetchall())
	
except sqlite3.DatabaseError as error:
	print(error)
else:
	print('Ok')
print(con.total_changes)
con.commit()
cur.close()
con.close()