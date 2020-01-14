import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306, user='root', passwd='1234',
                       charset='utf8')
print('연결완료')

# cursor 생성
cursor = conn.cursor()

# 데이터베이스 만들기
# cursor.execute(
#     'CREATE DATABASE sqldb2;'
# )
# 데이터베이스 접속하기
cursor.execute(
    'USE sqldb2;'
)

# 테이블 만들기
# bookTbl
# id int primary key auto_increment
# title text
# writer text
# page int
# price int

# cursor.execute(
#     'DROP TABLE IF EXISTS bookTbl;'
# )
#
# cursor.execute('''
#     CREATE TABLE bookTbl
#     (id int not null primary key auto_increment,
#     title text not null,
#     writer text not null,
#     page int not null,
#     price int not null);
# ''')

cursor.execute(
    'DESC bookTbl;'
)
result = cursor.fetchall()
print(result)



conn.close()
