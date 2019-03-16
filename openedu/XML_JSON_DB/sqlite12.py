import sqlite3
import os
import datetime
db_path='C:/winpython/notebooks/XML_JSON_DB/'
db_file='db001.db'
full_path=os.path.join(db_path,db_file)

#os.remove(full_path)

sql="""\
CREATE TABLE IF NOT EXISTS author(
id_author INTEGER PRIMARY KEY,
name_author TEXT,
descr_author TEXT
);
CREATE TABLE publication(
id_publication INTEGER PRIMARY KEY,
name_publication TEXT
);
CREATE TABLE books(
id_book INTEGER PRIMARY KEY,
id_author INTEGER,
id_publication INTEGER,
title_book TEXT,
descr_book TEXT,
number_book INTEGER
);
"""
con=sqlite3.connect(full_path)
cur=con.cursor()
cur.executescript(sql)
cur.close()
con.close()