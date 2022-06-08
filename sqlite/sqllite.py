import sqlite3
import datetime

# db 생성
make_db = sqlite3.connect('tdb.db',isolation_level=None)

data = make_db.cursor()

#  테이블 생성
data.execute("create table if not exists user(id integer primary key, username text, email text, phone text, wetsite text, regdate text)")

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

print(nowDatetime)

#  데이터 입력
data.execute("insert into user values( 2, 'park', 'park@.com','010-0000-0000','www.com',?)", (nowDatetime,))

# 데이터 조회
data.execute("select * from user")

rows = data.fetchall()

for r in rows:
    print(r)
