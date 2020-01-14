import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306, user='root',
                       passwd='1234', db='world', charset='utf8')
print('연결완료')
# print(type(conn))  # <class 'pymysql.connections.Connection'>

# cursor 생성
cursor = conn.cursor()
# print(type(cursor))  # <class 'pymysql.cursors.Cursor'>

# sql 명령 실행
# cursor.execute(sql명령)
cursor.execute(
    'SELECT * FROM city;'
)

# 파이썬 자료구조로 저장
# 리스트명 = cursor.fetchall()
cityList = cursor.fetchall()
# print(cityList)
cityList = list(cityList)
# print(cityList)



# world.country에서 첫번째 레코드만 출력
cursor.execute(
    'SELECT * FROM country;'
)
result = cursor.fetchone()
# print(result)
# print(list(result))

# 특정 갯수만큼 출력
cursor.execute(
    'SELECT * FROM gnpcountry;'
)

result = cursor.fetchmany(5)
# for row in result:
    # print(row)

# quiz
# 1. world.worldcity 테이블의 Code 값이 JPN인 레코드 정보 출력
cursor.execute(
    'SELECT * FROM worldcity WHERE Code = "JPN";'
)
result1 = cursor.fetchone()
print(result1)

print('-'*30)

# 2. world.gnpcountry에서 gnp가 가장 높은 10개 레코드 출력하기
cursor.execute(
    'SELECT * FROM gnpcountry ORDER BY gnp DESC LIMIT 10;'
)
result2 = cursor.fetchall()
for row in result2:
    print(row)

print('-'*30)

# 3. world.city 테이블에서 Name(국가명)이 H로 시작하는 레코드 수
cursor.execute(
    'SELECT COUNT(*) FROM city WHERE Name LIKE "H%";'
)
result3 = cursor.fetchone()
print(result3[0])

conn.close()
