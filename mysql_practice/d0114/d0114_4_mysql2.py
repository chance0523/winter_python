import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306, user='root', passwd='1234',
                       db='world', charset='utf8')
print('연결완료')

# 딕셔너리 구조로 데이터 저장하기
cursor = conn.cursor(pymysql.cursors.DictCursor)

# cursor.execute(
#     'SELECT * FROM city;'
# )
# resultDict = cursor.fetchall()
# print(resultDict) # type : list
# for row in resultDict:
#     print(row, type(row)) # type : dict

# 키로 출력하기 (키 = 테이블의 필드)
# for row in resultDict:
#     print(row['Name'], row['CountryCode'], row['Population'])
#
# 마지막행의 Population 값 출력하기
# print(resultDict[-1]['Population'])

# 위의 딕셔너리 리스트 전체 레코드 출력
# 5, 10, 15, 20에 해당하는 id 값과 name 값 출력하기

cursor.execute(
    'SELECT * FROM city;'
)
resultDict = cursor.fetchall()
i = 1
for row in resultDict:
    if i % 5 == 0:
        print(row['ID'], row['Name'])
    i += 1
    if i > 20:
        break
conn.close()
