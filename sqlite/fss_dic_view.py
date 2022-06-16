import sqlite3

conn = sqlite3.connect('fdic.db',isolation_level=None)

cur = conn.cursor()

cur.execute("select * from fss_dic")

rows = cur.fetchall()

for r in rows:
    print(r)
