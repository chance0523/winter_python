import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306, user='root', passwd='1234',
                       db='sqldb2', charset='utf8')
print('연결완료')

cursor = conn.cursor()

# 레코드 삽입 1 - 필드명 생략
# cursor.execute('''
#     INSERT INTO bookTbl
#     VALUES(NULL, '자바를 잡아라', '한빛', 600, 36000);
# ''')
#
# conn.commit()

# 레코드 삽입 2 - %s
# sql = '''
#       INSERT INTO bookTbl (title, writer, page, price)
#       VALUES(%s, %s, %s, %s);
#       '''
# cursor.execute(sql, ('c언어', '영진', 700, 20000));
# conn.commit()

# cursor.execute(
#     'SELECT * FROM bookTbl;'
# )
# result = cursor.fetchall()
# print(result)

# 레코드 삽입 3 - 다중 레코드 삽입
# 데이터 변수
# sql 명령어 변수
# cursor.executemany(sql명령어, 데이터변수)
# data = (('파이썬', '영진2', 500, 23000),
#         ('MySQL', '영진3', 450, 18000),
#         ('DATA', '한빛2', 790, 50000))
# sql = '''
# INSERT INTO bookTbl (title, writer, page, price)
# VALUES (%s, %s, %s, %s);
# '''
# cursor.executemany(sql,data)
# conn.commit()
# cursor.execute(
#     'SELECT * FROM bookTbl;'
# )
# result = cursor.fetchall()
# print(result)

# 레코드 수정 : %s 방식
# sql 변수 = update 명령
# cursor.execute(sql변수, (값1, 값2, ... ))

# sql = '''
#       UPDATE bookTbl
#       SET price = %s
#       WHERE id = 1;
#       '''
# cursor.execute(sql, 20000)
#
# cursor.execute(
#     'SELECT * FROM bookTbl;'
# )
# conn.commit()
# result = cursor.fetchall()
# for row in result:
#     print(row)

# 레코드 삭제 : % 방식
# sql 변수 = delete 명령
# cursor.execute (sql변수, (값1 ...))

# sql='''
# DELETE FROM bookTbl WHERE id = %s;
# '''
# conn.commit()
# cursor.execute(sql,5)
# cursor.execute(
#     'SELECT * FROM bookTbl;'
# )
# result = cursor.fetchall()
# for row in result:
#     print(row)


conn.close()
