import sqlite3
import os
import datetime
db_path='C:/winpython/notebooks/XML_JSON_DB/'
db_file='db001.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()
var1=("Роман",)
var2=(2,"Рассказ")
var3={"id":3, "name":"Стихотворение"}
sql1="""INSERT INTO publication (name_publication) VALUES(?)"""
sql2="""INSERT INTO publication VALUES(?,?)"""
sql3="""INSERT INTO publication VALUES(:id, :name)"""

try:
	cur.execute(sql1,var1)
	cur.execute(sql2,var2)
	cur.execute(sql3,var3)
except sqlite3.DatabaseError as error:
	print(error)
else:
	print('Ok')
con.commit()
cur.close()
con.close()
