import sqlite3

'''
quiz
1) 데이터베이스 생성 - productDB
2) 테이블 생성 - productTB
모든 필드는 NOT NULL
제품코드 (pCode) - TEXT, Primary Key
제품명 (pName) - TEXT
가격 (pPrice) - INTEGER
재고수량 (pAmount) - INTEGER
3) 레코드 삽입 5개정도
4) 레코드 출력함수 정의
5) 레코드의 데이터 수정
   예) p001 레코드의 가격을 220으로 수정
6) 레코드 삭제
   예) 첫번째 레코드 삭제
'''

# 데이터베이스 생성
conn = sqlite3.connect('data/productDB.db')
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "productTB"(
        "pCode" TEXT NOT NULL PRIMARY KEY,
        "pName" TEXT NOT NULL,
        "pPrice" INTEGER NOT NULL,
        "pAmount" INTEGER NOT NULL
    );
''')


# 레코드 삽입
# insert = '''INSERT INTO productTB (pCode, pName, pPrice, pAmount) VALUES (?, ?, ?, ?)'''
# cursor.execute(insert, ('p001', 'pencil', 300, 1000))
# cursor.execute(insert, ('p002', 'eraser', 500, 1000))
# cursor.execute(insert, ('p003', 'ruler', 700, 300))
# cursor.execute(insert, ('p004', 'pencil case', 2000, 150))
# cursor.execute(insert, ('p005', 'bag', 10000, 20))
#
# conn.commit()

# 레코드 출력함수 정의
def printTable():
    cursor.execute('''SELECT * FROM productTB;''')
    resultList = cursor.fetchall()
    print(f'전체 레코드 갯수 : {len(resultList)}')
    print('-' * 30)
    for row in resultList:
        print(row)


printTable()

# 레코드의 데이터 수정
update = '''UPDATE productTB SET pAmount = ? WHERE pName = ?'''
cursor.execute(update, (500, 'eraser'))
conn.commit()
printTable()

# 레코드 삭제
delete = '''DELETE FROM productTB WHERE pName = ?'''
cursor.execute(delete, ['ruler'])
conn.commit()
printTable()

conn.close()
