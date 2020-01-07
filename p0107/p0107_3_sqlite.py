import sqlite3

# 연결변수 conn
conn = sqlite3.connect('data/student.db')

# 작업변수 cursor
cursor = conn.cursor()

# sql 명령 실행
cursor.execute('SELECT * FROM student;')

# 결과 리스트로 저장
# 작업변수.fechone() : 한개만
# 작업변수.fechmany(레코드수) : 레코드 수 만큼
# 작업변수.fechall() : 모든 레코드
# resultList = cursor.fetchone()
# resultList = cursor.fetchmany(2)
resultList = cursor.fetchall()
print(resultList)
for row in resultList:
    print(row)

print('-' * 30)

cursor.execute('SELECT * FROM student LIMIT 2;')
resultList = cursor.fetchall()
print(resultList)
print(len(resultList))

conn.close()

conn = sqlite3.connect('data/test.db')
cursor = conn.cursor()
cursor.execute('SELECT firstname, lastname, city, country FROM customers;')
resultList=cursor.fetchone()
print(resultList)

cursor.execute('SELECT * FROM playlists WHERE name = "Music";')
resultList=cursor.fetchall()
print(resultList)

conn.close()