import sqlite3
import os
import datetime
db_path='C:/winpython/notebooks/XML_JSON_DB/'
db_file='db001.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()

try:
	cur.execute('''
	update publication set name_publication='роман в стихах' where id_publication=3
	''')
	cur.execute('''
	insert into publication (name_publication)values('поэма для детей')
	''')
except sqlite3.DatabaseError as error:
	print(error)
else:
	print('Ok')
print(con.total_changes)
con.commit()
cur.close()
con.close()
