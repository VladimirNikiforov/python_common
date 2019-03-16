import sqlite3
import os
import datetime
db_path='C:/winpython/notebooks/XML_JSON_DB/'
db_file='db001.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()
var_list=[
	(1,1,"Айболит","Добрый доктор",100),
	(1,2,"Бармалей","Злой разбойник",200),
	(1,3,"Тяни-толкай","Непонятное существо",200)
]

sql="""INSERT INTO books(id_author,id_publication,title_book,descr_book,number_book)
	VALUES(?,?,?,?,?)
	"""

try:
	cur.executemany(sql,var_list)
except sqlite3.DatabaseError as error:
	print(error)
else:
	print('Ok')
con.commit()
cur.close()
con.close()
