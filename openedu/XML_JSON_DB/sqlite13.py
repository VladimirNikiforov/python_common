import sqlite3
import os
import datetime
db_path='C:/winpython/notebooks/XML_JSON_DB/'
db_file='db001.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()
sql="""\
INSERT INTO author (name_author, descr_author)
VALUES ("Чуковский","Авто множества книг для детей")
"""
cur.executescript(sql)
con.commit()
cur.close()
con.close()