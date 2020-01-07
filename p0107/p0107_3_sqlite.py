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
resultList = cursor.fetchone()
print(resultList)

cursor.execute('SELECT * FROM playlists WHERE name = "Music";')
resultList = cursor.fetchall()
print(resultList)

conn.close()

# DB 파일이 없는 경우에는 새로 생성
conn = sqlite3.connect('data/book.db')
cursor = conn.cursor()

# 테이블 명 : book1
# id => int, 기본키, 필수항목(NOT NULL), AUTOINCREMENT
# title => text, NN
# writer => text, NN
# page => int, NN
# price => int, NN
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "book1"(
        "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "title" TEXT NOT NULL,
        "writer" TEXT NOT NULL,
        "page" INTEGER NOT NULL,
        "price" INTEGER NOT NULL
    );
''')

# 실제 db에 반영
conn.commit()

cursor.execute('''
    INSERT INTO book1 (title, writer, page, price)
    VALUES ("Jump to Python", "E.Y.Park", 240, 9000);
''')

conn.commit()

conn.close()
