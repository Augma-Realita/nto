import sqlite3

import os.path
def make_ar():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "db.sqlite")
    conn =  sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("select * from lines")

    rows = cur.fetchall()

    res = [[None,None,None],[None,None,None],[None,None,None,None],[None,None,None]]
    for row in rows:
        res[row[2]][row[0]] = row[1]


    cur.close()
    return res

def get_arrow(start, end):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "db.sqlite")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("select arrowID from arrows where startID = ? and endID = ?", start, end)
   